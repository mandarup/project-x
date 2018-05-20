from flask import (
    Blueprint, flash, g, redirect, render_template, request, url_for
)
from werkzeug.exceptions import abort

from flaskr.auth import login_required
from flaskr.db import get_db
from flask import Flask
from string import Template

bp = Blueprint('places', __name__)

HTML_TEMPLATE = Template("""
{% extends 'base.html' %}

{% block content %}
    <h2>Hello ${place_name}!</h2>

    <img src="https://maps.googleapis.com/maps/api/staticmap?size=700x300&markers=${place_name}"
    alt="map of ${place_name}">

    <img src="https://maps.googleapis.com/maps/api/streetview?size=700x300&location=${place_name}"
    alt="street view of ${place_name}">
{% endblock %}
""")


@bp.route('/places/USA')
def index():
    return some_place_page("USA")

@bp.route('/places/<some_place>')
def some_place_page(some_place):
    # return HTML_TEMPLATE.substitute(place_name=some_place)
    return render_template('places/index.html', place_name=some_place)
