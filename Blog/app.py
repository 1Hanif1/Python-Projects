from pickle import GLOBAL
from flask import Flask, render_template
from requests import get

app = Flask(
    __name__,
    static_folder="./static",
    template_folder="./templates",
)

GLOBAL_DATA = []


@app.route("/")
def index():
    global GLOBAL_DATA
    data = get(url="https://api.npoint.io/4ae028647ab8ffdb21f9")
    data = data.json()
    GLOBAL_DATA = data
    return render_template(
        "index.html",
        title="Hanif's Blog",
        subtitle="Welcome to my Blog :)",
        imageurl="/static/assets/img/home-bg.jpg",
        posts=data
    )


@app.route("/aboutme")
def about_me():
    return render_template(
        "about.html",
        title="About Me",
        subtitle="Just another homo sapien ^^",
        imageurl="/static/assets/img/about-bg.jpg"
    )


@app.route("/contact")
def contact():
    return render_template(
        "contact.html",
        title="Contact Me",
        subtitle="You do the asking, I do the answering XD",
        imageurl="/static/assets/img/contact-bg.jpg"
    )


@app.route("/post/<int:id>")
def get_post(id):
    requested_post = None
    for post in GLOBAL_DATA:
        if post["id"] == id:
            requested_post = post

    return render_template(
        "post.html",
        post=requested_post["body"],
        title=requested_post["title"],
        subtitle=requested_post["subtitle"],
        imageurl="/static/assets/img/post-bg.jpg"
    )


if __name__ == '__main__':
    app.run(debug=True)
