from database.db_connection import get_connection


def get_skill_gap(user_skills):
    conn = get_connection()
    cursor = conn.cursor()

    # Get top skills from market
    query = """
            SELECT s.skill_name, COUNT(*) as demand
            FROM job_skills js
                     JOIN skills s ON js.skill_id = s.skill_id
            GROUP BY s.skill_name
            ORDER BY demand DESC; \
            """

    cursor.execute(query)
    market_skills = cursor.fetchall()

    cursor.close()
    conn.close()

    # Convert user skills to set
    user_skills_set = set(user_skills)

    # Find missing skills
    missing_skills = []

    for skill, demand in market_skills:
        if skill not in user_skills_set:
            missing_skills.append((skill, demand))

    # Return top 5 missing skills
    return missing_skills[:5]