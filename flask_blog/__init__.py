from flask import Flask
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)
app.config['SECRET_KEY'] = '1bd27a40a4656eddeefbd0c43d492bf7'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'  # holds the information
db = SQLAlchemy(app)

from flask_blog import routes # this is to avoid circular imports