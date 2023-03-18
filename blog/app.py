from flask import Flask, render_template
from blog.views.users import users_app
from blog.views.articles import articles_app
from blog.views.auth import auth_app, login_manager
from blog.models.database import db

app = Flask(__name__)


@app.route("/")
def index():
    return render_template("index.html")


app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:////tmp/blog.db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
app.config["SECRET_KEY"] = "abcdefg123456"

app.register_blueprint(users_app, url_prefix="/users")
app.register_blueprint(articles_app, url_prefix="/articles")
app.register_blueprint(auth_app, url_prefix="/auth")

db.init_app(app)

login_manager.init_app(app)


@app.cli.command("init-db")
def init_db():
    """
    Run in your terminal:
    flask init-db
    """
    db.create_all()
    print('done!')


@app.cli.command("create-users")
def create_users():
    """
    Run in your terminal:
    flask create-users
    > done! created users: <User #1 'admin'> <User #2 'james'>
    """
    from blog.models import User
    admin_4 = User(user_name='admin_4', is_staff=True)
    james_3 = User(user_name='james_3')

    db.session.add(admin_4)
    db.session.add(james_3)
    db.session.commit()

    print("done! created users:", admin_4, james_3)
