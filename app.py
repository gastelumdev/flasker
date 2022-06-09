from flask import Flask, render_template
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired

app = Flask(__name__)
app.config['SECRET_KEY'] = "my super secrete key"

# Create a form Class
class NamerForm(FlaskForm):
    name = StringField("What's your name?", validators=[DataRequired()])
    submit = SubmitField("Submit")

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

@app.route('/name', methods=['GET', 'POST'])
def name():
    name = None
    form = NamerForm()
    if form.validate_on_submit:
        name = form.name.data
        form.name.data = ''
    return render_template("name.html",
        name = name,
        form = form)