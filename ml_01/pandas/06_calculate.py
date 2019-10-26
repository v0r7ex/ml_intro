from animals import *

df = df.groupby('animal')
print('Dogs: ', df.get_group('dog').mean()[0])
print('Cats: ', df.get_group('cat').mean()[0])
print('Snakes: ', df.get_group('snake').mean()[0])
