# Dictionary Loop and String Formatting

Here is an example that combines a loop with string formatting. The loop iterates over the dictionary and generates and prints out a string in each iteration:

```
phone_numbers = {"John": +16573419912, "Jenny": +19038675309}

for pair in phone_numbers.items():
    print(f"{pair[0]} has a phone number of {pair[1]}")

```

And here is a better way to achieve the same results by iterating over keys and values:

```
phone_numbers = {"John": +1657341991, "Jenny": +19038675309}

for key, value in phone_numbers.items():
    print(f"{key} has a phone number of {value}")
```

In both cases, the output is:

```John has a phone number of +16537341991```
```Jenny has a phone number of +19038675309```