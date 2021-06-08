from requestController import  RequestController
import json
import time



if __name__ == '__main__':
    my_request_controller = RequestController()
    first_project_id = 2501685

    # .... :::: Get my profile :::: ....
    my_request_controller.send_request('GET', '/me')
    time.sleep(2)

    # .... :::: Get all projects :::: ....
    resp = my_request_controller.send_request('GET', '/projects')
    print(resp.json()[0]['id'])
    time.sleep(2)

    # .... :::: Get specific project :::: ....
    resp = my_request_controller.send_request('GET', f"/projects/{resp.json()[0]['id']}")
    print('\n\n')
    print(resp.json())
    time.sleep(2)

    # .... :::: Post a project :::: ....
    # payload_dict = {}
    # payload_dict.update({'name': 'API_Tests_2'})
    # payload_dict.update({'iteration_length': 2})
    # payload_dict.update({'week_start_day': 'Monday'})
    #
    # response = my_request_controller.send_request('POST', '/projects/', payload=payload_dict)
    # response_dict = response.json()
    # new_project_id = response_dict['id']
    # time.sleep(2)

    # # .... :::: Post story to project :::: ....
    # payload_dict = {}
    # payload_dict.update({'project_id': new_project_id})
    # payload_dict.update({'name': 'First test Story of this project'})
    # payload_dict.update({'description': 'This story is a test, it was created by sending a POST request to the API'})
    # payload_dict.update({'story_type': 'feature'})
    # payload_dict.update({'current_state': 'unscheduled'})
    #
    # response = api.run('POST', f'/projects/{new_project_id}/stories/', payload=payload_dict)
    # response_dict = response.json()
    # new_story_id = response_dict['id']
    # time.sleep(2)
    #
    # # .... :::: Get all stories from project :::: ....
    # api.run('GET', f'/projects/{new_project_id}/stories/')
    # time.sleep(2)
    #
    # # .... :::: Get a specific story from project :::: ....
    # api.run('GET', f'/projects/{new_project_id}/stories/{new_story_id}')
    # time.sleep(2)
    #
    # # .... :::: Update a specific story from project :::: ....
    # payload_dict = {}
    # payload_dict.update({"name": "Updated test story"})
    # payload_dict.update({"labels": [{"name": "automation"}, {"name": "testing"}]})
    # api.run('PUT', f'/projects/{new_project_id}/stories/{new_story_id}', payload=payload_dict)
    # time.sleep(2)
    #
    # # .... :::: Delete a specific story from project :::: ....
    # api.run('DELETE', f'/projects/{new_project_id}/stories/{new_story_id}')
    # time.sleep(2)
    #
    # # .... :::: Update a specific project :::: ....
    # payload_dict = {}
    # payload_dict.update({"name": "Updated test project"})
    # payload_dict.update({"week_start_day": "Tuesday"})
    # api.run('PUT', f'/projects/{new_project_id}', payload=payload_dict)
    # time.sleep(2)
    #
    # # .... :::: Delete a specific project :::: ....
    # api.run('DELETE', f'/projects/{new_project_id}')