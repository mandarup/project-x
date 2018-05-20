from flask import (
    Blueprint, flash, g, redirect, render_template, request, url_for
)
from werkzeug.exceptions import abort

from flaskr.auth import login_required
from flaskr.db import get_db
from flask import Flask
from string import Template

bp = Blueprint('places', __name__)


@bp.route('/places')
def index():
    return some_place_page()

@bp.route('/places/<some_place>')
def some_place_page(some_place=None):
    if some_place is None:
        some_place = "USA"
    return render_template('places/index.html', place_name=some_place)


@bp.route('/places', methods=['POST'])
def places_post():
    text = request.form['text']
    new_place = text.upper()
    return some_place_page(some_place=new_place)
