from flask import Flask, jsonify

app = Flask(__name__)

@app.route("/", methods=["GET"])
def hello_world():
    return jsonify("Hello World")

@app.route("/search", methods=["GET"])
def search():
    pass

# Is this still a thing?
@app.route("/track", methods=["POST"])
def track():
    pass

if __name__ == "__main__":
    app.run(debug=True, port="8080")