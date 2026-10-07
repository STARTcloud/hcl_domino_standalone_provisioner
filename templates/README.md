# Hosts Configuration Templates

This repository (`hcl_domino_standalone_provisioner`) is the HCL Domino Standalone provisioner — it installs a standalone HCL Domino server that creates a new Domino domain (plus optional Leap, Nomad Web, Traveler, Verse, REST API and Sametime add-ons) on a STARTcloud base box using the `startcloud.startcloud_roles` and `startcloud.hcl_roles` collections. Adjust the enabled roles under `roles:` in your `Hosts.yml`.

## Hosts.template.yml

- **Purpose**: A true Jinja2 template rendered by the hyperweaver-agent generator (gonja; nunjucks on zoneweaver when its render step lands) to produce the final `Hosts.yml`. Context comes from the machine spec: structured `settings`/`networks`/`roles` plus manifest field answers by exact field name; every settings key echoes the create context with the package value as fallback (`| default(...)`), and enabled picker roles are appended after the base foundation roles.
- **Usage**: Rendered by the agent at machine create. Dialect: standard Jinja2 — parenthesized filter args (`|default("x")`), `loop.*` metadata, `is defined` works; undefined variables render empty.

## Hand-writing a Hosts.yml (plain vagrant use)

Create `Hosts.yml` at the repository root (it is gitignored). The driver ships reference documents under `driver/examples/` — the driver directory is fetched automatically on first `vagrant up` from the core_provisioner release pinned in `driver.version`.

## Add your own

If you add your own template, update this README.md with a brief description of what it does, and in your pull request mention why it differs from the existing ones.
