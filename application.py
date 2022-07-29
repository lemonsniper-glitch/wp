from flask import Flask

application = Flask(__name__)

@application.route("/")
def hello_world():
    return "hello world Swaroop chutiya"


application.run()
