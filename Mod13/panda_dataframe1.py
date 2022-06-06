import pandas

df1 = pandas.DataFrame([[2,4,6],[10,20,30]])

print("Simple Data Frame")

print(df1)

df2=pandas.DataFrame([[2,4,6],[10, 20, 30]], columns=["Price", "Age", "Value"])

print("Data Frame with columns")

print(df2)

df3=pandas.DataFrame([[2,4,6],[10, 20, 30]], columns=["Price", "Age", "Value"], index=["First", "Second"])

print("Dataframes with column and index")

print(df3)

df4 = pandas.DataFrame([{"Name":"John"},{"Name":"Jack"}])

print("Dataframe with simple dictionary entries")

print(df4)

df5 = pandas.DataFrame([{"Name":"John", "Surname":"Williams"},{"Name":"Jack"}])

print("Dataframe with multi-value dictionary entries")

print(df5)

print("Determine the Mean of an individual data frame")

print(df1.mean())

print("Determine the mean of the entire table of data")

print(df1.mean().mean())

print("The current data in section 3 is:")

print(df3.Price) 

print(type(df3.Price))

print("Apply the mean function to df3")

print(df3.Price.mean())

print("Apply the max function to the df3 data")

print(df3.Price.max())

