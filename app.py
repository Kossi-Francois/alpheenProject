import os
from flask import Flask, jsonify, request,make_response, render_template
import re
import json








app = Flask(__name__)

@app.route('/')
def hello():
    return 'Hello world zouzou!'









@app.route("/cv", methods=['GET', 'POST'])
def testCaption():

    return render_template("myCV.html")







if __name__ == '__main__':
    #app.run(host='0.0.0.0')

    port = int(os.environ.get('PORT', 5000))
    app.run(host = '0.0.0.0', port = port)
