import psycopg2

conn = psycopg2.connect(host="localhost", dbname="NutrientTracker", user="User",
                        password="Tehran14!", port=5432)

cursor = conn.cursor()

def create_tracked_calories_table():
    query = """
    CREATE TABLE IF NOT EXISTS food (
    name TEXT PRIMARY KEY,
    total_calories INT,
    protein INT,
    carbs INT,
    sugars INT,
    fats INT
    )
    """
    cursor.execute(query)
    conn.commit()


create_tracked_calories_table()
cursor.close()
conn.close()