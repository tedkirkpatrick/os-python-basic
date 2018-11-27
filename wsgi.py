from flask import Flask
application = Flask(__name__)

@application.route("/")
def hello():
    return "Salut, monde!"

if __name__ == "__main__":
    application.run()
