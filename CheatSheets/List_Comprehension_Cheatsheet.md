# Cheatsheet: List Comprehensions

In Module 9 we learned the following items:

* A list comprehension is an expression that creates a list by iterating over another container.
* A **basic** list comprehension example:
```
[i*2 for i in [1, 5, 10]]
```
Output would be: ``` [2, 10, 20]```

* List comprehension with the **if** condition:

```
[i*2 for i in [1, -2, 10] if i>0]
```

Output would be: ``` [2, 20]```

* List comprehension with an **if and else** condition:
```
[i*2 if i>0 else 0 for i in [1, -2, 10]]
```

Output would be: ```[2, 0, 20]```