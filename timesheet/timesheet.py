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
    


@timesheet_bp.route('/history', methods=['POST'])
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





@timesheet_bp.route('/summary')
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