#!/usr/bin/env python

"""
ApiConnection

Class provides methods for authenticating into ExaVault API,
uploading, downloading and deleting files from an ExaVault
account.

@author Dylan Gleason, support -at- exavault -dot- com
"""

import os
import json
import V1Api
import requests
import ApiClient

class ApiConnection:

    def __init__(self, apiKey, apiServer):
        """ Initialize the ExaVault API client """
        self.api = V1Api.V1Api(ApiClient.ApiClient(apiKey, apiServer))

    def login(self, username, password):
        """ Authenticate into the ExaVault API """
        self.username = username
        self.password = password

        # authenticate the user
        response = self.api.authenticateUser(self.username, self.password)
        self.loginSuccess = response.success

        # if login was successful, save access token and return true,
        # otherwise return false

        if self.loginSuccess:
            self.accessToken = response.results.accessToken
            return True
        else:
            return False
            
    def logout(self):
        """ Logout user from the ExaVault API """
        if self.loginSuccess:
            self.api.logoutUser(self.accessToken)
            return True
        else:
            return False

    def uploadFile(self, remoteFile, localFile):
        """ Upload a file to the ExaVault host """
        fileInfo = os.stat(localFile)
        fileSize = fileInfo.st_size

        # obtain the upload file URL from the API
        response = self.api.getUploadFileUrl(self.accessToken, fileSize, remoteFile)

        # if the response was successful, send another API request to
        # actually upload the file

        if response.success:
            url = response.results.url

            with open (localFile, 'rb') as payload:
                headers = {
                    "X_File_Size": str(fileSize),
                    "Content-Type": "multipart/form-data",
                    "Content-Length":  str(fileSize)
                }

                # POST the request
                result = requests.post(url, data=payload, verify=True, headers=headers)

                # decode the response
                result = json.loads(result.text)

                # return the success code
                return result['success']

        else:
            return False   # there was an error


    def downloadFile(self, remoteFile, localFile):
        """ Download a file from the ExaVault host """
        response = self.api.getDownloadFileUrl(self.accessToken, remoteFile)

        if response.success:
            url = response.results.url

            with open(localFile, 'wb') as f:
                result = requests.get(url, stream=True)

                if not result.ok: return False

                # iterate over each block and write to file
                for block in result.iter_content(1024):
                    if not block: break
                    f.write(block)

                return True
        else:
            return False

    def deleteFile(self, remoteFile):
        """ Delete a file from the ExaVault host """
        deleteResults = self.api.deleteResources(self.accessToken, remoteFile)
        return deleteResults.success

