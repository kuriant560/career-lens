from database.db_connection import get_connection


def get_jobs_by_skills(user_skills):
    conn = get_connection()
    cursor = conn.cursor()

    # Convert list → SQL tuple
    skills_tuple = tuple(user_skills)

    query = """
            SELECT j.job_title, j.location, COUNT(js.skill_id) as match_count
            FROM jobs j
                     JOIN job_skills js ON j.job_id = js.job_id
                     JOIN skills s ON js.skill_id = s.skill_id
            WHERE LOWER(s.skill_name) IN %s
            GROUP BY j.job_id
            ORDER BY match_count DESC
                LIMIT 20; \
            """

    cursor.execute(query, (skills_tuple,))
    results = cursor.fetchall()

    cursor.close()
    conn.close()

    return results