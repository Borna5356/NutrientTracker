from flask import Flask, request
import users, food

app = Flask(__name__)

@app.route("/")
def home():
    return "<h1>Hello World</h1>"

#loads webpage to display specific user from the data table
@app.route("/users", methods=["GET"])
def get_users():
    username = request.args.get("username")
    user = users.get_user(username)
    if (user == None):
        return f"{user} account has not been created"
    return {"Name": user[0], "Password": user[1], "Age": user[2], "Sex": user[3], "Weight": user[4]}


# loads webpage displaying food information from the data table
@app.route("/food", methods=["GET"])
def get_food():
        name = request.args.get("name")
        food_info = food.get_food(name)
        if (food_info == None):
             return f"{name} does not exist in the foods database"
        return {"Name": food_info[0], "Calories": food_info[1], "Protein": food_info[2], "Carbs": food_info[3], "Sugars": food_info[4], "Fats": food_info[5]}


if (__name__ == "__main__"):
    app.run()