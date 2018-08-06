import os
from flask import Flask, render_template, request
import requests
import pandas as pd

# create a Flask instance in your main module 
app = Flask(__name__)

def import_file(file_path):
	df = pd.read_csv(file_path, header=0)
	return df


def moyenne(df, colname):
	col_mean = df[colname].means()
	return col_mean


@app.route('/', methods = ['GET', 'POST'])
def index():

	if request.method == 'POST':
		query = request.form["question"]
		luis_url = "https://westus.api.cognitive.microsoft.com/luis/v2.0/apps/157c5d1d-760d-42e9-8ffe-f64f9e696449?subscription-key=ef7c7e3a660c48218d7907a5453847e4&timezoneOffset=0&q=" + str(query)
		luis_result = requests.get(luis_url)
		result = luis_result.json()
		print(result)
		intent= result['topScoringIntent']['intent']
		entity= result['entities'][1]['entity']
		df = import_file('C:\\Users\\ARLETTE\\Documents\\COURS IA\\KATA\\2016 School Explorer.csv')
		list_col = []
		list_col.append(df[df.columns[int(entity)]])
		response = pd.DataFrame(list_col).to_html()
		return render_template('luis_send.html', result = response)
	else:
		return render_template("form.html")


if __name__ == "__main__":
	#decide what port to run the app in
	port = int(os.environ.get('PORT', 8000))
	#run the app locally on the givn port
	app.run(host='0.0.0.0', port=port)