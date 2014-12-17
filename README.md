evapi-python
============

evapi-python is an API client written in Python for connecting to the
ExaVault API. The ExaVault API is a REST-like API providing operations
for file and user management, and supports both ``POST`` and ``GET``
requests.

To get started using ExaVault's API, you first must have an ExaVault
account and obtain an API key. For more information, please refer to
our [Developer page](https://www.exavault.com/developer) or contact
support@exavault.com for details.

## Prerequisites ##

evapi-python makes use of the [requests]
(https://github.com/kennethreitz/requests) library. Please ensure that
this library is installed before proceeding to use evapi-python.

**Note:** Some users have reported issues authenticating over SSL with
Python versions <= 2.7.2 (see [this
issue](https://github.com/kennethreitz/requests/issues/1847)). This
problem appears to be due to Python's SSL library automatically
choosing SSLv2/3 during SSL handshake, which will result in failure as
ExaVault has disabled both of these protocols due to the POODLE
exploit. As of this writing, testing the evapi-python client using
Python 2.7.8 does not reproduce this issue.

## Usage ##

Once you have obtained your API key, you can begin making API requests
to upload/download files, and also to manage your users.

##### Setting the API key #####

Before you can make valid API requests, you will need to import the
API client libraries, the [requests]
(https://github.com/kennethreitz/requests) library, as well as `json`
and `os` libraries for decoding JSON responses and working with the
file system (respectively). Here you will also want to set your API
key and instantiate the `V1Api` object.

```python
# Import the evapi-python API client libs
import V1Api
import ApiClient

# Additionally, the following libraries are needed:
import os
import json
import requests

apiKey    = "yourappname-XXXXXXXXXXXXXXXX"
apiServer = "https://api.exavault.com"
api       = V1Api.V1Api(ApiClient.ApiClient(apiKey, apiServer))
```

##### Authenticating #####

Once your API key is in place, you will likely want to authenticate so
that you can begin uploading and downloading files, creating users,
and all that other fun stuff

```python
username = "yourusername"
password = "yourpassword"

# authenticate the user
response = api.authenticateUser(username, password)
loginSuccess = response.success

# if login was successful, save the access token for later
# use, otherwise report an error

if loginSuccess:
    accessToken = response.results.accessToken
else
    # Whoopsie! There was an error. Check your credentials.
```

##### Uploading a file #####

Uploading is a bit more complicated, as it first requires obtaining an
appropriate upload URL from the API and then making a separate HTTP
request to upload the file to your account's storage server at the
correct path.

```python
localFile  = "/path/to/your/local/file"
remoteFile = "/path/on/remote/host"
fileInfo   = os.stat(localFile)
fileSize   = fileInfo.st_size

# obtain the upload file URL from the API
response = api.getUploadFileUrl(accessToken, fileSize, remoteFile)

# if the response was successful, send another request to
# actually upload the file to the storage server

if response.success:
    url = response.results.url

    with open(localFile, 'rb') as payload:
    
        # set the request headers by specifying the file_size, 
        # content_type and content_length
        
        headers = {
            "X_File_Size": str(fileSize),
            "Content-Type": "multipart/form-data",
            "Content-Length":  str(fileSize)
        }

        # POST the request
        result = requests.post(url, data=payload, verify=True, headers=headers)

        # decode the response
        result = json.loads(result.text)
        success = result['success']

        # return the success code
        if not success
            # Whoopsie, there was an error uploading the file
else:
    # Whoopsie, there was an error from the API
```

##### Downloading a file #####

Downloading, like the upload process, first requires obtaining an
appropriate download URL and then making a separate HTTP request to
your account's storage server.

```python
remoteFile = "/path/to/file/on/remote/host"

# send the API request with the accessToken and the file to download
response = api.getDownloadFileUrl(accessToken, remoteFile)

if response.success:
    url = response.results.url

    with open(localFile, 'wb') as f:
    
        # initiate the file transfer
        result = requests.get(url, stream=True)

        # iterate over each block and write to file
        if result.ok:
            for block in result.iter_content(1024):
                if not block: break
                f.write(block)
        else:
            # Whoopsie, there was an error
else:
    # Whoopsie, there was an error. Please verify the remote path is correct.
```    

##### Logging out #####

To logout the current user, simply check the `loginSuccess` flag that
was stored earlier and then call the `logoutUser` method:

```python
if loginSuccess:
    api.logoutUser(accessToken)
```
