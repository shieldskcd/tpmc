# Cheatsheet: Loops

In this section, we learned the following items:

## A *for-loop* is useful to repeatedly execute a block of code. 

### You can create a *for-loop* like so:

```
for letter in 'abc':
    print(letter.upper())
```

Output would be:
```
A
B
C
```

As you can see, the for-loop repeatedly converted all the items of ```abc``` to uppercase. 

### The name after ```for``` (e.g. ```letter```) is just a variable name. 

## You can loop over *dictionary keys* as follows:

```
phone_numbers = {"John Smith":"+19042929288", "Jenny Smith":" "+19038675309"}
    for value in phone_numbers.keys():
        print(value)
```

Output would be:

```
John Smith
Jenny Smith
```

## You can loop over *dictionary values*:

```
phone_numbers = {"John Smith":"+19042929288", "Jenny Smith":" "+19038675309"}
    for value in phone_numbers.values():
        print(value)
```

Output would be:

```
+19042929288
+19038675309
```

## You can loop over *dictionary items*:

```
phone_numbers = {"John Smith":"+1904292928", "Jenny Smith":" "+"}
    for key, value in phone_numbers.items():
        print(key, value)
```

Output would be:

```
John Smith: +19042929288
Jenny Smith: 19038675309
```

## We also have *while-loops*. The code under a while-loop will run as long as the while-loop condition is true:

```
while datetime.datetime.now() < datetime.datetime(2090, 8, 20, 19, 20, 30):
    print ("It's not yet 19:30:20 of 2090.8.20")

```

The loop above will print out the string inside ```print()``` over and over again until the 20th of August, 2090. 