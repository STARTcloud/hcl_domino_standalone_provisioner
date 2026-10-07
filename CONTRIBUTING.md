# Contributing to HCL Domino Standalone Provisioner

Thank you for your interest in contributing! Community contributions directly impact the pace of feature development and bug fixes.

## How to Contribute

### Reporting Issues

Before creating an issue, please:

1. **Search existing issues** to avoid duplicates
2. **Use the appropriate issue template** (bug report, feature request, question)
3. **Provide detailed information** — the relevant `Hosts.yml` portion (redact secrets), steps to reproduce, expected vs. actual behavior
4. **Include environment details** (host OS, Vagrant version, provider + version)

### Submitting Pull Requests

1. **Fork the repository** and create your feature branch from `main`
2. **Keep changes focused** and write commit messages using [Conventional Commits](https://www.conventionalcommits.org/) — release-please builds the changelog and version bumps from them (`fix:` = patch, `feat:` = minor)
3. **Make sure CI passes**: `ansible-lint --strict` must be clean over `provisioners/ansible`
4. **Fill out the pull request template** completely
5. **Role changes live in the collections** — submit those to [STARTcloud/hcl_roles](https://github.com/STARTcloud/hcl_roles) or [STARTcloud/startcloud_roles](https://github.com/STARTcloud/startcloud_roles); the releases pinned in `collections/*.version` are bumped here by the Dependency Bump workflow when a collection release publishes

### Testing Changes

There is no unit test suite — the package is exercised by real `vagrant up` runs. Before submitting:

1. Test with a real `Hosts.yml` (start from `examples/Hosts.yml` or `templates/Hosts.template.yml`)
2. State in the PR which providers you tested (VirtualBox, Bhyve/zones)
3. Call out anything that changes the `Hosts.yml` schema, the manifest (`provisioner.yml`), or the platform template contract

### What We're Looking For

- Bug fixes, especially provisioning-order or role-variable ones
- Template and manifest improvements for the platform wizard
- Better error handling and clearer provisioning output
- Documentation improvements

## Response Times and Review Process

Due to limited development resources:

- **Issue responses**: we aim to acknowledge new issues within a few days
- **Pull request reviews**: may take time depending on complexity and workload
- **Documentation updates**: generally reviewed quickly as they're high-impact, low-risk

## Recognition

All contributors are recognized in our [AUTHORS.md](AUTHORS.md) file.

## Code of Conduct

This project follows our [Code of Conduct](CODE_OF_CONDUCT.md). By participating, you agree to abide by its terms.

## License

By contributing to HCL Domino Standalone Provisioner, you agree that your contributions will be licensed under the [Apache License 2.0](LICENSE.md).
