import psycopg2

def get_db_connection():
    return psycopg2.connect(
        database="your_database_name",
        user="postgres",
        password="password",
        host="localhost",
        port="5432"
    )

conn = get_db_connection()
print("Database connection successful!")
conn.close()