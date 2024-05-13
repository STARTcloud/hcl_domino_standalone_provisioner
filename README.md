<!-- PROJECT LOGO -->
<br />
<p align="center">
  <a href="https://github.com/STARTcloud/hcl_domino_standalone_provisioner/">
    <img src="https://startcloud.com/assets/images/logos/startcloud-logo40.png" alt="Logo" width="200" height="100">
  </a>

  <h3 align="center">HCL Domino Standalone Provisioner</h3>

  <p align="center">
    Documentation for HCL Domino Standalone Provisioner
    <br />
    <a href="https://github.com/STARTcloud/hcl_domino_standalone_provisioner/"><strong>Explore the docs »</strong></a>
    <br />
    <br />
    <a href="https://github.com/STARTcloud/hcl_domino_standalone_provisioner/">View Demo</a>
    ·
    <a href="https://github.com/STARTcloud/hcl_domino_standalone_provisioner/issues">Report Bug</a>
    ·
    <a href="https://github.com/STARTcloud/hcl_domino_standalone_provisioner/issues">Request Feature</a>
  </p>
</p>

<!-- TABLE OF CONTENTS -->
## Table of Contents

* [About the Project](#hcl-domino-standalone-provisioner)
* [Key Features](#key-features)
* [Galaxy Role File Structure](#galaxy-role-file-structure)
* [Roadmap](#roadmap)
* [Contributing](#contributing)
* [License](#license)
* [Contact](#authors)
* [Acknowledgements](#acknowledgments)


## HCL Domino Standalone Provisioner
HCL Domino Standalone Provisioner is a collection of Ansible roles designed to install HCL technologies such as Verse, Domino, Traveler, and Nomad. These roles are part of the STARTcloud ecosystem, working in conjunction with the Core Provisioner to automate the provisioning and configuration of VMs. This project streamlines the setup process for these technologies, ensuring a more efficient and manageable deployment.

## Key Features

- **Role Management**: Offers a comprehensive set of Ansible roles for various aspects of VM preparation and configuration.
- **Technology Installation**: Automates the installation of proprietary technologies like Verse, Domino, Traveler, and Nomad, simplifying the deployment process.
- **Service Configuration**: Simplifies the setup of necessary services on VMs, streamlining the deployment process.
- **Dependency Installation**: Handles the installation of required dependencies, reducing manual setup efforts.

### Including HCL Domino Standalone Provisioner

### ~~Including HCL Domino Standalone Provisioner~~

1. **~~Add HCL Domino Standalone Provisioner as a Git Submodule~~**: ~~First, ensure that HCL Domino Standalone Provisioner is added as a submodule to your project. This can be done using the following command:~~

~~git submodule add -b submodule https://github.com/STARTcloud/hcl_domino_standalone_provisioner hcl_domino_standalone_provisioner~~
   ~~Replace `path/to/submodule` with the desired path within your project where you want to include HCL Domino Standalone Provisioner.~~

2. **~~Update the Submodule~~**: 
~~After cloning your project, navigate to the submodule directory and pull the latest changes:~~

~~bash cd path/to/submodule git pull origin main~~

### Interacting with `Hosts.yml` and `Hosts.rb`

To integrate HCL Domino Standalone Provisioner with the Core Provisioner, specifically with the `Hosts.yml` and `Hosts.rb` files, follow these steps:

HCL Domino Standalone Provisioner enhances the provisioning process by automating the configuration of VMs. To utilize these roles effectively, they need to be referenced within the `Hosts.yml` for the Core Provisioner `Hosts.rb`.

1. **Reference Roles in `Hosts.yml`**: Within the `Hosts.yml` file, you can specify which roles from HCL Domino Standalone Provisioner should be applied to a particular host. This is done by including the role names under the `roles` key for each host configuration. For example:
```
hosts: all
roles: 
  - startcloud.roles.ssl_setup
  - startcloud.roles.service_configuration
```


   This configuration indicates that the `ssl_setup` and `service_configuration` roles from HCL Domino Standalone Provisioner should be applied to all hosts via `all`.

2. **Execution in `Hosts.rb`**: The `Hosts.rb` script is responsible for interpreting the `Hosts.yml` file and generating the necessary Vagrant configurations. When the `Hosts.rb` script encounters a host configuration that includes roles, it automatically applies these roles during the provisioning process. There's no need for additional modifications in `Hosts.rb` for this purpose, as the script is designed to handle role application based on the `Hosts.yml` configurations.

By following these steps, you can seamlessly integrate HCL Domino Standalone Provisioner with the Core Provisioner, leveraging the power of Ansible roles to automate the configuration and security of your VMs. This approach enhances the flexibility and extensibility of your provisioning process, allowing for a more declarative and manageable setup.

## Roadmap
See the [open issues](https://github.com/STARTcloud/hcl_domino_standalone_provisioner/issues) for a list of proposed features (and known issues).

## Provider Support

| Provider       | Supported by HCL Domino Standalone Provisioner |
|----------------|--------------------------------|
| VirtualBox     | Yes                            |
| Bhyve/Zones    | Yes                            |
| VMware Fusion  | No                             |
| Hyper-V        | No                             |
| Parallels      | No                             |
| AWS EC2        | Yes                            |
| Google Cloud   | No                             |
| Azure          | No                             |
| DigitalOcean   | No                             |
| Linode         | No                             |
| Vultr          | No                             |
| Oracle Cloud   | No                             |
| OpenStack      | No                             |
| Rackspace      | No                             |
| Alibaba Cloud  | No                             |
| Aiven          | No                             |
| Packet         | No                             |
| Scaleway       | No                             |
| OVH            | No                             |
| Exoscale       | No                             |
| Hetzner Cloud  | No                             |
| KVM            | Yes                            |
| QEMU           | Yes                            |
| Docker Desktop | No                             |
| HyperKit       | No                             |
| WSL2           | No                             |

## Built With
* [Vagrant](https://www.vagrantup.com/) - Portable Development Environment Suite.
* [VirtualBox](https://www.virtualbox.org/wiki/Downloads) - Hypervisor.
* [Ansible](https://www.ansible.com/) - Virtual Machine Automation Management.
* [Core Provisioner](https://github.com/STARTcloud/core_provisioner) - Core Provisioner.

## Contributing

Please read [CONTRIBUTING.md](https://www.prominic.net) for details on our code of conduct, and the process for submitting pull requests to us.

## Authors
* **Joel Anderson** - *Initial work* - [JoelProminic](https://github.com/JoelProminic)
* **Justin Hill** - *Initial work* - [JustinProminic](https://github.com/JustinProminic)
* **Mark Gilbert** - *Refactor* - [MarkProminic](https://github.com/MarkProminic)

See also the list of [contributors](https://github.com/STARTcloud/hcl_domino_standalone_provisioner/graphs/contributors) who participated in this project.

## License

This project is licensed under the SSLP v3 License - see the [LICENSE.md](LICENSE.md) file for details

## Acknowledgments

* Hat tip to anyone whose code was used
