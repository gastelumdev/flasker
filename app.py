from flask import Flask, render_template

app = Flask(__name__)

# Root route
@app.route('/')
# def index():
#     return "<h1>Hello World!</h1>"
def index():
    return render_template("index.html")

# This route displays hello based on the name entered to the URL
@app.route('/user/<name>')
def user(name):
    return render_template('user.html', name=name)

# Create custom error pages
# Invalid URL
@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404

# internal server error
@app.errorhandler(500)
def page_not_found(e):
    return render_template('500.html'), 500