from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from os import path
import os
from flask_login import LoginManager

db = SQLAlchemy()
DB_NAME = "database.db"


def create_app():
    app = Flask(__name__)
    # Use environment variables in production; fall back to local defaults for development
    app.config['SECRET_KEY'] = os.environ.get('SECRET_KEY', 'hjshjhdjah kjshkjdhjs')
    database_url = os.environ.get('DATABASE_URL', f'sqlite:///{DB_NAME}')
    # Handle Postgres URL format for Vercel deployment
    if database_url.startswith('postgres://'):
        database_url = database_url.replace('postgres://', 'postgresql://', 1)
    app.config['SQLALCHEMY_DATABASE_URI'] = database_url
    # Recommended to disable track modifications for performance
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    db.init_app(app)

    from .views import views
    from .auth import auth

    app.register_blueprint(views, url_prefix='/')
    app.register_blueprint(auth, url_prefix='/')

    from .models import User, Note
    
    # Optimize database initialization for serverless environment
    with app.app_context():
        try:
            # Check if tables exist by querying the User table
            User.query.first()
        except Exception as e:
            # Tables don't exist, create them
            db.create_all()
            print('Created database tables')

    login_manager = LoginManager()
    login_manager.login_view = 'auth.login'
    login_manager.init_app(app)

    @login_manager.user_loader
    def load_user(id):
        return User.query.get(int(id))

    return app


def create_database(app):
    if not path.exists('website/' + DB_NAME):
        db.create_all(app=app)
        print('Created Database!')
