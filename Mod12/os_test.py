import time
import os 

while True:
    if os.path.exists("files/vegetables.txt"):
        with open("files/vegetables.txt") as file:
            print(file.read())
    else:
        print("File Does Not Exist!")
    time.sleep(10)