from flask import Flask, redirect, url_for, request, render_template
import os
from google.cloud import bigquery
import pandas as pd
from random import random
import plotly.graph_objects as go
from plotly.offline import plot
from datetime import date, timedelta

app = Flask(__name__)

# Main page. index.html must be in templates folder
@app.route('/')
def hello_world():
	# The below lines allow for file paths to be shared on localhost and pythonanywhere server __file__ is a python majic variable 
	THIS_FOLDER = os.path.dirname(os.path.abspath(__file__))
	my_file = os.path.join(THIS_FOLDER,"../../dev-smoke-278920-cb67e104d184.json")
	os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = my_file

	client = bigquery.Client()	# start bigquery

		# Google BigQuery Query
	query = """
		SELECT * FROM bigquery-public-data.covid19_usafacts.confirmed_cases
		"""
	query_job = client.query(query)  # call query to bigquery
	casesdf = query_job.to_dataframe() # convert results into dataframe

	
	return render_template('/index.html') # returns index.html



# DONT NEED TO ADD THIS TO WEB SERVER---------
if __name__ == '__main__':
   app.run()