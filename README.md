# **Route Documentation**

## **1. Login**

- **Route:** `/login`
- **Methods:** `GET`, `POST`
- **Description:** Handles user login.
- **Inputs:**
  - `username` (string) - User's username.
  - `password` (string) - User's password.
- **Outputs:**
  - **Success:** Redirects to the `home` page upon successful login.
  - **Failure:** Displays an error message indicating invalid credentials.

### Test Cases for `/login`

| **Sr. No** | **Test Case Description** | **Input**                                      | **Expected Output**                |
| ---------- | ------------------------- | ---------------------------------------------- | ---------------------------------- |
| 1          | Valid login credentials   | username: valid_user, password: valid_password | Redirect to `/home`                |
| 2          | Invalid username          | username: invalid_user, password: any_password | Display "Username not found" error |
| 3          | Incorrect password        | username: valid_user, password: wrong_password | Display "Incorrect password" error |
| 4          | Access login page         | `GET` request                                  | Render `login.html`                |

#### **Test Case:**

```python
def test_login(client):
    response = client.post('/login', data={'username': 'test_user', 'password': 'test_password'})
    assert response.status_code == 302
```

---

## **2. Logout**

- **Route:** `/logout`
- **Methods:** `GET`
- **Description:** Logs out the current user and redirects to login.
- **Outputs:**
  - **Success:** Redirects to the `login` page.

### Test Cases for `/logout`

| **Sr. No** | **Test Case Description**       | **Input**      | **Expected Output**             |
| ---------- | ------------------------------- | -------------- | ------------------------------- |
| 1          | Logout a logged-in user         | User logged in | Redirect to `/login`            |
| 2          | Logout without a logged-in user | Not logged in  | Redirect to `/login` with error |

#### **Test Case:**

```python
def test_logout(client, login_user):
    response = client.get('/logout')
    assert response.status_code == 302
```

---

## **3. Change Password**

- **Route:** `/changepassword`
- **Methods:** `GET`, `POST`
- **Description:** Allows the user to change their password.
- **Inputs:**
  - `username` (string) - User's username.
  - `current_password` (string) - Current password.
  - `new_password` (string) - New password.
  - `confirm_password` (string) - Confirmation of new password.
- **Outputs:**
  - **Success:** Redirects to the login page after password change.
  - **Failure:** Displays an error message indicating issues (invalid username, incorrect current password, etc.).

### Test Cases for `/changepassword`

| **Sr. No** | **Test Case Description**               | **Input**                                                                    | **Expected Output**                         |
| ---------- | --------------------------------------- | ---------------------------------------------------------------------------- | ------------------------------------------- |
| 1          | Change password successfully            | Valid username, correct current password, matching new passwords             | Redirect to `/login`                        |
| 2          | Incorrect username                      | Invalid username                                                             | Display "Username not found"                |
| 3          | Incorrect current password              | Valid username, incorrect current password                                   | Display "Current password is incorrect"     |
| 4          | New passwords do not match              | Valid username, correct current password, mismatched new passwords           | Display "New passwords do not match"        |
| 5          | Old password is match with current pass | Valid username, correct current password, new password with current password | Display "This password is currently in use" |
| 6          | Access password change page             | `GET` request                                                                | Render `changepassword.html`                |

#### **Test Case:**

```python
def test_change_password(client, login_user):
    response = client.post('/changepassword', data={
        'username': 'test_user',
        'current_password': 'test_password',
        'new_password': 'new_password',
        'confirm_password': 'new_password'
    })
    assert response.status_code == 302
```

---

## **4. Index**

- **Route:** `/`
- **Methods:** `GET`
- **Description:** Redirects users to the `/login` route.
- **Outputs:**
  - Redirects to `/login`.

### Test Cases for `/`

| **Sr. No** | **Test Case Description** | **Input**     | **Expected Output**  |
| ---------- | ------------------------- | ------------- | -------------------- |
| 1          | Access root URL           | `GET` request | Redirect to `/login` |

#### **Test Case:**

```python
def test_index_redirect(client):
    response = client.get('/')
    assert response.status_code == 302
```

---

## 5. **Home**

- **Route:** `/home`
- **Methods:** `GET`
- **Description:** Displays the home page for the user.
- **Outputs:**
  - Renders home page.

### Test Cases for `/home`

| **Sr. No** | **Test Case Description**       | **Input**          | **Expected Output**  |
| ---------- | ------------------------------- | ------------------ | -------------------- |
| 1          | Access home page when logged in | User logged in     | Render `home.html`   |
| 2          | Access home page without login  | User not logged in | Redirect to `/login` |

#### **Test Case:**

