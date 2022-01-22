import json
import os

from features.common.file_opr import read_excel, read_yaml
from setting import data_path, page_dir, ENV


def parse_test_data():
    cases_data = read_excel(data_path, ENV)
    for case_data in cases_data:
        case_data['id'] = case_data['feature_name'] + '/' + case_data['scenario_name']
        case_data['data'] = json.loads(case_data['data'])
    return cases_data


def init_data(feature_name, scenario_name):
    s_id = feature_name + '/' + scenario_name
    for data in parse_test_data():
        if data['id'] == s_id:
            return data['data']
    return None


def read_page(page_name):
    path = os.path.join(page_dir, page_name+'.yml')
    data = read_yaml(path)
    return data

