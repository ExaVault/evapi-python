from __future__ import print_function
from random import randint
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
authentication_api_instance = swagger_client.AuthenticationApi()
api_key = 'your_api_key_goe_here' 
username = 'existing_username_goes_here' 
password = 'user_password_goes_here' 

# authenticate_user
try:

  api_response = authentication_api_instance.authenticate_user(api_key, authenticate_user={'username': username, 'password': password})
  loginSuccess = api_response.success

  if loginSuccess:
    accessToken = api_response.results.access_token
  else:
    # something went wrong check api_response.error for more details
    raise Exception(api_response.error);

except ApiException as e:
  # server error occured
  print("Exception when calling AuthenticationApi->authenticate_user: %s\n" % e)

# create an instance of the API class
files_folders_api_instance = swagger_client.FilesAndFoldersApi()
folder_name = 'api_test_folder%d' % randint(0, 400)
path = '/'

# create_folder
try:
  
  api_response = files_folders_api_instance.create_folder(api_key, create_folder={'access_token': accessToken, 'folderName':  folder_name, 'path': path })
  createSuccess = api_response.success

  if createSuccess:
    # Folder created successfully
    print('Folder created successfully');
  else:
    # something went wrong check api_response.error for more details
    raise Exception(api_response.error);

except ApiException as e:
  # server error occured
  print("Exception when calling FilesAndFoldersApi->create_folder: %s\n" % e)

# create an instance of the API class
activity_api_instance = swagger_client.ActivityApi()
offset = 0 
sort_by = 'sort_logs_date' 
sort_order = 'desc' 

# get_file_activity_logs
try:

  api_response = activity_api_instance.get_file_activity_logs(api_key, accessToken, offset=offset, sort_by=sort_by, sort_order=sort_order)
  success = api_response.success

  if success:
    # get array with logs from the response
    logs = api_response.results
    print(logs)
  else:
    # something went wrong check api_response.error for more details
    raise Exception(api_response.error);

except ApiException as e:
  # server error occured
  print("Exception when calling ActivityApi->get_file_activity_logs: %s\n" % e)

# To logout the current user, simply check the loginSuccess flag that was stored earlier and then call the `logout_user` method
if loginSuccess:
  authentication_api_instance.logout_user(api_key, logout_user={'access_token': accessToken})