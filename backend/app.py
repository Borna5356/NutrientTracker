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
        return f"{username} account has not been created"
    return user


# loads webpage displaying food information from the data table
@app.route("/food", methods=["GET"])
def get_food():
        name = request.args.get("name")
        food_info = food.get_food(name)
        if (food_info == None):
             return f"{name} does not exist in the foods database"
        return food_info

@app.route("/food_table", methods=["GET"])
def get_all_food():
     foods = food.get_all_food()
     return foods


if (__name__ == "__main__"):
    app.run()