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

# ----------------------------------------------------TimesheetHome-------------------------------------------------------------------

# @app.route('/timesheet')
# @login_required
# def timesheethome():
#     is_manager = db.session.query(EMPWD).filter_by(LineManagerID=str(current_user.EMPID)).first() is not None
#     return render_template('timesheet/timesheethome.html', is_manager=is_manager, user=current_user)

# ----------------------------------------------------------TimesheetForm--------------------------------------------------------------


# @app.route('/timesheet/fill', methods=['GET', 'POST'])
# @login_required
# def filltimesheet():
#     if request.method == 'POST':
#         try:
#             return redirect(url_for('submit_timesheet'))
#         except Exception as e:
#             db.session.rollback()
#             session['error_type'] = "Internal Server Error"
#             session['error_message'] = "Unable to Submit Timesheet at this  Moment, Please Try After SomeTime."
#             session['error_code'] = 500
#             return redirect(url_for('error_page')) 

#     return render_template(
#         'timesheet/timesheet-fill/filltimesheet.html',
#         user=current_user,
#     )

# ______________________________________________________________________

@app.route('/timesheet/history', methods=['POST'])
@login_required
def timesheet_history():
    dates = request.json.get('dates')
    emp_id = current_user.EMPID

    if dates:
        history = {}
        for date in dates:
            total_time_query = db.session.query(
                db.func.coalesce(db.func.sum((TimesheetEntry.Hours * 60) + TimesheetEntry.Minutes ),0)
                ).filter(
                TimesheetEntry.DateofEntry == date,
                TimesheetEntry.EmpID == emp_id
            ).scalar()
            total_time_in_hours = round(total_time_query / 60, 2) if total_time_query else 0.0

            history[date] = total_time_in_hours
        return jsonify(history)
    return jsonify({})

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



# ______________________________________________________________________

# @app.route('/submit_timesheet', methods=['POST'])
# @login_required
# def submit_timesheet():
#     try:
#         dates = request.form.getlist('DateofEntry')
#         dates = [date.strip() for date in dates[0].split(',')]
#         allocation_type = request.form['AllocationType']
#         category_1 = request.form['Category1']
#         category_2 = request.form.get('Category2')
#         category_3 = request.form.get('Category3', "")
#         project_code = request.form['ProjectCode']
#         comments = request.form.get('comments', "")

#         for date in dates:
#             hours = float(request.form[f'hours_{date}'])
#             minutes = float(request.form[f'minutes_{date}'])
#             entry_date = datetime.strptime(date, '%Y-%m-%d').date()

#             entry = TimesheetEntry(
#                 Uniq_ID=str(uuid.uuid4()),
#                 EmpID=current_user.EMPID,
#                 Team=current_user.Team,
#                 DateofEntry=entry_date,
#                 Hours=hours,
#                 Minutes=minutes,
#                 AllocationType=allocation_type,
#                 Category1=category_1,
#                 Category2=category_2,
#                 Category3=category_3,
#                 ProjectCode=project_code,
#                 Comment=comments,
#                 SubmitDate = datetime.now(timezone.utc),
#                 LastUploadDate = datetime.now(timezone.utc),
#                 LastUpdatedBy=current_user.username
#             )
#             db.session.add(entry)

#         db.session.commit()
#         return redirect(url_for('success'))

#     except Exception as e:
#         db.session.rollback()
#         session['error_type'] = "500 Internal Server Error"
#         session['error_message'] = "An unexpected error occurred on the server."
#         session['error_code'] = 500
#         return redirect(url_for('error_page'))


# ------------------------------------------------------------------------TimesheetSummmary-----------------------------------


