import datetime
from datetime import date
import psycopg
from psycopg import sql
import hashlib
import configparser
import csv

DB_CONFIG = {
    "dbname": "mdb_412",
    "user": "postgres",
    "password": "password",
    "host": "localhost",  # or your database host
    "port": "5432"        # or your database port
}

def get_db_connection():
    try:
        conn = psycopg.connect(**DB_CONFIG)
        return conn
    except psycopg.Error as e:
        print(f"Error connecting to database: {e}")
        raise e

conn = get_db_connection()
cur = conn.cursor()


# Every table from the ER Diagram is created
# Serial: automatically increments with each new entry
def initializeDatabaseTables():
    cur.execute("""CREATE TABLE user_ (
                uid SERIAL PRIMARY KEY,
                username VARCHAR(50) NOT NULL,
                hash VARCHAR(128) NOT NULL,
                join_date DATE NOT NULL,
                bio TEXT NOT NULL
    );""")
    cur.execute("""CREATE TABLE review_ (
                rid SERIAL PRIMARY KEY, 
                uid INT NOT NULL,
                mid INT NOT NULL,
                comment TEXT NOT NULL, 
                rating FLOAT NOT NULL, 
                date DATE NOT NULL,
                vote INT DEFAULT 0
    );""")
    cur.execute("""CREATE TABLE user_votes (
                uid INT NOT NULL, 
                rid INT NOT NULL,
                vote INT NOT NULL,
                PRIMARY KEY (uid, rid),
                FOREIGN KEY (uid) REFERENCES user_(uid) ON DELETE CASCADE,
                FOREIGN KEY (rid) REFERENCES review_(rid) ON DELETE CASCADE
            )""")
    cur.execute("""CREATE TABLE movie_ (
                mid SERIAL PRIMARY KEY, 
                title TEXT NOT NULL,
                release_date DATE NOT NULL, 
                plot TEXT NOT NULL,  
                num_reviews INT NOT NULL,
                rating_sum INT NOT NULL
    );""")
    cur.execute("""CREATE TABLE genre_ (
                genre_name TEXT PRIMARY KEY,
                content TEXT
    );""")
    cur.execute("""CREATE TABLE genre_of_ (
                genre_name TEXT,
                mid INT,
                PRIMARY KEY(genre_name, mid)
    );""")
    cur.execute("""CREATE TABLE person_ (
                pid SERIAL PRIMARY KEY,
                name TEXT NOT NULL,
                dob DATE NOT NULL,
                description TEXT NOT NULL
    );""")
    cur.execute("""CREATE TABLE cast_ (
                pid INT,
                mid INT,
                roles TEXT[],
                PRIMARY KEY(pid, mid)
    );""")
    cur.execute("""CREATE TABLE crew_ (
                pid INT,
                mid INT,
                PRIMARY KEY(pid, mid)
    );""")
    cur.execute("""CREATE TABLE director_ (
                pid INT,
                mid INT,
                PRIMARY KEY(pid, mid)
    );""")

# Clear all tables, useful for when we need to make changes to table structure
def dropAllTables():
    cur.execute("DROP TABLE IF EXISTS user_ CASCADE")
    cur.execute("DROP TABLE IF EXISTS review_ CASCADE")
    cur.execute("DROP TABLE IF EXISTS movie_ CASCADE")
    cur.execute("DROP TABLE IF EXISTS genre_ CASCADE")
    cur.execute("DROP TABLE IF EXISTS genre_of_ CASCADE")
    cur.execute("DROP TABLE IF EXISTS person_ CASCADE")
    cur.execute("DROP TABLE IF EXISTS user_votes CASCADE")
    cur.execute("DROP TABLE IF EXISTS cast_ CASCADE")
    cur.execute("DROP TABLE IF EXISTS crew_ CASCADE")
    cur.execute("DROP TABLE IF EXISTS director_ CASCADE")

# Handles hashing as well as join_date within this function.
def addUser(username, password, bio=""):
    if username == "": 
        print("FAIL: No username specified")
        return
    hash = hashlib.sha256(password.encode())
    hash_digest = hash.hexdigest()
    insert_query = """INSERT INTO user_(username, hash, join_date, bio) 
                    VALUES (%s, %s, %s, %s)""" # Avoid SQL Injection (this should only be used by groupmates, but it's good practice)
    cur.execute(insert_query, (username, hash_digest, date.today(), bio))

# Designed as a sanity check to make sure users and hashes are stored correctly, not necessarily best practice
def authTest(username, password):
    hash = hashlib.sha256(password.encode())
    hash_digest = hash.hexdigest()
    retrieve_user_query = "SELECT username FROM user_ WHERE username = %s AND hash = %s"
    cur.execute(retrieve_user_query, (username, hash_digest))
    user = cur.fetchall()
    if(len(user) == 1): print("Authenticated!")
    else: print("AUTH FAIL")

