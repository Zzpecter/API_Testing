from main.core.request_controller import RequestController


class ProjectEndpoints:
    def __init__(self):
        self.my_request_controller = RequestController()

    def get_projects(self):
        return self.my_request_controller.\
            send_request('GET',
                         "/projects/")

    def get_project(self, project_id):
        return self.my_request_controller.\
            send_request('GET',
                         f"/projects/{project_id}")

    def post_project(self, payload_dict):
        return self.my_request_controller.\
            send_request('POST',
                         '/projects/',
                         payload=payload_dict)

    def put_project(self, project_id, payload_dict):
        return self.my_request_controller.\
            send_request('PUT',
                         f'/projects/{project_id}',
                         payload=payload_dict)

    def delete_project(self, project_id):
        return self.my_request_controller.\
            send_request('DELETE',
                         f'/projects/{project_id}')
