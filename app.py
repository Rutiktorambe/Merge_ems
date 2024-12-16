from flask import Flask, render_template, redirect, url_for, flash, request , session ,send_from_directory,abort ,jsonify
from flask_login import LoginManager, login_user, login_required, logout_user, current_user
# from flask_sqlalchemy import SQLAlchemy
# from sqlalchemy.exc import SQLAlchemyError
from models import db, EMPWD , TimesheetEntry ,Resourceinfo,TrainingRegistration,Training
from datetime import timedelta , date ,datetime ,timezone
import uuid ,os ,traceback
from timesheet import timesheet_bp


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
            return redirect(url_for('error_page'))
        

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
            return redirect(url_for('error_page'))

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

# ______________________________________________________________________


# ______________________________________________________________________

@app.route('/get_projects/<category>', methods=['GET'])
@login_required
def get_projects(category):
    projects = Resourceinfo.query.filter_by(Team=category,EmpID=current_user.EMPID).all()
    project_data = [{"ProjectName": project.ProjectName, "ProjectCode": project.ProjectCode} for project in projects]
    return jsonify(project_data)

# ______________________________________________________________________

@app.route('/get_datetime/<date>', methods=['GET'])
@login_required
def get_datetime(date):
    # if request.headers.get("X-Requested-With") != "XMLHttpRequest":
    #     abort(403)  # Forbidden
    date_obj = datetime.strptime(date, "%Y-%m-%d").date()
    entries = TimesheetEntry.query.filter_by(DateofEntry=date_obj, EmpID=current_user.EMPID).all()
    total_time = sum(entry.Hours + (entry.Minutes / 60) for entry in entries)
    return jsonify({"total_time": round(total_time, 2)}) 

# ______________________________________________________________________

@app.route('/projectCode/<projectCode>', methods=['GET'])
@login_required
def get_projects_dates(projectCode):
    projects=Resourceinfo.query.filter_by(ProjectCode=projectCode,EmpID=current_user.EMPID).all()
    project_data = [{"ProjectName": project.ProjectName, "ProjectCode": project.ProjectCode,"FromDate": project.FromDate, "ToDate": project.ToDate} for project in projects]
    return jsonify(project_data)

# ______________________________________________________________________

@app.route('/get_trainings/<training>', methods=['GET'])
@login_required
def get_trainings(training):
    if training.lower() == "internal":
        trainings = TrainingRegistration.query.join(Training, TrainingRegistration.TID == Training.TID) \
            .filter(Training.TType == "Internal",TrainingRegistration.EmpID == current_user.EMPID).all()
    elif training.lower() == "external":
        trainings = TrainingRegistration.query.join(Training, TrainingRegistration.TID == Training.TID) \
            .filter(Training.TType == "External", TrainingRegistration.EmpID == current_user.EMPID).all()
    else:
        trainings = []
    if trainings:
        trainings_data = [
            {"TID": training.TID, "TName": Training.query.filter_by(TID=training.TID).first().TName} 
            for training in trainings
        ]
    else:
        trainings_data = []
    return jsonify(trainings_data)



# ------------------------------------------------------------------------ViewEntries-----------------------------------------------------------
      



    
# ---------------------------------------------------------Error_Handling---------------------------------------------------
@app.route('/error')
def error_page():
    error_type = session.get('error_type', 'Unknown Error')
    error_message = session.get('error_message', 'No additional information provided.')
    error_code = session.get('error_code', 500)
    return render_template('error/error.html', error_type=error_type, error_message=error_message, error_code=error_code, user=current_user)

@app.errorhandler(404)
def not_found_error(error):
    print("404 Error:", traceback.format_exc())  # Print full traceback
    session['error_type'] = "404 Not Found"
    session['error_message'] = "The requested resource could not be found."
    session['error_code'] = 404
    return redirect(url_for('error_page'))

@app.errorhandler(500)
def internal_error(error):
    print("500 Error:", traceback.format_exc())  # Print full traceback
    session['error_type'] = "500 Internal Server Error"
    session['error_message'] = "An unexpected error occurred on the server."
    session['error_code'] = 500
    return redirect(url_for('error_page'))

@app.errorhandler(Exception)
def handle_exception(error):
    print("Unhandled Exception:", traceback.format_exc())  # Print full traceback
    session['error_type'] = "Exception"
    session['error_message'] = str(error)
    session['error_code'] = 500
    return redirect(url_for('error_page'))



if __name__ == "__main__":
    app.run(host='0.0.0.0',port=5000, debug=True)


# from app import db
# db.create_all()
