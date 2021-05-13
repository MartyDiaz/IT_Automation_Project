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
