To organize your Flask app into separate files (modules), you can use **blueprints**. This structure improves code readability and maintainability by grouping related routes into distinct files. Below is an example of how you can refactor your application into separate files for `home`, `timesheet`, `login`, and `error` routes.

### Directory Structure
```plaintext
project/
├── app/
│   ├── __init__.py
│   ├── home.py
│   ├── login.py
│   ├── timesheet.py
│   ├── error.py
│   ├── models.py
│   ├── static/
│   └── templates/
│       ├── home/
│       ├── login/
│       ├── timesheet/
│       └── error/
├── config.py
├── run.py
└── database.db
```

### Refactoring Steps

#### 1. `__init__.py`
This initializes the Flask app and registers the blueprints.

```python
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from datetime import timedelta

db = SQLAlchemy()
login_manager = LoginManager()

def create_app():
    app = Flask(__name__)
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
    app.config['SECRET_KEY'] = 'WinterIsComing'
    app.config['PERMANENT_SESSION_LIFETIME'] = timedelta(minutes=99)

    db.init_app(app)
    login_manager.init_app(app)
    login_manager.login_view = 'login.login'

    # Register Blueprints
    from app.home import home_bp
    from app.login import login_bp
    from app.timesheet import timesheet_bp
    from app.error import error_bp

    app.register_blueprint(home_bp)
    app.register_blueprint(login_bp)
    app.register_blueprint(timesheet_bp)
    app.register_blueprint(error_bp)

    return app
```

---

#### 2. `home.py`
Defines the routes for the home section.

```python
from flask import Blueprint, render_template
from flask_login import login_required, current_user

home_bp = Blueprint('home', __name__, template_folder='templates/home')

@home_bp.route('/home')
@login_required
def home():
    return render_template('home.html', user=current_user)

@home_bp.route('/comingsoon')
@login_required
def comingsoon():
    return render_template('comingsoon.html', user=current_user)

@home_bp.route('/leavesystem')
@login_required
def leavesystem():
    return render_template('leavesystem.html', user=current_user)
```

---

#### 3. `login.py`
Handles user authentication.

```python
from flask import Blueprint, render_template, redirect, url_for, request
from flask_login import login_user, logout_user, login_required, current_user
from app.models import EMPWD, db

login_bp = Blueprint('login', __name__, template_folder='templates/login')

@login_bp.route('/login', methods=['GET', 'POST'])
def login():
    message = None
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        user = EMPWD.query.filter_by(username=username).first()

        if not user:
            message = 'Username not found'
        elif user.Password != password:
            message = 'Incorrect password'
        else:
            login_user(user)
            return redirect(url_for('home.home'))

    return render_template('login.html', message=message)

@login_bp.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('login.login'))
```

---

#### 4. `timesheet.py`
Defines the timesheet-related routes.

```python
from flask import Blueprint, render_template, redirect, url_for, request, jsonify, session
from flask_login import login_required, current_user
from app.models import TimesheetEntry, db
from datetime import datetime, timedelta, timezone
import uuid

timesheet_bp = Blueprint('timesheet', __name__, template_folder='templates/timesheet')

@timesheet_bp.route('/timesheet')
@login_required
def timesheethome():
    is_manager = db.session.query(TimesheetEntry).filter_by(LineManagerID=current_user.EMPID).first() is not None
    return render_template('timesheet_home.html', is_manager=is_manager, user=current_user)

@timesheet_bp.route('/timesheet/fill', methods=['GET', 'POST'])
@login_required
def filltimesheet():
    if request.method == 'POST':
        # Handle form submission logic here
        return redirect(url_for('timesheet.submit_timesheet'))
    return render_template('filltimesheet.html', user=current_user)

# Add other timesheet routes...
```

---

#### 5. `error.py`
Handles error routes.

```python
from flask import Blueprint, render_template, session

error_bp = Blueprint('error', __name__, template_folder='templates/error')

@error_bp.route('/error')
def error_page():
    error_type = session.get('error_type', 'Unknown Error')
    error_message = session.get('error_message', 'No additional information provided.')
    error_code = session.get('error_code', 500)
    return render_template('error.html', error_type=error_type, error_message=error_message, error_code=error_code)
```

---

#### 6. `run.py`
The entry point for running the app.

```python
from app import create_app

app = create_app()

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
```

---

### Benefits
- Each file focuses on a specific part of the application.
- Code is easier to navigate and maintain.
- Using **blueprints**, you can extend the application effortlessly. 

Let me know if you need help with templates or additional routes!