# Print out a whole table
def printTable(table):
    print_table_query = sql.SQL("SELECT * FROM {table}").format(table=sql.Identifier(table)) # Paramterized queries not great for table names, neat workaround but should be avoided in production
    cur.execute(print_table_query)
    rows = cur.fetchall()
    columns = [desc[0] for desc in cur.description]
    print("Columns: ", end="")
    for column in columns: print(str(column),end=", ")
    print()
    j = 0
    for row in rows:
        print("Row "+str(j)+": ")
        for i in range(len(columns)):
            print("\t"+columns[i]+": "+str(row[i]))
        j += 1

def readMoviesFromCSV():
    csv_file_path = 'movieinfo.csv'  # Replace with your actual CSV file path

    try:
        with open(csv_file_path, newline='', encoding='utf-8') as csv_file:
            csvReader = csv.reader(csv_file, delimiter=',', quotechar='"')

            count = 0
            for row in csvReader:
                if count == 0:  # Skip the header row
                    count += 1
                    continue

                # Process the movie data as before
                movie_title = row[0]
                movie_released_date = datetime.datetime.strptime(row[3], '%d %b %Y').strftime('%Y-%m-%d')
                movie_plot = row[9]

                # Insert movie into the database
                insert_movie_query = """INSERT INTO movie_ (title, release_date, plot, rating_sum, num_reviews)
                                        VALUES (%s, %s, %s, 0, 0)"""
                cur.execute(insert_movie_query, (movie_title, movie_released_date, movie_plot))
                conn.commit()

                # Add logic for genres, cast, etc. as before

            print("Movies imported successfully!")
    except FileNotFoundError:
        print(f"Error: The file {csv_file_path} was not found.")
    except Exception as e:
        print(f"Error reading from CSV: {e}")

def leaveReview(uid, mid, rating, comment):
    insert_review_query = """INSERT INTO review_(uid, mid, rating, comment, date, vote)
                            VALUES(%s, %s, %s, %s, %s, 0)"""
    cur.execute(insert_review_query, (uid,mid,rating,comment,date.today()))
    cur.execute("""UPDATE movie_ SET rating_sum = rating_sum + %s, num_reviews = num_reviews+1 WHERE mid = %s""",(rating,mid))

def getUUID(value, valname1, valname2, table):
    query = sql.SQL("SELECT {valname1} FROM {table} WHERE {valname2} = {value}").format(table=sql.Identifier(table), valname1=sql.Identifier(valname1), valname2=sql.Identifier(valname2), value=value)
    cur.execute(query)

while(True):
    print("**********************************")    
    print("Welcome to Ryan's database helper!")
    print("**********************************")
    print("Options:")
    print("1: Initialize Tables")
    print("2: Drop All Tables")
    print("3: Create New User")
    print("4: Test Authentication")
    print("5: Leave Review")
    print("6: Insert Movies")
    print("7: Print Out a Table")
    print("8: Quit")
    choice = input("Enter your choice: ")
    match choice:
        case "1":
            print("----------------------------------")
            initializeDatabaseTables()
            print("INITIALIZED")
            print("----------------------------------")
            conn.commit()
        case "2":
            confirm_input = input("Confirm (y/n): ")
            if(confirm_input == "y"):
                print("----------------------------------")
                dropAllTables()
                print("DROPPED")
                print("----------------------------------")
                conn.commit()
            else:
                print("Aborted")
        case "3":
            print("----------------------------------")
            username = input("Username: ")
            password = input("Password: ")
            bio = input("Bio: ")
            addUser(username, password, bio)
            conn.commit()
            print("USER CREATED")
            print("----------------------------------")
        case "4":
            print("----------------------------------")
            username = input("Username: ")
            password = input("Password: ")
            authTest(username,password)
            print("----------------------------------")
        case "5":
            print("----------------------------------")
            printTable("user_")
            user = input("Select uid: ")
            print()
            printTable("movie_")
            movie = input("Select mid: ")
            rating = input("Rating: ")
            review = input("Review: ")
            leaveReview(user,movie,float(rating),review)
            conn.commit()
            print("Review Left!")
            print("----------------------------------")
        case "6":
            print("----------------------------------")
            readMoviesFromCSV()
            conn.commit()
            print("Movies read!")
            print("----------------------------------")
        case "7":
            print("----------------------------------")
            print("Options: ")
            cur.execute("SELECT table_name FROM information_schema.tables WHERE table_schema = 'public';")
            rows = cur.fetchall()
            for row in rows:
                print(row[0])
            selected_table = input("Please choose a table by name: ")
            printTable(selected_table)
            print("----------------------------------")
        case "8":
            print("Goodbye!")
            cur.close()
            conn.close()
            exit()
        case _:
            print("Unrecognized command, try again")

cur.close()
conn.close()