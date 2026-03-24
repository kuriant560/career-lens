import psycopg2


# ---------- DB CONNECTION ----------
def get_connection():
    return psycopg2.connect(
        dbname="careerlens",
        user="kurian",      # 🔴 change this
        password="",  # 🔴 change this
        host="localhost",
        port="5432"
    )


# ---------- NORMALIZE SKILLS ----------
def normalize_skills(skills):
    return [s.lower().strip() for s in skills]


# ---------- JOB RECOMMENDATIONS ----------
def get_recommendations(user_skills):
    user_skills = normalize_skills(user_skills)

    conn = get_connection()
    cur = conn.cursor()

    query = """
            SELECT j.job_title, j.location, COUNT(*) AS match_score
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


# ---------- TOP SKILLS ----------
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


# ---------- SKILL GAP ----------
def get_skill_gap(user_skills):
    user_skills = normalize_skills(user_skills)

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
    all_skills = cur.fetchall()

    cur.close()
    conn.close()

    # remove already known skills
    gap = [skill for skill in all_skills if skill[0].lower() not in user_skills]

    return gap[:5]