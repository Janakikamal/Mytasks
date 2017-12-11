from flask import Flask, render_template

app = Flask(__name__)

@app.route('/robots.txt/')
def deny_request():
    return 'You Should Not Be Here...Request Denied'
if __name__ == "__main__":
    app.run()
