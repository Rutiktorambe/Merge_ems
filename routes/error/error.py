from flask import Flask, Blueprint, render_template, redirect, url_for, flash, request, session, send_from_directory, jsonify, current_app
from flask_login import LoginManager, login_user, logout_user, login_required, current_user
from models import db, EmpWD, TimesheetEntry, Resourceinfo, Trainings, TrainingRegistration
from datetime import datetime, timedelta, timezone
import os
import uuid
import traceback

# Create a blueprint for error handling
error_bp = Blueprint('error', __name__)

@error_bp.app_errorhandler(404)
def not_found_error(error):
    # print("404 Error:", traceback.format_exc()) 
    session['error_type'] = "404 Not Found"
    session['error_message'] = "The requested resource could not be found."
    session['error_code'] = 404
    return redirect(url_for('error.error_page'))

@error_bp.app_errorhandler(500)
def internal_error(error):
    # print("500 Error:", traceback.format_exc())  
    session['error_type'] = "500 Internal Server Error"
    session['error_message'] = "An unexpected error occurred on the server."
    session['error_code'] = 500
    return redirect(url_for('error.error_page'))

@error_bp.app_errorhandler(Exception)
def handle_exception(error):
    # print("Unhandled Exception:", traceback.format_exc())  
    session['error_type'] = "Exception"
    session['error_message'] = str(error)
    session['error_code'] = 500
    return redirect(url_for('error.error_page'))

@error_bp.route('/error')
def error_page():
    error_type = session.get('error_type', 'Unknown Error')
    error_message = session.get('error_message', 'No additional information provided.')
    error_code = session.get('error_code', 500)
    return render_template('error/error.html', error_type=error_type, error_message=error_message, error_code=error_code)
