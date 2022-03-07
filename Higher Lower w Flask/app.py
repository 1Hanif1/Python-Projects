import random
from flask import Flask
app = Flask(__name__)
random_num = None


@app.route('/')
def hello_world():
    global random_num
    random_num = random.randint(0, 9)
    return '<h1>Guess a Number between 0 and 9</h1>'\
        '<img src="https://media.giphy.com/media/3o7aCSPqXE5C6T8tBC/giphy.gif"/>'


@app.route('/<int:num>')
def greet(num):
    if num < random_num:
        return f'<h1 style="color:red">Too Low, Try Again</h1>'\
            '<img src="https://media.giphy.com/media/jD4DwBtqPXRXa/giphy.gif"/>'
    elif num > random_num:
        return f'<h1 style="color:red">Too High, Try Again</h1>'\
            '<img src="https://media.giphy.com/media/3o6ZtaO9BZHcOjmErm/giphy.gif"/>'
    else:
        return f'<h1 style="color:green">Correct!</h1>'\
            '<img src="https://media.giphy.com/media/4T7e4DmcrP9du/giphy.gif"/>'


if __name__ == '__main__':
    app.run(debug=True)
