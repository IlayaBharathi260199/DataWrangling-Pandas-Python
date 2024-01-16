import pandas as pd

df = pd.read_csv("C:/Users/ILAYA BHARATHI M/Desktop/Pandas data/Cricket_Data_final2.csv")
print(df.dtypes)

#Q1.Find total career year for each player
df['Career_Years'] = df['FinalYear'] - df['FirstYear']
print(df)

#Q2.Avg career length
avg = df['Career_Years'].mean()
print(avg)

#Q3.Get Avg SR ['Career_Years'] > 10 ]
df1=df[df['Career_Years'] > 10 ]['SR'].mean()
print(df1)

#Q4. Select Player and Country, who played before 1960
print(df[df['FirstYear'] < 1960][['Player','Country']])

#Q5.Get the high_score from each country and sort descending order
print(df.groupby('Country')['High_Score'].max().to_frame('maxScore').sort_values('maxScore',ascending = False))

#Q6.Get the count of each country
print(df.groupby('Country').count())

# Check if any duplicates are exist or not
print(df.duplicated().any())

# Count df column based
print(df.count())

# Select single column
print(df['Country'])

# Change all columns to upper
print(df.columns.str.upper())

# show number of rows and columns
print(df.shape)

# show Distinct or unique value from Country
print(df['Country'].unique())

# get Number of players from Each country
print(df.groupby('Country')['Player'].count().to_frame('count').reset_index())