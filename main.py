from utils import *
from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def index():
    candidates = get_candidates()
    # info_candidate = '<br>'
    # for candidate in get_candidates():
    #    #info_candidate += f"<img src={candidate['picture']}>" '<br>'
    #     info_candidate += str(candidate["position"]) + '<br>' # тоже что '\n'
    #     info_candidate += candidate["name"] + '<br>'
    #     info_candidate += candidate["skills"] + '<br>''<br>'
    #
    # #return f"<pre>{info_candidate}</pre>"
    return render_template("list.html", candidates=candidates)


@app.route("/candidate/<int:pk>")
def candidates_by_pk(pk):
    candidate = get_by_pk(pk)
    return render_template("card.html", candidate=candidate)


@app.route("/skill/<skill_name>")
def candidate_by_skills(skill_name):
    candidates = get_by_skill(skill_name)
    return render_template("skill.html", candidates=candidates)


@app.route("/search/<candidate_name>")
def candidates_by_name(candidate_name):
    candidates = get_candidates_by_name(candidate_name)
    return render_template("search.html", candidates=candidates)

app.run()



