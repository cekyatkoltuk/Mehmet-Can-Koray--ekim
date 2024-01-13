from flask import render_template
from app import app
from app.models import Client
from app.models import Blog
from app.models import About
from app.models import Services
from app.models import Contact
from app.models import Subscriber

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/whatwedo')
def whatwedo():
    return render_template('whatwedo.html')

@app.route('/about')
def about():
    return render_template('about.html')


@app.route('/client')
def client():
    
    return render_template('client.html')

@app.route('/contact')
def contact():
    return render_template('contact.html')

@app.route('/services')
def services():
    return render_template('services.html')