```python
def test_home(client, login_user):
    response = client.get('/home')
    assert response.status_code == 200
```

---

## **6. TimesheetHome**

- **Route:** `/timesheet`
- **Methods:** `GET`
- **Description:** Displays the timesheet home page for the user.
- **Outputs:**
  - Renders timesheet home page.

### Test Cases for `/timesheet`

| **Sr. No** | **Test Case Description**  | **Input**     | **Expected Output**         |
| ---------- | -------------------------- | ------------- | --------------------------- |
| 1          | Access timesheet home page | `GET` request | Render `timesheethome.html` |

#### **Test Case:**

```python
def test_timesheet_home(client, login_user):
    response = client.get('/timesheet')
    assert response.status_code == 200
```

---

## **7. Fill Timesheet**

- **Route:** `/timesheet/fill`
- **Methods:** `GET`, `POST`
- **Description:** Displays the form for timesheet submission and processes the data.
- **Inputs:**
  - `DateofEntry`, `hours_<date>`, `minutes_<date>`, etc. (POST)
- **Outputs:**
  - Renders form (GET)
  - Redirects to timesheet submission confirmation (POST).

### Test Cases for `/timesheet/fill`

| **Sr. No** | **Test Case Description**     | **Input**                      | **Expected Output**         |
| ---------- | ----------------------------- | ------------------------------ | --------------------------- |
| 1          | Access fill timesheet page    | `GET` request                  | Render `filltimesheet.html` |
| 2          | Submit valid timesheet data   | Valid timesheet form data      | Redirect to `/success`      |
| 3          | Submit invalid timesheet data | Missing or invalid form fields | Display appropriate error   |

#### **Test Case:**

```python
def test_fill_timesheet(client, login_user):
    response = client.get('/timesheet/fill')
    assert response.status_code == 200
```

---

## **8. Get Timesheet History**

- **Route:** `/timesheet/history`
- **Methods:** `GET`, `POST`
- **Description:** Returns total duration for the specified date.
- **Inputs:**
  - `dates` (list) - A list of dates for which the history is needed.
- **Outputs:**
  - A dictionary with dates as keys and total time in hours as values.

### Test Cases for `/timesheet/history`

| **Sr. No** | **Test Case Description**        | **Input**         | **Expected Output**                                  |
| ---------- | -------------------------------- | ----------------- | ---------------------------------------------------- |
| 1          | Get data for date have entries   | `date:has enties` | Return JSON response with duration details date.     |
| 2          | GGet data for date has 0 entries | `date:no enties`  | Return JSON response with 0.0 duration for the date. |

#### **Test Case:**

```python
def test_timesheet_history(client, login_user):
    response = client.post('/timesheet/history', json={'dates': ['2024-12-01', '2024-12-02']})
    assert response.status_code == 200
    assert '2024-12-01' in response.json
```

---

## **9. Get Projects by Category**

- **Route:** `/get_projects/<category>`
- **Methods:** `GET`
- **Description:** Fetches a list of projects filtered by a given category.
- **Inputs:**
  - `category` (URL parameter)
- **Outputs:**
  - A list of project names and codes for the given category.

### Test Cases for `/get_projects/<category>`

| **Sr. No** | **Test Case Description**         | **Input**           | **Expected Output**                      |
| ---------- | --------------------------------- | ------------------- | ---------------------------------------- |
| 1          | Get projects for valid category   | `category: valid`   | Return JSON list of projects in category |
| 2          | Get projects for invalid category | `category: invalid` | Return empty JSON list or error message  |

#### **Test Case:**

```python
def test_get_projects(client, login_user):
    response = client.get('/get_projects/team_name')
    assert response.status_code == 200
    assert len(response.json) > 0
```

---

## **10. Get Projects Details by Project Code**

- **Route:** `/projectCode/<projectCode>`
- **Methods:** `GET`
- **Description:** Fetches a start date and end date of projects by a given project code.
- **Inputs:**
  - `project code` (URL parameter)
- **Outputs:**
  - A list of project names, dates, and project codes.

### Test Cases for `/projectCode/<projectCode>`

| **Sr. No** | **Test Case Description**                     | **Input**              | **Expected Output**                                 |
| ---------- | --------------------------------------------- | ---------------------- | --------------------------------------------------- |
| 1          | Get projects Details for valid Project Code   | `projectCode: valid`   | Return JSON details of projects having project code |
| 2          | Get projects Details for invalid Project Code | `projectCode: invalid` | Return empty JSON list or error message             |

#### **Test Case:**

