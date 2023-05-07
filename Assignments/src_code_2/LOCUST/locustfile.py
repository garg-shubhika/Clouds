import time
from locust import HttpUser,task,between
class Quickstartuser(HttpUser):
	@task
	def fun(self):
		self.client.get("")

