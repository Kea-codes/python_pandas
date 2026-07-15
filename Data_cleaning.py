import pandas as pd

df = pd.read_csv("pokemon.csv")
#print(df)

#-------------DROP IRRELEVANT COLUMNS-------------
#df = df.drop(columns=["Generation" , "Speed"])
print(df)

#-------------Handle missing data----------------
#removing rows that DO have not TYPE2
df = df.dropna(subset=["Type 2"])
print(df.to_string()) #to_string to see evrything in the dataframe

#adding data where there is missing data or re-assign
df =  df.fillna({"Type 2":  "None"}) #replace NaN values of type2 with None

#--------------fixing inconsistent values---------
#change an instance of Grass to GRASS in TYPE 1
df["Type 1"] = df["Type 1"].replace({"Grass": "GRASS"})
print(df)

#-------------Standardize text-------------------
#Making the text in the  in the Name column to be lower case
df["Name"] = df["Name"].str.lower() 
print(df)


