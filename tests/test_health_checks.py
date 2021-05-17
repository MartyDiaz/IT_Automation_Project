#!/usr/bin/env python3

import pytest
from unittest import mock
from health_checks import check_cpu, check_disk_space, check_memory, \
    check_localhost_name_resolution, check_systems

@pytest.mark.parametrize("_input, expected", [(20, True), (80, False)])
@mock.patch("health_checks.psutil.cpu_percent")
def test_check_cpu(mock_psutil_cpu_percent, _input, expected):
    mock_psutil_cpu_percent.return_value = _input
    assert check_cpu(50) == expected
    mock_psutil_cpu_percent.assert_called()


@pytest.mark.parametrize(
    "_input, expected",
    [((1000,900,100),False),
     ((1000,100,900), True)]
)
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


@pytest.mark.parametrize(
    "_input, expected",
    [('127.0.0.1', True), ('123.0.0.1', False)]
)
@mock.patch("health_checks.socket.gethostbyname")
def test_check_localhost_name_resolution(
        mock_socket_gethostbyname,
        _input,
        expected
):
    mock_socket_gethostbyname.return_value = _input
    assert check_localhost_name_resolution() == expected
    mock_socket_gethostbyname.assert_called()


@pytest.mark.parametrize(
    "_input, expected",
    [([True, True, True], 0), ([False, False, False], 3)]
)
@mock.patch("health_checks.email_health_error")
@mock.patch("health_checks.check_cpu")
@mock.patch("health_checks.check_disk_space")
@mock.patch("health_checks.check_localhost_name_resolution")
def test_check_systems(
        mock_check_localhost_name_resolution,
        mock_check_disk_space,
        mock_check_cpu,
        mock_email_health_error,
        _input, expected
):
    mock_check_localhost_name_resolution.return_value = _input[0]
    mock_check_disk_space.return_value = _input[1]
    mock_check_cpu.return_value = _input[2]
    check_systems()
    assert mock_email_health_error.call_count == expected

