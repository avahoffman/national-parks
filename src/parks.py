import requests
from config import api_key
from utils import request_to_pd

# https://www.nps.gov/subjects/developer/api-documentation.htm#/

# Limit to 600 Parks - should cover all of them, but needs to be done in chunks of 200:
# r1 = requests.get("https://developer.nps.gov/api/v1/parks?limit=200&fields=entranceFees&fields=entrancePasses&fields=images&fields=operatingHours&api_key=" + api_key)
# chunk1 = request_to_pd(r1)
# r2 = requests.get("https://developer.nps.gov/api/v1/parks?start=201&limit=200&fields=entranceFees&fields=entrancePasses&fields=images&fields=operatingHours&api_key=" + api_key)
# chunk2 = request_to_pd(r2)
# r3 = requests.get("https://developer.nps.gov/api/v1/parks?start=401&limit=200&fields=entranceFees&fields=entrancePasses&fields=images&fields=operatingHours&api_key=" + api_key)
# chunk3 = request_to_pd(r3)
# 
# chunk1.append(chunk2).append(chunk3).to_csv("data/parks.csv")

# Only want the 400 most recent alerts out of 491
r1 = requests.get("https://developer.nps.gov/api/v1/alerts?limit=200&api_key=" + api_key)
chunk1 = request_to_pd(r1)
r2 = requests.get("https://developer.nps.gov/api/v1/alerts?start=201&limit=200&api_key=" + api_key)
chunk2 = request_to_pd(r2)

chunk1.append(chunk2).to_csv("data/alerts.csv")

# Only want the 600 most recent events
# r1 = requests.get("https://developer.nps.gov/api/v1/events?limit=200&api_key=" + api_key)
# chunk1 = request_to_pd(r1)
# r2 = requests.get("https://developer.nps.gov/api/v1/events?start=201limit=200&api_key=" + api_key)
# chunk2 = request_to_pd(r2)
# r3 = requests.get("https://developer.nps.gov/api/v1/events?start=401limit=200&api_key=" + api_key)
# chunk3 = request_to_pd(r3)
# 
# chunk1.append(chunk2).append(chunk3).to_csv("data/events.csv")

# Want all 508 campgrounds
# r1 = requests.get("https://developer.nps.gov/api/v1/campgrounds?limit=200&api_key=" + api_key)
# chunk1 = request_to_pd(r1)
# r2 = requests.get("https://developer.nps.gov/api/v1/campgrounds?start=201limit=200&api_key=" + api_key)
# chunk2 = request_to_pd(r2)
# r3 = requests.get("https://developer.nps.gov/api/v1/campgrounds?start=401limit=200&api_key=" + api_key)
# chunk3 = request_to_pd(r3)
# 
# chunk1.append(chunk2).append(chunk3).to_csv("data/campgrounds.csv")

# Only want the 600 most recent news releases
# r1 = requests.get("https://developer.nps.gov/api/v1/newsreleases?limit=200&api_key=" + api_key)
# chunk1 = request_to_pd(r1)
# r2 = requests.get("https://developer.nps.gov/api/v1/newsreleases?start=201limit=200&api_key=" + api_key)
# chunk2 = request_to_pd(r2)
# r3 = requests.get("https://developer.nps.gov/api/v1/newsreleases?start=401limit=200&api_key=" + api_key)
# chunk3 = request_to_pd(r3)
# 
# chunk1.append(chunk2).append(chunk3).to_csv("data/newsreleases.csv")