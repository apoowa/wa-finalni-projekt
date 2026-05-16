from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

#filmy
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

#listky 
ticket_types = ["Standard", "Student", "VIP"]

@app.route("/")
def home():
    return render_template("index.html", movies=movies)

@app.route("/movie/<int:movie_id>")
def movie_detail(movie_id):
    movie = next((m for m in movies if m["id"] == movie_id), None)
    if movie is None:
        return render_template("404.html"), 404
    return render_template("movie_detail.html", movie=movie)

@app.route("/movie/<int:movie_id>/reservation", methods=["GET", "POST"])
def reservation(movie_id):
    movie = next((m for m in movies if m["id"] == movie_id), None)
    if movie is None:
        return render_template("404.html"), 404
    
    if request.method == "POST":
        email = request.form.get("email")
        ticket_type = request.form.get("ticket_type")
        
        #overeni
        if not email or not ticket_type:
            return "Please fill in all fields!", 400
            
        return render_template("reservation_success.html", movie=movie, email=email)
    
    return render_template("reservation_form.html", movie=movie, ticket_types=ticket_types)

@app.errorhandler(404)
def page_not_found(e):
    return render_template("404.html"), 404

if __name__ == "__main__":
    app.run(debug=True)