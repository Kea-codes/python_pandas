import pandas as pd

calories = {"day1": 420,"day2": 380, "day3": 390, "day4": 400, "day5": 450}

series = pd.Series(calories)
print(f"printing the series:\n{series}")

#Number of calories on day 1
print(f"Number of calories on day 1: {series['day1']}")

# updating the value of calories on day 3
series['day3']= 500


# adding calories for day 5
series['day5'] += 60
print(f"Adding calories for day 5 from 450 to 510:\n{series}")