#!/usr/bin/env python3

import pytest
from unittest import mock
from health_checks import check_cpu, check_disk_space, check_memory, \
    check_localhost_name_resolution


@pytest.mark.parametrize("_input, expected", [(20, True), (80, False)])
@mock.patch("health_checks.psutil.cpu_percent")
def test_check_cpu(mock_psutil_cpu_percent, _input, expected):
    mock_psutil_cpu_percent.return_value = _input
    assert check_cpu(50) == expected
    mock_psutil_cpu_percent.assert_called()

@pytest.mark.parametrize("_input, expected", [((1000,900,100),False), ((1000,100,900), True)])
@mock.patch("health_checks.shutil.disk_usage")
def test_check_disk_space(mock_shutil_disk_usage, _input, expected):
    mock_shutil_disk_usage.return_value = _input
    assert check_disk_space(25) == expected
    mock_shutil_disk_usage.assert_called()


@pytest.mark.parametrize("_input, expected", [(1000, True), (200, False)])
@mock.patch("health_checks.psutil.virtual_memory")
def test_check_memory(mock_psutil_virtual_memory, _input, expected):
    mock_psutil_virtual_memory.return_value = mock.Mock(**{"available": _input})
    assert check_memory(500) == expected
    mock_psutil_virtual_memory.assert_called()

@pytest.mark.parametrize("_input, expected", [('127.0.0.1', True), ('123.0.0.1', False)])
@mock.patch("health_checks.socket.gethostbyname")
def test_check_localhost_name_resolution(mock_socket_gethostbyname, _input, expected):
    mock_socket_gethostbyname.return_value = _input
    assert check_localhost_name_resolution() == expected