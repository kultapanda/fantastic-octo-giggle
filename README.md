# Windows IIS Configuration Management

This repository contains Ansible roles and playbooks for managing Windows IIS application servers. The project is designed to be maintainable and testable, with clear contribution guidelines for the DevOps/SRE team.

## Prerequisites

- Python 3.8 or higher
- Windows host with PowerShell remoting enabled
- pywinrm package for Windows remote management
- Ansible 2.14 or higher

## Control Host Requirements

Ansible must be run from a Linux control host, not from Windows. For Windows users, we recommend using Windows Subsystem for Linux (WSL). Here's how to set it up:

### Installing WSL on Windows

1. Open PowerShell as Administrator and run:
```powershell
wsl --install
```

2. Restart your computer when prompted.

3. After restart, open Microsoft Store and install Ubuntu 22.04 LTS.

4. Launch Ubuntu and set up your username and password when prompted.

### Setting up Ansible in WSL

1. Update package list and install prerequisites:
```bash
sudo apt update
sudo apt install -y python3-pip python3-venv
```

2. Configure WSL for better Windows integration:
```bash
# Add to your ~/.bashrc
echo "export ANSIBLE_CONFIG=\$PWD/ansible.cfg" >> ~/.bashrc
echo "export PATH=\$PATH:\$HOME/.local/bin" >> ~/.bashrc
source ~/.bashrc
```

3. Clone this repository in WSL:
```bash
# Navigate to where you want to store the project
cd /mnt/c/Users/YourUsername/Projects  # Example path
git clone <repository-url>
cd <repository-name>
```

### WSL Development Tips

- Access Windows files through `/mnt/c/`
- Use VS Code with "Remote - WSL" extension for better integration
- Keep project files in the Linux filesystem for better performance
- Use Windows Terminal for improved WSL experience

## Quick Start

1. Set up the virtual environment in WSL:
```bash
# Create and activate virtual environment
python3 -m venv venv
source venv/bin/activate

# Install dependencies
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

## Standard Execution Steps

1. Create an Ansible vault for sensitive data:
```bash
# Create a new vault file
ansible-vault create group_vars/windows_servers/vault.yml

# Add your sensitive variables
vault_ansible_password: your-windows-password
```

2. Test connectivity to your Windows hosts:
```bash
# Test with --ask-vault-pass if using vault
ansible windows_servers -i inventory/staging.yml -m win_ping --ask-vault-pass
```

3. Run playbook with different options:
```bash
# Run complete playbook
ansible-playbook -i inventory/staging.yml site.yml --ask-vault-pass

# Run with specific tags
ansible-playbook -i inventory/staging.yml site.yml --tags iis --ask-vault-pass

# Run in check mode (dry run)
ansible-playbook -i inventory/staging.yml site.yml --check --ask-vault-pass

# Run with extra variables
ansible-playbook -i inventory/staging.yml site.yml --extra-vars "iis_logging_enabled=false" --ask-vault-pass
```

## Testing

We use a comprehensive testing approach with multiple levels of validation:

### 1. Syntax Checking
```bash
# Check playbook syntax
ansible-playbook -i inventory/staging.yml site.yml --syntax-check

# Run ansible-lint
ansible-lint roles/iis
```

### 2. Molecule Testing
Each role includes Molecule tests for automated testing. To run tests:

```bash
# Install Molecule dependencies
pip install -r requirements.txt

# Run complete test sequence
cd roles/iis
molecule test

# Run individual test phases
molecule create    # Create test instance
molecule converge  # Run playbook
molecule verify    # Run tests
molecule destroy   # Clean up

# Run with debug logging
molecule --debug test
```

### 3. TestInfra Tests
Our TestInfra tests verify:
- IIS service status
- Port availability
- Feature installation
- Application pool configuration
- Website configuration

To run only TestInfra tests after converge:
```bash
molecule verify
```

### 4. Integration Testing
For testing against staging environments:

```bash
# Test against staging inventory
ansible-playbook -i inventory/staging.yml site.yml --check
ansible-playbook -i inventory/staging.yml site.yml

# Verify results
ansible windows_servers -i inventory/staging.yml -m win_service -a "name=W3SVC"
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