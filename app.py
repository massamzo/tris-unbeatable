from flask import Flask, render_template, request
from tris import minMax

app = Flask(__name__)

@app.route("/")
def main():
    return render_template("index.html")

@app.route("/process", methods=["POST", "GET"])
def process():
    if request.method == 'POST':
        data = request.get_json()
        tris = data['tris']

        # second parameter is the player's turn: in this case it's 1 for x robot
        inp = minMax(tris, 1, 0)
        print(inp)
        return str(inp);


    return "ciao"
app.run(host="0.0.0.0", port=5000, debug=True)