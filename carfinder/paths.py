"""
Where things live.

Two different places, deliberately kept apart:

  APP_DIR   the code and its bundled demo data. Read-only as far as the
            tool is concerned. It may be a git checkout, an installed
            skill folder, or a temporary copy that is deleted after the
            run, so nothing worth keeping is ever written here.

  home()    everything the tool remembers: config.yaml, .env (the API
            key), output/ and .cache/. This has to outlive the code,
            because the cache and the call counter are what protect a
            500-call API quota.

home() resolves, in order:

  1. $CAR_FINDER_HOME, if set.
  2. APP_DIR itself, if a config.yaml sits next to the code. That keeps
     a self-contained checkout working exactly as it always has.
  3. ~/.car-finder
"""
import os

APP_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
ENV_HOME = "CAR_FINDER_HOME"
DEFAULT_HOME = os.path.join(os.path.expanduser("~"), ".car-finder")


def home():
    override = os.environ.get(ENV_HOME, "").strip()
    if override:
        return os.path.abspath(os.path.expanduser(override))
    if os.path.exists(os.path.join(APP_DIR, "config.yaml")):
        return APP_DIR
    return DEFAULT_HOME


def config_file():
    return os.path.join(home(), "config.yaml")


def env_file():
    return os.path.join(home(), ".env")


def output_dir():
    return os.path.join(home(), "output")


def cache_dir():
    return os.path.join(home(), ".cache")


def example_config():
    return os.path.join(APP_DIR, "config.example.yaml")
