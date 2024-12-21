from flask import Flask, Blueprint, render_template, redirect, url_for, flash, request, session, send_from_directory, jsonify, current_app
from flask_login import LoginManager, login_user, logout_user, login_required, current_user
from models import db, EmpWD, TimesheetEntry, Resourceinfo, Trainings, TrainingRegistration
from datetime import datetime, timedelta, timezone
from routes  import timesheet_bp ,error_bp  ,auth ,home_bp ,other_bp
from logging.handlers import TimedRotatingFileHandler
from asgiref.wsgi import WsgiToAsgi
import os, uuid ,traceback, logging, uvicorn



app = Flask(__name__)
asgi_app = WsgiToAsgi(app)

app.config['SQLALCHEMY_DATABASE_URI'] = r'sqlite:///database.db'
app.config['SECRET_KEY'] = 'WinterIsComing'
app.config['PERMANENT_SESSION_LIFETIME'] = timedelta(minutes=99)
app.config['DEBUG'] = True

db.init_app(app)
login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = 'auth.login'

@login_manager.user_loader
def load_user(user_id):
    session = db.session
    return session.get(EmpWD, user_id)

app.register_blueprint(error_bp)
app.register_blueprint(auth)
app.register_blueprint(home_bp)
app.register_blueprint(timesheet_bp)
app.register_blueprint(other_bp)


# ------------------------logging System---------------------------------------------

def setup_logging():
    os.makedirs("logs", exist_ok=True)
    flask_logger = logging.getLogger("flask_logger")
    flask_logger.setLevel(logging.INFO) 
    def get_daily_log_filename():
        today_date = datetime.now().strftime("%Y-%m-%d")
        return f"logs/flask_app_{today_date}.log"
    flask_handler = TimedRotatingFileHandler(get_daily_log_filename(), when="midnight", interval=1)
    flask_handler.setFormatter(logging.Formatter("%(asctime)s - %(levelname)s - %(message)s"))
    flask_logger.addHandler(flask_handler)
    return flask_logger

flask_logger = setup_logging()
@app.before_request
def log_request():
    user_ip = request.remote_addr
    route = request.path
    flask_logger.info(f"User IP: {user_ip}, Requested Route: {route}")

@app.errorhandler(Exception)
def handle_exception(e):
    error_trace = traceback.format_exc()
    flask_logger.error(f"Unhandled Exception: {e}\n{error_trace}")
    return jsonify({"error": "Internal Server Error"}), 500
# -----------------------------------------------------------------------------------------


if __name__ == "__main__":
    try:
        flask_logger.critical("Starting server.")
        print("Starting server.")
        uvicorn.run(asgi_app, host="0.0.0.0",port=5000,log_level="critical", lifespan="off")
    except KeyboardInterrupt:
        flask_logger.critical("Server shutting down.")
        print("Server shutting down.")
    finally:
        flask_logger.critical("Server ended.")
        print("Server ended.")


