import openpyxl
import yaml
from yaml import Loader


def read_excel(path, sheet_name='Sheet1'):
    wb = openpyxl.load_workbook(path)
    sheet = wb[sheet_name]

    rows_data = list(sheet.rows)

    headers = []
    for header in rows_data[0]:
        headers.append(header.value)

    result = []
    for row in rows_data[1:]:
        data = {}
        row_data = list(row)
        for i in range(0, len(row_data)):
            data[headers[i]] = row_data[i].value
        result.append(data)
    return result


def read_yaml(path):
    with open(path) as f:
        data = yaml.load(f, Loader)
    f.close()
    return data


