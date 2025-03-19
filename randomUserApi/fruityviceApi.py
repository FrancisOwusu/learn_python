import requests
import json

# from randomuser import RandomUser
import pandas as pd


data = requests.get(
    "https://web.archive.org/web/20240929211114/https://fruityvice.com/api/fruit/all"
)
results = json.loads(data.text)

# We will convert our json data into pandas data frame.
pd.DataFrame(results)

df2 = pd.json_normalize(results)
print(df2)

cherry = df2.loc[df2["name"] == "Cherry"]
(cherry.iloc[0]["family"]), (cherry.iloc[0]["genus"])

# In this Exercise, find out how many calories are contained in a banana.