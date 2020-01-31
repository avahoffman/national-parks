import pandas as pd


def request_to_pd (r: None):
	# This function takes a request and turns the resulting data into a .csv file

	# Gather data from request
	dat = r.json()['data']

	# Convert data to pandas df and iterate through the dictionary
	df = pd.DataFrame()
	for i in dat:
		df = df.append(pd.DataFrame([i]))
	
	return(df)