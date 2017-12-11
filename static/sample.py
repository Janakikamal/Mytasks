from flask import  Flask
import sys

app = Flask(__name__)

@app.route('/')

sys.stdout.write("hai")

if __name__== '__main__':
    app.run()
