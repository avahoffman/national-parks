import requests
import pandas as pd
import config

r = requests.get("https://developer.nps.gov/api/v1/parks?limit=10&api_key=" + api_key)

dat = r.json()['data']

dat_df = pd.DataFrame()
for i in dat:
    dat_df = dat_df.append(pd.DataFrame([i]))