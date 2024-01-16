import pandas as pd

pd.set_option('display.max.rows', 70)  # will show us 70 rows (we can change as per our requirement)

# Reading data as CSV
df = pd.read_csv(r"C:\Users\ILAYA BHARATHI M\Desktop\dataWrangling\DataWrangling-Pandas-Python\Data\Raw\Cricket_Data1.csv")
print(df.count())
# printing Schema
print(df.dtypes)

# Rename Columns
df1 = df.rename(columns={'HS': "High_Score", 'BF': 'Balls_Faced', 'Ave': 'Avg', '100': 'Cenrury', '50': 'Half_century'})
print(df1.info())

# Check if Duplicates are present or not
print(df1.duplicated().any())
print(df[df.duplicated()])

# Remove Duplicates
df2 = df1.drop_duplicates()
print(df2.duplicated().any())

# Split and Add new columns in df2
df2['Country'] = df2['Player'].str.split(pat='(').str.get(1)
df2['FirstYear'] = df2['Span'].str.split('-').str[0]
df2['FinalYear'] = df2['Span'].str.split('-').str[1]
df2['Player'] = df2['Player'].str.split(pat='(').str.get(0)

# Replace unnecessary special characters(+,*,/) from data
df2['Country'] = df2['Country'].str.replace('[^a-zA-Z0-9]', '', regex=True)
df2['Country'] = df2['Country'].str.replace('ICC', '', regex=True)
df2['4s'] = df2['4s'].str.replace('[^a-zA-Z0-9]', '', regex=True)
df2['6s'] = df2['6s'].str.replace('[^a-zA-Z0-9]', '', regex=True)
df2['Balls_Faced'] = df2['Balls_Faced'].str.replace('[^a-zA-Z0-9]', '', regex=True)
df2['High_Score'] = df2['High_Score'].str.replace('[^a-zA-Z0-9]', '', regex=True)

# Drop Multiple columns
dropColumns = ['Span']
df3 = df2.drop(dropColumns, axis=1)

# Rename Column name
df4 = df3.rename(columns={'Cenrury': 'Century'})
print(df4['Century'])

# Check Null Values
print(df4.isnull().any())

# Check Number of NUll per Column
print(df4.isnull().sum())

# Replace Null With '0'
df4['Balls_Faced'] = df4['Balls_Faced'].fillna(0)
df4['SR'] = df4['SR'].fillna(0)

# Change Datatypes
df5 = df4.astype({'FinalYear':'int','FirstYear':'int'})

df5['Career_length'] = df5['FinalYear'] - df5['FirstYear']

# Final Check
print('========Null=========')
print(df4.isnull().any())
print('========Duplicates===')
print(df4.duplicated())
print('========NullCounts====')
print(df4.isnull().sum())

# Writing Cleansed data
df4.to_csv(r'C:\Users\ILAYA BHARATHI M\Desktop\dataWrangling\DataWrangling-Pandas-Python\Data\Cleansed\Cricket_Data1_cleansed.csv', index=False)

print(df5.dtypes)
print(df5)

