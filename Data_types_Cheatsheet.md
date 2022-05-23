# Cheatsheet: Data Types in Python
Here is a summary of the various data types found in Python and what they contain.

## **Integers** are used to represent whole numbers
- rank = 10
- eggs = 12
- people = 3

## **Floats** represent decimal numbers
- temperature = 88.5
- rainfall = 1.2
- elevation = 5548.7

## **Strings** represent text
- message = "Welcome to our website"
- name = "John"
- serial = "R001199RT2WSQ"

## **Lists** represent arrays of values that may change during the course of the program.
- members = ["Sammy Sosa", "Babe Ruth", "Barry Switzer"]
- pixel_values = [252, 251, 251, 253, 250, 248, 247]

## **Dictionaries** reprsent pairs of keys and values
- phone_numbers = {"John Smith" : "+13755457843", "Jenny Smith:" : "+19038675309"}
- volcano_elevations = {"Glacier Peak" : 3213.9, "Rainer" : 4392.1}

### **Keys** of a dictionary can be extracted with:
``` phone_numbers.keys()```

### **Values** of a dictionary can be extracted with:
``` phone_numbers.values()```

## **Tuples** represent arrays of values that are not to be changed during the course of the program:
- vowels = ('a', 'e', 'i', 'o', 'u')
- single_digits = (0 ,1 , 2, 3, 4, 5, 6, 7, 8 9)

## You can get a list of **attributes** of a data type using:
- ```dir(str)```
- ``` dir(list)```
- ``` dir(dict) ```

## You can get a list of Python's **built-in functions** using:
``` dir(__builtins__)```

## You can get the **documentation** of a Python data type using:
- ``` help(str) ```
- ``` help(str.replace)```
- ``` help(dict.values) ```