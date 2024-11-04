from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/")
def home_page():
    return render_template("chat.html")

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000)
