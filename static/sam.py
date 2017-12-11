from flask import Flask
import urllib.request

app = Flask(__name__)
@app.route("/author")

def index():
    response = urllib.request.urlopen('http://python.org/')
    html = response.read()
    return html

if __name__== '__main__':
    app.run(debug=True)
