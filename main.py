
from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def boogle():
    return render_template("boogle.html")

@app.route("/Fakebook")
def Fakebook():
    return render_template("Fakebook.html")
@app.route("/bootstrap")
def Bootstrap():
    return render_template("bootstrap.html")


if __name__ == "__main__":
    app.run(use_reloader=True)






