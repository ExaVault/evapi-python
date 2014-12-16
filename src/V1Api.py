#!/usr/bin/env python
"""
Copyright 2014 ExaVault, Inc.

NOTE: This file was generated automatically. Do not modify by hand.
"""

import sys
import os

from models import *


class V1Api(object):

    def __init__(self, apiClient):
      self.apiClient = apiClient

    
    def authenticateUser(self, username, password, **kwargs):
        """Authenticates a user into the API

        Args:
            username, str: Name of of user to authenticate (required)
            password, str: User's password (required)
            
        Returns: AuthResponse
        """

        allParams = ['username', 'password']

        params = locals()
        for (key, val) in params['kwargs'].iteritems():
            if key not in allParams:
                raise TypeError("Got an unexpected keyword argument '%s' to method authenticateUser" % key)
            params[key] = val
        del params['kwargs']

        resourcePath = '/v1/authenticateUser'
        resourcePath = resourcePath.replace('{format}', 'json')
        method = 'POST'

        queryParams = {}
        headerParams = {}

        if ('username' in params):
            queryParams['username'] = self.apiClient.toPathValue(params['username'])
        if ('password' in params):
            queryParams['password'] = self.apiClient.toPathValue(params['password'])
        postData = (params['body'] if 'body' in params else None)

        response = self.apiClient.callAPI(resourcePath, method, queryParams,
                                          postData, headerParams)

        if not response:
            return None

        responseObject = self.apiClient.deserialize(response, 'AuthResponse')
        return responseObject
        
        
    def checkFilesExist(self, access_token, filePaths, **kwargs):
        """Checks to see if each file or folder in the array exists

        Args:
            access_token, str: Access token required to make the API call (required)
            filePaths, list[str]: Array containing paths of the files or folders to check (required)
            
        Returns: ExistingResourcesResponse
        """

        allParams = ['access_token', 'filePaths']

        params = locals()
        for (key, val) in params['kwargs'].iteritems():
            if key not in allParams:
                raise TypeError("Got an unexpected keyword argument '%s' to method checkFilesExist" % key)
            params[key] = val
        del params['kwargs']

        resourcePath = '/v1/checkFilesExist'
        resourcePath = resourcePath.replace('{format}', 'json')
        method = 'POST'

        queryParams = {}
        headerParams = {}

        if ('access_token' in params):
            queryParams['access_token'] = self.apiClient.toPathValue(params['access_token'])
        if ('filePaths' in params):
            queryParams['filePaths'] = self.apiClient.toPathValue(params['filePaths'])
        postData = (params['body'] if 'body' in params else None)

        response = self.apiClient.callAPI(resourcePath, method, queryParams,
                                          postData, headerParams)

        if not response:
            return None

        responseObject = self.apiClient.deserialize(response, 'ExistingResourcesResponse')
        return responseObject
        
        
    def copyResources(self, access_token, filePaths, destinationPath, **kwargs):
        """Copies files, folders to the destination path

        Args:
            access_token, str: Access token required to make the API call (required)
            filePaths, list[str]: Remote paths of the files or folders to copy (required)
            destinationPath, str: Remote destination path to copy files/folders to (required)
            
        Returns: ModifiedResourcesResponse
        """

        allParams = ['access_token', 'filePaths', 'destinationPath']

        params = locals()
        for (key, val) in params['kwargs'].iteritems():
            if key not in allParams:
                raise TypeError("Got an unexpected keyword argument '%s' to method copyResources" % key)
            params[key] = val
        del params['kwargs']

        resourcePath = '/v1/copyResources'
        resourcePath = resourcePath.replace('{format}', 'json')
        method = 'POST'

        queryParams = {}
        headerParams = {}

        if ('access_token' in params):
            queryParams['access_token'] = self.apiClient.toPathValue(params['access_token'])
        if ('filePaths' in params):
            queryParams['filePaths'] = self.apiClient.toPathValue(params['filePaths'])
        if ('destinationPath' in params):
            queryParams['destinationPath'] = self.apiClient.toPathValue(params['destinationPath'])
        postData = (params['body'] if 'body' in params else None)

        response = self.apiClient.callAPI(resourcePath, method, queryParams,
                                          postData, headerParams)

        if not response:
            return None

        responseObject = self.apiClient.deserialize(response, 'ModifiedResourcesResponse')
        return responseObject
        
        
    def createFolder(self, access_token, folderName, path, **kwargs):
        """Create a folder at a specified path

        Args:
            access_token, str: Access token required to make the API call (required)
            folderName, str: Name of the folder to create (required)
            path, str: Where to create the folder (required)
            
        Returns: Response
        """

        allParams = ['access_token', 'folderName', 'path']

        params = locals()
        for (key, val) in params['kwargs'].iteritems():
            if key not in allParams:
                raise TypeError("Got an unexpected keyword argument '%s' to method createFolder" % key)
            params[key] = val
        del params['kwargs']

        resourcePath = '/v1/createFolder'
        resourcePath = resourcePath.replace('{format}', 'json')
        method = 'POST'

        queryParams = {}
        headerParams = {}

        if ('access_token' in params):
            queryParams['access_token'] = self.apiClient.toPathValue(params['access_token'])
        if ('folderName' in params):
            queryParams['folderName'] = self.apiClient.toPathValue(params['folderName'])
        if ('path' in params):
            queryParams['path'] = self.apiClient.toPathValue(params['path'])
        postData = (params['body'] if 'body' in params else None)

        response = self.apiClient.callAPI(resourcePath, method, queryParams,
                                          postData, headerParams)

        if not response:
            return None

        responseObject = self.apiClient.deserialize(response, 'Response')
        return responseObject
        
        
    def createUser(self, access_token, username, destinationFolder, email, password, role, permissions, timeZone= None, **kwargs):
        """Adds a new subaccount user to the current account

        Args:
            access_token, str: Access token required to make the API call (required)
            username, str: Name of the subaccount user to create (required)
            destinationFolder, str: The user's home folder (required)
            email, str: The user's email address (required)
            password, str: The user's password (required)
            role, str: The user's role, i.e: 'user' or 'admin' (required)
            permissions, list[str]: An array of permissions for the user. The following values are supported: upload, download, delete, modify, list, changePassword, share, notification (required)
            nickname, str: The user's nickname (optional)
            locked, bool: If true, the user's account is locked by default (optional)
            welcomeEmail, bool: If true, send a user email upon creation (optional)
            timeZone, str: The user's timezone, used for accurate time display within SWFT. See &lt;a href='https://php.net/manual/en/timezones.php' target='blank'&gt;this page&lt;/a&gt; for allowed values (required)
            
        Returns: Response
        """

        allParams = ['access_token', 'username', 'destinationFolder', 'email', 'password', 'role', 'permissions', 'nickname', 'locked', 'welcomeEmail', 'timeZone']

        params = locals()
        for (key, val) in params['kwargs'].iteritems():
            if key not in allParams:
                raise TypeError("Got an unexpected keyword argument '%s' to method createUser" % key)
            params[key] = val
        del params['kwargs']

        resourcePath = '/v1/createUser'
        resourcePath = resourcePath.replace('{format}', 'json')
        method = 'POST'

        queryParams = {}
        headerParams = {}

        if ('access_token' in params):
            queryParams['access_token'] = self.apiClient.toPathValue(params['access_token'])
        if ('username' in params):
            queryParams['username'] = self.apiClient.toPathValue(params['username'])
        if ('destinationFolder' in params):
            queryParams['destinationFolder'] = self.apiClient.toPathValue(params['destinationFolder'])
        if ('email' in params):
            queryParams['email'] = self.apiClient.toPathValue(params['email'])
        if ('password' in params):
            queryParams['password'] = self.apiClient.toPathValue(params['password'])
        if ('role' in params):
            queryParams['role'] = self.apiClient.toPathValue(params['role'])
        if ('permissions' in params):
            queryParams['permissions'] = self.apiClient.toPathValue(params['permissions'])
        if ('timeZone' in params):
            queryParams['timeZone'] = self.apiClient.toPathValue(params['timeZone'])
        if ('nickname' in params):
            queryParams['nickname'] = self.apiClient.toPathValue(params['nickname'])
        if ('locked' in params):
            queryParams['locked'] = self.apiClient.toPathValue(params['locked'])
        if ('welcomeEmail' in params):
            queryParams['welcomeEmail'] = self.apiClient.toPathValue(params['welcomeEmail'])
        postData = (params['body'] if 'body' in params else None)

        response = self.apiClient.callAPI(resourcePath, method, queryParams,
                                          postData, headerParams)

        if not response:
            return None

        responseObject = self.apiClient.deserialize(response, 'Response')
        return responseObject
        
        
    def deleteResources(self, access_token, filePaths, **kwargs):
        """Delete the specified files/folders

        Args:
            access_token, str: Access token required to make the API call (required)
            filePaths, list[str]: Array containing paths of the files or folder to delete (required)
            
        Returns: FilesResponse
        """

        allParams = ['access_token', 'filePaths']

        params = locals()
        for (key, val) in params['kwargs'].iteritems():
            if key not in allParams:
                raise TypeError("Got an unexpected keyword argument '%s' to method deleteResources" % key)
            params[key] = val
        del params['kwargs']

        resourcePath = '/v1/deleteResources'
        resourcePath = resourcePath.replace('{format}', 'json')
        method = 'POST'

        queryParams = {}
        headerParams = {}

        if ('access_token' in params):
            queryParams['access_token'] = self.apiClient.toPathValue(params['access_token'])
        if ('filePaths' in params):
            queryParams['filePaths'] = self.apiClient.toPathValue(params['filePaths'])
        postData = (params['body'] if 'body' in params else None)

        response = self.apiClient.callAPI(resourcePath, method, queryParams,
                                          postData, headerParams)

        if not response:
            return None

        responseObject = self.apiClient.deserialize(response, 'FilesResponse')
        return responseObject
        
        
    def deleteUser(self, access_token, username, **kwargs):
        """Deletes a subaccount user for the current account

        Args:
            access_token, str: Access token required to make the API call (required)
            username, str: Name of the subaccount user to delete (required)
            
        Returns: Response
        """

        allParams = ['access_token', 'username']

        params = locals()
        for (key, val) in params['kwargs'].iteritems():
            if key not in allParams:
                raise TypeError("Got an unexpected keyword argument '%s' to method deleteUser" % key)
            params[key] = val
        del params['kwargs']

        resourcePath = '/v1/deleteUser'
        resourcePath = resourcePath.replace('{format}', 'json')
        method = 'POST'

        queryParams = {}
        headerParams = {}

        if ('access_token' in params):
            queryParams['access_token'] = self.apiClient.toPathValue(params['access_token'])
        if ('username' in params):
            queryParams['username'] = self.apiClient.toPathValue(params['username'])
        postData = (params['body'] if 'body' in params else None)

        response = self.apiClient.callAPI(resourcePath, method, queryParams,
                                          postData, headerParams)

        if not response:
            return None

        responseObject = self.apiClient.deserialize(response, 'Response')
        return responseObject
        
        
    def getAccount(self, access_token, **kwargs):
        """Gets the account object for the currently logged in user

        Args:
            access_token, str: Access token required to make the API call (required)
            
        Returns: AccountResponse
        """

        allParams = ['access_token']

        params = locals()
        for (key, val) in params['kwargs'].iteritems():
            if key not in allParams:
                raise TypeError("Got an unexpected keyword argument '%s' to method getAccount" % key)
            params[key] = val
        del params['kwargs']

        resourcePath = '/v1/getAccount'
        resourcePath = resourcePath.replace('{format}', 'json')
        method = 'POST'

        queryParams = {}
        headerParams = {}

        if ('access_token' in params):
            queryParams['access_token'] = self.apiClient.toPathValue(params['access_token'])
        postData = (params['body'] if 'body' in params else None)

        response = self.apiClient.callAPI(resourcePath, method, queryParams,
                                          postData, headerParams)

        if not response:
            return None

        responseObject = self.apiClient.deserialize(response, 'AccountResponse')
        return responseObject
        
        
    def getCurrentUser(self, access_token, **kwargs):
        """Gets the user object for the currently logged in user

        Args:
            access_token, str: Access token required to make the API call (required)
            
        Returns: UserResponse
        """

        allParams = ['access_token']

        params = locals()
        for (key, val) in params['kwargs'].iteritems():
            if key not in allParams:
                raise TypeError("Got an unexpected keyword argument '%s' to method getCurrentUser" % key)
            params[key] = val
        del params['kwargs']

        resourcePath = '/v1/getCurrentUser'
        resourcePath = resourcePath.replace('{format}', 'json')
        method = 'POST'

        queryParams = {}
        headerParams = {}

        if ('access_token' in params):
            queryParams['access_token'] = self.apiClient.toPathValue(params['access_token'])
        postData = (params['body'] if 'body' in params else None)

        response = self.apiClient.callAPI(resourcePath, method, queryParams,
                                          postData, headerParams)

        if not response:
            return None

        responseObject = self.apiClient.deserialize(response, 'UserResponse')
        return responseObject
        
        
    def getDownloadFileUrl(self, access_token, filePaths, **kwargs):
        """Returns a unique URL for handling file downloads

        Args:
            access_token, str: Access token required to make the API call (required)
            filePaths, str: Path of file to be downloaded (required)
            downloadName, str: The name of the file to be downloaded (optional)
            
        Returns: UrlResponse
        """

        allParams = ['access_token', 'filePaths', 'downloadName']

        params = locals()
        for (key, val) in params['kwargs'].iteritems():
            if key not in allParams:
                raise TypeError("Got an unexpected keyword argument '%s' to method getDownloadFileUrl" % key)
            params[key] = val
        del params['kwargs']

        resourcePath = '/v1/getDownloadFileUrl'
        resourcePath = resourcePath.replace('{format}', 'json')
        method = 'POST'

        queryParams = {}
        headerParams = {}

        if ('access_token' in params):
            queryParams['access_token'] = self.apiClient.toPathValue(params['access_token'])
        if ('filePaths' in params):
            queryParams['filePaths'] = self.apiClient.toPathValue(params['filePaths'])
        if ('downloadName' in params):
            queryParams['downloadName'] = self.apiClient.toPathValue(params['downloadName'])
        postData = (params['body'] if 'body' in params else None)

        response = self.apiClient.callAPI(resourcePath, method, queryParams,
                                          postData, headerParams)

        if not response:
            return None

        responseObject = self.apiClient.deserialize(response, 'UrlResponse')
        return responseObject
        
        
    def getFileActivityLogs(self, access_token, **kwargs):
        """Returns a list of account activity. Allows for searching the activity log.

        Args:
            access_token, str: Access token required to make the API call (required)
            filterBy, str: Field to search on ['filter_logs_date' or 'filter_logs_ip_address' or 'filter_logs_username' or 'filter_logs_operation' or 'filter_logs_file'] (optional)
            filter, str: Search criteria. For date ranges, use format 'start_date::end_date' (optional)
            itemLimit, int: Number of logs to return. Can be used for pagination. (optional)
            offset, int: Starting record in the result set. Can be used for pagination. (optional)
            sortBy, str: Sort method ['sort_logs_date' or 'sort_logs_ip_address' or 'sort_logs_username' or 'sort_logs_file' or 'sort_logs_file_source' or 'sort_logs_operation', or 'sort_logs_duration', or 'sort_logs_size', or 'sort_logs_protocol'] (optional)
            sortOrder, str: Sort in either ascending or descending order: asc, desc (optional)
            
        Returns: LogResponse
        """

        allParams = ['access_token', 'filterBy', 'filter', 'itemLimit', 'offset', 'sortBy', 'sortOrder']

        params = locals()
        for (key, val) in params['kwargs'].iteritems():
            if key not in allParams:
                raise TypeError("Got an unexpected keyword argument '%s' to method getFileActivityLogs" % key)
            params[key] = val
        del params['kwargs']

        resourcePath = '/v1/getFileActivityLogs'
        resourcePath = resourcePath.replace('{format}', 'json')
        method = 'POST'

        queryParams = {}
        headerParams = {}

        if ('access_token' in params):
            queryParams['access_token'] = self.apiClient.toPathValue(params['access_token'])
        if ('offset' in params):
            queryParams['offset'] = self.apiClient.toPathValue(params['offset'])
        if ('sortBy' in params):
            queryParams['sortBy'] = self.apiClient.toPathValue(params['sortBy'])
        if ('sortOrder' in params):
            queryParams['sortOrder'] = self.apiClient.toPathValue(params['sortOrder'])
        if ('filterBy' in params):
            queryParams['filterBy'] = self.apiClient.toPathValue(params['filterBy'])
        if ('filter' in params):
            queryParams['filter'] = self.apiClient.toPathValue(params['filter'])
        if ('itemLimit' in params):
            queryParams['itemLimit'] = self.apiClient.toPathValue(params['itemLimit'])
        postData = (params['body'] if 'body' in params else None)

        response = self.apiClient.callAPI(resourcePath, method, queryParams,
                                          postData, headerParams)

        if not response:
            return None

        responseObject = self.apiClient.deserialize(response, 'LogResponse')
        return responseObject
        
        
    def getFolders(self, access_token, path, **kwargs):
        """Get folders for a specified path

        Args:
            access_token, str: Access token required to make the API call (required)
            path, str: The remote file path (required)
            
        Returns: ResourcePropertiesResponse
        """

        allParams = ['access_token', 'path']

        params = locals()
        for (key, val) in params['kwargs'].iteritems():
            if key not in allParams:
                raise TypeError("Got an unexpected keyword argument '%s' to method getFolders" % key)
            params[key] = val
        del params['kwargs']

        resourcePath = '/v1/getFolders'
        resourcePath = resourcePath.replace('{format}', 'json')
        method = 'POST'

        queryParams = {}
        headerParams = {}

        if ('access_token' in params):
            queryParams['access_token'] = self.apiClient.toPathValue(params['access_token'])
        if ('path' in params):
            queryParams['path'] = self.apiClient.toPathValue(params['path'])
        postData = (params['body'] if 'body' in params else None)

        response = self.apiClient.callAPI(resourcePath, method, queryParams,
                                          postData, headerParams)

        if not response:
            return None

        responseObject = self.apiClient.deserialize(response, 'ResourcePropertiesResponse')
        return responseObject
        
        
    def getResourceList(self, access_token, path, sortBy, sortOrder, offset, limit, **kwargs):
        """Get a listing of files/folders for the specified path

        Args:
            access_token, str: Access token required to make the API call (required)
            path, str: The remote file path (required)
            sortBy, str: Sort according to attribute: sort_files_name, sort_files_size, sort_files_date, sort_files_type, sort_files_timeline (required)
            sortOrder, str: Sort in either ascending or descending order: asc, desc (required)
            offset, int: Determines which item to start on for pagination (required)
            limit, int: The number of files to limit the result (required)
            detailed, bool: If true, returns sharedFolder, notifications or other objects associated with specified path (optional)
            pattern, str: Regex string. If not null, perform a search with specified pattern (optional)
            
        Returns: ResourceResponse
        """

        allParams = ['access_token', 'path', 'sortBy', 'sortOrder', 'offset', 'limit', 'detailed', 'pattern']

        params = locals()
        for (key, val) in params['kwargs'].iteritems():
            if key not in allParams:
                raise TypeError("Got an unexpected keyword argument '%s' to method getResourceList" % key)
            params[key] = val
        del params['kwargs']

        resourcePath = '/v1/getResourceList'
        resourcePath = resourcePath.replace('{format}', 'json')
        method = 'POST'

        queryParams = {}
        headerParams = {}

        if ('access_token' in params):
            queryParams['access_token'] = self.apiClient.toPathValue(params['access_token'])
        if ('path' in params):
            queryParams['path'] = self.apiClient.toPathValue(params['path'])
        if ('sortBy' in params):
            queryParams['sortBy'] = self.apiClient.toPathValue(params['sortBy'])
        if ('sortOrder' in params):
            queryParams['sortOrder'] = self.apiClient.toPathValue(params['sortOrder'])
        if ('offset' in params):
            queryParams['offset'] = self.apiClient.toPathValue(params['offset'])
        if ('limit' in params):
            queryParams['limit'] = self.apiClient.toPathValue(params['limit'])
        if ('detailed' in params):
            queryParams['detailed'] = self.apiClient.toPathValue(params['detailed'])
        if ('pattern' in params):
            queryParams['pattern'] = self.apiClient.toPathValue(params['pattern'])
        postData = (params['body'] if 'body' in params else None)

        response = self.apiClient.callAPI(resourcePath, method, queryParams,
                                          postData, headerParams)

        if not response:
            return None

        responseObject = self.apiClient.deserialize(response, 'ResourceResponse')
        return responseObject
        
        
    def getResourceProperties(self, access_token, filePaths, **kwargs):
        """Get the properties for each of the specified files/folders.

        Args:
            access_token, str: Access token required to make the API call (required)
            filePaths, list[str]: Array containing paths of the files or folder to get (required)
            
        Returns: ResourcePropertiesResponse
        """

        allParams = ['access_token', 'filePaths']

        params = locals()
        for (key, val) in params['kwargs'].iteritems():
            if key not in allParams:
                raise TypeError("Got an unexpected keyword argument '%s' to method getResourceProperties" % key)
            params[key] = val
        del params['kwargs']

        resourcePath = '/v1/getResourceProperties'
        resourcePath = resourcePath.replace('{format}', 'json')
        method = 'POST'

        queryParams = {}
        headerParams = {}

        if ('access_token' in params):
            queryParams['access_token'] = self.apiClient.toPathValue(params['access_token'])
        if ('filePaths' in params):
            queryParams['filePaths'] = self.apiClient.toPathValue(params['filePaths'])
        postData = (params['body'] if 'body' in params else None)

        response = self.apiClient.callAPI(resourcePath, method, queryParams,
                                          postData, headerParams)

        if not response:
            return None

        responseObject = self.apiClient.deserialize(response, 'ResourcePropertiesResponse')
        return responseObject
        
        
    def getUploadFileUrl(self, access_token, fileSize, destinationPath, **kwargs):
        """Returns a unique URL for handling file uploads

        Args:
            access_token, str: Access token required to make the API call (required)
            fileSize, int: Size of the file to upload, in bytes (required)
            destinationPath, str: Path relative to account's home directory, including file name (required)
            allowOverwrite, bool: True if the file should be overwritten, false if different file names should be generated (optional)
            resume, bool: True if upload resume is supported, false if it isn't (optional)
            
        Returns: UrlResponse
        """

        allParams = ['access_token', 'fileSize', 'destinationPath', 'allowOverwrite', 'resume']

        params = locals()
        for (key, val) in params['kwargs'].iteritems():
            if key not in allParams:
                raise TypeError("Got an unexpected keyword argument '%s' to method getUploadFileUrl" % key)
            params[key] = val
        del params['kwargs']

        resourcePath = '/v1/getUploadFileUrl'
        resourcePath = resourcePath.replace('{format}', 'json')
        method = 'POST'

        queryParams = {}
        headerParams = {}

        if ('access_token' in params):
            queryParams['access_token'] = self.apiClient.toPathValue(params['access_token'])
        if ('fileSize' in params):
            queryParams['fileSize'] = self.apiClient.toPathValue(params['fileSize'])
        if ('destinationPath' in params):
            queryParams['destinationPath'] = self.apiClient.toPathValue(params['destinationPath'])
        if ('allowOverwrite' in params):
            queryParams['allowOverwrite'] = self.apiClient.toPathValue(params['allowOverwrite'])
        if ('resume' in params):
            queryParams['resume'] = self.apiClient.toPathValue(params['resume'])
        postData = (params['body'] if 'body' in params else None)

        response = self.apiClient.callAPI(resourcePath, method, queryParams,
                                          postData, headerParams)

        if not response:
            return None

        responseObject = self.apiClient.deserialize(response, 'UrlResponse')
        return responseObject
        
        
    def getUser(self, access_token, username, **kwargs):
        """Get the specified subaccount user for the current account

        Args:
            access_token, str: Access token required to make the API call (required)
            username, str: Name of the subaccount user to get (required)
            
        Returns: UserResponse
        """

        allParams = ['access_token', 'username']

        params = locals()
        for (key, val) in params['kwargs'].iteritems():
            if key not in allParams:
                raise TypeError("Got an unexpected keyword argument '%s' to method getUser" % key)
            params[key] = val
        del params['kwargs']

        resourcePath = '/v1/getUser'
        resourcePath = resourcePath.replace('{format}', 'json')
        method = 'POST'

        queryParams = {}
        headerParams = {}

        if ('access_token' in params):
            queryParams['access_token'] = self.apiClient.toPathValue(params['access_token'])
        if ('username' in params):
            queryParams['username'] = self.apiClient.toPathValue(params['username'])
        postData = (params['body'] if 'body' in params else None)

        response = self.apiClient.callAPI(resourcePath, method, queryParams,
                                          postData, headerParams)

        if not response:
            return None

        responseObject = self.apiClient.deserialize(response, 'UserResponse')
        return responseObject
        
        
    def getUsers(self, access_token, sortBy, sortOrder, **kwargs):
        """Gets the user object for the currently logged in user

        Args:
            access_token, str: Access token required to make the API call (required)
            sortBy, str: sort method ['sort_users_username' or 'sort_users_nickname' or 'sort_users_email' or 'sort_users_home_folder'] (required)
            sortOrder, str: sort order, i.e. 'asc' or 'desc' (required)
            
        Returns: UsersResponse
        """

        allParams = ['access_token', 'sortBy', 'sortOrder']

        params = locals()
        for (key, val) in params['kwargs'].iteritems():
            if key not in allParams:
                raise TypeError("Got an unexpected keyword argument '%s' to method getUsers" % key)
            params[key] = val
        del params['kwargs']

        resourcePath = '/v1/getUsers'
        resourcePath = resourcePath.replace('{format}', 'json')
        method = 'POST'

        queryParams = {}
        headerParams = {}

        if ('access_token' in params):
            queryParams['access_token'] = self.apiClient.toPathValue(params['access_token'])
        if ('sortBy' in params):
            queryParams['sortBy'] = self.apiClient.toPathValue(params['sortBy'])
        if ('sortOrder' in params):
            queryParams['sortOrder'] = self.apiClient.toPathValue(params['sortOrder'])
        postData = (params['body'] if 'body' in params else None)

        response = self.apiClient.callAPI(resourcePath, method, queryParams,
                                          postData, headerParams)

        if not response:
            return None

        responseObject = self.apiClient.deserialize(response, 'UsersResponse')
        return responseObject
        
        
    def logoutUser(self, access_token, **kwargs):
        """Removes user's access token from database, logging them out of API

        Args:
            access_token, str: Access token required to make the API call (required)
            
        Returns: Response
        """

        allParams = ['access_token']

        params = locals()
        for (key, val) in params['kwargs'].iteritems():
            if key not in allParams:
                raise TypeError("Got an unexpected keyword argument '%s' to method logoutUser" % key)
            params[key] = val
        del params['kwargs']

        resourcePath = '/v1/logoutUser'
        resourcePath = resourcePath.replace('{format}', 'json')
        method = 'POST'

        queryParams = {}
        headerParams = {}

        if ('access_token' in params):
            queryParams['access_token'] = self.apiClient.toPathValue(params['access_token'])
        postData = (params['body'] if 'body' in params else None)

        response = self.apiClient.callAPI(resourcePath, method, queryParams,
                                          postData, headerParams)

        if not response:
            return None

        responseObject = self.apiClient.deserialize(response, 'Response')
        return responseObject
        
        
    def moveResources(self, access_token, filePaths, destinationPath, **kwargs):
        """Moves files, folders to the destination path

        Args:
            access_token, str: Access token required to make the API call (required)
            filePaths, list[str]: Remote paths of the files or folders to move (required)
            destinationPath, str: Remote destination path to move files/folders to (required)
            
        Returns: ModifiedResourcesResponse
        """

        allParams = ['access_token', 'filePaths', 'destinationPath']

        params = locals()
        for (key, val) in params['kwargs'].iteritems():
            if key not in allParams:
                raise TypeError("Got an unexpected keyword argument '%s' to method moveResources" % key)
            params[key] = val
        del params['kwargs']

        resourcePath = '/v1/moveResources'
        resourcePath = resourcePath.replace('{format}', 'json')
        method = 'POST'

        queryParams = {}
        headerParams = {}

        if ('access_token' in params):
            queryParams['access_token'] = self.apiClient.toPathValue(params['access_token'])
        if ('filePaths' in params):
            queryParams['filePaths'] = self.apiClient.toPathValue(params['filePaths'])
        if ('destinationPath' in params):
            queryParams['destinationPath'] = self.apiClient.toPathValue(params['destinationPath'])
        postData = (params['body'] if 'body' in params else None)

        response = self.apiClient.callAPI(resourcePath, method, queryParams,
                                          postData, headerParams)

        if not response:
            return None

        responseObject = self.apiClient.deserialize(response, 'ModifiedResourcesResponse')
        return responseObject
        
        
    def previewFile(self, access_token, path, size, **kwargs):
        """Returns a resized image of the specified document for support file types

        Args:
            access_token, str: Access token required to make the API call (required)
            path, str: Path of the image relative to the user's home directory (required)
            size, str: The size of the image: small, medium, large (required)
            width, int: Overrides sizes. Sets to a specific width (optional)
            height, int: Overrides sizes. Sets to a specific height (optional)
            page, int: Page number for the document (optional)
            
        Returns: PreviewFileResponse
        """

        allParams = ['access_token', 'path', 'size', 'width', 'height', 'page']

        params = locals()
        for (key, val) in params['kwargs'].iteritems():
            if key not in allParams:
                raise TypeError("Got an unexpected keyword argument '%s' to method previewFile" % key)
            params[key] = val
        del params['kwargs']

        resourcePath = '/v1/previewFile'
        resourcePath = resourcePath.replace('{format}', 'json')
        method = 'POST'

        queryParams = {}
        headerParams = {}

        if ('access_token' in params):
            queryParams['access_token'] = self.apiClient.toPathValue(params['access_token'])
        if ('path' in params):
            queryParams['path'] = self.apiClient.toPathValue(params['path'])
        if ('size' in params):
            queryParams['size'] = self.apiClient.toPathValue(params['size'])
        if ('width' in params):
            queryParams['width'] = self.apiClient.toPathValue(params['width'])
        if ('height' in params):
            queryParams['height'] = self.apiClient.toPathValue(params['height'])
        if ('page' in params):
            queryParams['page'] = self.apiClient.toPathValue(params['page'])
        postData = (params['body'] if 'body' in params else None)

        response = self.apiClient.callAPI(resourcePath, method, queryParams,
                                          postData, headerParams)

        if not response:
            return None

        responseObject = self.apiClient.deserialize(response, 'PreviewFileResponse')
        return responseObject
        
        
    def renameResource(self, access_token, filePath, newName, **kwargs):
        """Rename a file or folder at the specified path

        Args:
            access_token, str: Access token required to make the API call (required)
            filePath, str: Remote path of the files or folder to rename (required)
            newName, str: The new name of the file or folder (required)
            
        Returns: Response
        """

        allParams = ['access_token', 'filePath', 'newName']

        params = locals()
        for (key, val) in params['kwargs'].iteritems():
            if key not in allParams:
                raise TypeError("Got an unexpected keyword argument '%s' to method renameResource" % key)
            params[key] = val
        del params['kwargs']

        resourcePath = '/v1/renameResource'
        resourcePath = resourcePath.replace('{format}', 'json')
        method = 'POST'

        queryParams = {}
        headerParams = {}

        if ('access_token' in params):
            queryParams['access_token'] = self.apiClient.toPathValue(params['access_token'])
        if ('filePath' in params):
            queryParams['filePath'] = self.apiClient.toPathValue(params['filePath'])
        if ('newName' in params):
            queryParams['newName'] = self.apiClient.toPathValue(params['newName'])
        postData = (params['body'] if 'body' in params else None)

        response = self.apiClient.callAPI(resourcePath, method, queryParams,
                                          postData, headerParams)

        if not response:
            return None

        responseObject = self.apiClient.deserialize(response, 'Response')
        return responseObject
        
        
    def updateUser(self, access_token, userId, **kwargs):
        """Updates a subaccount user for the current account

        Args:
            access_token, str: Access token required to make the API call (required)
            userId, int: The user ID, must be obtained from getUser method first (required)
            username, str: Name of the subaccount user to modify (optional)
            nickname, str: The user's nickname (optional)
            email, str: The user's email (optional)
            destinationFolder, str: The user's home folder (optional)
            password, str: The user's password (optional)
            locked, bool: If true, the user's account is locked by default (optional)
            role, str: The user's role, i.e: 'user', 'admin', 'master' (optional)
            permissions, list[str]: An array of permissions for the user (optional)
            
        Returns: Response
        """

        allParams = ['access_token', 'userId', 'username', 'nickname', 'email', 'destinationFolder', 'password', 'locked', 'role', 'permissions']

        params = locals()
        for (key, val) in params['kwargs'].iteritems():
            if key not in allParams:
                raise TypeError("Got an unexpected keyword argument '%s' to method updateUser" % key)
            params[key] = val
        del params['kwargs']

        resourcePath = '/v1/updateUser'
        resourcePath = resourcePath.replace('{format}', 'json')
        method = 'POST'

        queryParams = {}
        headerParams = {}

        if ('access_token' in params):
            queryParams['access_token'] = self.apiClient.toPathValue(params['access_token'])
        if ('userId' in params):
            queryParams['userId'] = self.apiClient.toPathValue(params['userId'])
        if ('username' in params):
            queryParams['username'] = self.apiClient.toPathValue(params['username'])
        if ('nickname' in params):
            queryParams['nickname'] = self.apiClient.toPathValue(params['nickname'])
        if ('email' in params):
            queryParams['email'] = self.apiClient.toPathValue(params['email'])
        if ('destinationFolder' in params):
            queryParams['destinationFolder'] = self.apiClient.toPathValue(params['destinationFolder'])
        if ('password' in params):
            queryParams['password'] = self.apiClient.toPathValue(params['password'])
        if ('locked' in params):
            queryParams['locked'] = self.apiClient.toPathValue(params['locked'])
        if ('role' in params):
            queryParams['role'] = self.apiClient.toPathValue(params['role'])
        if ('permissions' in params):
            queryParams['permissions'] = self.apiClient.toPathValue(params['permissions'])
        postData = (params['body'] if 'body' in params else None)

        response = self.apiClient.callAPI(resourcePath, method, queryParams,
                                          postData, headerParams)

        if not response:
            return None

        responseObject = self.apiClient.deserialize(response, 'Response')
        return responseObject
        
        
    def userAvailable(self, access_token, username, **kwargs):
        """Returns true if requested username has not already been taken in the system

        Args:
            access_token, str: Access token required to make the API call (required)
            username, str: Username to check (required)
            
        Returns: AvailableUserResponse
        """

        allParams = ['access_token', 'username']

        params = locals()
        for (key, val) in params['kwargs'].iteritems():
            if key not in allParams:
                raise TypeError("Got an unexpected keyword argument '%s' to method userAvailable" % key)
            params[key] = val
        del params['kwargs']

        resourcePath = '/v1/userAvailable'
        resourcePath = resourcePath.replace('{format}', 'json')
        method = 'POST'

        queryParams = {}
        headerParams = {}

        if ('access_token' in params):
            queryParams['access_token'] = self.apiClient.toPathValue(params['access_token'])
        if ('username' in params):
            queryParams['username'] = self.apiClient.toPathValue(params['username'])
        postData = (params['body'] if 'body' in params else None)

        response = self.apiClient.callAPI(resourcePath, method, queryParams,
                                          postData, headerParams)

        if not response:
            return None

        responseObject = self.apiClient.deserialize(response, 'AvailableUserResponse')
        return responseObject
        
        
    


