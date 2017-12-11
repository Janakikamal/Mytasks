from flask import  Flask

app = Flask(__name__)

@app.route('/')
def show_user_profile ():
    return 'Hello World Janaki'


if __name__== '__main__':
    app.run(debug=true)
