from flask import Flask,make_response,request,render_template,redirect

import sys

app=Flask(__name__)

@app.route("/setcookie")

def setcookie():
    
    resp = make_response(render_template('link.html'))

    resp.set_cookie('name','Janaki')
    resp.set_cookie('Age','30')
    
    return resp
    



@app.route("/getcookie")

def getcookie():

 
    Ag=request.cookies.get('Age')
    Nm=request.cookies.get('name')
    return render_template('cookies.html',**locals())
    
    

if __name__== '__main__':
    app.run(debug=True)
