import os
import pytest

import testinfra.utils.ansible_runner

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ['MOLECULE_INVENTORY_FILE']).get_hosts('all')

@pytest.mark.parametrize('file, content', [
  ('/etc/passwd', 'testuser'),
  ('/etc/group', "testgroup.*testuser"),
  ('/home/testuser/.ssh/authorized_keys', 'testuser@key'),
])

def test_files(host, file, content):
    file = host.file(file)

    assert file.exists
    assert file.contains(content)
