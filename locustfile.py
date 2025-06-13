from locust import HttpUser, task, between
import json
import random

class ProductUser(HttpUser):
    wait_time = between(1, 2)  # Adjust the wait time between tasks

    def on_start(self):
        self.default_name = "Product0"
        payload = {
            "name": self.default_name,
            "price": 50.0,
            "description": "Initial product"
        }
        self.client.post("/products/", data=json.dumps(payload), headers={"Content-Type": "application/json"})

    @task(2)
    def create_product(self):
        product_id = random.randint(1, 10000)
        payload = {
            "name": f"Product{product_id}",
            "price": round(random.uniform(10.0, 100.0), 2),
            "description": "Load test product"
        }
        self.client.post("/products/", data=json.dumps(payload), headers={"Content-Type": "application/json"})

    @task(1)
    def get_product(self):
        self.client.get(f"/products/{self.default_name}")

    @task(1)
    def put_product(self):
        payload = {
            "name": self.default_name,
            "price": 123.45,
            "description": "Updated by PUT"
        }
        self.client.put(f"/products/{self.default_name}", data=json.dumps(payload), headers={"Content-Type": "application/json"})

    @task(1)
    def patch_product(self):
        payload = {
            "price": 88.88
        }
        self.client.patch(f"/products/{self.default_name}", data=json.dumps(payload), headers={"Content-Type": "application/json"})

    @task(1)
    def delete_and_restore_product(self):
        self.client.delete(f"/products/{self.default_name}")
        payload = {
            "name": self.default_name,
            "price": 50.0,
            "description": "Restored after delete"
        }
        self.client.post("/products/", data=json.dumps(payload), headers={"Content-Type": "application/json"})
