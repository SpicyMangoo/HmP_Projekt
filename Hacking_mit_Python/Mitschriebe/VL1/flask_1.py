from flask import Flask

app = Flask(__name__)

@app.route("/")
def landing_page():
    return "Hello page"

@app.route("/home")
def home_page():
    return "<h1>HOMEPAGE</h1>"

if __name__ == "__main__": 
    app.run(debug=True)