# importing the requests library 
import requests
import json
from flask import Flask, escape, request, render_template

def output(data):
    list = []
    templist = []
    
    for i in data["hits"]["hits"]:
        templist.append("<p style=\"margin-left:2.5em\"> " + "score: " + str(i["_score"])  + "<br>")
        templist.append("username: " + str(i["_source"]["user"]["name"]) + "<br>")
        templist.append("text: " + str(i["_source"]["text"]) + "<br>")
        templist.append("location: " + str(i["_source"]["place"]["full_name"]) + "<br>")
        templist.append("time: " + str(i["_source"]["created_at"]) + "<br>" + "<br>" + "<br>")
        list.append(templist)

    tempstr = "Finished search. Total hits: "
    tempstr += str(data["hits"]["total"]["value"]) + "<br><br><br>"

    for i in list[0]:
        tempstr += i
    return tempstr

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

#@app.after_request
#def treat_as_plain_text(response):
#    response.headers["content-type"] = "text/plain"
#    return response

@app.route('/', methods=['POST'])
def elastic_search():
    # api-endpoint
    URL = "http://localhost:9200/twitter/_search?"
    query = request.form["name"]
    # defining a params dict for the parameters to be sent to the API
    PARAMS = {'q':query}
    # sending get request and saving the response as response object
    r = requests.get(url = URL, params = PARAMS)

    # extracting data in json format
    data = r.json()
    if data["hits"]["total"]["value"] == 0:
        return "No result"
    else:
        tempstr = output(data)
        return tempstr

    # next step is to parse the json
    # print # results
    # print results one by one  (tweet text, time, score?)


if __name__ == '__main__':
    app.run()
