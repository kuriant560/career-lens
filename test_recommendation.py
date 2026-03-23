from analysis.recommendation_engine import get_jobs_by_skills

skills = ["python", "sql"]

jobs = get_jobs_by_skills(skills)

for job in jobs:
    print(job)