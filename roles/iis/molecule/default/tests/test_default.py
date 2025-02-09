import os
import testinfra.utils.ansible_runner

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ['MOLECULE_INVENTORY_FILE']).get_hosts('all')

def test_iis_service_running(host):
    iis_service = host.service('W3SVC')
    assert iis_service.is_running
    assert iis_service.is_enabled

def test_iis_listening_80(host):
    socket = host.socket('tcp://0.0.0.0:80')
    assert socket.is_listening

def test_default_website_directory(host):
    website_dir = host.file('C:\\inetpub\\wwwroot')
    assert website_dir.exists
    assert website_dir.is_directory

def test_iis_features_installed(host):
    # Test for core IIS feature
    cmd = host.run('powershell -Command "Get-WindowsFeature Web-Server | Select-Object -ExpandProperty InstallState"')
    assert cmd.succeeded
    assert 'Installed' in cmd.stdout

def test_app_pool_exists(host):
    cmd = host.run('powershell -Command "Import-Module WebAdministration; Test-Path IIS:\\AppPools\\DefaultAppPool"')
    assert cmd.succeeded
    assert 'True' in cmd.stdout 