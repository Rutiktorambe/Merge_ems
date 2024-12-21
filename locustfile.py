from locust import HttpUser, task, between
import random

class TimesheetTestUser(HttpUser):
    host = "http://127.0.0.1:5000"
    wait_time = between(0, 1) 


    @task(2)
    def home_page(self):
        self.client.get("/timesheet/")

    @task(3)
    def fill_timesheet(self):
        self.client.get("/timesheet/fill")
        self.client.post("/timesheet/submit", data={
            "DateofEntry": "2023-12-01,2023-12-02",
            "AllocationType": "Billable",
            "Category1": "Development",
            "Category2": "Backend",
            "ProjectCode": "PRJ123",
            "comments": "Completed API development.",
            "hours_2023-12-01": "8",
            "minutes_2023-12-01": "30",
            "hours_2023-12-02": "7",
            "minutes_2023-12-02": "45",
        })

    @task(2)
    def view_timesheet_entries(self):
        random_date = "2023-12-01"  
        self.client.get(f"/timesheet/view_entries/{random_date}")

    @task(1)
    def delete_entry(self):
        random_entry_id = "entry-id-placeholder"  
        self.client.post(f"/timesheet/delete_entry/{random_entry_id}")

    @task(2)
    def view_summary(self):
        selected_date = "2023-12-01"  
        self.client.get(f"/timesheet/summary?selected_date={selected_date}")

    @task(1)
    def get_project_data(self):
        category = "Development"
        self.client.get(f"/timesheet/get_projects/{category}")

    @task(1)
    def get_training_data(self):
        training_type = random.choice(["internal", "external"])
        self.client.get(f"/timesheet/get_trainings/{training_type}")

    def on_start(self):
        self.client.post("/auth/login", data={"username": "johnsm", "password": "pass"})
