from flask import Flask

app = Flask(__name__)



##########################################
### Contains Directory Information & Pages
##########################################
from app import app

# Your main page
@app.route('/')

# Signup Page

@app.route('/signup')
def sign_up():
    return ("this is sign up page")
