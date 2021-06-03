import requests
import json

API_URL = "https://www.pivotaltracker.com/services/v5"
API_TOKEN = "GENERATE YOUR OWN UNDER www.pivotaltracker.com -> PROFILE"
print('\n\n..:: PIVOTAL TRACKER API TESTBOT ::..')

#------------------ GET PERSONAL INFO FROM THE ACCOUNT --------------------------------------
print('....:::: using method: GET ::::....')
print('....::::  endpoint:   /me  ::::....')
print('....::::  Sending Request  ::::....')
print('\n\n')

endpoint = "/me"
response = requests.get("{}{}".format(API_URL, endpoint), headers={'X-TrackerToken':API_TOKEN})
response_dict = json.loads(response.text)
project_dict = response_dict['projects'][0]
print('Getting response...')
print(response)
print('\nWALL OF TEXT (Complete response):')
print(project_dict)
print('\nGetting user info...')
print('ID: {}'.format(response_dict['id']))
print('Project ID: {}'.format(response_dict['name']))
print('Project Name: {}'.format(response_dict['initials']))
print('Project Color: {}'.format(response_dict['username']))

print('\nGetting user projects...')
print('Project ID: {}'.format(project_dict['project_id']))
print('Project Name: {}'.format(project_dict['project_name']))
print('Project Color: {}'.format(project_dict['project_color']))
print('Is Favorite: {}'.format(project_dict['favorite']))
print('Last Viewed: {}'.format(project_dict['last_viewed_at']))
print('\n\n')


#------------------ CREATE A STORY IN THE DEFAULT PROJECT -----------------------------------
print('....::::            using method: POST          ::::....')
print('....:::: endpoint: /projects/project_id/stories ::::....')
print('....::::             Sending Request            ::::....')
print('\n\n')

project_id = int(project_dict['project_id'])
endpoint = "/projects/{}/stories".format(project_id)
post_dict = {}
post_dict.update({'project_id':project_id})
post_dict.update({'name': 'First test Story'})
post_dict.update({'description':'This story is a test, it was created by sending a POST request to the API'})
post_dict.update({'story_type': 'feature'})
post_dict.update({'current_state': 'unscheduled'})

print('Payload dict: \n{}'.format(post_dict))
response = requests.post("{}{}".format(API_URL, endpoint),data=post_dict, headers={'Content-type': 'application/json', 'X-TrackerToken':API_TOKEN})

print('Getting response...')
print(response)
print('\nLOL error code 500, complete log below:')
response_dict = json.loads(response.text)
print(response_dict)
print("idk let's try somewhere else")
print('\n\n')


#------------------ CREATE A NEW PROJECT --------------------------------------------------------

print('....::::  using method: POST ::::....')
print('....:::: endpoint: /projects ::::....')
print('....::::   Sending Request   ::::....')
print('\n\n')

endpoint = "/projects"
post_dict = {}
post_dict.update({'name': 'First test Project'})
post_dict.update({'iteration_length': 2})
post_dict.update({'week_start_day': 'Monday'})

print('Payload dict: \n{}'.format(post_dict))
response = requests.post("{}{}".format(API_URL, endpoint),data=post_dict, headers={'Content-type': 'application/json', 'X-TrackerToken':API_TOKEN})

print('Getting response...')
print(response)
print('\n')
response_dict = json.loads(response.text)
print(response_dict)