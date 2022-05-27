phone_numbers = {"John": +16573419912, "Jenny": +19038675309}

for pair in phone_numbers.items():
    print(f"{pair[0]} has a phone number of {pair[1]}")

phone_numbers = {"John": +16573419912, "Jenny": +19038675309}
for key, value in phone_numbers.items():
    print(f"{key} has a phone number of {value}")