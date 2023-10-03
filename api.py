# this API library contains methods for all main requests

import json
import requests


class TT:

    def __init__(self):
        self.base_url = "http://localhost"

    def user_sign_in(self, email, password):
        request_body = {
            "email": email,
            "password": password
        }
        session = requests.Session()
        response = session.post(self.base_url + "/users/auth/sign-in/", data=json.dumps(request_body))
        status = response.status_code
        return status, session

    def create_project(self, session, test_data):
        request_body = {
            "resource": {
                "name": test_data["proj_name"],
                "description": test_data["proj_desc"]
            },
            "color": test_data["proj_color"]
        }
        response = session.post(self.base_url + f"/entities/projects/{test_data['location'].dep_id}/add/?organization_id={test_data['location'].org_id}", data=json.dumps(request_body))
        response_json = response.json()  # by that we parse json file of response into Python object to use later
        status = response.status_code
        return status, response_json

    def update_project(self, session, test_data):
        request_body = {
            "resource": {
                "name": test_data["new_proj_name"],
                "description": test_data["new_proj_desc"]
            },
            "color": test_data["new_proj_color"]
        }
        response = session.put(
            self.base_url + f"/entities/projects/{test_data['location'].proj_id}/update/?organization_id={test_data['location'].org_id}",
            data=json.dumps(request_body))
        response_json = response.json()  # by that we parse json file of response into Python object to use later
        status = response.status_code
        return status, response_json

    def delete_project(self, session, test_data):
        response = session.delete(
            self.base_url + f"/entities/projects/{test_data['location'].proj_id}/delete/?organization_id={test_data['location'].org_id}")
        response_json = response.json()  # by that we parse json file of response into Python object to use later
        status = response.status_code
        return status, response_json