```python
def test_get_projects_dates(client, login_user):
    response = client.get('/projectCode/PROJECT123')
    assert response.status_code == 200
    assert len(response.json) > 0
```

---

## **11. Get Trainings**

- **Route:** `/get_trainings/<training>`
- **Methods:** `GET`
- **Description:** Returns training-related data for the specified training category.
- **Inputs:**
  - `training` (URL parameter)
- **Outputs:**
  - JSON response with training details.

### Test Cases for `/get_trainings/<training>`

| **Sr. No** | **Test Case Description**     | **Input**           | **Expected Output**               |
| ---------- | ----------------------------- | ------------------- | --------------------------------- |
| 1          | Get data for valid training   | `training: valid`   | Return JSON with training details |
| 2          | Get data for invalid training | `training: invalid` | Return error message in JSON      |

#### **Test Case:**

```python
def test_get_trainings(client, login_user):
    response = client.get('/get_trainings/internal')
    assert response.status_code == 200
    assert len(response.json) > 0
```

---

## **12. Get Datetime for a Given Date**

- **Route:** `/get_datetime/<date>`
- **Methods:** `GET`
- **Description:** Returns formatted datetime information for a given date.
- **Inputs:**
  - `date` (string) - A specific date (YYYY-MM-DD).(URL parameter)
- **Outputs:**
  - Total time worked for that day in hours.

### Test Cases for `/get_datetime/<date>`

| **Sr. No** | **Test Case Description**     | **Input**       | **Expected Output**                 |
| ---------- | ----------------------------- | --------------- | ----------------------------------- |
| 1          | Get datetime for valid date   | `date: valid`   | Return JSON with formatted datetime |
| 2          | Get datetime for invalid date | `date: invalid` | Return error message in JSON        |

#### **Test Case:**

```python
def test_get_datetime(client, login_user):
    response = client.get('/get_datetime/2024-12-01')
    assert response.status_code == 200
    assert 'total_time' in response.json
```

---

## **13. Submit Timesheet**

- **Route:** `/submit_timesheet`
- **Methods:** `POST`
- **Description:** Processes timesheet submission.
- **Inputs:**
  - `DateofEntry` (string) - List of dates when entries are made.
  - `AllocationType` (string) - Type of allocation (billable/non-billable).
  - `hours` (float) - Number of hours worked.
  - `minutes` (float) - Number of minutes worked.
  - Other details like `comments`, `ProjectCode`, etc.
- **Outputs:**
  - Redirects to success page on success.
  - Redirects to error page on failure.

### Test Cases for `/submit_timesheet`

| **Sr. No** | **Test Case Description**      | **Input**                        | **Expected Output**    |
| ---------- | ------------------------------ | -------------------------------- | ---------------------- |
| 1          | Submit valid timesheet data    | Valid timesheet data             | Redirect to `/success` |
| 2          | Submit invalid or missing data | Missing/invalid timesheet fields | Redirect to `/error`   |

#### **Test Case:**

```python
def test_submit_timesheet(client, login_user):
    response = client.post('/submit_timesheet', data={
        'DateofEntry': '2024-12-01',
        'AllocationType': 'billable',
        'hours_2024-12-01': 8,
        'minutes_2024-12-01': 0,
        'ProjectCode': 'PROJECT123'
    })
    assert response.status_code == 302
```

---

## **14. Timesheet Success Page**

- **Route:** `/timesheet/success`
- **Methods:** `GET`
- **Description:** Displays a success message after a successful action.
- **Outputs:**
  - Renders the success page.

### Test Cases for `/timesheet/success`

| **Sr. No** | **Test Case Description** | **Input**     | **Expected Output**   |
| ---------- | ------------------------- | ------------- | --------------------- |
| 1          | Access success page       | `GET` request | Render `success.html` |

#### **Test Case:**

```python
def test_success(client, login_user):
    response = client.get('/timesheet/success')
    assert response.status_code == 200
```

---

## **15. View Timesheet Summary**

- **Route:** `/timesheet/summary`
- **Methods:** `GET`
- **Description:** Displays a summary of all timesheets.
- **Outputs:**
  - Renders the summary page with data.

### Test Cases for `/timesheet/summary`

| **Sr. No** | **Test Case Description**     | **Input**     | **Expected Output**             |
| ---------- | ----------------------------- | ------------- | ------------------------------- |
| 1          | Access timesheet summary page | `GET` request | Render `summary.html` with data |

#### **Test Case:**

```python
def test_timesheet_summary(client, login_user):
    response = client.get('/timesheet/summary')
    assert response.status_code == 200
```

---

## **16. View Timesheet Entries**