@app.route('/timesheet/summary')
@login_required
def timesheet_summary():
    try:
        selected_date_str = request.args.get('selected_date')
        selected_date = datetime.strptime(selected_date_str, '%Y-%m-%d').date() if selected_date_str else datetime.now(timezone.utc).date()
        week_start = selected_date - timedelta(days=selected_date.weekday())
        week_end = week_start + timedelta(days=6)

        user_timesheets = TimesheetEntry.query.filter(
            TimesheetEntry.EmpID == current_user.get_id(),
            TimesheetEntry.DateofEntry >= week_start,
            TimesheetEntry.DateofEntry <= week_end
        ).all()
        entries_by_date = {week_start + timedelta(days=i): [] for i in range(7)}
        for entry in user_timesheets:
            entries_by_date[entry.DateofEntry].append(entry)

        weekly_summary = []
        total_billable = 0
        total_admin = 0
        total_training = 0
        total_unavailable = 0
        total_time = 0

        for day, entries in entries_by_date.items():
            billable_time = 0
            admin_time = 0
            training_time = 0
            unavailable_time = 0
            day_total_time = 0

            for entry in entries:
                time_in_hours = entry.Hours + (entry.Minutes / 60)

                if entry.AllocationType.lower() == 'billable':
                    billable_time += time_in_hours
                elif entry.AllocationType.lower() == 'non-billable':
                    if entry.Category1.lower() == 'admin':
                        admin_time += time_in_hours
                    elif entry.Category1.lower() == 'training':
                        training_time += time_in_hours
                    else:
                        unavailable_time += time_in_hours

                day_total_time += time_in_hours

            billable_time = round(billable_time, 2)
            admin_time = round(admin_time, 2)
            training_time = round(training_time, 2)
            unavailable_time = round(unavailable_time, 2)
            day_total_time = round(day_total_time, 2)

            summary = {
                'date': day,
                'billable_time': billable_time,
                'nonbillable_admin_time': admin_time,
                'nonbillable_training_time': training_time,
                'unavailable_time': unavailable_time,
                'total_time': day_total_time,
                'entries': entries
            }
            weekly_summary.append(summary)

            total_billable += billable_time
            total_admin += admin_time
            total_training += training_time
            total_unavailable += unavailable_time
            total_time += day_total_time

        percentages = {
            'billable': round((total_billable / total_time) * 100, 2) if total_time > 0 else 0,
            'admin': round((total_admin / total_time) * 100, 2) if total_time > 0 else 0,
            'training': round((total_training / total_time) * 100, 2) if total_time > 0 else 0,
            'unavailable': round((total_unavailable / total_time) * 100, 2) if total_time > 0 else 0,
            'total': 100.0 if total_time > 0 else 0,
        }

        prev_week_date = week_start - timedelta(days=7)
        next_week_date = week_start + timedelta(days=7)

        return render_template(
            'timesheet/timesheet-summery/timesheet_summary.html',
            weekly_summary=weekly_summary,
            total_billable=total_billable,
            total_admin=total_admin,
            total_training=total_training,
            total_unavailable=total_unavailable,
            total_time=total_time,
            percentages=percentages,
            selected_date=selected_date,
            week_start=week_start,
            week_end=week_end,
            prev_week_date=prev_week_date,
            next_week_date=next_week_date,
            user=current_user
        )
    except Exception as e:
            db.session.rollback()
            session['error_type'] = "Internal Server Error"
            session['error_message'] = "Unable to get Summery at this Moment"
            session['error_code'] = 500
            return redirect(url_for('error_page'))
        


# ------------------------------------------------------------------------ViewEntries-----------------------------------------------------------

@app.route('/timesheet/view_entries/<date>')
@login_required
def view_entries(date):
    try:
        date = datetime.strptime(date, '%Y-%m-%d').date()
        entries = TimesheetEntry.query.filter_by(EmpID=current_user.get_id(), DateofEntry=date).all()
        return render_template('timesheet/timesheet-summery/view_entries.html', entries=entries, date=date, user=current_user)
    except Exception as e:
            session['error_type'] = "Internal Server Error"
            session['error_message'] = f"Unable get data for the {date}"
            return redirect(url_for('error_page'))
        

