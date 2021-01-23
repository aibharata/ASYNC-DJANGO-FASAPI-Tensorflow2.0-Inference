import time
from locust import HttpUser, task

class QuickstartUser(HttpUser):
    @task
    def on_start(self):
        self.client.post("/api/predict", files={'files': ('cat.jpg',open('SampleImages/cat.jpg','rb'),'image/jpeg')})