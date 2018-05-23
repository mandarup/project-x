from flask import (
    Blueprint, flash, g, redirect, render_template, request, url_for
)
from werkzeug.exceptions import abort

from flaskr.auth import login_required
from flaskr.db import get_db

bp = Blueprint('messages', __name__)


@bp.route('/messages/')
def index():
    return render_template('messages/index.html')

# decorator which tells flask what url triggers this fn
@bp.route('/messages/list_messages/')
def list_messages():
    db = get_db()
    msg = db.execute(
        'SELECT p.id, body, created, author_id'
        ' FROM message p'
        ' ORDER BY created DESC'
    ).fetchall()
    return render_template('messages/list_messages.html', messages=msg)


@bp.route('/messages/submit_message', methods=['GET', 'POST'])
# @login_required
def submit_message():
    if request.method == 'POST':

        # title = request.form['title']
        body= request.form['body']
        author_id = request.form['who']
        # print("body:", body)
        error = None

        if not body:
            error = 'Message is required.'

        if error is not None:
            flash(error)
        else:
            db = get_db()
            db.execute(
                'INSERT INTO message ( body, author_id)'
                ' VALUES ( ?, ?)',
                (body, author_id)
            )
            db.commit()
            return redirect(url_for('messages.index'))

    return render_template('messages/submit_message.html')
