# Windows IIS Configuration Management

This repository contains Ansible roles and playbooks for managing Windows IIS application servers. The project is designed to be maintainable and testable, with clear contribution guidelines for the DevOps/SRE team.

## Prerequisites

- Python 3.8 or higher
- Windows host with PowerShell remoting enabled
- pywinrm package for Windows remote management
- Ansible 2.14 or higher

## Quick Start

1. Set up the virtual environment:
```powershell
python -m venv venv
.\venv\Scripts\Activate.ps1
pip install -r requirements.txt
```

2. Configure your inventory:
```yaml
# inventory/production.yml or inventory/staging.yml
windows_servers:
  hosts:
    win-iis-01:
      ansible_host: your-server.example.com
  vars:
    ansible_connection: winrm
    ansible_winrm_server_cert_validation: ignore
```

3. Run the playbook:
```bash
ansible-playbook -i inventory/staging.yml site.yml
```

## Project Structure

```
.
├── inventory/               # Inventory files for different environments
├── group_vars/             # Group variables
├── host_vars/              # Host-specific variables
├── roles/                  # Ansible roles
│   └── iis/               # IIS-specific role
├── playbooks/             # Task-specific playbooks
├── site.yml               # Main playbook
└── tests/                 # Test configurations and scripts
```

## Testing

We use Molecule for testing Ansible roles. Each role includes:
- Molecule scenarios for testing
- TestInfra for writing infrastructure tests
- GitHub Actions for CI/CD

To run tests:
```bash
cd roles/iis
molecule test
```

## Contributing

1. Create a feature branch from `main`
2. Make your changes following our coding standards
3. Include tests for new functionality
4. Update documentation as needed
5. Submit a pull request

### Coding Standards

- Use YAML files with `.yml` extension
- Include comments for complex tasks
- Follow [Ansible best practices](https://docs.ansible.com/ansible/latest/tips_tricks/style_guide.html)
- Test all changes using Molecule
- Document any new variables or dependencies

## License

Internal use only - Your Company Name