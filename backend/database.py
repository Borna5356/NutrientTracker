import psycopg2
import bcrypt
conn = psycopg2.connect(host="localhost", dbname="NutrientTracker", user="User",
                        password="Tehran14!", port=5432)

cursor = conn.cursor()
def create_user_table():
    """
    Creats a table that is used for user information
    """
    query = """
    CREATE TABLE IF NOT EXISTS users(
    username VARCHAR(255) PRIMARY KEY,
    password VARCHAR(255),
    age INT,
    sex CHAR,
    weight int
    )    
    """
    cursor.execute(query)

def create_user(username, password, age, sex, weight):
    hashed_password = bcrypt.hashpw(password, bcrypt.gensalt())
    query = """
    INSERT INTO users (username, password, age, sex, weight) 
    VALUES (%s, %s, %s, %s, %s)
    """
    values = [username, hashed_password, age, sex, weight]
    cursor.execute(query, values)

create_user_table()
create_user('test', 'test', 2, 'm', 23)
conn.commit()

cursor.close()
conn.close()