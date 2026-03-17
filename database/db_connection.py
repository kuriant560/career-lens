import psycopg2

def get_connection():
    conn = psycopg2.connect(
        dbname="careerlens",
        user="kurian",
        host="localhost",
        port="5432"
    )
    return conn


if __name__ == "__main__":
    try:
        conn = get_connection()
        print("Database connected successfully!")
        conn.close()
    except Exception as e:
        print("Connection failed:", e)