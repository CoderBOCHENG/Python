import pandas as pd

print("---Create a pandas series from a list -----------------")

series1 = pd.Series([4, 7, -5 ,3])
print(series1)

print("\n\n--By default: its index is 0 based -----------------")
print(series1.index)

print("\n\n--By default: its value -----------------")
print(series1.values)


print("---Create a pandas series from a list, with specified index -----------------")

series1 = pd.Series([4, 7, -5 ,3], index=['d', 'c', 'b', 'a'])
print(series1)

print("\n\n--By default: its index is 0 based -----------------")
print(series1.index)

print("\n\n--By default: its value -----------------")
print(series1.values)


print("\n\n--Show me its value with index 'a' -----------------")
print(series1['a'])


print("\n\n--Assign new values-----------------")
series1['a'] = 6
print(series1['a'])

print("\n\n--Filtering -----------------")
print(series1[series1 > 3])
