# Security Policy

## Supported Versions

Only the latest release is supported. Always consume the newest tagged version.

## Reporting a Vulnerability

**Please do not report security vulnerabilities through public GitHub issues.**

### Preferred Method: Security Advisory

1. Go to the [GitHub Security Advisory page](https://github.com/STARTcloud/hcl_domino_standalone_provisioner/security/advisories)
2. Click "Report a vulnerability"
3. Fill out the advisory form with detailed information
4. Submit the advisory

### What to Include

- **Description** of the vulnerability
- **Steps to reproduce** the issue
- **Potential impact** of the vulnerability
- **Affected versions** (if known)
- **Suggested fix** (if you have one)

## Response Process

Due to limited development resources:

- **Initial Response**: we aim to acknowledge receipt within 48–72 hours
- **Assessment**: initial assessment within about a week
- **Resolution**: timeline depends on severity, typically 1–4 weeks
- **Disclosure**: coordinated disclosure after a fix is available

## Focus Areas

HCL Domino Standalone Provisioner is an Ansible-based provisioner package driven by the core_provisioner Vagrant driver. The security-relevant areas are:

- **`Hosts.yml` is trusted input** — values from it are interpolated into the generated playbook and shell commands. Only run configurations you wrote or trust.
- **Secrets handling** — installer download credentials and Domino passwords belong in `.secrets.yml`, which is gitignored; never commit them to `Hosts.yml` or the repository. Domino ID files under `id-files/` are likewise gitignored — never commit them.
- **The development CA and default certificates** — shipped inside the fetched `driver/ssls/` tree and synced to `/secure/` on dev machines. Never add them to a production trust store; replace with your own certificates for production use.
- **Release integrity** — release assets are immutable and ship `.sha256` sidecars; consumers must verify checksums after download.
- **Supply chain** — Dependabot runs against this repository; the pinned core driver is sha256-verified at fetch time (`driver.version`).

## Acknowledgments

Contributors who responsibly report security vulnerabilities will be acknowledged here (with their permission):

- _No vulnerabilities reported yet_
