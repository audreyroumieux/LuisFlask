# -*- coding: utf-8 -*-
"""
Created on Wed Jul 11 15:38:40 2018

@author: nisha
"""

# Flask utils
from flask import Flask, render_template
import flask
import requests

#request pour envoyer des requête(get et post)

app = Flask(__name__)

@app.route("/", methods = ['GET','POST']) #page d'acceuil 
def index():
    print(request.method)
    if request.method == 'POST':
        query =  flask.request.form['question'] #resultat du formulaire
        print(query)
        apiurl = 'https://westus.api.cognitive.microsoft.com/luis/v2.0/apps/78c57c17-a06f-4a06-953c-105b04db79c6'
        
        headers = {'Ocp-Apim-Subscription-Key': 'ab9ed326b6a040c6acb4a8529038cfe5'}
        
        param = { 'q': query }
        
        var 
        print(apiurl)
        apiresult = requests.get(apiurl, headers = headers, params = param) #je get la question et je transforme en format json
        print(apiresult.content)
        
        return apiresult.json()
        
    else:
        print("NOOOOOOOOOOOOOOOOOOOOO")
        return render_template("formulaire.html")



if __name__ == "__main__":
    app.run()

