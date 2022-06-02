with open("bear1.txt", "r") as file1:
    content1 = file1.read()

with open("bear2.txt", "a") as file2:
    file2.write(content1)
