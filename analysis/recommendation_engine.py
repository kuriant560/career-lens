import psycopg2

def get_connection():
    return psycopg2.connect(
        dbname="careerlens",
        user="kurian",   # ⚠️ change if needed
        password="",
        host="localhost",
        port="5432"
    )


# -----------------------------
# JOB RECOMMENDATIONS
# -----------------------------
def get_recommendations(user_skills):
    conn = get_connection()
    cur = conn.cursor()

    # ✅ Normalize skills
    user_skills = [s.lower().strip() for s in user_skills]

    query = """
            SELECT DISTINCT j.job_title, j.location, COUNT(*) AS match_score
            FROM jobs j
                     JOIN job_skills js ON j.job_id = js.job_id
                     JOIN skills s ON js.skill_id = s.skill_id
            WHERE LOWER(s.skill_name) = ANY(%s)
            GROUP BY j.job_title, j.location
            ORDER BY match_score DESC
                LIMIT 10; \
            """

    cur.execute(query, (user_skills,))
    results = cur.fetchall()

    cur.close()
    conn.close()

    return results


# -----------------------------
# TOP SKILLS
# -----------------------------
def get_top_skills():
    conn = get_connection()
    cur = conn.cursor()

    query = """
            SELECT s.skill_name, COUNT(*) AS demand
            FROM job_skills js
                     JOIN skills s ON js.skill_id = s.skill_id
            GROUP BY s.skill_name
            ORDER BY demand DESC
                LIMIT 10; \
            """

    cur.execute(query)
    results = cur.fetchall()

    cur.close()
    conn.close()

    return results


# -----------------------------
# SKILL GAP
# -----------------------------
def get_skill_gap(user_skills):
    conn = get_connection()
    cur = conn.cursor()

    query = """
            SELECT s.skill_name, COUNT(*) AS demand
            FROM job_skills js
                     JOIN skills s ON js.skill_id = s.skill_id
            GROUP BY s.skill_name
            ORDER BY demand DESC
                LIMIT 15; \
            """

    cur.execute(query)
    results = cur.fetchall()

    cur.close()
    conn.close()

    # Remove skills user already has
    gap = [
        (skill, demand)
        for skill, demand in results
        if skill.lower() not in user_skills
    ]

    return gap[:10]