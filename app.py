from urllib import request
from flask import Flask,flash,request,render_template,redirect
from flask_cors import CORS,cross_origin
from werkzeug.utils import secure_filename
import os

app = Flask(__name__)

uploads = os.getcwd()+"//files//"

@app.route('/', methods=['GET', 'POST'])
def index():
    return "Flask app is running"

@app.route("/upload", methods = ['POST','GET'])
def upload():
    if request.method == 'POST':
        if 'file' not in request.files:
            flash('no file')
            return redirect(request.url)
        file = request.files['file']
    
        if file.filename == '':
            print('no filename')
            return redirect(request.url)

        else:

            filename = secure_filename(file.filename)
            file.save(uploads+"/"+filename)
            
            return redirect('/')

    return render_template('upload.html')




#if __name__ == "__main__":
 #   app.run(host="0.0.0.0",port=5000)
    #app.run()

    
if __name__ == "__main__":
    host = '0.0.0.0'
    #app.run()
    httpd = simple_server.make_server(host=host, port=port, app=app)
    #httpd = simple_server.make_server(host='127.0.0.1', port=5000, app=app)
    # print("Serving on %s %d" % (host, port))
    httpd.serve_forever()