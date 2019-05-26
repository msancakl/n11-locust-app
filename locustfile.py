import pandas
from locust import HttpLocust, TaskSet, task
class UserBehavior(TaskSet):
    
    @task
    def keyword(self):
        keyword = list(pandas.read_csv('n11.csv').Keyword.values)
        for i in keyword:
            self.client.get('/arama?q='+str(i))

class WebsiteUser(HttpLocust):
    task_set = UserBehavior
    min_wait = 2000
    max_wait = 9000