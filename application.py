from flask import Flask
application = Flask(__name__)
app = application

@app.route("/")
def index():
    return "Hello World - App is working!"

if __name__ == "__main__":
    app.run(host="0.0.0.0")
