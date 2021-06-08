from main.core.requestController import RequestController


class StoryEndpoints:
    def __init__(self):
        self.my_request_controller = RequestController('./main/pivotal/api/resources/config.json')

    def get_stories(self, project_id):
        return self.my_request_controller.send_request('GET', f"/projects/{project_id}/stories/")

    def get_story(self, project_id, story_id):
        return self.my_request_controller.send_request('GET', f"/projects/{project_id}/stories/{story_id}")

    def post_story(self, payload_dict):
        return self.my_request_controller.send_request('POST', '/projects/{project_id}/stories', payload=payload_dict)

    def put_story(self, project_id, story_id, payload_dict):
        return self.my_request_controller.send_request('PUT', f'/projects/{project_id}/stories/{story_id}',
                                                       payload=payload_dict)

    def delete_story(self, project_id, story_id):
        return self.my_request_controller.send_request('DELETE', f'/projects/{project_id}/stories/{story_id}')
