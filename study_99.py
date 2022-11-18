from pandas import DataFrame

data = {'name': ['zs', 'ls', 'ww'], 'age': [11, 12, 13], 'gender': ['man', 'man', 'woman']}
df = DataFrame(data)
df.to_excel('new.xlsx', 'sheet1')

df.to_excel('new.xlsx', 'sheet2')
