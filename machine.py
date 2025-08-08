import pandas as pd

df = pd.read_csv('students.csv')

print(df.dtypes)
print(df[df['Math'] == 0])
print(df)
