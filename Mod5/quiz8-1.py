def temp(temperature):
    if temperature > 25:
        temperature = "Hot"
        return temperature
        print(temp())

    elif 25 >= temperature >= 15:
        temperature = "Warm"
        return temperature
        print(temp())

    else:
        temperature = "Cold"
        return temperature
        print(temp())

print(temp(29))