- **Route:** `/timesheet/view_entries/<date>`
- **Methods:** `GET`
- **Description:** Displays timesheet entries for a given date.
- **Inputs:**
  - `date` (URL parameter)
- **Outputs:**
  - Renders page with timesheet entries for the date.

### Test Cases for `/timesheet/view_entries/<date>`

| **Sr. No** | **Test Case Description**        | **Input**          | **Expected Output**                |
| ---------- | -------------------------------- | ------------------ | ---------------------------------- |
| 1          | View entries for a valid date    | Date: valid_date   | Render entries for the given date  |
| 2          | View entries for an invalid date | Date: invalid_date | Render empty list or error message |

#### **Test Case:**

```python
def test_view_entries(client, login_user):
    response = client.get('/timesheet/view_entries/2024-12-01')
    assert response.status_code == 200
```

---

## **17. Edit Timesheet Entry**

- **Route:** `/timesheet/edit_entry/<entry_id>`
- **Methods:** `GET`, `POST`
- **Description:** Edits an existing timesheet entry.
- **Inputs:**
  - `entry_id` (URL parameter)
  - Form data (POST)
- **Outputs:**
  - Renders edit form (GET)
  - Updates entry and redirects to the corresponding date's entries page (POST).

### Test Cases for `/timesheet/edit_entry/<entry_id>`

| **Sr. No** | **Test Case Description**     | **Input**                       | **Expected Output**                              |
| ---------- | ----------------------------- | ------------------------------- | ------------------------------------------------ |
| 1          | Edit an existing entry        | Valid entry ID, valid form data | Update entry, redirect to `/view_entries/<date>` |
| 2          | Edit a non-existing entry     | Invalid entry ID                | Display error message                            |
| 3          | Access edit page without POST | Valid entry ID                  | Render `edit_entry.html`                         |

#### **Test Case:**

```python
def test_edit_entry(client, login_user):
    response = client.get('/timesheet/edit_entry/entry_id')
    assert response.status_code == 200
```

---

## **18. Delete Timesheet Entry**

- **Route:** `/timesheet/delete_entry/<entry_id>`
- **Methods:** `POST`
- **Description:** Deletes an existing timesheet entry using its unique ID.
- **Inputs:**
  - `entry_id` (URL parameter)
- **Outputs:**
  - Redirects to timesheet entries page with success or error message.

### Test Cases for `/timesheet/delete_entry/<entry_id>`

| **Sr. No** | **Test Case Description**            | **Input**          | **Expected Output**                             |
| ---------- | ------------------------------------ | ------------------ | ----------------------------------------------- |
| 1          | Delete an existing entry             | Valid `entry_id`   | Redirect to `/view_entries/<date>` with success |
| 2          | Attempt to delete non-existing entry | Invalid `entry_id` | Display error message                           |

#### **Test Case:**

```python
def test_delete_entry(client, login_user):
    response = client.post('/timesheet/delete_entry/entry_id')
    assert response.status_code == 302
```

---

## **19. Manage Repotree**

- **Route:** `/timesheet/manage_repotree`
- **Methods:** `GET`, `POST`
- **Description:** Handles management of repotree structure for timesheets.
- **Inputs:**
  - Various form data fields (POST)
- **Outputs:**
  - Renders the management page (GET)
  - Processes data and provides success or error messages (POST).

### Test Cases for `/timesheet/manage_repotree`

| **Sr. No** | **Test Case Description**    | **Input**                   | **Expected Output**                    |
| ---------- | ---------------------------- | --------------------------- | -------------------------------------- |
| 1          | Access manage repotree page  | `GET` request               | Render `manage_repotree.html`          |
| 2          | Submit valid repotree data   | Valid form data (POST)      | Redirect to `/success` or show success |
| 3          | Submit invalid repotree data | Missing/invalid form fields | Display error message                  |

---

## **21. Error Route**

- **Route:** `/error`
- **Methods:** `GET`
- **Description:** Displays a generic error page with details fetched from the session.
- **Outputs:**
  - Renders an error page with custom error details.

### Test Cases for `/error`

| **Sr. No** | **Test Case Description** | **Input**       | **Expected Output**                        |
| ---------- | ------------------------- | --------------- | ------------------------------------------ |
| 1          | Trigger error page        | Simulated error | Render `error.html` with sepicife message  |
| 2          | Trigger 404 error         | Invalid route   | Render `error.html` with 404 Error message |
| 3          | Trigger 500 error         | Server error    | Render `error.html` with 500 Error message |

#### **Test Case:**

```python
def test_error_page(client):
    response = client.get('/error')
    assert response.status_code == 200
```

---

## **22. Coming Soon Page**

