from flask import Flask, session, render_template, Response, request, redirect
from datetime import timedelta
import requests
statDir = './static/'
templateDir = './templates/'
# initialize a flask object
app = Flask(__name__,static_folder=statDir,
            template_folder=templateDir)

app.config['SECRET_KEY'] = 'abcd12345'

@app.route('/')
def index():
    return "no url"

@app.route("/api",methods =['POST','GET'])
def start():
    if request.method == "POST":
        print(request.form["url"])
        return requests.get(request.form["url"])
    return "request did not work how you wanted"


@app.after_request
def after_request(response):
    response.headers["Cache-Control"] = "no-cache, no-store, must-revalidate, public, max-age=0"
    response.headers["Expires"] = '0'
    response.headers["Pragma"] = "no-cache"
    return response

if __name__ == "__main__":
    app.run(debug=True)