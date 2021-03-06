import EmailVerify as ev
from flask import Flask, jsonify, request

app = Flask(__name__)

@app.route("/<str:email>", methods=["GET"])
def get(email):
    ev.load_web()
    ev.login(email)
    result = ev.verify()
    return(result)

if __name__ == "__main__":
    app.run(debug=True)