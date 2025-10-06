# test/hardcoded_db_password.py
import psycopg2

# Vulnerable: DB password in source
DB_HOST = "localhost"
DB_USER = "appuser"
DB_PASSWORD = "SuperSecretPassword123!"
DB_NAME = "appdb"

def connect_and_query():
    conn = psycopg2.connect(host=DB_HOST, user=DB_USER, password=DB_PASSWORD, dbname=DB_NAME)
    cur = conn.cursor()
    cur.execute("SELECT COUNT(*) FROM users;")
    return cur.fetchone()

if __name__ == "__main__":
    print(connect_and_query())
