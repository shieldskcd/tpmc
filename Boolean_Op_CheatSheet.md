# Boolean Operators "and" and "or"

## So far we have learend how to check for a single condition:

```
x = 1

if x == 1:
    print("Yes")
else:
    print("No")

```
## You can also check if two conditions are met at the same time using an ```and``` operator:

```
x = 1
y = 1

if x ==1 and y == 1:
    print("Yes")
else:
    print("No")
```
This will return ```Yes``` since ```x == 1``` and ```y == 1``` are both true.

## You can also check if one of two conditions are met using an ```or``` operator:

```
x = 1
y = 1

if x ==1 or y == 2:
    print("Yes")
else:
    print("No")
```
This will return ```Yes``` since at least one of the conditions is True. In this case ```x == 1 ``` is True. 