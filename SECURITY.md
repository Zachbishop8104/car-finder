# Security Policy

## Supported versions

Only the latest version on the `master` branch is supported. Fixes are
not backported.

## Reporting a vulnerability

Please do not open a public issue for a security problem.

Report it privately through GitHub: on this repository's **Security**
tab, choose **Report a vulnerability**. That opens a private advisory
only you and the maintainer can see.

Include what you found, how to reproduce it, and what an attacker could
do with it. You should hear back within a week. This is a spare-time
project, so a fix may take longer than that, but you will be kept
informed.

## What counts

Car Finder runs on the user's own machine, makes read-only requests to
a small set of public APIs, and stores the user's Marketcheck API key in
a local `.env` file. Reports of particular interest:

- Anything that could send the API key, or the user's search details,
  to a host other than the ones listed in the README.
- Anything that writes or deletes files outside the tool's data folder.
- Anything that executes content fetched from the network.

Wrong or outdated reliability data is not a security issue. Use the
"Reliability profile correction" issue form for that.
