import pandas as pd


s = pd.Series([1,2,4,5], index=list('abcd'))
print(s)
print(type(s))
print('*'*30)


data = {
    '数学': [88,99,100],
    '语言': [77,88,99],
    '英语': [33,44,55]
}
s2 = pd.DataFrame(data)
print(s2)
print('*'*30)
print(s2['数学'])

print('*'*30)
print(type(s2['数学']))