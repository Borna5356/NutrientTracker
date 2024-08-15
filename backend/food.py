import psycopg2

conn = psycopg2.connect(host="localhost", dbname="NutrientTracker", user="User",
                        password="Tehran14!", port=5432)

cursor = conn.cursor()

def create_food_table():
    query = """
    CREATE TABLE IF NOT EXISTS foods (
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

def create_food(name, calories, protein, carbs, sugars, fats):
    query = """
    INSERT INTO foods (name, total_calories, protein, carbs, sugars, fats) VALUES
    (%s, %s, %s, %s, %s, %s)
    """
    values = [name, calories, protein, carbs, sugars, fats]
    cursor.execute(query, values)
    conn.commit()

def get_food(name):
    query = """
    SELECT * FROM foods WHERE name=%s
    """
    values = [name]
    cursor.execute(query, values)
    conn.commit()
    return cursor.fetchone()

create_food_table()
create_food("Coke", 300, 23, 23, 34, 45)
#print(get_food("burger"))
cursor.close()
conn.close()