from flask import Flask
from Server.database.model import db
from Server.database.connection import DB_URL
from Server.api import other, confusion

app = Flask(__name__)
app.config["JSON_AS_ASCII"] = False
app.config["SQLALCHEMY_DATABASE_URI"] = DB_URL

db.init_app(app)

app.register_blueprint(confusion.bp)
app.register_blueprint(other.bp)


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8080, debug=True)
