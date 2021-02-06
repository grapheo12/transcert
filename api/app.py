from flask import Flask, request, make_response
from flask_cors import CORS

app = Flask('app')
CORS(app)

DATA = None
@app.before_first_request
def load_data():
    global DATA
    with open("suspect.dat", "r") as f:
        DATA = frozenset([a.strip() for a in f.readlines()])

    print("%d entries loaded" % len(DATA))


@app.route("/")
def hello():
    return """<h1>Welcome to <span style='color: red;'>Transcert</span></h1>
    <br>
    <p>%d entries in database</p>
    """ % len(DATA)


@app.route("/data")
def all_data():
    return "\n".join(list(DATA))

@app.route("/isindanger")
def check_danger():
    domain = request.args.get('domain')
    if domain is not None and domain in DATA:
        return "Yes"
    
    return "No"


if __name__ == "__main__":
    app.run()