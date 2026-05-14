from flask import Flask, render_template

app = Flask(__name__)


# Testovací data filmů
movies = [
    {
        "id": 1,
        "title": "The Handmaiden",
        "image": "thehandmaiden.jpg"
    },
    {
        "id": 2,
        "title": "Bound",
        "image": "bound.jpg"
    },
    {
        "id": 3,
        "title": "Redline",
        "image": "redline.jpg"
    }
]


@app.route("/")
def home():
    return render_template("index.html", movies=movies)



if __name__ == "__main__":
    app.run(debug=True)