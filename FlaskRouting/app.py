from flask import Flask, request, render_template

app = Flask(__name__)


# Home page
@app.route('/')
def index():
    return "Welcome to homepage"


# Login page
@app.route('/login')
def login():
    return "Welcome to login page"


# Using Variable
@app.route('/profile/<username>')
def profile_user(username):
    return "Username is %s " % username


# int variable
@app.route('/profile/<int:uid>')
def profile(uid):
    return "User profile id is %s " % uid


# HTTP Methods
@app.route('/accounts', methods=['GET', 'POST'])
def accounts():
    if request.method == "POST":
        return "Using POST Method"
    elif request.method == "GET":
        return "Using GET Method"


# Rendering template
@app.route('/pro/<name>')
def pro(name):
    return render_template('profile.html', name=name)


# Mapping multiple URL
@app.route('/user_profile')
@app.route('/user_profile/<username>')
def user_pro(username=None):
    return render_template('home.html', user=username)


# Passing Lists
@app.route('/shopping')
def shopping():
    cart = ['Levis Jeans', 'Chocolates', 'Water bottle', 'Mobile phone']
    return render_template('shopping.html', cart=cart)


if __name__ == "__main__":
    app.run(debug=True)
