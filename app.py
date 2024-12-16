from flask import Flask, render_template, redirect, url_for, flash, request , session ,send_from_directory,abort ,jsonify
from flask_login import LoginManager, login_user, login_required, logout_user, current_user
# from flask_sqlalchemy import SQLAlchemy
# from sqlalchemy.exc import SQLAlchemyError
from models import db, EMPWD , TimesheetEntry ,Resourceinfo,TrainingRegistration,Training
from datetime import timedelta , date ,datetime ,timezone
import uuid ,os ,traceback
from timesheet import timesheet_bp
from error import error_bp  # Import the error blueprint


app = Flask(__name__)
# db.init_app(app)

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
login_manager.login_view = 'login'

@login_manager.user_loader
def load_user(user_id):
    session = db.session 
    return session.get(EMPWD, user_id)

# ----------------------------------------------------------------Auth_Routes---------------------------------------------------


# Register the timesheet blueprint
app.register_blueprint(timesheet_bp)
app.register_blueprint(error_bp)  # Register the error blueprint
print(app.url_map)


@app.route('/login', methods=['GET', 'POST'])
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


@app.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('login'))

@app.route('/changepassword', methods=['GET', 'POST'])
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
                return redirect(url_for('login'))
        except Exception as e:
            db.session.rollback()
            session['error_type'] = "Internal Server Error"
            session['error_message'] = "Unable to Update Password at this  Moment, Please Try After Some Time."
            session['error_code'] = 500
            return redirect(url_for('error.error_page'))

    return render_template('login/changepassword.html',message=message)



@app.route('/')
def index():
    return redirect(url_for('login'))

@app.route('/favicon.ico')
def favicon():
    return send_from_directory(os.path.join(app.root_path, 'static'),
                               'images/favicon.ico', mimetype='image/vnd.microsoft.icon')

# ----------------------------------------------------------Home----------------------------------------------------------------------

@app.route('/home')
@login_required
def home():
    return render_template('home/home.html', user=current_user)
# -----------------------------------------------------------------------------------
@app.route('/comingsoon')
@login_required
def comingsoon():
    return render_template('comingsoon/comingsoon.html', user=current_user)

# -----------------------------------------------------------------------------------
@app.route('/leavesystem')
@login_required
def leavesystem():
    return render_template('leavesystem/leavesystem.html', user=current_user)


if __name__ == "__main__":
    app.run(host='0.0.0.0',port=5000, debug=True)


# from app import db
# db.create_all()
