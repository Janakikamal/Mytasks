from flask import Flask, render_template, request
app = Flask(__name__)

@app.route('/input')
def input():
   return render_template('input.html')

@app.route('/result',methods = ['POST', 'GET'])
def result():
   if request.method == 'POST':
      Name = request.form['Nm']
      Age=request.form['Ag']
      Phone=request.form['Ph']
      return render_template("result.html",**locals())

if __name__ == '__main__':
   app.run(debug = True)
