import requests

x = requests.get("https://pokeapi.co/api/v2/gender/3/")

data = x.json()['pokemon_species_details']

import pandas as pd
from pandas import json_normalize as from_json

df = from_json(data)

print(df.head(50))