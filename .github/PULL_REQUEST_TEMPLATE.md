# Description

Brief description of the changes in this pull request.

## Type of Change

Please delete options that are not relevant:

- [ ] Bug fix (non-breaking change which fixes an issue)
- [ ] New feature (non-breaking change which adds functionality)
- [ ] Breaking change (fix or feature that would cause existing functionality to not work as expected)
- [ ] Documentation update
- [ ] Code refactoring (no functional changes)

## Testing

Please describe how you verified your changes:

- [ ] `vagrant up` tested with a real `Hosts.yml`
- [ ] Tested on VirtualBox
- [ ] Tested on Bhyve/zones (vagrant-zones)
- [ ] `ansible-lint --strict` passes on `provisioners/ansible`

**Test Configuration:**

- Host OS:
- Vagrant Version:
- Provider + Version:

## Impact Assessment

- [ ] No breaking changes
- [ ] Requires a `Hosts.yml` schema change (call it out below)
- [ ] Changes the manifest (`provisioner.yml`) or the platform template contract
- [ ] Requires a collection pin bump (`collections/*.version`)

**Areas Affected:**

- [ ] Manifest / platform template (provisioner.yml, templates/)
- [ ] Ansible playbook generation (provisioners/ansible)
- [ ] Collection pins (`collections/startcloud.hcl_roles.version`, `collections/startcloud.startcloud_roles.version`)
- [ ] Installers layout
- [ ] Release / CI

## Additional Context

Any additional information that reviewers should know.

## Checklist

- [ ] I have read the [Contributing Guidelines](../CONTRIBUTING.md)
- [ ] Commit messages follow [Conventional Commits](https://www.conventionalcommits.org/) (release-please relies on them)
- [ ] I have updated documentation as needed
- [ ] I have considered the impact on machines provisioned from earlier releases
