import myanmar.encodings
import myanmar.converter
from flask import Flask,render_template,request

app = Flask(__name__)
@app.route('/zawgyitounicode',methods = ['GET','POST'])
def zawgyitouni():
    if request.method == 'GET':
        return render_template("index.html")
    else:
        input_mm = request.form['input_mm']
        conv = myanmar.converter.convert(input_mm,'zawgyi','unicode')
        return render_template('index.html',conv=conv)
@app.route('/unicodetozawgyi',methods = ['GET','POST'])
def unitozawgyi():
    if request.method == 'GET':
        return render_template("index.html")
    else:
        input_mm = request.form['input_mm']
        conv = myanmar.converter.convert(input_mm,'unicode','zawgyi')
        return render_template('index.html',conv=conv)

if __name__=="__main__":
    app.run(host="0.0.0.0",port=8888,debug=True)

