"""
Question 3-

Write a program, which would download the data from the provided link, and then read the data and convert
that into properly structured data and return it in Excel format.

Note - Write comments wherever necessary explaining the code written.

Link - https://raw.githubusercontent.com/Biuni/PokemonGO-Pokedex/master/pokedex.json


Data Attributes - id: Identification Number - int num: Number of the
● Pokémon in the official Pokédex - int name: Pokémon name -
● string img: URL to an image of this Pokémon - string type:
● Pokémon type -string height: Pokémon height - float
● weight: Pokémon weight - float candy: type of candy used to evolve Pokémon or
given
● when transferred - string candy_count: the amount of candies required to evolve
- int
● egg: Number of kilometers to travel to hatch the egg - float spawn_chance:
● Percentage of spawn chance (NEW) - float avg_spawns: Number of this
pokemon on 10.000 spawns (NEW) - int
● spawn_time: Spawns most active at the time on this field. Spawn times are the same for all
time zones and are expressed in local time. (NEW) - “minutes: seconds” multipliers:
Multiplier of Combat Power (CP) for calculating the CP after evolution See below - list of int
weakness: Types of
● Pokémon this Pokémon is weak to - list of strings next_evolution: Number and Name of
successive evolutions of Pokémon - list of dict prev_evolution: Number and Name of previous
evolutions of Pokémon - - list of dict

"""

##Ans:

import requests
import pandas as pd

# Downloading the data from the provided link
url = "https://raw.githubusercontent.com/Biuni/PokemonGO-Pokedex/master/pokedex.json"
response = requests.get(url)

# Converting the data into a pandas dataframe
data = response.json()
df = pd.json_normalize(data["pokemon"])

# Saving the dataframe to an Excel file
df.to_excel("pokemon_data.xlsx", index=False)

print("Data saved to pokemon_data.xlsx")

'''

Explanation :- This code downloads the data from the provided link using the requests library. 
It then converts the data into a pandas dataframe using the json_normalize() function. 
Finally, it saves the dataframe to an Excel file using the to_excel() function.

'''




