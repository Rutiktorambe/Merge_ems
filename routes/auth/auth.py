from flask import Blueprint, render_template, redirect, url_for, flash, request
from flask_login import login_user, logout_user, login_required, current_user
from flask import Flask, render_template, redirect, url_for, flash, request , session ,send_from_directory
from flask_login import LoginManager, login_user, login_required, logout_user, current_user
from models import db, EMPWD
from datetime import timedelta
import os 

auth = Blueprint('auth', __name__)


@auth.route('/')
def index():
    return redirect(url_for('auth.login'))


@auth.route('/login', methods=['GET', 'POST'])
def login():
    message = None
    if request.method == 'POST':
        try:
            username = request.form['username']
            password = request.form['password']
            user = EMPWD.query.filter_by(username=username).first()

            if user is None:
                message= 'Username not found'
            elif user.Password != password:
                message= 'Incorrect password'
            else:
                login_user(user)
                return redirect(url_for('home'))
        
        except Exception as e:
            db.session.rollback()
            session['error_type'] = "Internal Server Error"
            session['error_message'] = "Something Went Wrong"
            session['error_code'] = 500
            return redirect(url_for('error.error_page'))
        

    return render_template('login/login.html',message=message)



@auth.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('auth.login'))





@auth.route('/change-password', methods=['GET', 'POST'])
def change_password():
    message = None
    if request.method == 'POST':
        try:
            username = request.form['username']
            current_password = request.form['current_password']
            new_password = request.form['new_password']
            confirm_password = request.form['confirm_password']

            user = EMPWD.query.filter_by(username=username).first()

            if not user:
                message= 'Username not found'
            elif user.Password != current_password:
                message= 'Current password is incorrect'
            elif new_password != confirm_password:
                message= 'New passwords do not match'
            elif user.Password == new_password:
                message= 'This password is currently in use'
            else:
                user.Password = new_password
                db.session.commit()
                return redirect(url_for('auth.login'))
        except Exception as e:
            db.session.rollback()
            session['error_type'] = "Internal Server Error"
            session['error_message'] = "Unable to Update Password at this  Moment, Please Try After Some Time."
            session['error_code'] = 500
            return redirect(url_for('error.error_page'))

    return render_template('login/changepassword.html',message=message)
