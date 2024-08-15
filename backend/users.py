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
    makes sure that the password entered is correct 
    """
    hashed_password = hash_password(password)
    correct_password = user[1]
    return hashed_password == correct_password

def hash_password(password):
    """
    Helper function to hash a given password to be added to the table
    """
    hashing = hashlib.sha256()
    encoded_string = bytes(password, encoding="utf-8")
    hashing.update(encoded_string)
    hashed_password = str(hashing.digest())
    password_array = hashed_password.split('\\')
    hashed_password = ""
    for string in password_array:
        hashed_password += string
    return hashed_password

def change_password(username, password, newPassword):
    user = get_user(username)
    if (validate_user(user, password) == False):
        return False
    
    hashed_password = hash_password(newPassword)
    query = """
    UPDATE users SET password=%s WHERE username=%s 
    """
    values = [hashed_password, username]
    cursor.execute(query, values)
    conn.commit()
    return True

def delete_user(username, password):
    """
    Deletes a users information from the table
    """
    hashed_password = hash_password(password)
    query = """
    DELETE FROM users WHERE username=%s AND password=%s
    """
    values = [username, hashed_password]
    cursor.execute(query, values)
    conn.commit()

create_user_table()
create_user("John", "test", 32, 'f', 324)
#change_password("Boobby", "test", "testing")
#user = get_user("Boobby")
#print(validate_user(user, "testing"))
#delete_user("Boobby", "testing")


cursor.close()
conn.close()
