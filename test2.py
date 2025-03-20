import pandas as pd

# Creating a dictionary
data = {
    'Name': ['Alice', 'Bob', 'Charlie',None],
    'Age': [25, 30, 35, 48],
    'City': ['New York', 'San Francisco', 'Chicago',None]
}

# Creating a DataFrame
df = pd.DataFrame(data)

# Displaying the DataFrame
print(df)

# Accessing a single column
names = df['Name']
print(names)

# Accessing multiple columns
ages_and_cities = df[['Age', 'City']]
print(ages_and_cities)

# Accessing rows by index
first_row = df.iloc[0]
print(first_row)

# Accessing rows by label
alice_row = df.loc[df['Name'] == 'Alice']
print(alice_row)

print("-----------------------")
morethan30 = df[df['Age'] > 29]
print(morethan30)
print("-----------------------")


print("-----------------------")
morethan30 = df[df['Name'].notna()][df['Age'] > 29]
print(morethan30)
print("---------#######################--------------")



# Sample DataFrames
df1 = pd.DataFrame({
    'A': ['A0', 'A1', 'A2'],
    'B': ['B0', 'B1', 'B2']
})

df2 = pd.DataFrame({
    'A': ['A3', 'A4', 'A5'],
    'B': ['B3', 'B4', 'B5']
})

# Concatenate DataFrames by rows
result = pd.concat([df1, df2], axis=0)

# Display the result
print(result)

print("---------###########!!!!!!!!!!!!!!!!!!!!!!!!!!!############--------------")
# Sample DataFrames
df1 = pd.DataFrame({
    'A': ['A0', 'A1', 'A2']
})

df2 = pd.DataFrame({
    'B': ['B0', 'B1', 'B2']
})

df2 = pd.DataFrame({
    'B': ['B0', 'B1', 'B2']
})

# Concatenate DataFrames by columns
result = pd.concat([df1, df2], axis=1)

# Display the result
print(result)

print("AAAAALLLLLLLICE")

# Accessing rows by label
alice_row = df[df['Name'] == 'Alice']
print(alice_row)
