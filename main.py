from utils import *
from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def page_index():
    info_candidate = '<br>'
    for candidate in load_candidates():
        info_candidate += str(candidate["position"]) + '<br>' # тоже что '\n'
        info_candidate += candidate["name"] + '<br>'
        info_candidate += candidate["skills"] + '<br>'


    return f"<pre>{list_candidates}</pre>"


@app.route("/candidate/<int:pk>")
def get_candidates(pk):
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
def get_candidate_by_skills(skill):
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

app.run()


