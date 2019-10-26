from animals import *

#k = [{'animal':'hamster', 'age':0.5, 'visits':1, 'priority':'No'}]
#df = df.append(k)
df.loc['k'] = ['hamster', 0.5, 1, 'No']
print(df)

df = df.drop('k')
print("\n", df)