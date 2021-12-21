from flask import Flask, render_template
import pandas as pd

app = Flask(__name__)


@app.route("/")
def home_page():
    return render_template("country.html")


@app.route("/log_in", methods=("POST", "GET"))
def log_in():
    return render_template("log_in.html")


@app.route("/map", methods=("POST", "GET"))
def map():
    return render_template("map.html")


@app.route("/table", methods=("POST", "GET"))
def html_table():
    df = pd.read_csv("artist_top_album.csv")
    return render_template(
        "table.html",
        tables=[df.to_html(classes="data")],
        titles=df.columns.values,
    )


if __name__ == "__main__":
    app.run(debug=True)
