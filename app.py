from flask import Flask, Blueprint, render_template, redirect, url_for, flash, request, session, send_from_directory, jsonify, current_app
from flask_login import LoginManager, login_user, logout_user, login_required, current_user
from models import db, EmpWD, TimesheetEntry, Resourceinfo, Trainings, TrainingRegistration
from datetime import datetime, timedelta, timezone
import os
import uuid
import traceback
from routes  import timesheet_bp ,error_bp  ,auth ,home_bp ,other_bp


app = Flask(__name__)

# app.config['SQLALCHEMY_DATABASE_URI'] = r'sqlite:///Z:/0.0 EMS/New folder_Ma/RT/database.db' 
app.config['SQLALCHEMY_DATABASE_URI'] = r'sqlite:///database.db'     #local-foder DB
app.config['SECRET_KEY'] = 'WinterIsComing'
app.config['PERMANENT_SESSION_LIFETIME'] = timedelta(minutes=99)

@app.before_request
def session_management():
    session.permanent = True

db.init_app(app)

login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = 'auth.login'

@login_manager.user_loader
def load_user(user_id):
    session = db.session 
    return session.get(EmpWD, user_id)


app.register_blueprint(error_bp) 
app.register_blueprint(auth)
app.register_blueprint(home_bp)
app.register_blueprint(timesheet_bp)
app.register_blueprint(other_bp)

print(app.url_map)

if __name__ == "__main__":
    app.run(host='0.0.0.0',port=5000, debug=True)
