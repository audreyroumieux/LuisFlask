# -*- coding: utf-8 -*-
"""
Created on Tue Jul 10 16:50:54 2018
@author: audrey roumieux
Projet:
Description:
"""
import os
import flask
from flask import Flask, request, render_template, redirect
import requests

app = Flask(__name__)


@app.route('/reservation', methods = ['GET', 'POST'])
def index():
    return render_template("form.html")

@app.route('/reservation/traitement', methods = ['POST'])
def traitement():
    if request.method == 'POST':
        query = flask.request.form["instruction"]
        luis_url = 'https://westus.api.cognitive.microsoft.com/luis/v2.0/apps/19db6bd1-63cc-4fb8-ba4a-ba69fa6e50a0'
        entete = {'Ocp-Apim-Subscription-Key':'30c03cdde1cf49c590eb1e1ca6c7c83e'}
        parametre = {'q': query}
        luis_result = requests.get(luis_url, headers = entete, params = parametre )
        print(luis_result.content)
        resulta = luis_result.json()
        print('RES :::: ', resulta)
        intent = resulta['topScoringIntent']['intent']
        entity_date = resulta['entities']['entity']
        entity_pays = resulta['entities']['entity']
        entity_ville = resulta['entities']['entity']['ville']['entity']
        print('ENTITY 1', entity_date)
        print('ENTITY 2', entity_pays)
        print('ENTITY', entity_ville)



#{'query': "j'aimerais aller à Rome le 4 septembre", 
#'topScoringIntent': {'intent': 'Destination_voyage','score': 0.9360706}, 
#'entities': [{'entity': '4 septembre', 'type': 'builtin.datetimeV2.date',
#            'startIndex': 27, 'endIndex': 37, 
#            'resolution': {'values': [{'timex': 'XXXX-09-04', 
#                                        'type': 'date', 
#                                        'value': '2017-09-04'}, 
#            {'timex': 'XXXX-09-04', 'type': 'date', 'value': '2018-09-04'}]}}, 
#            {'entity': '4', 'type': 'builtin.number', 
#             'startIndex': 27, 'endIndex': 27, 
#             'resolution': {'value': '4'}}, 
#            {'entity': 'rome', 'type': 'Ville', 
#             'startIndex': 19, 'endIndex': 22, 
#             'resolution': {'values': ['Rome']}}], 
#    'sentimentAnalysis': {'score': 0.52647984}}
#

if __name__ == "__main__":
	#decide what port to run the app in
	port = int(os.environ.get('PORT', 8000))
	#run the app locally on the givn port
	app.run(host='0.0.0.0', port=port)