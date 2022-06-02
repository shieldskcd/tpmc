def upper(*args):
    args = [x.upper() for x in args]
    return sorted(args)

print(upper("snow", "ice", "glacier"))