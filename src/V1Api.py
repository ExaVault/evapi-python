
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

        # EV NOTE: instead of a "body", we want to process the
        # argument list as a dictionary type and set it to the body
        # field of the POST request in the apiClient

        #postData = (params['body'] if 'body' in params else None)
        postData = {}
        if ('username' in params):
            postData['username'] = params['username']
        if ('password' in params):
            postData['password'] = params['password']
        response = self.apiClient.callAPI(resourcePath, method, queryParams, postData, headerParams)

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

        # EV NOTE: instead of a "body", we want to process the
        # argument list as a dictionary type and set it to the body
        # field of the POST request in the apiClient

        #postData = (params['body'] if 'body' in params else None)
        postData = {}
        if ('access_token' in params):
            postData['access_token'] = params['access_token']
        if ('filePaths' in params):
            postData['filePaths'] = params['filePaths']
        response = self.apiClient.callAPI(resourcePath, method, queryParams, postData, headerParams)

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

        # EV NOTE: instead of a "body", we want to process the
        # argument list as a dictionary type and set it to the body
        # field of the POST request in the apiClient

        #postData = (params['body'] if 'body' in params else None)
        postData = {}
        if ('access_token' in params):
            postData['access_token'] = params['access_token']
        if ('filePaths' in params):
            postData['filePaths'] = params['filePaths']
        if ('destinationPath' in params):
            postData['destinationPath'] = params['destinationPath']
        response = self.apiClient.callAPI(resourcePath, method, queryParams, postData, headerParams)

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

        # EV NOTE: instead of a "body", we want to process the
        # argument list as a dictionary type and set it to the body
        # field of the POST request in the apiClient

        #postData = (params['body'] if 'body' in params else None)
        postData = {}
        if ('access_token' in params):
            postData['access_token'] = params['access_token']
        if ('folderName' in params):
            postData['folderName'] = params['folderName']
        if ('path' in params):
            postData['path'] = params['path']
        response = self.apiClient.callAPI(resourcePath, method, queryParams, postData, headerParams)

        if not response:
            return None

        responseObject = self.apiClient.deserialize(response, 'Response')

        return responseObject
        
        
    def createNotification(self, access_token, path, action, usernames, sendEmail, **kwargs):
        """Creates a new Notification object

        Args:
            access_token, str: Access token required to make the API call (required)
            path, str: Full path of file/folder where notification is set. (required)
            action, str: Type of action to filter on: 'upload', 'download', 'delete', 'all' (required)
            usernames, str: User type to filter on: 'notice_user_all', 'notice_user_all_recipients', 'notice_user_all_users' (required)
            sendEmail, bool: Set to true if the user should be notified by email when the notification is triggered. (required)
            emails, list[str]: Email addresses to send notification to. If not specified, sends to owner by default. (optional)
            
        Returns: Response
        """

        allParams = ['access_token', 'path', 'action', 'usernames', 'sendEmail', 'emails']

        params = locals()
        for (key, val) in params['kwargs'].iteritems():
            if key not in allParams:
                raise TypeError("Got an unexpected keyword argument '%s' to method createNotification" % key)
            params[key] = val
        del params['kwargs']

        resourcePath = '/v1/createNotification'
        resourcePath = resourcePath.replace('{format}', 'json')
        method = 'POST'

        queryParams = {}
        headerParams = {}

        # EV NOTE: instead of a "body", we want to process the
        # argument list as a dictionary type and set it to the body
        # field of the POST request in the apiClient

        #postData = (params['body'] if 'body' in params else None)
        postData = {}
        if ('access_token' in params):
            postData['access_token'] = params['access_token']
        if ('path' in params):
            postData['path'] = params['path']
        if ('action' in params):
            postData['action'] = params['action']
        if ('usernames' in params):
            postData['usernames'] = params['usernames']
        if ('sendEmail' in params):
            postData['sendEmail'] = params['sendEmail']
        if ('emails' in params):
            postData['emails'] = params['emails']
        response = self.apiClient.callAPI(resourcePath, method, queryParams, postData, headerParams)

        if not response:
            return None

        responseObject = self.apiClient.deserialize(response, 'Response')

        return responseObject
        
        
    def createShare(self, access_token, type, name, filePaths, **kwargs):
        """Create a new Share object

        Args:
            access_token, str: Access token required to make the API call (required)
            type, str: The type of share to create: shared_folder, send, receive. (required)
            name, str: Name of the Share. (required)
            filePaths, list[str]: Array of strings containing the file paths to share. (required)
            subject, str: Share message subject (for email invitations). (optional)
            message, str: Share message contents (for email invitations). (optional)
            emails, list[str]: Array of strings for email recipients (for email invitations). (optional)
            ccEmail, str: Specifies a CC email recipient. (optional)
            requireEmail, bool: Requires a user's email to access (defaults to false if not specified). (optional)
            accessMode, str: Type of permissions share recipients have (upload, download, modify). Defaults to download if no option specified. (optional)
            embed, bool: Allows user to embed a widget with the share. Defaults to false if not specified. (optional)
            isPublic, bool: True if share has a public URL, otherwise defaults to false (optional)
            password, str: If not null, value of password is required to access this Share (optional)
            expiration, str: The date the current Share should expire, formatted YYYY-mm-dd (optional)
            hasNotification, bool: True if the user should be notified about activity on this Share. (optional)
            notificationEmails, list[str]: An array of recipients who should receive notification emails. (optional)
            fileDropCreateFolders, bool: If true, all receive folder submissions will be uploaded separate folders (only applicable for Receive folder types) (optional)
            
        Returns: Response
        """

        allParams = ['access_token', 'type', 'name', 'filePaths', 'subject', 'message', 'emails', 'ccEmail', 'requireEmail', 'accessMode', 'embed', 'isPublic', 'password', 'expiration', 'hasNotification', 'notificationEmails', 'fileDropCreateFolders']

        params = locals()
        for (key, val) in params['kwargs'].iteritems():
            if key not in allParams:
                raise TypeError("Got an unexpected keyword argument '%s' to method createShare" % key)
            params[key] = val
        del params['kwargs']

        resourcePath = '/v1/createShare'
        resourcePath = resourcePath.replace('{format}', 'json')
        method = 'POST'

        queryParams = {}
        headerParams = {}

        # EV NOTE: instead of a "body", we want to process the
        # argument list as a dictionary type and set it to the body
        # field of the POST request in the apiClient

        #postData = (params['body'] if 'body' in params else None)
        postData = {}
        if ('access_token' in params):
            postData['access_token'] = params['access_token']
        if ('type' in params):
            postData['type'] = params['type']
        if ('name' in params):
            postData['name'] = params['name']
        if ('filePaths' in params):
            postData['filePaths'] = params['filePaths']
        if ('subject' in params):
            postData['subject'] = params['subject']
        if ('message' in params):
            postData['message'] = params['message']
        if ('emails' in params):
            postData['emails'] = params['emails']
        if ('ccEmail' in params):
            postData['ccEmail'] = params['ccEmail']
        if ('requireEmail' in params):
            postData['requireEmail'] = params['requireEmail']
        if ('accessMode' in params):
            postData['accessMode'] = params['accessMode']
        if ('embed' in params):
            postData['embed'] = params['embed']
        if ('isPublic' in params):
            postData['isPublic'] = params['isPublic']
        if ('password' in params):
            postData['password'] = params['password']
        if ('expiration' in params):
            postData['expiration'] = params['expiration']
        if ('hasNotification' in params):
            postData['hasNotification'] = params['hasNotification']
        if ('notificationEmails' in params):
            postData['notificationEmails'] = params['notificationEmails']
        if ('fileDropCreateFolders' in params):
            postData['fileDropCreateFolders'] = params['fileDropCreateFolders']
        response = self.apiClient.callAPI(resourcePath, method, queryParams, postData, headerParams)

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
            permissions, str: A CSV string of user permissions. The following values are supported: upload, download, delete, modify, list, changePassword, share, notification. (required)
            nickname, str: The user's nickname (optional)
            expiration, str: The date when the user should expire, formatted YYYY-mm-dd (optional)
            locked, bool: If true, the user's account is locked by default (optional)
            welcomeEmail, bool: If true, send a user email upon creation (optional)
            timeZone, str: The user's timezone, used for accurate time display within SWFT. See &lt;a href='https://php.net/manual/en/timezones.php' target='blank'&gt;this page&lt;/a&gt; for allowed values (required)
            
        Returns: Response
        """

        allParams = ['access_token', 'username', 'destinationFolder', 'email', 'password', 'role', 'permissions', 'nickname', 'expiration', 'locked', 'welcomeEmail', 'timeZone']

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

        # EV NOTE: instead of a "body", we want to process the
        # argument list as a dictionary type and set it to the body
        # field of the POST request in the apiClient

        #postData = (params['body'] if 'body' in params else None)
        postData = {}
        if ('access_token' in params):
            postData['access_token'] = params['access_token']
        if ('username' in params):
            postData['username'] = params['username']
        if ('destinationFolder' in params):
            postData['destinationFolder'] = params['destinationFolder']
        if ('email' in params):
            postData['email'] = params['email']
        if ('password' in params):
            postData['password'] = params['password']
        if ('role' in params):
            postData['role'] = params['role']
        if ('permissions' in params):
            postData['permissions'] = params['permissions']
        if ('nickname' in params):
            postData['nickname'] = params['nickname']
        if ('expiration' in params):
            postData['expiration'] = params['expiration']
        if ('locked' in params):
            postData['locked'] = params['locked']
        if ('welcomeEmail' in params):
            postData['welcomeEmail'] = params['welcomeEmail']
        if ('timeZone' in params):
            postData['timeZone'] = params['timeZone']
        response = self.apiClient.callAPI(resourcePath, method, queryParams, postData, headerParams)

        if not response:
            return None

        responseObject = self.apiClient.deserialize(response, 'Response')

        return responseObject
        
        
    def deleteNotification(self, access_token, id, **kwargs):
        """Deletes a Notification by ID

        Args:
            access_token, str: Access token required to make the API call (required)
            id, int: ID of the Notification to delete. (required)
            
        Returns: Response
        """

        allParams = ['access_token', 'id']

        params = locals()
        for (key, val) in params['kwargs'].iteritems():
            if key not in allParams:
                raise TypeError("Got an unexpected keyword argument '%s' to method deleteNotification" % key)
            params[key] = val
        del params['kwargs']

        resourcePath = '/v1/deleteNotification'
        resourcePath = resourcePath.replace('{format}', 'json')
        method = 'POST'

        queryParams = {}
        headerParams = {}

        # EV NOTE: instead of a "body", we want to process the
        # argument list as a dictionary type and set it to the body
        # field of the POST request in the apiClient

        #postData = (params['body'] if 'body' in params else None)
        postData = {}
        if ('access_token' in params):
            postData['access_token'] = params['access_token']
        if ('id' in params):
            postData['id'] = params['id']
        response = self.apiClient.callAPI(resourcePath, method, queryParams, postData, headerParams)

        if not response:
            return None

        responseObject = self.apiClient.deserialize(response, 'Response')

        return responseObject
        
        
    def deleteResources(self, access_token, filePaths, **kwargs):
        """Delete the specified files/folders

        Args:
            access_token, str: Access token required to make the API call (required)
            filePaths, list[str]: Array containing paths of the files or folder to delete (required)
            
        Returns: DeletedResourcesResponse
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

        # EV NOTE: instead of a "body", we want to process the
        # argument list as a dictionary type and set it to the body
        # field of the POST request in the apiClient

        #postData = (params['body'] if 'body' in params else None)
        postData = {}
        if ('access_token' in params):
            postData['access_token'] = params['access_token']
        if ('filePaths' in params):
            postData['filePaths'] = params['filePaths']
        response = self.apiClient.callAPI(resourcePath, method, queryParams, postData, headerParams)

        if not response:
            return None

        responseObject = self.apiClient.deserialize(response, 'DeletedResourcesResponse')

        return responseObject
        
        
    def deleteShare(self, access_token, id, **kwargs):
        """Deletes a Share by ID

        Args:
            access_token, str: Access token required to make the API call (required)
            id, int: ID of the Share to delete. (required)
            
        Returns: Response
        """

        allParams = ['access_token', 'id']

        params = locals()
        for (key, val) in params['kwargs'].iteritems():
            if key not in allParams:
                raise TypeError("Got an unexpected keyword argument '%s' to method deleteShare" % key)
            params[key] = val
        del params['kwargs']

        resourcePath = '/v1/deleteShare'
        resourcePath = resourcePath.replace('{format}', 'json')
        method = 'POST'

        queryParams = {}
        headerParams = {}

        # EV NOTE: instead of a "body", we want to process the
        # argument list as a dictionary type and set it to the body
        # field of the POST request in the apiClient

        #postData = (params['body'] if 'body' in params else None)
        postData = {}
        if ('access_token' in params):
            postData['access_token'] = params['access_token']
        if ('id' in params):
            postData['id'] = params['id']
        response = self.apiClient.callAPI(resourcePath, method, queryParams, postData, headerParams)

        if not response:
            return None

        responseObject = self.apiClient.deserialize(response, 'Response')

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

        # EV NOTE: instead of a "body", we want to process the
        # argument list as a dictionary type and set it to the body
        # field of the POST request in the apiClient

        #postData = (params['body'] if 'body' in params else None)
        postData = {}
        if ('access_token' in params):
            postData['access_token'] = params['access_token']
        if ('username' in params):
            postData['username'] = params['username']
        response = self.apiClient.callAPI(resourcePath, method, queryParams, postData, headerParams)

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

        # EV NOTE: instead of a "body", we want to process the
        # argument list as a dictionary type and set it to the body
        # field of the POST request in the apiClient

        #postData = (params['body'] if 'body' in params else None)
        postData = {}
        if ('access_token' in params):
            postData['access_token'] = params['access_token']
        response = self.apiClient.callAPI(resourcePath, method, queryParams, postData, headerParams)

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

        # EV NOTE: instead of a "body", we want to process the
        # argument list as a dictionary type and set it to the body
        # field of the POST request in the apiClient

        #postData = (params['body'] if 'body' in params else None)
        postData = {}
        if ('access_token' in params):
            postData['access_token'] = params['access_token']
        response = self.apiClient.callAPI(resourcePath, method, queryParams, postData, headerParams)

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

        # EV NOTE: instead of a "body", we want to process the
        # argument list as a dictionary type and set it to the body
        # field of the POST request in the apiClient

        #postData = (params['body'] if 'body' in params else None)
        postData = {}
        if ('access_token' in params):
            postData['access_token'] = params['access_token']
        if ('filePaths' in params):
            postData['filePaths'] = params['filePaths']
        if ('downloadName' in params):
            postData['downloadName'] = params['downloadName']
        response = self.apiClient.callAPI(resourcePath, method, queryParams, postData, headerParams)

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

        # EV NOTE: instead of a "body", we want to process the
        # argument list as a dictionary type and set it to the body
        # field of the POST request in the apiClient

        #postData = (params['body'] if 'body' in params else None)
        postData = {}
        if ('access_token' in params):
            postData['access_token'] = params['access_token']
        if ('filterBy' in params):
            postData['filterBy'] = params['filterBy']
        if ('filter' in params):
            postData['filter'] = params['filter']
        if ('itemLimit' in params):
            postData['itemLimit'] = params['itemLimit']
        if ('offset' in params):
            postData['offset'] = params['offset']
        if ('sortBy' in params):
            postData['sortBy'] = params['sortBy']
        if ('sortOrder' in params):
            postData['sortOrder'] = params['sortOrder']
        response = self.apiClient.callAPI(resourcePath, method, queryParams, postData, headerParams)

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

        # EV NOTE: instead of a "body", we want to process the
        # argument list as a dictionary type and set it to the body
        # field of the POST request in the apiClient

        #postData = (params['body'] if 'body' in params else None)
        postData = {}
        if ('access_token' in params):
            postData['access_token'] = params['access_token']
        if ('path' in params):
            postData['path'] = params['path']
        response = self.apiClient.callAPI(resourcePath, method, queryParams, postData, headerParams)

        if not response:
            return None

        responseObject = self.apiClient.deserialize(response, 'ResourcePropertiesResponse')

        return responseObject
        
        
    def getNotification(self, access_token, id, **kwargs):
        """Returns a notification based on the given ID

        Args:
            access_token, str: Access token required to make the API call (required)
            id, int: ID of the Notification (required)
            
        Returns: NotificationResponse
        """

        allParams = ['access_token', 'id']

        params = locals()
        for (key, val) in params['kwargs'].iteritems():
            if key not in allParams:
                raise TypeError("Got an unexpected keyword argument '%s' to method getNotification" % key)
            params[key] = val
        del params['kwargs']

        resourcePath = '/v1/getNotification'
        resourcePath = resourcePath.replace('{format}', 'json')
        method = 'POST'

        queryParams = {}
        headerParams = {}

        # EV NOTE: instead of a "body", we want to process the
        # argument list as a dictionary type and set it to the body
        # field of the POST request in the apiClient

        #postData = (params['body'] if 'body' in params else None)
        postData = {}
        if ('access_token' in params):
            postData['access_token'] = params['access_token']
        if ('id' in params):
            postData['id'] = params['id']
        response = self.apiClient.callAPI(resourcePath, method, queryParams, postData, headerParams)

        if not response:
            return None

        responseObject = self.apiClient.deserialize(response, 'NotificationResponse')

        return responseObject
        
        
    def getNotifications(self, access_token, type, **kwargs):
        """Returns all notifications for the current user

        Args:
            access_token, str: Access token required to make the API call (required)
            type, str: Type of notification to filter on: 'file', 'folder', 'shared_folder', 'send_receipt', 'share_receipt', 'file_drop' (required)
            sortBy, str: Sort by one of the following: 'sort_notifications_folder_name', 'sort_notifications_path', 'sort_notifications_date' (optional)
            sortOrder, str: Sort by 'asc' or 'desc' order. (optional)
            filter, str: Filter by the provided search terms. (optional)
            
        Returns: NotificationsResponse
        """

        allParams = ['access_token', 'type', 'sortBy', 'sortOrder', 'filter']

        params = locals()
        for (key, val) in params['kwargs'].iteritems():
            if key not in allParams:
                raise TypeError("Got an unexpected keyword argument '%s' to method getNotifications" % key)
            params[key] = val
        del params['kwargs']

        resourcePath = '/v1/getNotifications'
        resourcePath = resourcePath.replace('{format}', 'json')
        method = 'POST'

        queryParams = {}
        headerParams = {}

        # EV NOTE: instead of a "body", we want to process the
        # argument list as a dictionary type and set it to the body
        # field of the POST request in the apiClient

        #postData = (params['body'] if 'body' in params else None)
        postData = {}
        if ('access_token' in params):
            postData['access_token'] = params['access_token']
        if ('type' in params):
            postData['type'] = params['type']
        if ('sortBy' in params):
            postData['sortBy'] = params['sortBy']
        if ('sortOrder' in params):
            postData['sortOrder'] = params['sortOrder']
        if ('filter' in params):
            postData['filter'] = params['filter']
        response = self.apiClient.callAPI(resourcePath, method, queryParams, postData, headerParams)

        if not response:
            return None

        responseObject = self.apiClient.deserialize(response, 'NotificationsResponse')

        return responseObject
        
        
    def getNotificationActivity(self, access_token, **kwargs):
        """Returns all notification activity for the current user

        Args:
            access_token, str: Access token required to make the API call (required)
            
        Returns: NotificationActivityResponse
        """

        allParams = ['access_token']

        params = locals()
        for (key, val) in params['kwargs'].iteritems():
            if key not in allParams:
                raise TypeError("Got an unexpected keyword argument '%s' to method getNotificationActivity" % key)
            params[key] = val
        del params['kwargs']

        resourcePath = '/v1/getNotificationActivity'
        resourcePath = resourcePath.replace('{format}', 'json')
        method = 'POST'

        queryParams = {}
        headerParams = {}

        # EV NOTE: instead of a "body", we want to process the
        # argument list as a dictionary type and set it to the body
        # field of the POST request in the apiClient

        #postData = (params['body'] if 'body' in params else None)
        postData = {}
        if ('access_token' in params):
            postData['access_token'] = params['access_token']
        response = self.apiClient.callAPI(resourcePath, method, queryParams, postData, headerParams)

        if not response:
            return None

        responseObject = self.apiClient.deserialize(response, 'NotificationActivityResponse')

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

        # EV NOTE: instead of a "body", we want to process the
        # argument list as a dictionary type and set it to the body
        # field of the POST request in the apiClient

        #postData = (params['body'] if 'body' in params else None)
        postData = {}
        if ('access_token' in params):
            postData['access_token'] = params['access_token']
        if ('path' in params):
            postData['path'] = params['path']
        if ('sortBy' in params):
            postData['sortBy'] = params['sortBy']
        if ('sortOrder' in params):
            postData['sortOrder'] = params['sortOrder']
        if ('offset' in params):
            postData['offset'] = params['offset']
        if ('limit' in params):
            postData['limit'] = params['limit']
        if ('detailed' in params):
            postData['detailed'] = params['detailed']
        if ('pattern' in params):
            postData['pattern'] = params['pattern']
        response = self.apiClient.callAPI(resourcePath, method, queryParams, postData, headerParams)

        if not response:
            return None

        responseObject = self.apiClient.deserialize(response, 'ResourceResponse')

        return responseObject
        
        
    def getResourceProperties(self, access_token, filePaths, **kwargs):
        """Get the properties for each of the specified files/folders

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

        # EV NOTE: instead of a "body", we want to process the
        # argument list as a dictionary type and set it to the body
        # field of the POST request in the apiClient

        #postData = (params['body'] if 'body' in params else None)
        postData = {}
        if ('access_token' in params):
            postData['access_token'] = params['access_token']
        if ('filePaths' in params):
            postData['filePaths'] = params['filePaths']
        response = self.apiClient.callAPI(resourcePath, method, queryParams, postData, headerParams)

        if not response:
            return None

        responseObject = self.apiClient.deserialize(response, 'ResourcePropertiesResponse')

        return responseObject
        
        
    def getShare(self, access_token, id, **kwargs):
        """Returns a share by the specified ID

        Args:
            access_token, str: Access token required to make the API call (required)
            id, int: ID of the requested Share (required)
            
        Returns: ShareResponse
        """

        allParams = ['access_token', 'id']

        params = locals()
        for (key, val) in params['kwargs'].iteritems():
            if key not in allParams:
                raise TypeError("Got an unexpected keyword argument '%s' to method getShare" % key)
            params[key] = val
        del params['kwargs']

        resourcePath = '/v1/getShare'
        resourcePath = resourcePath.replace('{format}', 'json')
        method = 'POST'

        queryParams = {}
        headerParams = {}

        # EV NOTE: instead of a "body", we want to process the
        # argument list as a dictionary type and set it to the body
        # field of the POST request in the apiClient

        #postData = (params['body'] if 'body' in params else None)
        postData = {}
        if ('access_token' in params):
            postData['access_token'] = params['access_token']
        if ('id' in params):
            postData['id'] = params['id']
        response = self.apiClient.callAPI(resourcePath, method, queryParams, postData, headerParams)

        if not response:
            return None

        responseObject = self.apiClient.deserialize(response, 'ShareResponse')

        return responseObject
        
        
    def getShares(self, access_token, **kwargs):
        """Returns all Shares for the current user

        Args:
            access_token, str: Access token required to make the API call (required)
            type, str: The type of share to return: 'shared_folder', 'send', or 'receive'. If no argument specified, will return all Shares types. (optional)
            sortBy, str: Sort by one of the following: 'sort_shares_name', 'sort_shares_date', 'sort_shares_user', 'sort_shares_access_mode'. (optional)
            sortOrder, str: Sort by 'asc' or 'desc' order. (optional)
            filter, str: Filter by the provided search terms. (optional)
            include, str: Filter by all, active-only, or current user's only. (optional)
            offset, int: Start position of results to return, for pagination. (optional)
            limit, int: Maximum number of elements to return or 0 if no limit. (optional)
            
        Returns: SharesResponse
        """

        allParams = ['access_token', 'type', 'sortBy', 'sortOrder', 'filter', 'include', 'offset', 'limit']

        params = locals()
        for (key, val) in params['kwargs'].iteritems():
            if key not in allParams:
                raise TypeError("Got an unexpected keyword argument '%s' to method getShares" % key)
            params[key] = val
        del params['kwargs']

        resourcePath = '/v1/getShares'
        resourcePath = resourcePath.replace('{format}', 'json')
        method = 'POST'

        queryParams = {}
        headerParams = {}

        # EV NOTE: instead of a "body", we want to process the
        # argument list as a dictionary type and set it to the body
        # field of the POST request in the apiClient

        #postData = (params['body'] if 'body' in params else None)
        postData = {}
        if ('access_token' in params):
            postData['access_token'] = params['access_token']
        if ('type' in params):
            postData['type'] = params['type']
        if ('sortBy' in params):
            postData['sortBy'] = params['sortBy']
        if ('sortOrder' in params):
            postData['sortOrder'] = params['sortOrder']
        if ('filter' in params):
            postData['filter'] = params['filter']
        if ('include' in params):
            postData['include'] = params['include']
        if ('offset' in params):
            postData['offset'] = params['offset']
        if ('limit' in params):
            postData['limit'] = params['limit']
        response = self.apiClient.callAPI(resourcePath, method, queryParams, postData, headerParams)

        if not response:
            return None

        responseObject = self.apiClient.deserialize(response, 'SharesResponse')

        return responseObject
        
        
    def getShareActivity(self, access_token, id, **kwargs):
        """Return activity log entries for the specified Share ID

        Args:
            access_token, str: Access token required to make the API call (required)
            id, int: ID of the Share (required)
            
        Returns: ShareActivityResponse
        """

        allParams = ['access_token', 'id']

        params = locals()
        for (key, val) in params['kwargs'].iteritems():
            if key not in allParams:
                raise TypeError("Got an unexpected keyword argument '%s' to method getShareActivity" % key)
            params[key] = val
        del params['kwargs']

        resourcePath = '/v1/getShareActivity'
        resourcePath = resourcePath.replace('{format}', 'json')
        method = 'POST'

        queryParams = {}
        headerParams = {}

        # EV NOTE: instead of a "body", we want to process the
        # argument list as a dictionary type and set it to the body
        # field of the POST request in the apiClient

        #postData = (params['body'] if 'body' in params else None)
        postData = {}
        if ('access_token' in params):
            postData['access_token'] = params['access_token']
        if ('id' in params):
            postData['id'] = params['id']
        response = self.apiClient.callAPI(resourcePath, method, queryParams, postData, headerParams)

        if not response:
            return None

        responseObject = self.apiClient.deserialize(response, 'ShareActivityResponse')

        return responseObject
        
        
    def getUploadFileUrl(self, access_token, fileSize, destinationPath, **kwargs):
        """Returns a unique URL for handling file uploads

        Args:
            access_token, str: Access token required to make the API call (required)
            fileSize, long: Size of the file to upload, in bytes (required)
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

        # EV NOTE: instead of a "body", we want to process the
        # argument list as a dictionary type and set it to the body
        # field of the POST request in the apiClient

        #postData = (params['body'] if 'body' in params else None)
        postData = {}
        if ('access_token' in params):
            postData['access_token'] = params['access_token']
        if ('fileSize' in params):
            postData['fileSize'] = params['fileSize']
        if ('destinationPath' in params):
            postData['destinationPath'] = params['destinationPath']
        if ('allowOverwrite' in params):
            postData['allowOverwrite'] = params['allowOverwrite']
        if ('resume' in params):
            postData['resume'] = params['resume']
        response = self.apiClient.callAPI(resourcePath, method, queryParams, postData, headerParams)

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

        # EV NOTE: instead of a "body", we want to process the
        # argument list as a dictionary type and set it to the body
        # field of the POST request in the apiClient

        #postData = (params['body'] if 'body' in params else None)
        postData = {}
        if ('access_token' in params):
            postData['access_token'] = params['access_token']
        if ('username' in params):
            postData['username'] = params['username']
        response = self.apiClient.callAPI(resourcePath, method, queryParams, postData, headerParams)

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

        # EV NOTE: instead of a "body", we want to process the
        # argument list as a dictionary type and set it to the body
        # field of the POST request in the apiClient

        #postData = (params['body'] if 'body' in params else None)
        postData = {}
        if ('access_token' in params):
            postData['access_token'] = params['access_token']
        if ('sortBy' in params):
            postData['sortBy'] = params['sortBy']
        if ('sortOrder' in params):
            postData['sortOrder'] = params['sortOrder']
        response = self.apiClient.callAPI(resourcePath, method, queryParams, postData, headerParams)

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

        # EV NOTE: instead of a "body", we want to process the
        # argument list as a dictionary type and set it to the body
        # field of the POST request in the apiClient

        #postData = (params['body'] if 'body' in params else None)
        postData = {}
        if ('access_token' in params):
            postData['access_token'] = params['access_token']
        response = self.apiClient.callAPI(resourcePath, method, queryParams, postData, headerParams)

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

        # EV NOTE: instead of a "body", we want to process the
        # argument list as a dictionary type and set it to the body
        # field of the POST request in the apiClient

        #postData = (params['body'] if 'body' in params else None)
        postData = {}
        if ('access_token' in params):
            postData['access_token'] = params['access_token']
        if ('filePaths' in params):
            postData['filePaths'] = params['filePaths']
        if ('destinationPath' in params):
            postData['destinationPath'] = params['destinationPath']
        response = self.apiClient.callAPI(resourcePath, method, queryParams, postData, headerParams)

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

        # EV NOTE: instead of a "body", we want to process the
        # argument list as a dictionary type and set it to the body
        # field of the POST request in the apiClient

        #postData = (params['body'] if 'body' in params else None)
        postData = {}
        if ('access_token' in params):
            postData['access_token'] = params['access_token']
        if ('path' in params):
            postData['path'] = params['path']
        if ('size' in params):
            postData['size'] = params['size']
        if ('width' in params):
            postData['width'] = params['width']
        if ('height' in params):
            postData['height'] = params['height']
        if ('page' in params):
            postData['page'] = params['page']
        response = self.apiClient.callAPI(resourcePath, method, queryParams, postData, headerParams)

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

        # EV NOTE: instead of a "body", we want to process the
        # argument list as a dictionary type and set it to the body
        # field of the POST request in the apiClient

        #postData = (params['body'] if 'body' in params else None)
        postData = {}
        if ('access_token' in params):
            postData['access_token'] = params['access_token']
        if ('filePath' in params):
            postData['filePath'] = params['filePath']
        if ('newName' in params):
            postData['newName'] = params['newName']
        response = self.apiClient.callAPI(resourcePath, method, queryParams, postData, headerParams)

        if not response:
            return None

        responseObject = self.apiClient.deserialize(response, 'Response')

        return responseObject
        
        
    def updateNotification(self, access_token, id, **kwargs):
        """Updates an existing notification by ID

        Args:
            access_token, str: Access token required to make the API call (required)
            id, int: The notification ID (required)
            path, str: Full path of file/folder where notification is set. (optional)
            action, str: Type of action to filter on: 'upload', 'download', 'delete', 'all' (optional)
            usernames, str: User type to filter on: 'notice_user_all', 'notice_user_all_recipients', 'notice_user_all_users' (optional)
            emails, list[str]: Email addresses to send notification to. If not specified, sends to owner by default. (optional)
            sendEmail, bool: Set to true if the user should be notified by email when the notification is triggered. (optional)
            
        Returns: Response
        """

        allParams = ['access_token', 'id', 'path', 'action', 'usernames', 'emails', 'sendEmail']

        params = locals()
        for (key, val) in params['kwargs'].iteritems():
            if key not in allParams:
                raise TypeError("Got an unexpected keyword argument '%s' to method updateNotification" % key)
            params[key] = val
        del params['kwargs']

        resourcePath = '/v1/updateNotification'
        resourcePath = resourcePath.replace('{format}', 'json')
        method = 'POST'

        queryParams = {}
        headerParams = {}

        # EV NOTE: instead of a "body", we want to process the
        # argument list as a dictionary type and set it to the body
        # field of the POST request in the apiClient

        #postData = (params['body'] if 'body' in params else None)
        postData = {}
        if ('access_token' in params):
            postData['access_token'] = params['access_token']
        if ('id' in params):
            postData['id'] = params['id']
        if ('path' in params):
            postData['path'] = params['path']
        if ('action' in params):
            postData['action'] = params['action']
        if ('usernames' in params):
            postData['usernames'] = params['usernames']
        if ('emails' in params):
            postData['emails'] = params['emails']
        if ('sendEmail' in params):
            postData['sendEmail'] = params['sendEmail']
        response = self.apiClient.callAPI(resourcePath, method, queryParams, postData, headerParams)

        if not response:
            return None

        responseObject = self.apiClient.deserialize(response, 'Response')

        return responseObject
        
        
    def updateShare(self, access_token, id, **kwargs):
        """Update an existing Share by ID

        Args:
            access_token, str: Access token required to make the API call (required)
            id, int: The ID of the Share to update. (required)
            name, str: Name of the Share. (optional)
            filePaths, list[str]: Array of strings containing the file paths to share. (optional)
            subject, str: Share message subject (for email invitations). (optional)
            message, str: Share message contents (for email invitations). (optional)
            emails, list[str]: Array of strings for email recipients (for email invitations). (optional)
            ccEmail, str: Specifies a CC email recipient. (optional)
            requireEmail, bool: Requires a user's email to access (defaults to false if not specified). (optional)
            accessMode, str: Type of permissions share recipients have (upload, download, modify). Defaults to download if no option specified. (optional)
            embed, bool: Allows user to embed a widget with the share. Defaults to false if not specified. (optional)
            isPublic, bool: True if share has a public URL, otherwise defaults to false (optional)
            password, str: If not null, value of password is required to access this Share (optional)
            expiration, str: The date the current Share should expire, formatted YYYY-mm-dd (optional)
            hasNotification, bool: True if the user should be notified about activity on this Share. (optional)
            notificationEmails, list[str]: An array of recipients who should receive notification emails. (optional)
            fileDropCreateFolders, bool: If true, all receive folder submissions will be uploaded separate folders (only applicable for Receive folder types) (optional)
            
        Returns: Response
        """

        allParams = ['access_token', 'id', 'name', 'filePaths', 'subject', 'message', 'emails', 'ccEmail', 'requireEmail', 'accessMode', 'embed', 'isPublic', 'password', 'expiration', 'hasNotification', 'notificationEmails', 'fileDropCreateFolders']

        params = locals()
        for (key, val) in params['kwargs'].iteritems():
            if key not in allParams:
                raise TypeError("Got an unexpected keyword argument '%s' to method updateShare" % key)
            params[key] = val
        del params['kwargs']

        resourcePath = '/v1/updateShare'
        resourcePath = resourcePath.replace('{format}', 'json')
        method = 'POST'

        queryParams = {}
        headerParams = {}

        # EV NOTE: instead of a "body", we want to process the
        # argument list as a dictionary type and set it to the body
        # field of the POST request in the apiClient

        #postData = (params['body'] if 'body' in params else None)
        postData = {}
        if ('access_token' in params):
            postData['access_token'] = params['access_token']
        if ('id' in params):
            postData['id'] = params['id']
        if ('name' in params):
            postData['name'] = params['name']
        if ('filePaths' in params):
            postData['filePaths'] = params['filePaths']
        if ('subject' in params):
            postData['subject'] = params['subject']
        if ('message' in params):
            postData['message'] = params['message']
        if ('emails' in params):
            postData['emails'] = params['emails']
        if ('ccEmail' in params):
            postData['ccEmail'] = params['ccEmail']
        if ('requireEmail' in params):
            postData['requireEmail'] = params['requireEmail']
        if ('accessMode' in params):
            postData['accessMode'] = params['accessMode']
        if ('embed' in params):
            postData['embed'] = params['embed']
        if ('isPublic' in params):
            postData['isPublic'] = params['isPublic']
        if ('password' in params):
            postData['password'] = params['password']
        if ('expiration' in params):
            postData['expiration'] = params['expiration']
        if ('hasNotification' in params):
            postData['hasNotification'] = params['hasNotification']
        if ('notificationEmails' in params):
            postData['notificationEmails'] = params['notificationEmails']
        if ('fileDropCreateFolders' in params):
            postData['fileDropCreateFolders'] = params['fileDropCreateFolders']
        response = self.apiClient.callAPI(resourcePath, method, queryParams, postData, headerParams)

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
            expiration, str: The date when use should expire in format: YYYY-MM-DD (optional)
            email, str: The user's email (optional)
            destinationFolder, str: The user's home folder (optional)
            password, str: The user's password (optional)
            locked, bool: If true, the user's account is locked by default (optional)
            role, str: The user's role, i.e: 'user', 'admin', 'master' (optional)
            permissions, str: A CSV string of user permissions. (optional)
            
        Returns: Response
        """

        allParams = ['access_token', 'userId', 'username', 'nickname', 'expiration', 'email', 'destinationFolder', 'password', 'locked', 'role', 'permissions']

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

        # EV NOTE: instead of a "body", we want to process the
        # argument list as a dictionary type and set it to the body
        # field of the POST request in the apiClient

        #postData = (params['body'] if 'body' in params else None)
        postData = {}
        if ('access_token' in params):
            postData['access_token'] = params['access_token']
        if ('userId' in params):
            postData['userId'] = params['userId']
        if ('username' in params):
            postData['username'] = params['username']
        if ('nickname' in params):
            postData['nickname'] = params['nickname']
        if ('expiration' in params):
            postData['expiration'] = params['expiration']
        if ('email' in params):
            postData['email'] = params['email']
        if ('destinationFolder' in params):
            postData['destinationFolder'] = params['destinationFolder']
        if ('password' in params):
            postData['password'] = params['password']
        if ('locked' in params):
            postData['locked'] = params['locked']
        if ('role' in params):
            postData['role'] = params['role']
        if ('permissions' in params):
            postData['permissions'] = params['permissions']
        response = self.apiClient.callAPI(resourcePath, method, queryParams, postData, headerParams)

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

        # EV NOTE: instead of a "body", we want to process the
        # argument list as a dictionary type and set it to the body
        # field of the POST request in the apiClient

        #postData = (params['body'] if 'body' in params else None)
        postData = {}
        if ('access_token' in params):
            postData['access_token'] = params['access_token']
        if ('username' in params):
            postData['username'] = params['username']
        response = self.apiClient.callAPI(resourcePath, method, queryParams, postData, headerParams)

        if not response:
            return None

        responseObject = self.apiClient.deserialize(response, 'AvailableUserResponse')

        return responseObject
        
        
    


