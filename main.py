from flask import Flask, request, render_template

app = Flask(__name__)

@app.route("/")
def root():
    return render_template("index.html")

@app.route("/search", methods=['GET', 'POST'])
def search():
    return render_template("second.html")

@app.route('/', methods=['POST'])
def my_form_post():
    text = request.form['text'] 
    str = text.upper()
    print(str)
    return render_template("index.html", str = str)

if __name__ == "__main__":
    app.run()

