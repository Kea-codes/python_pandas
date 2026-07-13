import pandas as pd

# Dictionary of employees and

data = {"Name": ["Kam", "Tshiamo", "Matsu", "Genzu"] , "AGE": [30,35, 40, 50]}

df = pd.DataFrame(data, index = ["employee1","employee2","employee3","employee4" ])
print(df)

# I WANT INFO OF EMPLOYEE 1 
print(f"\nEmployee 1 INFO: {df.loc['employee1']}")
# INTEGER LOCATION
print(f"Integer location 2: {df.iloc[2]}")

# ADDING A NEW COLUMN
df["job"] =["COOK", "SHOP CASHIER", "MANAGER", "HR"]
print(df)

# ADDING A NEW ROW
new_row = pd.DataFrame([{"Name": "Sandy", "AGE": 28, "job": "Engineer"}] , index = ["employee4"])
df = pd.concat([df, new_row])
print(df)

