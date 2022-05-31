my_data = ['1.2', '2.6', '3.3']

def sum_up(my_data):
    return sum([float(i) for i in my_data])

print(sum_up(my_data))