- **Route:** `/comingsoon`
- **Methods:** `GET`
- **Description:** Displays a "Coming Soon" page for incomplete or unavailable features.
- **Outputs:**
  - Renders a placeholder "Coming Soon" page.

### Test Cases for `/comingsoon`

| **Sr. No** | **Test Case Description** | **Input**     | **Expected Output**      |
| ---------- | ------------------------- | ------------- | ------------------------ |
| 1          | Access "Coming Soon" page | `GET` request | Render `comingsoon.html` |

#### **Test Case:**

```python
def test_comingsoon(client, login_user):
    response = client.get('/comingsoon')
    assert response.status_code == 200
```

---

## **23. Favicon Route**

- **Route:** `/favicon.ico`
- **Methods:** `GET`
- **Description:** Provides the favicon for the application.
- **Outputs:**
  - Returns the favicon file.

### Test Cases for `/favicon.ico`

| **Sr. No** | **Test Case Description** | **Input**     | **Expected Output**   |
| ---------- | ------------------------- | ------------- | --------------------- |
| 1          | Request favicon           | `GET` request | Serve the favicon.ico |

---

## **24. Leave System**

- **Route:** `/leavesystem`
- **Methods:** `GET`
- **Description:** Displays the leave management system page.
- **Outputs:**
  - Renders the leave system page.

### Test Cases for `/leavesystem`

| **Sr. No** | **Test Case Description** | **Input**     | **Expected Output**       |
| ---------- | ------------------------- | ------------- | ------------------------- |
| 1          | Access leave system page  | `GET` request | Render `leavesystem.html` |

#### **Test Case:**

```python
def test_leavesystem(client, login_user):
    response = client.get('/leavesystem')
    assert response.status_code == 200
```

---

## **API and Route Documentation**

| **Sr. No.** | **Route**                                              | **Method** | **Description**                                                                        |
| ----------- | ------------------------------------------------------ | ---------- | -------------------------------------------------------------------------------------- |
| 001         | `/login`                                               | GET, POST  | User login endpoint. Renders login page on `GET` and handles authentication on `POST`. |
| 002         | `/logout`                                              | GET        | Logs out the current user and redirects to the login page.                             |
| 003         | `/changepassword`                                      | GET, POST  | Allows users to change their password.                                                 |
| 4           | `/`                                                    | GET        | Redirects to the login page.                                                           |
| 5           | `/favicon.ico`                                         | GET        | Returns the favicon file for the application.                                          |
| 006         | `/home`                                                | GET        | Renders the home page after login.                                                     |
| 7           | `/comingsoon`                                          | GET        | Renders a "Coming Soon" page.                                                          |
| 8           | `/leavesystem`                                         | GET        | Renders the leave system page.                                                         |
| 009         | `/timesheet`                                           | GET        | Renders the timesheet home page.                                                       |
| 010         | `/timesheet/fill`                                      | GET, POST  | Renders the timesheet fill page. Handles timesheet submission on `POST`.               |
| 011         | `/timesheet/history`                                   | POST       | Fetches the timesheet history for specific dates.                                      |
| 012         | `/get_projects/<category>`                             | GET        | Fetches projects based on a category and the user's Employee ID.                       |
| 013         | `/get_datetime/<date>`                                 | GET        | Calculates total hours for a specific date.                                            |
| 014         | `/projectCode/<projectCode>`                           | GET        | Fetches project details based on project code and Employee ID.                         |
| 015         | `/get_trainings/<training>`                            | GET        | Fetches training data (internal or external) for the user.                             |
| 016         | `/submit_timesheet`                                    | POST       | Submits timesheet entries for specific dates and projects.                             |
| 017         | `/timesheet/summary`                                   | GET        | Provides a weekly summary of timesheets.                                               |
| 018         | `/timesheet/view_entries/<date>`                       | GET        | Fetches and displays all timesheet entries for a specific date.                        |
| 019         | `/timesheet/edit_entry/<entry_id>`                     | GET, POST  | Edits an existing timesheet entry.                                                     |
| 20          | `/timesheet/delete_entry/<entry_id>`                   | POST       | Deletes an existing timesheet entry by its unique ID.                                  |
| 021         | `/timesheet/success`                                   | GET        | Renders a success page upon timesheet submission.                                      |
| 022         | `/timesheet/manage_repotree`                           | GET, POST  | Manages reporting tree for managers.                                                   |
| 23          | `/timesheet/manage_repotree/employee_entries/<emp_id>` | GET        | Fetches timesheet entries for a specific employee for a week.                          |
| 024         | `/error`                                               | GET        | Renders a generic error page with details from the session.                            |

```

```
