from flask import Flask, render_template, Response, request,  make_response
import urllib.request, json
with urllib.request.urlopen("https://jsonplaceholder.typicode.com/users") as url:
    auth_data = json.loads(url.read().decode())
with urllib.request.urlopen("https://jsonplaceholder.typicode.com/posts") as url:
    post_data = json.loads(url.read().decode())

app = Flask(__name__)


@app.route("/author")
def auth():
    return render_template('author.html',data=auth_data)


if __name__== '__main__':
    app.run(debug=True)
