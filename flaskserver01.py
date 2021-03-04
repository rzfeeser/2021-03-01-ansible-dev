#!/usr/bin/python3
# An object of Flask class is our WSGI application
from flask import Flask

# Flask constructor takes the name of current
# module (__name__) as argument
app = Flask(__name__)

# route() function of the Flask class is a
# decorator, tells the application which URL
# should call the associated function
@app.route("/", methods=["GET"])        # http://0.0.0.0:2224/
def hello_world():
    return "Hello World"

@app.route("/northtrust", methods=["GET"])
def north_trust():
    x = 1
    y = 2
    z = x + y
    return str(z)


if __name__ == "__main__":
   app.run(host="0.0.0.0", port=2224) # runs the application
   # app.run(host="0.0.0.0", port=2224, debug=True) # DEBUG MODE
