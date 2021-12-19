from flask import Flask, render_template
import pandas as pd

app = Flask(__name__)


@app.route("/")
def hello():
    return "Hello, World!"


@app.route("/table", methods=("POST", "GET"))
def html_table():
    df = pd.read_csv("artist_top_album.csv")
    return render_template(
        "simple.html",
        tables=[df.to_html(classes="data")],
        titles=df.columns.values,
    )


if __name__ == "__main__":
    app.run(debug=True)
