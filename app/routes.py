from flask import Blueprint, render_template, request
from analysis.recommendation_engine import (
    get_recommendations,
    get_top_skills,
    get_skill_gap
)

routes = Blueprint("routes", __name__)


@routes.route("/", methods=["GET"])
def home():
    # ✅ ALWAYS inside function
    skills_input = request.args.get("skills")

    if skills_input:
        user_skills = [s.strip().lower() for s in skills_input.split(",")]
    else:
        user_skills = ["python", "sql"]

    # ✅ backend calls
    jobs = get_recommendations(user_skills)
    top_skills = get_top_skills()
    skill_gap = get_skill_gap(user_skills)

    return render_template(
        "index.html",
        jobs=jobs,
        top_skills=top_skills,
        skill_gap=skill_gap,
        user_skills=user_skills
    )