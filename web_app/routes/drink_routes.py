# this is the "web_app/routes/drink_routes.py" file...

from flask import Blueprint, request, render_template
import requests, json

drink_routes = Blueprint("drink_routes", __name__)

@drink_routes.route("/drinks")
def drinks_list():
    print("DRINKS...")
    
    response = requests.get("https://www.thecocktaildb.com/api/json/v1/1/filter.php?a=Non_Alcoholic").json()
    drinks = response.get("drinks", [])

    return render_template("drinks.html", drinks=drinks)