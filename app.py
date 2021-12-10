import os
from flask import Flask, jsonify, request,make_response, render_template
import re
import json








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






if __name__ == '__main__':
    #app.run(host='0.0.0.0')

    port = int(os.environ.get('PORT', 5000))
    app.run(host = '0.0.0.0', port = port)







# <section class="section summary-section">
#                 <h2 align="center" class="section-title"><span class="icon-holder"><i class="fas fa-user"></i></span>Description</h2>
#                 <div class="summary">
#                     <p>Mich begeistern neue Technologien und Clean Code. Ich baue Brücken zwischen Technik und Menschen und setze meine analytische Denkweise für die Entwicklung von passgenauen Lösungen ein. Als Entwickler mit siebenjähriger Leadership-Erfahrung ist es mir wichtig, mein Team zu Eigeninitiative, selbstorganisierter Arbeitsweise und konstruktiver Zusammenarbeit zu befähigen. Deshalb beschreibt eine Mischung aus Teamlead und Hands-On für mich den idealen Arbeitsplatz.</p>
#                 </div><!--//summary-->
#             </section><!--//section-->





# <section class="honorary-container container-block">
#                 <h2 class="section-title"><span class="icon-holder"><i class="fas fa-home"></i></span>Ehrenamt und Nebentätigkeiten</h2>
#                 <div class="item">
#                     <div class="meta">
#                         <div class="upper-row">
#                             <h3 class="job-title">Tanzlehrer (West Coast Swing)</h3>
#                             <div class="time">2016 - heute</div>
#                         </div><!--//upper-row-->
#                         <div class="company">Ausgebildeter West Coast Swing Instructor (Global PDIA Intermediate Instructor)</div>
#                     </div><!--//meta-->
#                 </div><!--//item-->
#                 <div class="item">
#                     <div class="meta">
#                         <div class="upper-row">
#                             <h3 class="job-title">Tanzlehrer</h3>
#                             <div class="time">2008 - 2018</div>
#                         </div><!--//upper-row-->
#                         <div class="company">Hochschulsport der Universität Münster</div>
#                     </div><!--//meta-->
#                 </div><!--//item-->
#             </section><!--//education-container-->
