import psycopg2

conn = psycopg2.connect(host="localhost", dbname="NutrientTracker", user="User",
                        password="Tehran14!", port=5432)

cursor = conn.cursor()
def create_calorie_tracker_table():
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

create_calorie_tracker_table()
cursor.close()
conn.close()