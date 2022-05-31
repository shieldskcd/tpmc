temps = [221, 234, 340, 230]

# Common way to handle lists using a list interation loop
# new_temps = []
# for temp in temps:
#    new_temps.append(temp / 10)

# List Comprehension example
new_temps = [temp /10 for temp in temps]

print(new_temps)