@app.route('/timesheet/edit_entry/<entry_id>', methods=['GET', 'POST'])
@login_required
def edit_entry(entry_id):
    entry = TimesheetEntry.query.get(entry_id)
    
    if request.method == 'POST':
        try:
            entry.DateofEntry = datetime.strptime(request.form['DateofEntry'], '%Y-%m-%d').date()
            entry.Hours = float(request.form['hours'])
            entry.Minutes = float(request.form['minutes'])
            entry.total_time = round(entry.Hours + (entry.Minutes / 60.0), 2)
            entry.AllocationType = request.form['AllocationType']
            entry.Category1 = request.form['Category1']
            entry.Category2 = request.form.get('Category2', '')
            entry.Category3 = request.form.get('Category3', '')
            entry.ProjectCode = request.form['ProjectCode']
            entry.Comment = request.form.get('comments', '')
            entry.LastUpdatedBy = current_user.username
            entry.LastUploadDate = datetime.utcnow()
            entry.billable_time = entry.nonbillable_admin_time = entry.nonbillable_training_time = entry.unavailable_time = 0
            if entry.AllocationType == 'billable':
                entry.billable_time = entry.total_time
            elif entry.AllocationType == 'non-billable':
                if entry.Category1.lower() == 'admin':
                    entry.nonbillable_admin_time = entry.total_time
                elif entry.Category1.lower() == 'training':
                    entry.nonbillable_training_time = entry.total_time
                else:
                    entry.unavailable_time = entry.total_time

            db.session.commit()
            return redirect(url_for('view_entries', date=entry.DateofEntry))
        
        except Exception as e:
            db.session.rollback()
            session['error_type'] = "500 Internal Server Error"
            session['error_message'] = "An unexpected error occurred on the server."
            session['error_code'] = 500
            return redirect(url_for('error_page'))
    return render_template('timesheet/timesheet-summery/edit_entry.html', entry=entry, user=current_user)

# ------------------------------------------------------------DeleteEntry---------------------------------------------------------------

@app.route('/timesheet/delete_entry/<entry_id>', methods=['POST'])
@login_required
def delete_entry(entry_id):
    entry = TimesheetEntry.query.filter_by(Uniq_ID=entry_id).first()
    if entry:
        db.session.delete(entry)
        db.session.commit()
    else:
        None
    return redirect(url_for('view_entries', date=entry.DateofEntry))


# --------------------------------------------------------Success--------------------------------------------------------------------------

@app.route('/timesheet/success')
@login_required
def success():
    return render_template('success/success.html', user=current_user)

# -----------------------------------------------------------------Manage_Repotree----------------------------------------------------------

@app.route('/timesheet/manage_repotree', methods=['GET', 'POST'])
@login_required
def manage_repotree():

    search_term = request.form.get('search', '').strip()
    query = EMPWD.query.filter_by(LineManagerID=current_user.EMPID)
    if search_term:
        query = query.filter(EMPWD.EName.ilike(f"%{search_term}%"))
    employees = query.all()
    
    return render_template('timesheet/timesheet-manager/manage_repotree.html', employees=employees, search_term=search_term, user=current_user)


@app.route('/timesheet/manage_repotree/employee_entries/<emp_id>')
@login_required
def employee_entries(emp_id):
    selected_date_str = request.args.get('selected_date', datetime.utcnow().strftime('%Y-%m-%d'))
    selected_date = datetime.strptime(selected_date_str, '%Y-%m-%d').date()
    week_start = selected_date - timedelta(days=selected_date.weekday())
    week_end = week_start + timedelta(days=6)

    entries = TimesheetEntry.query.filter(
        TimesheetEntry.EmpID == emp_id,
        TimesheetEntry.DateofEntry >= week_start,
        TimesheetEntry.DateofEntry <= week_end
    ).all()

    entries_by_date = []
    for entry in entries:
        entry_data = {
            'date': entry.DateofEntry,
            'day': entry.DateofEntry.strftime('%A'),
            'hours': entry.Hours,
            'minutes': entry.Minutes,
            'allocation_type': entry.AllocationType,
            'comments': entry.Comment,
            'project_code': entry.ProjectCode
        }
        entries_by_date.append(entry_data)

    prev_week_date = week_start - timedelta(days=7)
    next_week_date = week_start + timedelta(days=7)

    return render_template(
        'timesheet/timesheet-manager/employee_entries.html',
        emp_id=emp_id,
        entries_by_date=entries_by_date,
        week_start=week_start,
        week_end=week_end,
        prev_week_date=prev_week_date,
        next_week_date=next_week_date,
         user=current_user
    )
    
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
