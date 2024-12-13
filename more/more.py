To separate the routes and app run logic into different files, you can follow the modular structure. Here's how you can do it:

---

### 1. **Main Application File (`app.py`)**
This file sets up the Flask application and integrates the routes.

```python
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from datetime import timedelta
from models import db
from routes import init_routes

app = Flask(__name__)

# Configuration
app.config['SQLALCHEMY_DATABASE_URI'] = r'sqlite:///database.db'  # Update with your actual DB path
app.config['SECRET_KEY'] = 'WinterIsComing'
app.config['PERMANENT_SESSION_LIFETIME'] = timedelta(minutes=99)

# Initialize extensions
db.init_app(app)

login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = 'login'

@login_manager.user_loader
def load_user(user_id):
    session = db.session
    return session.get(EMPWD, user_id)

# Initialize routes
init_routes(app)

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000, debug=True)
```

---

### 2. **Routes File (`routes.py`)**
This file contains all the route definitions and logic.

```python
from flask import render_template, redirect, url_for, flash, request, session, send_from_directory, jsonify
from flask_login import login_user, login_required, logout_user, current_user
from models import db, EMPWD, TimesheetEntry, Resourceinfo, TrainingRegistration, Training
from datetime import timedelta, date, datetime, timezone
import uuid
import os
import traceback

def init_routes(app):
    @app.before_request
    def session_management():
        session.permanent = True

    # ------------------------------- Authentication Routes -------------------------------
    @app.route('/login', methods=['GET', 'POST'])
    def login():
        message = None
        if request.method == 'POST':
            username = request.form['username']
            password = request.form['password']
            user = EMPWD.query.filter_by(username=username).first()

            if user is None:
                message = 'Username not found'
            elif user.Password != password:
                message = 'Incorrect password'
            else:
                login_user(user)
                return redirect(url_for('home'))

        return render_template('login/login.html', message=message)

    @app.route('/logout')
    @login_required
    def logout():
        logout_user()
        return redirect(url_for('login'))

    @app.route('/changepassword', methods=['GET', 'POST'])
    def change_password():
        message = None
        if request.method == 'POST':
            username = request.form['username']
            current_password = request.form['current_password']
            new_password = request.form['new_password']
            confirm_password = request.form['confirm_password']

            user = EMPWD.query.filter_by(username=username).first()

            if not user:
                message = 'Username not found'
            elif user.Password != current_password:
                message = 'Current password is incorrect'
            elif new_password != confirm_password:
                message = 'New passwords do not match'
            elif user.Password == new_password:
                message = 'This password is currently in use'
            else:
                user.Password = new_password
                db.session.commit()
                return redirect(url_for('login'))

        return render_template('login/changepassword.html', message=message)

    # Add the rest of your routes here in the same way as above

    # ------------------------------- Home Route -------------------------------
    @app.route('/home')
    @login_required
    def home():
        return render_template('home/home.html', user=current_user)

    # ------------------------------- Error Handling -------------------------------
    @app.route('/error')
    def error_page():
        error_type = session.get('error_type', 'Unknown Error')
        error_message = session.get('error_message', 'No additional information provided.')
        error_code = session.get('error_code', 500)
        return render_template('error/error.html', error_type=error_type, error_message=error_message, error_code=error_code, user=current_user)

    @app.errorhandler(404)
    def not_found_error(error):
        session['error_type'] = "404 Not Found"
        session['error_message'] = "The requested resource could not be found."
        session['error_code'] = 404
        return redirect(url_for('error_page'))

    @app.errorhandler(500)
    def internal_error(error):
        session['error_type'] = "500 Internal Server Error"
        session['error_message'] = "An unexpected error occurred on the server."
        session['error_code'] = 500
        return redirect(url_for('error_page'))

    @app.errorhandler(Exception)
    def handle_exception(error):
        session['error_type'] = "Exception"
        session['error_message'] = str(error)
        session['error_code'] = 500
        return redirect(url_for('error_page'))
```

---

### 3. **Models File (`models.py`)**
Your models file remains unchanged. It contains all the SQLAlchemy models.

---

### Benefits of This Structure
- **Modularity**: Routes are defined separately, making the `app.py` file cleaner.
- **Scalability**: New routes or functionality can be added in the `routes.py` file without cluttering the main app file.
- **Reusability**: Common functions can also be separated into utility files if needed.

You can further modularize by creating submodules for specific functionalities like `timesheet_routes.py`, `auth_routes.py`, etc. and import them into `routes.py`.