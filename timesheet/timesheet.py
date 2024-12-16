from flask import Blueprint, render_template, redirect, url_for, jsonify, session, request
from flask_login import login_required, current_user
from models import db, TimesheetEntry, Resourceinfo, Training, TrainingRegistration,EMPWD
from datetime import datetime, timedelta, timezone
import uuid

# Define a blueprint
timesheet_bp = Blueprint('timesheet', __name__, url_prefix='/timesheet')

@timesheet_bp.route('/')
@login_required
def timesheethome():
    is_manager = db.session.query(EMPWD).filter_by(LineManagerID=str(current_user.EMPID)).first() is not None
    return render_template('timesheet/timesheethome.html', is_manager=is_manager, user=current_user)

@timesheet_bp.route('/fill', methods=['GET', 'POST'])
@login_required
def filltimesheet():
    if request.method == 'POST':
        try:
            return redirect(url_for('timesheet.submit_timesheet'))
        except Exception as e:
            db.session.rollback()
            session['error_type'] = "Internal Server Error"
            session['error_message'] = "Unable to Submit Timesheet at this  Moment, Please Try After SomeTime."
            session['error_code'] = 500
            return redirect(url_for('error_page')) 

    return render_template('timesheet/timesheet-fill/filltimesheet.html', user=current_user)

@timesheet_bp.route('/submit', methods=['POST'])
@login_required
def submit_timesheet():
    try:
        dates = request.form.getlist('DateofEntry')
        dates = [date.strip() for date in dates[0].split(',')]
        allocation_type = request.form['AllocationType']
        category_1 = request.form['Category1']
        category_2 = request.form.get('Category2')
        category_3 = request.form.get('Category3', "")
        project_code = request.form['ProjectCode']
        comments = request.form.get('comments', "")

        for date in dates:
            hours = float(request.form[f'hours_{date}'])
            minutes = float(request.form[f'minutes_{date}'])
            entry_date = datetime.strptime(date, '%Y-%m-%d').date()

            entry = TimesheetEntry(
                Uniq_ID=str(uuid.uuid4()),
                EmpID=current_user.EMPID,
                Team=current_user.Team,
                DateofEntry=entry_date,
                Hours=hours,
                Minutes=minutes,
                AllocationType=allocation_type,
                Category1=category_1,
                Category2=category_2,
                Category3=category_3,
                ProjectCode=project_code,
                Comment=comments,
                SubmitDate=datetime.now(timezone.utc),
                LastUploadDate=datetime.now(timezone.utc),
                LastUpdatedBy=current_user.username
            )
            db.session.add(entry)

        db.session.commit()
        return redirect(url_for('timesheet.success'))

    except Exception as e:
        db.session.rollback()
        session['error_type'] = "500 Internal Server Error"
        session['error_message'] = "An unexpected error occurred on the server."
        session['error_code'] = 500
        return redirect(url_for('error_page'))

@timesheet_bp.route('/success')
@login_required
def success():
    return render_template('success/success.html', user=current_user)


@timesheet_bp.route('/delete_entry/<entry_id>', methods=['POST'])
@login_required
def delete_entry(entry_id):
    entry = TimesheetEntry.query.filter_by(Uniq_ID=entry_id).first()
    if entry:
        db.session.delete(entry)
        db.session.commit()
    else:
        None
    return redirect(url_for('timesheet.view_entries', date=entry.DateofEntry))



@timesheet_bp.route('/view_entries/<date>')
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