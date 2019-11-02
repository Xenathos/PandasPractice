import pandas as pd

df = pd.read_csv('pokemon_data.csv')

##print(df.head(3))


##Read Headers
#print(df.columns)


##Read each Column
#print(df[['Name','Type 1','HP']])



##Read Each Row
#prints row,range of rows
#print(df.iloc[1:4])

##Read through rows in list
#for index, row in df.iterrows():
#    print(index, row['Name'])


#Target data with parameter
#print(df.loc[df['Type 1'] == "Fire"])


##Read specific Location (Row,Column)

##Read specific cells
#print(df.iloc[2,1])


##Gives data such as avg, min, max
#print(df.describe())

##sorting with multiple parameters
#print(df.sort_values(['Name','HP'],ascending=[1,0]))

##modify column of totals
#df['Total'] = df['HP']+df['Attack']+df['Defense']+df['Sp. Atk']+df['Sp. Def']+df['Speed']
#df = df.drop(columns=['Total'])
df['Total'] = df.iloc[:,4:10].sum(axis = 1)
#move column
cols = list(df.columns.values)
df = df[cols[0:4] + [cols[-1]] + cols[4:12]]

print(df.head(5))

##save updated csv
df.to_csv('modified.csv')
