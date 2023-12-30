import http.client
import json
import os


def finderCall():
    conn = http.client.HTTPSConnection("moviesdatabase.p.rapidapi.com")

    headers = {
        'X-RapidAPI-Key': "8bf0871ea3msh8bbb7d0dd036a04p15f9cajsn0e547477cf42",
        'X-RapidAPI-Host': "moviesdatabase.p.rapidapi.com"
    }

    conn.request("GET", "/titles/search/title/Iron%20Man?exact=true&info=base_info&titleType=movie", headers=headers)

    res = conn.getresponse()
    data = res.read()

    with open(os.path.dirname(__file__) + '\dataFromURL.json','w') as f_json:    
        f_json.write(data.decode("utf-8"))
        f_json.write("\n")
    f_json.close()


def getValuesFromJSON():

    # Opening JSON file
    # UPDATE the abs path using os.path.abspath("data.json")
    f = open(os.path.dirname(__file__) + ("\dataFromURL.json"))
    
    # returns JSON object as 
    # a dictionary
    dataJSON = json.load(f)
    
    # Iterating through the json
    # list
    for i in dataJSON['results']:
        print(i["primaryImage"]["id"] + "\n")

    # Closing file
    f.close()



#finderCall()
getValuesFromJSON()

print(os.getcwd())


