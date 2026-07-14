import pandas as pd

df = pd.read_csv("pokemon.csv")
#print(df)

#--------------WHOLE DATAFRAM--------------------

# FIND THE MEAN OF ALL THE COLUMNS WITH NUMBERS
# print(df.mean(numeric_only=True))
# FIND THE SUM OF ALL THE COLUMNS WITH NUMBERS
# print(df.sum(numeric_only=True))
# FIND THE MIN OF ALL THE COLUMNS WITH NUMBERS
# print(df.min(numeric_only=True))
# FIND THE MAX OF ALL THE COLUMNS WITH NUMBERS
# print(df.max(numeric_only=True))
# FIND THE NUMBER OF ALL THE COLUMNS WITH NUMBERS
# print(df.count())

#--------------SINGLE COLUMN----------------------

# THE MEAN OF THE SPEED
# print(f"Average speed:  {df["Speed"].mean()}")
# print(f"Sum of speed:  {df["Speed"].sum()}")
# print(f"Min speed:  {df["Speed"].min()}")
# print(f"Max speed:  {df["Speed"].max()}")
# print(f"Count of the row-speed:  {df["Speed"].count()}") #NUMBER OF ROWS WITH SPEED


#------------Grouping by---------------------

#grouping by type 1
# group = df.groupby("Type 1") # GRASS FIRE ROCK ...
# print(group["Speed"].mean()) # THE AVERAGE SPEED FOR EACH GROUP
# print(group["Speed"].sum()) # THE SUM SPEED FOR EACH GROUP
# print(group["Speed"].min()) # THE MIN SPEED FOR EACH GROUP
# print(group["Speed"].max()) # THE MAX SPEED FOR EACH GROUP
# print(f"ROWS: {group["Speed"].count()}") # THE TOTAL row NUMBER FOR EACH GROUP