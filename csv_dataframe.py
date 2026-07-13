import pandas as pd

# CREATING THE DATAFRAME AND READING THE CSV FILE
df = pd.read_csv("pokemon.csv", index_col = "Name") #Setting theindex of the rows to be names
print(df) # PRINTING THE DATA FRAME

# SELECTION BY COLUMN
# print(df["Name"].to_string()) # to_string() allows printing of all names
# PRINTING A LIST OF LISTS => MULTIPLE COLUMNS
#print(df[["Name", "Speed", "Defense"]])

# SELECTION BY ROWS
#print(df.iloc[1:10]) # LOKING FOR THE FIRST 10 ROWS
#print(f"Pikachu:\n{df.loc["Pikachu"]}")

user_input = input("ENTER THE POKEMON NAME: ")

try:
    print(df.loc[user_input])
except:
    print(f"{user_input} DOES NOT EXIST")





