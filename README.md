# national-parks

### Code to pull data from National Park Service websites
*THIS CODE IS ONLY TO BE USED FOR ACADEMIC AND LEARNING PURPOSES*

### Contents

```
├── data
```
These are data obtained via scraping and via the NPS API. Since data are large they should be ignored.
```
├── src | api.py
```
This script connects to the [NPS API](https://www.nps.gov/subjects/developer/guides.htm) for general park info, alerts, events, news releases, and campground information.
```
├── src | scrape.py
```
This script will scrape the [NPS National Reports](https://irma.nps.gov/STATS/Reports/National) for traffic and visitor counts.
```
├── src | config.py
```
This script should contain a user specific api-key for connecting to the API.
```
├── src | utils.py
```
This script contains general purpose utility functions.
