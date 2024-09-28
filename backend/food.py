import psycopg2

conn = psycopg2.connect(host="localhost", dbname="NutrientTracker", user="User",
                        password="Tehran14!", port=5432)

cursor = conn.cursor()

def create_food_table():
    #Creates a table that hold data for food
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
    #Adds a food item to the food table
    query = """
    INSERT INTO foods (name, total_calories, protein, carbs, sugars, fats) VALUES
    (%s, %s, %s, %s, %s, %s)
    """
    values = [name, calories, protein, carbs, sugars, fats]
    cursor.execute(query, values)
    conn.commit()

def get_all_food():
    #gets all the food from the foods table
    query = "SELECT * FROM foods"
    cursor.execute(query)
    conn.commit()
    foods =  cursor.fetchall()
    food_list = []
    for food in foods:
        food_dict = {"Name": food[0], "Calories": food[1], "Protein": food[2], "Carbs": food[3], "Sugars": food[4], "Fats": food[5]}
        food_list.append(food_dict)
    return food_list




def get_food(name):
    #gets a specific food from the database using the name
    query = """
    SELECT * FROM foods WHERE name=%s
    """
    values = [name]
    cursor.execute(query, values)
    conn.commit()
    food = cursor.fetchone()
    if (food == None):
        return None
    return {"Name": food[0], "Calories": food[1], "Protein": food[2], "Carbs": food[3], "Sugars": food[4], "Fats": food[5]}

def main():
    print(get_all_food())
    cursor.close()
    conn.close()

if (__name__ == "__main__"):
    main()