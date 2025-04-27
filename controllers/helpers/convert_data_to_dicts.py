def convert_data_to_dicts(headers, data):
    return [dict(zip(headers, row)) for row in data]
