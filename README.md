evapi-python
============

evapi-python is an API client written in Python for connecting to the
ExaVault API. The ExaVault API is a REST-like API providing operations
for file and user management, and supports both ``POST`` and ``GET``
requests.

To get started using ExaVault's API, you first must have an ExaVault
account and obtain an API key. For more information, please refer to
our [Developer page](https://www.exavault.com/developer/) or contact
support@exavault.com for details.

## Prerequisites 

Python 2.7+ and 3.4+

## Installation

1. Clone the repo `git clone https://github.com/ExaVault/evapi-python.git evapi-python` or manually download the library.
2. Run setup script `python setup.py install` Depending on your python setup, you may need to run the script as root; e.g. `sudo python setup.py install`

## Getting started

First you need to obtain an API key for your application from your account.  To do so, please refer to the [API key setup instructions](https://www-dev.exavault.com/developer/api-docs/#section/Code-Libraries-and-Sample-PHP-Code/Obtain-your-API-key) in our documentation.

Once you obtain your API you can use the following snippet. It will allow you to authenticate into API, create folder, get activity logs and log out user from the API.

```python
from __future__ import print_function
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
  else
    # something went wrong check api_response.error for more details

except ApiException as e:
  # server error occured
  print("Exception when calling AuthenticationApi->authenticate_user: %s\n" % e)

# create an instance of the API class
files_folders_api_instance = swagger_client.FilesAndFoldersApi()
folder_name = 'desire_folder_name_goes_here'
path = '/'

# create_folder
try:
  
  api_response = files_folders_api_instance.create_folder(api_key, create_folder={'access_token': accessToken, 'folder_name':  folder_name, 'path': path'})
  createSuccess = api_response.success

  if createSuccess:
    # Folder created successfully
  else
    # something went wrong check api_response.error for more details

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
  else
    # something went wrong check api_response.error for more details

except ApiException as e:
  # server error occured
  print("Exception when calling ActivityApi->get_file_activity_logs: %s\n" % e)

# To logout the current user, simply check the loginSuccess flag that was stored earlier and then call the `logout_user` method
if loginSuccess:
  authentication_api_instance.logout_user(api_key, logout_user={'access_token': accessToken})
```

You can find list of all API requets here - [ExaVault API Docs](https://www.exavault.com/developer/api-docs/)
