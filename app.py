from flask import Flask, request
from datetime import datetime

from database import db
from models import Meal
from utils import success_response, error_response

app = Flask(__name__)

app.config["SQLALCHEMY_DATABASE_URI"] = (
    "mysql+pymysql://root:root@localhost:3306/daily_diet"
)

app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

db.init_app(app)

with app.app_context():
    db.create_all()

@app.route("/")
def health_check():
    return {"message": "API is running"}, 200

@app.route("/meals", methods=["POST"])
def create_meal():
    data = request.get_json()
    
    required_fields = [
        "name",
        "description",
        "datetime",
        "is_on_diet"
    ]
    
    for field in required_fields:
        if field not in data:
            return error_response(f"{field} is required")
        
    try:
        meal_datetime = datetime.fromisoformat(data["datetime"])
    except ValueError:
        return error_response("Invalid datetime format")
    
    meal = Meal(
        name=data["name"], # type: ignore
        description=data["description"], # type:ignore
        datetime=meal_datetime, # type: ignore
        is_on_diet=data["is_on_diet"] # type: ignore
    )
    
    db.session.add(meal)
    db.session.commit()
    
    return success_response("Meal created successfully", {"meal_id": meal.id}, 201)

@app.route("/meals", methods=["GET"])
def list_meals():
    meals = Meal.query.all()
    
    return success_response("Meals retrieved successfully", {"meals": [meal.to_dict() for meal in meals]})

@app.route("/meals/<int:meal_id>", methods=["GET"])
def get_meal(meal_id):
    meal = db.session.get(Meal, meal_id)
    
    if not meal:
        return error_response("Meal not found", 404)
    
    return success_response("Meal retrieved successfully", {"meal": meal.to_dict()})

if __name__ == "__main__":
    app.run(debug=True)