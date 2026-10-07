# Acknowledgments

HCL Domino Standalone Provisioner is built on excellent open-source projects. We're grateful to the developers and communities behind them.

## Core tooling

**Vagrant** — the machine lifecycle the Core Provisioner driver plugs into

- Website: [vagrantup.com](https://www.vagrantup.com/)
- License: BUSL-1.1

**VirtualBox** — the primary desktop hypervisor

- Website: [virtualbox.org](https://www.virtualbox.org/)
- License: GPL-3.0

**Ansible** — configuration management for the provisioning phase

- Website: [ansible.com](https://www.ansible.com/)
- License: GPL-3.0

**Core Provisioner** — the STARTcloud Vagrant driver this package rides on

- Repository: [STARTcloud/core_provisioner](https://github.com/STARTcloud/core_provisioner)

## Ansible collections

- **startcloud_roles** — base VM preparation and services ([STARTcloud/startcloud_roles](https://github.com/STARTcloud/startcloud_roles))
- **hcl_roles** — HCL technology installers: Domino, Verse, Traveler, Nomad ([STARTcloud/hcl_roles](https://github.com/STARTcloud/hcl_roles))

## Vagrant plugins

- **vagrant-zones** — Bhyve/zones provider for illumos hosts
- **vagrant-scp-sync** — SCP-based synced folders and guest-to-host syncback

## Infrastructure

- **release-please** — automated versioning and changelogs from Conventional Commits (Apache-2.0)
- **GitHub** — hosting, CI/CD, releases

## Standards

- **Semantic Versioning** — [semver.org](https://semver.org/)
- **Conventional Commits** — [conventionalcommits.org](https://www.conventionalcommits.org/)

## Disclaimer

This list may not be exhaustive. If you believe a project should be acknowledged here, please open an issue or a pull request. All trademarks are the property of their respective owners.
