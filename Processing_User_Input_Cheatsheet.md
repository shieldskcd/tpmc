# Cheatsheet: Processing User Input

In this section, we learned the following items:

## A Python program can get *user input* via the ```input``` fucntion:

### The *input fucntion* halts the exectuion of the program and gets text input from the user:

``` name = Input("Enter your name: ") ```

### The input function converts any *input to a string*, but you can convert it back to int or float:

``` experience_months = input("Enter your experience in months: ")```
``` experience_years = int(exeprience_months) / 12 ```

## You can also *format strings* with:

```
name = "Sam"
experience_years = 1.5
print("Hi {}, you have {} years experience".format(name, experince_years))
```
Output: ```Hi Sam, you have 1.5 years experience.```