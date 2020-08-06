import os
import pytest

import testinfra.utils.ansible_runner

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ['MOLECULE_INVENTORY_FILE']).get_hosts('all')


@pytest.mark.parametrize('package', ['sudo', 'python3', 'bash'])

def test_package_is_installed(host,package):
    pkg = host.package(package)
    assert pkg.is_installed

