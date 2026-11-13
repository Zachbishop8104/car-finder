"""
Five-year total cost of ownership.

Sticker price is the least interesting number in a car purchase. What
actually separates two cars over five years is depreciation, fuel or
electricity, insurance, maintenance and tires.

Every input is either measured (depreciation from local listings, MPG
from the EPA) or configurable (fuel price, your insurance baseline,
annual mileage). Nothing here is a black box, the breakdown shows
exactly where each dollar came from and which figures are estimates.
"""
import math

# Used when a model has no profile, so an unrated car still gets a
# number instead of a blank. Flagged in `assumptions` when it applies.
DEFAULT_ANNUAL_MAINTENANCE = 600
DEFAULT_MPG = 28

# The EPA's annual fuel cost figure assumes this many miles a year.
EPA_ANNUAL_MILES = 15000

DEFAULTS = {
    "years": 5,
    "annual_miles": 12000,
    "fuel_price_per_gallon": 3.35,
    "baseline_insurance_annual": 1650,
    "tire_replacement_interval_miles": 45000,
    "annual_registration_usd": 180,
    # Repair costs climb as a car ages; this is the extra fraction of
    # annual maintenance added per 10k miles already on the clock.
    "maintenance_escalation_per_10k": 0.06,
}


def _cfg(ownership):
    out = dict(DEFAULTS)
    out.update({k: v for k, v in (ownership or {}).items() if v is not None})
    return out


def estimate(listing, profile, curve=None, mpg=None, ownership=None,
             epa=None):
    """Full 5-year cost picture for one listing.

    listing  a scored listing dict (needs price and miles)
    profile  the reliability profile for that generation
    curve    local depreciation curve from market.depreciation_curve()
    mpg      EPA combined mpg, if we have it
    epa      the matched EPA variant from research.fuel_economy(), if any.
             Needed to cost an electric or plug-in car correctly.
    """
    from . import market  # local import keeps the module dependency-light

    c = _cfg(ownership)
    years = int(c["years"])
    price = listing.get("price") or 0
    start_miles = listing.get("miles") or 0
    miles_driven = c["annual_miles"] * years
    assumptions = []

    # --- depreciation -------------------------------------------------
    proj = market.project_value(price, curve, years=years)
    depreciation = proj["total_depreciation"]
    if proj["basis"] != "local market curve":
        assumptions.append(
            "Depreciation uses a generic 13%/yr fallback: too few local "
            "comparables to fit a real curve."
        )

    # --- fuel -----------------------------------------------------------
    epa = epa or {}
    fuel_type = str(epa.get("fuel_type") or "")
    electric = (epa.get("atv_type") == "EV"
                or fuel_type.lower() == "electricity")
    plug_in_hybrid = epa.get("atv_type") == "Plug-in Hybrid"
    epa_annual = epa.get("annual_fuel_cost_usd")
    if electric and epa_annual:
        # MPGe is an efficiency rating, not gallons. Dividing miles by it
        # and multiplying by a pump price understates an EV's running
        # cost by a wide margin, so use the EPA's own annual figure.
        fuel = epa_annual * (c["annual_miles"] / EPA_ANNUAL_MILES) * years
        fuel_basis = "EPA annual energy cost, scaled to your mileage"
        assumptions.append(
            f"Electric car: energy cost uses the EPA's "
            f"${epa_annual:,.0f}/yr estimate (national average electricity "
            f"price at {EPA_ANNUAL_MILES:,} mi/yr) scaled to your mileage, "
            f"not your configured fuel price. Charging rates vary a lot; "
            f"check it against your own."
        )
    else:
        if electric:
            assumptions.append(
                "Electric car, but the EPA gave no annual energy cost; "
                "the fuel figure treats MPGe as mpg and is too low."
            )
        elif plug_in_hybrid:
            assumptions.append(
                "Plug-in hybrid: fuel is costed as if it never charges "
                "(gasoline mode only). Regular charging will bring the "
                "real figure well under this."
            )
        if not mpg:
            mpg = DEFAULT_MPG
            assumptions.append(
                f"No EPA mpg found; assumed {DEFAULT_MPG} mpg combined.")
        elif fuel_type and "regular" not in fuel_type.lower() and not electric:
            assumptions.append(
                f"The EPA lists {fuel_type} for this car; the fuel figure "
                f"uses your configured ${c['fuel_price_per_gallon']:.2f}/gal "
                f"as-is, so set that to the right fuel's price."
            )
        fuel = (miles_driven / float(mpg)) * c["fuel_price_per_gallon"]
        fuel_basis = "EPA combined mpg x your fuel price"

    # --- insurance ------------------------------------------------------
    factor = profile.get("insurance_factor") or 1.0
    insurance = c["baseline_insurance_annual"] * factor * years
    assumptions.append(
        f"Insurance is your ${c['baseline_insurance_annual']:,.0f}/yr baseline "
        f"x {factor:.2f} for this model. Replace the baseline with a real quote."
    )

    # --- maintenance and repairs ----------------------------------------
    annual = profile.get("annual_maintenance_usd")
    if annual is None:
        annual = DEFAULT_ANNUAL_MAINTENANCE
        assumptions.append(
            f"No maintenance profile for this model; assumed "
            f"${DEFAULT_ANNUAL_MAINTENANCE}/yr."
        )
    maintenance = 0.0
    for y in range(years):
        odo = start_miles + c["annual_miles"] * y
        maintenance += annual * (1 + c["maintenance_escalation_per_10k"] * odo / 10000.0)

    # --- tires ------------------------------------------------------------
    # Costed as full sets of four.
    sets = math.ceil(miles_driven / float(c["tire_replacement_interval_miles"]))
    tire_cost = (profile.get("tire_set_usd") or 750) * sets

    # --- registration ------------------------------------------------------
    registration = c["annual_registration_usd"] * years

    breakdown = {
        "depreciation": round(depreciation),
        "fuel": round(fuel),
        "insurance": round(insurance),
        "maintenance_repairs": round(maintenance),
        "tires": round(tire_cost),
        "registration": round(registration),
    }
    total = sum(breakdown.values())

    return {
        "years": years,
        "annual_miles": c["annual_miles"],
        "purchase_price": price,
        "projected_resale": proj["projected_value"],
        "breakdown": breakdown,
        "total": total,
        "total_plus_purchase": total + price - depreciation,
        "cost_per_month": round(total / (years * 12)),
        "cost_per_mile": round(total / miles_driven, 3) if miles_driven else None,
        "tire_sets_needed": sets,
        "mpg_used": mpg,
        "fuel_basis": fuel_basis,
        "depreciation_basis": proj["basis"],
        "assumptions": assumptions,
    }


def compare(estimates):
    """Rank several TCO estimates cheapest-first and show the spread."""
    ranked = sorted(estimates, key=lambda e: e[1]["total"])
    if not ranked:
        return []
    cheapest = ranked[0][1]["total"]
    return [
        {
            "vin": vin,
            "total": est["total"],
            "cost_per_month": est["cost_per_month"],
            "premium_over_cheapest": est["total"] - cheapest,
        }
        for vin, est in ranked
    ]
