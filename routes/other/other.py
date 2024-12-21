from flask import Flask, Blueprint, render_template, redirect, url_for, flash, request, session, send_from_directory, jsonify, current_app
from flask_login import LoginManager, login_user, logout_user, login_required, current_user
from models import db, EmpWD, TimesheetEntry, Resourceinfo, Trainings, TrainingRegistration
from datetime import datetime, timedelta, timezone
import os
import uuid
import traceback

other_bp = Blueprint('other', __name__)


@other_bp.route('/comingsoon')
@login_required
def comingsoon():
    return render_template('comingsoon/comingsoon.html', user=current_user)

@other_bp.route('/leavesystem')
@login_required
def leavesystem():
    return render_template('leavesystem/leavesystem.html', user=current_user)
