from os import environ
from smtplib import SMTP
from flask import Flask, request, render_template
from dotenv import load_dotenv
from requests import get
load_dotenv(dotenv_path="./cred.env")
app = Flask(
    __name__,
    static_folder="./static",
    template_folder="./templates",
)

GLOBAL_DATA = []
MY_EMAIL = environ["email"]
PASSWORD = environ["password"]


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


@app.route("/message", methods=["POST", "GET"])
def send_message():
    if request.method == "GET":
        return render_template(
            "contact.html",
            title="Contact Me",
            subtitle="You do the asking, I do the answering XD",
            imageurl="/static/assets/img/contact-bg.jpg"
        )

    data = {
        "name": request.form["user--name"],
        "email": request.form["user--email"],
        "number": request.form["user--number"],
        "message": request.form["user--message"],
    }
    print(send_email(data))
    name = request.form["user--name"]
    return render_template(
        "contact.html",
        title="Message Sent",
        subtitle=f"I'll get back to you soon, {name}",
        imageurl="/static/assets/img/contact-bg.jpg"
    )


def send_email(data):
    try:
        name = data["name"]
        email = data["email"]
        number = data["number"]
        message = data["message"]
        message = f"{message}\nContact:{number}\nEmail:{email}"
        with SMTP("smtp.gmail.com") as mail:
            mail.starttls()
            mail.login(user=MY_EMAIL, password=PASSWORD)
            mail.sendmail(
                from_addr=MY_EMAIL,
                to_addrs="hanifmohammed869@gmail.com",
                msg=f"Subject:{name} wants to get in touch\n\n{message}"
            )
    except Exception:
        pass


if __name__ == '__main__':
    app.run(debug=True)
