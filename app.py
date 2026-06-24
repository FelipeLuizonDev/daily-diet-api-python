from flask import Flask

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


if __name__ == "__main__":
    app.run(debug=True)