import pandas as pd

df = pd.read_csv('pokemon_data.csv')

print(df.head(3))

##Read Headers
print(df.columns)

##Read each Column
print(df[['Name','Type 1','HP']])

##Read Each Row
#prints row,range of rows
print(df.iloc[1:4])

##Read through rows in list
for index, row in df.iterrows():
   print(index, row['Name'])


#Target data with parameter
print(df.loc[df['Type 1'] == "Fire"])


##Read specific Location (Row,Column)

##Read specific cells
print(df.iloc[2,1])


##Gives data such as avg, min, max
print(df.describe())

##sorting with multiple parameters
print(df.sort_values(['Name','HP'],ascending=[1,0]))

##modify column of totals
df['Total'] = df['HP']+df['Attack']+df['Defense']+df['Sp. Atk']+df['Sp. Def']+df['Speed']
df = df.drop(columns=['Total'])
df['Total'] = df.iloc[:,4:10].sum(axis = 1)
##move column
cols = list(df.columns.values)
df = df[cols[0:4] + [cols[-1]] + cols[4:12]]

print(df.head(5))

##save updated csv
df.to_csv('modified.csv', index = False)

print(df.loc[(df['Type 1'] == 'Grass') & (df['Type 2'] == 'Poison')])
print(df.loc[(df['Type 1'] == 'Grass') | (df['Type 2'] == 'Poison')])

##new dataframe to csv
new_df = df.loc[(df['Type 1'] == 'Grass') | (df['Type 2'] == 'Poison') & (df['HP'] > 70)]
new_df.reset_index(drop = True, inplace = True)
new_df.to_csv('filtered.csv')
print(new_df)

##filter out ones that include condition (~ is not)
df.loc[~df['Name'].str.contains('Mega')]

##RegEx  flags = re.I means ignore case
#import re

#df.loc[~df['Name'].str.contains('fire|grass', flags = re.i, regex = True)]
#new_df = df.loc[df['Name'].str.contains('pidg[a-z]*', flags=re.I, regex = True)]

##replace text on condition
df.loc[df['Type 1'] == 'Fire', 'Type 1'] = 'Flame'

##Groupby
df = pd.read_csv('modified.csv')
new_df = df.groupby(['Type 1']).mean().sort_values('Attack', ascending=False)
new_df = df.groupby(['Type 1']).sum()

#count by type
df['count'] = 1
new_df = df.groupby(['Type 1']).count()['count']
print(new_df)


##workin with large amounts of data with chunks this example gives in rows
new_df = pd.DataFrame(columns=df.columns)

for df in pd.read_csv('modified.csv', chunksize = 5):
       print("CHUNK DF")


new_df = pd.DataFrame(columns=df.columns)
for df in pd.read_csv('modified.csv', chunksize = 5):
    results = df.groupby(['Type 1']).count()

    new_df = pd.concat([new_df, results], sort=False)
print(new_df)




