# HCL Domino Standalone Provisioner

[![HCL Domino Standalone Provisioner logo](https://raw.githubusercontent.com/STARTcloud/startcloud_roles/refs/heads/main/roles/startcloud_theme/files/github-header.svg)](https://github.com/STARTcloud/hcl_domino_standalone_provisioner/)

Documentation for HCL Domino Standalone Provisioner

[**Explore the docs »**](https://github.com/STARTcloud/hcl_domino_standalone_provisioner/)

[Report Bug](https://github.com/STARTcloud/hcl_domino_standalone_provisioner/issues) ·
[Request Feature](https://github.com/STARTcloud/hcl_domino_standalone_provisioner/issues)

## Table of Contents

- [About the Project](#about-the-project)
- [Key Features](#key-features)
- [Roadmap](#roadmap)
- [Provider Support](#provider-support)
- [Built With](#built-with)
- [Contributing](#contributing)
- [License](#license)
- [Contact](#authors)
- [Acknowledgements](#acknowledgments)

## About the Project

HCL Domino Standalone Provisioner is a provisioner package that installs a standalone HCL Domino server — the first server of a new Domino domain — along with optional add-ons such as Leap, Nomad Web, Traveler, Verse and the Domino REST API. It is part of the STARTcloud ecosystem, riding on the [Core Provisioner](https://github.com/STARTcloud/core_provisioner) driver (fetched automatically from the release pinned in `driver.version`) and the `startcloud.startcloud_roles` and `startcloud.hcl_roles` Ansible collections.

## Key Features

- **Role Management**: Offers a comprehensive set of Ansible roles for various aspects of VM preparation and configuration.
- **Technology Installation**: Automates the installation of proprietary technologies like Verse, Domino, Traveler, and Nomad, simplifying the deployment process.
- **Service Configuration**: Simplifies the setup of necessary services on VMs, streamlining the deployment process.
- **Dependency Installation**: Handles the installation of required dependencies, reducing manual setup efforts.

### Including HCL Domino Standalone Provisioner

Releases are built by release-please from conventional commits: every release
carries an immutable `hcl_domino_standalone_provisioner-<version>.tar.gz` (plus
a mutable `hcl_domino_standalone_provisioner.tar.gz` "latest" alias) with
`.sha256` sidecars — the registry-shaped artifact contract the provisioner
catalog uses. See [RELEASE.md](RELEASE.md) for how releases are produced.

For plain vagrant use, clone this repository, copy `examples/Hosts.yml` to
`Hosts.yml` at the repository root, place the collection releases pinned in
`collections/*.version` under `provisioners/ansible_collections/`, and run
`vagrant up` — the pinned core driver bootstraps itself on first run.

### Interacting with `Hosts.yml` and `Hosts.rb`

To integrate HCL Domino Standalone Provisioner with the Core Provisioner, specifically with the `Hosts.yml` and `Hosts.rb` files, follow these steps:

HCL Domino Standalone Provisioner enhances the provisioning process by automating the configuration of VMs. To utilize these roles effectively, they need to be referenced within the `Hosts.yml` for the Core Provisioner `Hosts.rb`.

1. **Reference Roles in `Hosts.yml`**: Within the `Hosts.yml` file, you can specify which roles should be applied to a particular host. This is done by including the role names under the `roles` key for each host configuration. For example:

   ```yaml
   hosts: all
   roles:
     - startcloud.hcl_roles.domino_install
     - startcloud.hcl_roles.domino_config
   ```

   This configuration indicates that the `domino_install` and `domino_config` roles from the `startcloud.hcl_roles` collection should be applied to all hosts via `all`.

1. **Execution in `Hosts.rb`**: The `Hosts.rb` script is responsible for interpreting the `Hosts.yml` file and generating the necessary Vagrant configurations. When the `Hosts.rb` script encounters a host configuration that includes roles, it automatically applies these roles during the provisioning process. There's no need for additional modifications in `Hosts.rb` for this purpose, as the script is designed to handle role application based on the `Hosts.yml` configurations.

By following these steps, you can seamlessly integrate HCL Domino Standalone Provisioner with the Core Provisioner, leveraging the power of Ansible roles to automate the configuration and security of your VMs. This approach enhances the flexibility and extensibility of your provisioning process, allowing for a more declarative and manageable setup.

## Roadmap

See the [open issues](https://github.com/STARTcloud/hcl_domino_standalone_provisioner/issues) for a list of proposed features (and known issues).

## Provider Support

| Provider       | Supported by HCL Domino Standalone Provisioner |
| -------------- | ---------------------------------------------- |
| VirtualBox     | Yes                                            |
| Bhyve/Zones    | Yes                                            |
| VMware Fusion  | No                                             |
| Hyper-V        | No                                             |
| Parallels      | No                                             |
| AWS EC2        | Yes                                            |
| Google Cloud   | No                                             |
| Azure          | No                                             |
| DigitalOcean   | No                                             |
| Linode         | No                                             |
| Vultr          | No                                             |
| Oracle Cloud   | No                                             |
| OpenStack      | No                                             |
| Rackspace      | No                                             |
| Alibaba Cloud  | No                                             |
| Aiven          | No                                             |
| Packet         | No                                             |
| Scaleway       | No                                             |
| OVH            | No                                             |
| Exoscale       | No                                             |
| Hetzner Cloud  | No                                             |
| KVM            | Yes                                            |
| QEMU           | Yes                                            |
| Docker Desktop | No                                             |
| HyperKit       | No                                             |
| WSL2           | No                                             |

## Built With

- [Vagrant](https://www.vagrantup.com/) - Portable Development Environment Suite.
- [VirtualBox](https://www.virtualbox.org/wiki/Downloads) - Hypervisor.
- [Ansible](https://www.ansible.com/) - Virtual Machine Automation Management.
- [Core Provisioner](https://github.com/STARTcloud/core_provisioner) - Core Provisioner.

## Contributing

Please read [CONTRIBUTING.md](CONTRIBUTING.md) for details on our code of conduct, and the process for submitting pull requests to us.

## Authors

- **Joel Anderson** - _Initial work_ - [JoelProminic](https://github.com/JoelProminic)
- **Justin Hill** - _Initial work_ - [JustinProminic](https://github.com/JustinProminic)
- **Mark Gilbert** - _Refactor_ - [MarkProminic](https://github.com/MarkProminic)

See also the list of [contributors](https://github.com/STARTcloud/hcl_domino_standalone_provisioner/graphs/contributors) who participated in this project.

## License

This project is licensed under the Apache License 2.0 - see the [LICENSE.md](LICENSE.md) file for details

## Acknowledgments

- Hat tip to anyone whose code was used — see [ACKNOWLEDGMENTS.md](ACKNOWLEDGMENTS.md)
