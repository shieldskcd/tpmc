student_grades = {"Mary": 9.1, "Sam": 8.8, "John": 7.5}


## Show all items
for grades in student_grades.items():
    print(grades)

## Show keys
for grades in student_grades.keys():
    print(grades)

## Show only values
for grades in student_grades.values():
    print(grades)