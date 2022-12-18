from utils import *
from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def index():
    info_candidate = '<br>'
    for candidate in get_candidates():
       #info_candidate += f"<img src={candidate['picture']}>" '<br>'
        info_candidate += str(candidate["position"]) + '<br>' # тоже что '\n'
        info_candidate += candidate["name"] + '<br>'
        info_candidate += candidate["skills"] + '<br>''<br>'

    #return f"<pre>{info_candidate}</pre>"
    return render_template("list.html", value=info_candidate)


@app.route("/candidate/<int:pk>")
def candidates_by_pk(pk):
    candidate = get_by_pk(pk)
    if not candidate:
        return "Кандидат не найден"

    results = '<br>'
    results += candidate["name"] + '<br>'
    results += str(candidate["position"]) + '<br>'  # тоже что <br>
    results += candidate["skills"] + '<br>'

    return f'''
           <img src="{candidate['picture']}">
           <pre> {results} </pre>
           '''

@app.route("/candidate/<skill>")
def candidate_by_skills(skill):
    candidates = get_by_skill(skill)
    if not candidates:
         return "Кандидат с такими навыками не найден"

    results = "<br>"
    for candidate in candidates:
        results += f'''<img src="{candidate['picture']}"> <br>'''
        results += candidate["name"] + '<br>'
        results += str(candidate["position"]) + '<br>'
        results += candidate["skills"] + '<br>'

    return results

@app.route("/name/<name>")
def candidates_by_name(name):
    candidates = get_candidates_by_name(name)
    if not candidates:
        return "Кандидат с таким именем не найден"

    results = "<br>"
    for candidate in candidates:
        results += f'''<img src="{candidate['picture']}"> <br>'''
        results += candidate["name"] + '<br>'
        results += str(candidate["position"]) + '<br>'
        results += candidate["skills"] + '<br>''<br>'

    return results

app.run()



