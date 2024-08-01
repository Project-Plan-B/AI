from flask import Flask
from Server import confusion, other

app = Flask(__name__)

app.register_blueprint(confusion.bp)
app.register_blueprint(other.bp)


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8080, debug=True)
