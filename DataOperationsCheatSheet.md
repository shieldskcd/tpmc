# Cheatsheet: Operations with Data Types

In section 4, we learned the following things:

* Lists, strings, and tuples have a **positive index** system:

```
["Mon", "Tue", "Wed", "Thurs", "Fri", "Sat", "Sun"]
    0      1     2       3       4      5       6
```
* And they have a **negative index** system as well:

```
["Mon", "Tue", "Wed", "Thurs", "Fri", "Sat", "Sun"]
  -7      -6     -5       -4     -3     -2     -1
```

* In a list, the **2nd**, **3rd**, and **4th** items can be accessed with:

```
days = ["Mon", "Tue", "Wed", "Thurs", "Fri", "Sat", "Sun"]
days[1:4]
Output: ['Tue', 'Wed' , 'Thu']

```

* First three items of a list:

```
days = ["Mon", "Tue", "Wed", "Thurs", "Fri", "Sat", "Sun"]
days[:3]
Output: ['Mon', 'Tue' , 'Wed']
```

* Last three items of a list:

```
days = ["Mon", "Tue", "Wed", "Thurs", "Fri", "Sat", "Sun"]
days[-3:]
Output: ['Mon', 'Tue' , 'Wed']
```

* Everything but the last:

```
days = ["Mon", "Tue", "Wed", "Thurs", "Fri", "Sat", "Sun"]
days[:-1]
Output: ['Mon', 'Tue' , 'Wed']
```

* Everything but the last two:

```
days = ["Mon", "Tue", "Wed", "Thurs", "Fri", "Sat", "Sun"]
days[:-2]
Output: ['Mon', 'Tue' , 'Wed']
```

* A dictionary **value** can be accessed using its corresponding dictionary **Key**:

```
phone_numbers = {"John": "+19047650123", "Jenny":"+19378675309"}
phone_numbers["Jenny"]
Output: '+19378675309'
````