my_data = [99, 'no data', 95, 94, 'no data']

def data_parse(my_data):
    return [i if not isinstance(i, str) else 0 for i in my_data]

print(data_parse(my_data))