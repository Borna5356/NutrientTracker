import psycopg2
import hashlib
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
    password TEXT NOT NULL,
    age INT,
    sex CHAR,
    weight int
    )    
    """
    cursor.execute(query)
    conn.commit()

def create_user(username, password, age, sex, weight):
    """
    Hashes the password entered and adds the new user to the database
    """
    hashed_password = hash_password(password)
    query = """
    INSERT INTO users (username, password, age, sex, weight) 
    VALUES (%s, %s, %s, %s, %s)
    """
    values = [username, hashed_password, age, sex, weight]
    cursor.execute(query, values)
    conn.commit()
    return True

def get_user(username):
    """
    gets a user's information if the username exists
    """
    query = "SELECT * FROM users WHERE username=%s"
    values = [username]
    cursor.execute(query, values)
    conn.commit()
    return cursor.fetchone()

def validate_user(user, password):
    """
    makes sure that the password entered is 
    """
    hashed_password = hash_password(password)
    correct_password = user[1]
    return hashed_password == correct_password

def hash_password(password):
    hashing = hashlib.sha256()
    encoded_string = bytes(password, encoding="utf-8")
    hashing.update(encoded_string)
    hashed_password = str(hashing.digest())
    password_array = hashed_password.split('\\')
    hashed_password = ""
    for string in password_array:
        hashed_password += string
    return hashed_password

create_user_table()
#create_user("Boobby", "test", 32, 'f', 324)
user = get_user("Boobby")
print(validate_user(user, "test"))


cursor.close()
conn.close()
