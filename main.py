from flask import Flask, request, render_template
import http.client
import json

app = Flask(__name__)
searchDict = {}

@app.route("/", methods=['GET', 'POST'] )
def root():
    return render_template("index.html")

@app.route("/search")
def search():
    return render_template("second.html", jsonObj = "", start = 1)

@app.route("/search", methods=['POST'])
def search_post():
    str = request.form['text']
    if str != "":
        result = finderCall(str)
        if result["results"]:
            return render_template("second.html", jsonObj = result, start = 0)
        else:
            return render_template("second.html", jsonObj = "", start = 0)
    else:
        return render_template("second.html", jsonObj = "", start = 0)

def finderCall(str):
    conn = http.client.HTTPSConnection("moviesdatabase.p.rapidapi.com")

    headers = {
        'X-RapidAPI-Key': "8bf0871ea3msh8bbb7d0dd036a04p15f9cajsn0e547477cf42",
        'X-RapidAPI-Host': "moviesdatabase.p.rapidapi.com"
    }
    conn.request("GET", "/titles/search/title/" + str.replace(" ", "%20") + "?exact=false&info=base_info&titleType=movie", headers=headers)

    res = conn.getresponse()
    data = res.read()

    return json.loads(data.decode("utf-8"))
    

if __name__ == "__main__":
    app.run()

