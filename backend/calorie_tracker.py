import psycopg2

conn = psycopg2.connect(host="localhost", dbname="NutrientTracker", user="User",
                        password="Tehran14!", port=5432)

cursor = conn.cursor()
def create_calorie_tracker_table():
    #Creates a table to hold the nutrient informaton for a user
    query = """
    CREATE TABLE IF NOT EXISTS calorie_tracker (
    username VARCHAR(255),
    date DATE,
    food TEXT,
    calories INT,
    FOREIGN KEY (username) REFERENCES users(username),
    FOREIGN KEY (food) REFERENCES foods(name)
    ) 
    """
    cursor.execute(query)
    conn.commit()


def add_calories(username, date, food, calories):
    #adds calorie information for a user
    query = """
    INSERT INTO calorie_tracker (username, date, food, calories) VALUES
    (%s, %s, %s, %s)
    """
    values = [username, date, food, calories]
    cursor.execute(query, values)
    conn.commit()


def get_calories_from_user(username):
    #gets all the calorie information using for a specfic user
    query = "SELECT * FROM calorie_tracker WHERE username=%s"
    values = [username]
    cursor.execute(query, values)
    conn.commit()
    return cursor.fetchall()

def main():
    create_calorie_tracker_table()
    add_calories("John", "02/12/2001", "Coke", 300)
    print(get_calories_from_user("John"))
    cursor.close()
    conn.close()

if (__name__ == "__main__"):
    main()