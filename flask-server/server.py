from flask import Flask

app = Flask(__name__)

# Members Api Route


@app.route("/members")
def members():
    return {"members": ["Conor", "Jack", "Other"]}


if __name__ == "__main__":
    app.run(debug=True)
