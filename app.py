from flask import Flask, request
from datetime import datetime

from database import db
from models import Meal

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
            return {"message": f"{field} is required."}, 400
        
    try:
        meal_datetime = datetime.fromisoformat(data["datetime"])
    except ValueError:
        return {"message": "Invalid datetime format"}, 400
    
    meal = Meal(
        name=data["name"], # type: ignore
        description=data["description"], # type:ignore
        datetime=meal_datetime, # type: ignore
        is_on_diet=data["is_on_diet"] # type: ignore
    )
    
    db.session.add(meal)
    db.session.commit()
    
    return {"message": "Meal created successfully", "meal_id": meal.id}, 201


if __name__ == "__main__":
    app.run(debug=True)