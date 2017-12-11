from flask import  Flask,make_response,request,render_template,redirect
import sys
import urllib.request, json
with urllib.request.urlopen("https://jsonplaceholder.typicode.com/users") as url:
    auth_data = json.loads(url.read().decode())
with urllib.request.urlopen("https://jsonplaceholder.typicode.com/posts") as url:
    post_data = json.loads(url.read().decode())

app = Flask(__name__)

@app.route('/')
def show_user_profile ():
    return 'Hello World Janaki'

@app.route("/setcookie")
def setcookie():
    
    resp = make_response(render_template('link.html'))
    resp.set_cookie('name','Janaki')
    resp.set_cookie('Age','30')    
    return resp

@app.route("/getcookies")
def getcookies(): 
    Ag=request.cookies.get('Age')
    Nm=request.cookies.get('name')
    return render_template('cookies.html',**locals())

@app.route('/robots.txt')
def robots_txt():
    return send_from_directory(app.static_folder, request.path[1:])

@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'),404



@app.route('/html')
def page():
    return render_template('hello.html')



@app.route('/input')
def input():
   return render_template('input.html')

@app.route('/result',methods = ['POST', 'GET'])
def result():
     if request.method == 'POST':
      Name = request.form['Nm']
      Age=request.form['Ag']
      Phone=request.form['Ph']
      sys.stdout.write(Name)
      sys.stdout.write(Age)
      sys.stdout.write(Phone)      
      sys.stdout.flush()
      return render_template("result.html",**locals())
     

                            
@app.route("/author")
def auth():
    return render_template('author.html',data=auth_data)

@app.route("/post")
def posts():
    return render_template('post.html',data1=post_data)


@app.route('/count')
def task2c():
    tot = []

    for i in auth_data:
        totp = 0
        for j in post_data:
            if j["userId"] == i["id"]:
                totp += 1
        tot.append(totp)

    respstr = ""
    for i in auth_data:
        respstr += "Author: {}".format(i["name"])
        respstr += "</br>"

    respstr += "Total posts in order of the user"

    for i in range(0,10):
        respstr += "&nbsp"*5
        respstr += "</br>"
        respstr += "Total Posts: {}".format(tot[i])
    return respstr



if __name__== '__main__':
    app.run(debug=True)
