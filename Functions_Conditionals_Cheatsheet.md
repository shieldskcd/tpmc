# Cheatsheet: Functions and Conditionals

In this section we learned the following items:

## Define **functions**

```
def cube_volume(a):
    return a * a * a
```

## Write **if-else conditionals**

```
message = "hello there"

if "hello" in message:
    print ("hi")
else:
    print("I don't understand")
```

## Write **if-elif-else conditionals**

```
message = "Hello There"

if "hello" in message:
    print("hi")
elif "hi" in message:
    print("hi")
elif "hey" in message:
    print("hi")
else:
    print("I don't understand")

```
## Use the ``` and ``` operator to check if **both conditions** are True at the same time:

```
x = 1
y = 1

if x == 1 and y ==1:
    print("Yes")
else:
    print("No")

```

## Use the ``` or ``` operator to check if **at least one condition** is True:

```
x = 1
y = 2

if x == 1 or y ==2:
    print("Yes")
else:
    print("No")

```
## Check if a value is of a particular **type** with **isinstance**:

```
isinstance("abc", str)
isinstance([1, 2, 3], list)

```
### or directly:

```
type("abc") == str
type([1,2,3]) == lst
```
