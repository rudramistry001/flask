from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello World!!! this is my first flask application"
app.run()