import pandas as pd

data = [100,103, 104, 105, 106]

series = pd.Series(data, index= ["a","b","c", "d", "e"])

print(f"printing values greater than or equal to 103:\n{series[series>=103]}")

# # LOCATING A VLUE AT A VERTAIN LABLE
# print(f"Locating a value at lable a: {series.loc["a"]}")
# print(f"Locating a value at lable b: {series.loc["b"]}")
# print(f"Locating a value at lable c: {series.loc["c"]}")

# # INTEGER LOCATION
# print(f"printing integer location index 0: {series.iloc[0]}")
# print(f"printing integer location index 1: {series.iloc[1]}")
# print(f"printing integer location index 2: {series.iloc[2]}")
