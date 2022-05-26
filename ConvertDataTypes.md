# Converting Between Data Types

Sometimes you might need to convert between different data types in Python for one reason or another. That is very easy to do:

## From Tuple to list:

``` >>> cool_tuple = (1, 2, 3)```
```>>> cool_list = list(cool_tuple)```
```>>> cool_list```
```[1, 2, 3]```

## From List to Tuple:

``` >>> cool_list = [1, 2, 3] ```
``` >>> cool_tuple = tuple(cool_list) ```
``` >>> cool_tuple ```
``` (1, 2, 3) ```

## From string to list:

``` >>> cool_string = "Hello" ```
``` >>> cool_list = str.join("", cool_list) ```
``` >>> cool_list ```
``` ['H', 'e', 'l', 'l', 'o'] ```

## From list to string:

``` >>> cool_list = ['H', 'e', 'l', 'l', 'o'] ```
``` >>> cool_string = str.join("", cool_list) ```
``` >>> cool_string ```
``` 'Hello' ```

As scan be seen above, converting a list into a string is more complex. Here ``` str()``` is not sufficient. We need ```str.join()```. Try running the code above again, but this time using ```str.join("---", cool_list) ``` in the second line. You will understand how ```str.join()``` works.