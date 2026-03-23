from database.db_connection import get_connection


def get_top_skills():
    conn = get_connection()
    cursor = conn.cursor()

    query = """
            SELECT s.skill_name, COUNT(*) as demand
            FROM job_skills js
                     JOIN skills s ON js.skill_id = s.skill_id
            GROUP BY s.skill_name
            ORDER BY demand DESC
                LIMIT 10; \
            """

    cursor.execute(query)
    results = cursor.fetchall()

    cursor.close()
    conn.close()

    return results