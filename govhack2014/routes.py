from govhack2014 import app
from govhack2014.models import *
from flask import render_template, request, flash, redirect, url_for
from govhack2014.resources import *

def get_post_value(key):
    try:
        return request.form[key]
    except KeyError:
        return None


@app.route('/')
def index():
    return render_template('index.html')