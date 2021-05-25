import pytest
import os
from report_email import read_data


def test_read_data():
    test_description_directory = os.path.join(
        os.path.expanduser('~'),
        'Documents/'
        'google_class/'
        'project_8/'
        'tests/'
        'test_data/'
        'read_data'
    )

    name_list, weight_list = read_data(test_description_directory)
    test_name_list = ['Avocado', 'Apple']
    test_weight_list = ['200 lbs', '500 lbs']
    assert (name_list == test_name_list)
    assert (weight_list == test_weight_list)