from flask import Flask
from flask import request

application = Flask(__name__)

@application.route("/")
def hello():
    return "Coordinated, this time?: " + request.url

if __name__ == "__main__":
    application.run()
