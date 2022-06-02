# Write the first 90 characters of the bear.txt file

file = open("bear.txt")
bear_con = file.read()
file.close()

print(bear_con[:90])