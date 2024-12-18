from flask import Flask, Blueprint, render_template, redirect, url_for, flash, request, session, send_from_directory, jsonify, current_app
from flask_login import LoginManager, login_user, logout_user, login_required, current_user
from flask_sqlalchemy import SQLAlchemy
from os import path
from datetime import timedelta
from .models import db, EMPWD, TimesheetEntry, Resourceinfo, Training, TrainingRegistration
from .routes import timesheet_bp, error_bp, auth, home_bp, other_bp

db = SQLAlchemy()
DB_NAME = "database.db"

def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = 'WinterIsComing'
    app.config['SQLALCHEMY_DATABASE_URI'] = f'sqlite:///{path.join(app.root_path, DB_NAME)}'
    
    @app.before_request
    def session_management():
        session.permanent = True

    db.init_app(app)
    create_database(app)

    login_manager = LoginManager()
    login_manager.init_app(app)
    login_manager.login_view = 'auth.login'

    @login_manager.user_loader
    def load_user(user_id):
        return db.session.get(EMPWD, user_id)

    # Register Blueprints
    app.register_blueprint(timesheet_bp)
    app.register_blueprint(error_bp)
    app.register_blueprint(auth)
    app.register_blueprint(home_bp)
    app.register_blueprint(other_bp)

    return app

def create_database(app):
    if not path.exists(f'{app.root_path}/{DB_NAME}'):
        with app.app_context():
            db.create_all()
        print("Created Database!")
    else:
        print('Database already exists')
