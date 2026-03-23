import psycopg2


def get_connection():
    return psycopg2.connect(
        dbname="careerlens",
        user="kurian",
        host="localhost",
        port="5432"
    )


# ✅ Insert job and return job_id
def insert_job(title, location):
    conn = get_connection()
    cursor = conn.cursor()

    query = """
            INSERT INTO jobs (job_title, location)
            VALUES (%s, %s)
                RETURNING job_id \
            """

    cursor.execute(query, (title, location))
    job_id = cursor.fetchone()[0]

    conn.commit()
    cursor.close()
    conn.close()

    return job_id


# ✅ Insert skill (or reuse if exists)
def insert_skill(skill_name):
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute(
        "SELECT skill_id FROM skills WHERE LOWER(skill_name) = LOWER(%s)",
        (skill_name,)
    )

    result = cursor.fetchone()

    if result:
        skill_id = result[0]
    else:
        cursor.execute(
            "INSERT INTO skills (skill_name) VALUES (%s) RETURNING skill_id",
            (skill_name,)
        )
        skill_id = cursor.fetchone()[0]

    conn.commit()
    cursor.close()
    conn.close()

    return skill_id


# ✅ Link job ↔ skill
def link_job_skill(job_id, skill_id):
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute(
        "INSERT INTO job_skills (job_id, skill_id) VALUES (%s, %s)",
        (job_id, skill_id)
    )

    conn.commit()
    cursor.close()
    conn.close()