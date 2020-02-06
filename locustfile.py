from locust import HttpLocust, TaskSet, task, between

key = "123"
header = {"accept": "application/json", "api_key":key}

# def create_pet(self):
#     self.client.post()
#
# def delete_pet(self):
#     self.client.delete()


class PetLoadTasks(TaskSet):

    # def on_start(self):
    #     create_pet(self)
    #
    # def on_stop(self):
    #     delete_pet(self)

    # @task
    # def get_pet_by_status(self):
    #     pet_status = 'available'
    #     with self.client.get("/findByStatus", headers=header, json={"status":pet_status}) as response:
    #         if response == 200:
    #             print(response.status_code)
    #             # print(response.status_code)
    #         else:
    #             print(response.json())

    @task
    def get_pet_by_id(self):
        pet_id = "21435431255389"
        resp = self.client.get("/" + pet_id, headers=header)
        # print(resp.status_code)
        # print(resp.request.headers)
        print(resp.text)
        req_response = resp.json()
        print(req_response["category"]["id"])

class WebsiteUser(HttpLocust):
    task_set = PetLoadTasks
    # min_wait = 1000
    # max_wait = 3000
    wait_time = between(1, 3)
    host = 'https://petstore.swagger.io/v2/pet'