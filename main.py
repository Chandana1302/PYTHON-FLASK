from flask import Flask
app = Flask(__name__)
@app.route("/")
def hello():
    return "Hello,Chandana"
if __name__ == "__main__":
    app.run()
    