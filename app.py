from flask import Flask, render_template

app = Flask(__name__)


# Testovací data filmů
movies = [
    {
        "id": 1,
        "title": "The Handmaiden",
        "image": "thehandmaiden.jpg",
        "description": "A woman is hired as a handmaid to a Japanese heiress, but secretly she is involved in a plot to defraud her.",
        "cast": "Kim Min-hee, Kim Tae-ri",
        "director": "Park Chan-wook"
    },
    {
        "id": 2,
        "title": "Bound",
        "image": "bound.jpg",
        "description": "A tough female ex-con and her lover hatch a scheme to steal millions of stashed mob cash.",
        "cast": "Jennifer Tilly, Gina Gershon",
        "director": "Lana & Lilly Wachowski"
    },
    {
        "id": 3,
        "title": "Redline",
        "image": "redline.jpg",
        "description": "A story about the most dangerous car race in the galaxy and the deadly illegal underworld that runs it.",
        "cast": "Takuya Kimura, Yuu Aoi",
        "director": "Takeshi Koike"
    }
]


@app.route("/")
def home():
    return render_template("index.html", movies=movies)



if __name__ == "__main__":
    app.run(debug=True)