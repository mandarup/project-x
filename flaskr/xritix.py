from flask import (
    Blueprint, flash, g, redirect, render_template, request, url_for,
    send_file, render_template_string
)
from werkzeug.exceptions import abort
import logging

from flaskr.auth import login_required
from flaskr.db import get_db


bp = Blueprint('xritix', __name__)

@bp.route('/xritix/')
def index():
    # db = get_db()
    # posts = db.execute(
    #     'SELECT p.id, title, body, created, author_id, username'
    #     ' FROM arxiv p JOIN user u ON p.author_id = u.id'
    #     ' ORDER BY created DESC'
    # ).fetchall()
    # paper = sample_paper()
    # print(paper)

    # split_paragraphs()
    return render_template('xritix/index.html')


# @bp.route('/xritix/sample_paper')
@bp.route('/xritix/sample_paper/')
def sample_paper():
    return send_file('templates/xritix/sample_paper.html')


@bp.route('/xritix/sample_paper_render/')
def sample_paper_render():
    # html = split_paragraphs('xritix/sample_paper_raw.html', isfile=True)
    htmlfile = "/Users/mupadhye/git/mandarup/projects/arxiv-reader/flaskr/templates/xritix/sample_paper_raw.html"

    html = split_paragraphs(htmlfile, isfile=True)
    # print(render_template('xritix/sample_paper_raw.html'))
    # return render_template('xritix/sample_paper_raw.html')

    html_str = str(html)
    return render_template_string(html_str)


def split_paragraphs(html_input, isfile=True):
    from bs4 import BeautifulSoup
    # soup = BeautifulSoup(html_doc, 'html.parser')
    if isfile:
        with open(html_input, 'rb') as fp:
            html = split_html_paragraphs_from_str(fp)
    else:
        html = split_html_paragraphs_from_str(html_input)

    # print(html)
    return html

def split_html_paragraphs_from_str(htmltxt):
    from bs4 import BeautifulSoup
    # soup = BeautifulSoup(html_doc, 'html.parser')
    # htmlfile = "/Users/mupadhye/git/mandarup/projects/arxiv-reader/flaskr/templates/xritix/sample_paper_raw.html"
    soup = BeautifulSoup(htmltxt, "html.parser")
    paragraphs = soup.find_all('p')
    counter = 0
    # print(paragraphs)

    for e, p in enumerate(paragraphs):
        # print(e, p, '\n')
        p, counter = insert_id(p, counter)
        counter += 1
        # print('paragraph id', p['id'])

    # first_para = soup.find('p')
    # print(first_para)
    # print(first_para['id'])
    # raise
    # while True:
    #     counter += 1
    #     next_para = soup.find_next('p')
        # print(next_para)
        # soup.find_next('p')['id'] = counter

    return soup




def insert_id(tag, counter):
    tag['id'] = counter
    return tag, counter
