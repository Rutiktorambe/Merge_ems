from flask import Flask, Blueprint, render_template, redirect, url_for, flash, request, session, send_from_directory, jsonify, current_app
from flask_login import LoginManager, login_user, logout_user, login_required, current_user
from models import db, EMPWD, TimesheetEntry, Resourceinfo, Training, TrainingRegistration
from datetime import datetime, timedelta, timezone
import os
import uuid
import traceback

home_bp = Blueprint('home', __name__)



@home_bp.route('/home')
@login_required
def home():
    return render_template('home/home.html', user=current_user)


@home_bp.route('/favicon.ico')
def favicon():
    return send_from_directory(os.path.join(current_app.root_path, 'static'),
                               'images/favicon.ico', mimetype='image/vnd.microsoft.icon')
