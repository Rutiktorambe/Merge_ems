from flask import Flask, render_template, redirect, url_for, flash, request , session ,send_from_directory
from flask_login import LoginManager, login_user, login_required, logout_user, current_user
from models import db, EMPWD
from datetime import timedelta
import os 
from routes  import timesheet_bp ,error_bp  ,auth


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
    return session.get(EMPWD, user_id)

# ----------------------------------------------------------------Auth_Routes---------------------------------------------------


# Register the timesheet blueprint
app.register_blueprint(timesheet_bp)
app.register_blueprint(error_bp) 
app.register_blueprint(auth)
print(app.url_map)



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
