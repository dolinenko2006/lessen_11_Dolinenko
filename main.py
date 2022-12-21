from utils import *
from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def index():
    candidates = get_candidates()
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



