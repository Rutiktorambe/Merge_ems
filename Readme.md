# Flask Project Setup

## Prerequisites

- `Python 3.9.21` Onwards
- `pip` (Python package manager)
- `Virtualenv` (optional but recommended)

  - ```bash
    pip install virtualenv
    ```

## Setting Up the Environment

### 1. Create a Virtual Environment

- ```bash
  python -m venv venv
  ```

### 2. Activate the virtual environment:

- **On Windows:**

  ```bash
  venv\Scripts\activate
  ```

- **On macOS/Linux:**
  ```bash
  source venv/bin/activate
  ```

### 3. Install Dependencies

Install the required Python packages listed in `requirements.txt`:

- ```bash
  pip install -r requirements.txt
  ```

## Running the Application

### 1. Run the Application

Run the Flask application:

- ```bash
  python app.py
  ```

By default, the app will be accessible at `http://127.0.0.1:5000`.

### 2. Stopping the Application

Press `Ctrl+C` in the terminal to stop the application.

## Additional Notes

- To deactivate the virtual environment, use:

  ```bash
  deactivate
  ```
