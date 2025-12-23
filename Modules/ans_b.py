import pandas as pd

data ={
    'ID': [1, 2, 3],
    'Name': ['Alice', 'Bob', 'Charlie'],
    'Math': [85, 90, 78],
    'Science': [92, 88, 95],
    'English': [88, 76, 90]

}

df = pd.DataFrame(data)


# also there are some operations 

print(df)
print(df.info())
print(df.describe())
print(df['Name'])