import os
from flask import Flask, jsonify, request,make_response, render_template
import re
import json



from firbasemod.mainFirebase import myUser, rtdb




app = Flask(__name__)

@app.route('/')
def hello():
    return "<h1>Hello world!  Welcome to François public page</h1>"









@app.route("/cv", methods=['GET', 'POST'])
def testCaption():

    return render_template("myCV.html")




@app.route("/downloadpronoprofoot", methods=['GET', 'POST'])
def downloadpronoprofoot():

    return render_template("downloadProno.html")




@app.route("/deepVisionHome", methods=['GET', 'POST'])
def deepVisionHome():

    return render_template("deepvisionHome.html")




@app.route("/meteo", methods=['GET', 'POST'])
def meteo():

    return render_template("AppDebut/index.html")





@app.route("/testjs", methods=['GET', 'POST'])
def testjs():



    return render_template("tesjs.html")




#*******poe pages

@app.route("/poe_home", methods=['GET', 'POST'])
def poe_home():

    return render_template("poe/index.html")


@app.route("/poe_formulaire", methods=['GET', 'POST'])
def poe_formulaire():

    return render_template("poe/formulaire.html")


@app.route("/poe_liste", methods=['GET', 'POST'])
def poe_liste():

    return render_template("poe/liste.html")

#*******





#*********from js


@app.route("/postmethode", methods=['GET', 'POST'])
def setUser():


   # print(myUser.addUser({"name": "kossi"}))

    # print(myUser.getAllUser())
    print("in post")

    jsonData = request.get_json()

    print(jsonData)

    outputJsData = myUser.methode[jsonData["methode"]](jsonData["data"])


    print(outputJsData)

    return jsonify(outputJsData)





@app.route("/post2RTDB", methods=['GET', 'POST'])
def toRTDB():



    print("in post")

    jsonData = request.get_json()

    print(jsonData)

    outputJsData = rtdb.methode[jsonData["methode"]](jsonData["data"])


    print(outputJsData)


    return jsonify(outputJsData)








if __name__ == '__main__':
    #app.run(host='0.0.0.0')

    port = int(os.environ.get('PORT', 5000))
    app.run(host = '0.0.0.0', port = port)







# https://stackoverflow.com/questions/42388989/bootstrap-center-vertical-and-horizontal-alignment

#https://stackoverflow.com/questions/6396101/pure-javascript-send-post-data-without-a-form

#https://gist.github.com/KentaYamada/2eed4af1f6b2adac5cc7c9063acf8720


