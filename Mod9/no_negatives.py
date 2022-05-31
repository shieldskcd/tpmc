my_data = [-5, 3, -1, 101]

def pos_parse(my_data):
    return [ i for i in my_data if i > 0]
print(pos_parse(my_data))