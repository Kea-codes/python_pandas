import pandas as pd

df = pd.read_csv("pokemon.csv")
#print(df)

# FILTERING POKEMONS WITH SPEED OF 120 AND ABOVE
faster_pokemon = df[df["Speed"] >= 120]
#print(faster_pokemon)

# ATTACK MORE THAN 100
Attack_pokemon = df[df["Attack"]>= 100]
#print(Attack_pokemon)

# LEGENDARY POKEMON
legendary_pokemo = df[df["Legendary"] == True]
#print(legendary_pokemo)

# OR , AND OPERATORS
#POKEMONS WITH TYPE1 WATER OR TYPE2 WATER
water_pokemons = df[(df["Type 1"] == "Water") | (df["Type 2"]== "Water")]
#print(water_pokemons)

FF_pokemons = df[(df["Type 1"] == "Fire") & (df["Type 2"]== "Flying")]
print(FF_pokemons)