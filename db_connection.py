import psycopg

def get_db_connection():
    return psycopg.connect(
        database="mdb_412",
        user="postgres",
        password="password",
        host="localhost",
        port="5432"
    )

conn = get_db_connection()
print("Database connection successful!")
conn.close()