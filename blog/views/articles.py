from flask import Blueprint, render_template
from werkzeug.exceptions import NotFound
from blog.views.users import USERS

articles_app = Blueprint("articles_app", __name__)

ARTICLES = {
    1: {
        "title": "Flask",
        "text": "many texts",
        "author": 2
    },
    2: {
        "title": "Django",
        "text": "more texts",
        "author": 2
    },
    3: {
        "title": "JSON:API",
        "text": "not many texts",
        "author": 1
    },
    4: {
        "title": "Python",
        "text": "fantasy is end",
        "author": 3
    }
}


@articles_app.route("/", endpoint="list")
def articles_list():
    return render_template("articles/list.html", articles=ARTICLES)


@articles_app.route("/<int:article_id>/", endpoint="details")
def article_details(article_id: int):
    try:
        article_raw = ARTICLES[article_id]
    except KeyError:
        raise NotFound(f"Article #{article_id} doesn't exist!")
    title = article_raw['title']
    text = article_raw['text']
    author = USERS[article_raw['author']]
    return render_template(
        "articles/details.html",
        title=title,
        text=text,
        author=author
    )
