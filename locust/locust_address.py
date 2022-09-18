from locust import TaskSet, task, HttpLocust, between
import os
mock_data = """
[{
  first_name: "Jason",
  last_name: "Piere",
  phone: "0426 781 881"
}]
"""

class GetAddress(TaskSet):
    @task(20)
    def get_address_task(self):
        with self.client.get("/api/v1/address/", catch_response=True) as response:
            if response.status_code == 200:
                response.success()
    @task(1)
    def post_address_task(self):
        with self.client.post("/api/v1/address/",
        {'first_name' : 'Jason', 'last_name': 'Piere', 'phone': '0426 781 881'},
        catch_response=True) as response:
            if response.status_code == 201:
                response.success()

class Get(HttpLocust):
    task_set = GetAddress
    wait_time = between(5, 9)
    host = os.environ.get("ADDRESSBOOK_API") or "http://australia-addressbook-api:8007"
    stop_timeout = 2000
