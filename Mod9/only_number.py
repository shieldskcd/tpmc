my_data = [99, 'no data', 95, 94, 'no data']

def data_parse(my_data):
    return [ i for i in my_data if isinstance(i, int)]

print(data_parse(my_data))