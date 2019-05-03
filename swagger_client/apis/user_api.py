# coding: utf-8

"""
    ExaVault API

    # Introduction  Welcome to the ExaVault API documentation. Our API lets you control nearly all aspects of your ExaVault account programatically, from uploading and downloading files to creating and managing shares and notifications. Our API supports both GET and POST operations.  Capabilities of the API include:  - Uploading and downloading files. - Managing files and folders; including standard operations like move, copy and delete. - Getting information about activity occuring in your account. - Creating, updating and deleting users. - Creating and managing shares, including download-only shares and recieve folders.  - Setting up and managing notifications.  ## The API Endpoint  The ExaVault API is located at: https://api.exavault.com/v1.2/  # Testing w/ Postman  We've made it easy for you to test our API before you start full-scale development. Download [Postman](https://www.getpostman.com/) or the [Postman Chrome Extension](https://chrome.google.com/webstore/detail/postman/fhbjgbiflinjbdggehcddcbncdddomop?hl=en), and then download our Postman collection, below. [Obtain your API key](#section/Code-Libraries-and-Sample-PHP-Code/Obtain-your-API-key) and you'll be able to interact with your ExaVault account immediately, so you can better understand what the capabilities of the API are.  <div class=\"postman-run-button\" data-postman-action=\"collection/import\" data-postman-var-1=\"e13395afc6278ce1555f\"></div>  ![ExaVault API Postman Colletion Usage](/images/postman.png)  If you'd prefer to skip Postman and start working with code directly, take a look at the sample code below.    # Code Libraries & Sample PHP Code  Once you're ready for full-scale development, we recommend looking at our code libraries available on [GitHub](https://github.com/ExaVault). We offer code libraries for [Python](https://github.com/ExaVault/evapi-python), [PHP](https://github.com/ExaVault/evapi-php) and [JavaScript](https://github.com/ExaVault/evapi-javascript).  While we recommend using our libraries, you're welcome to interact directly with our API via HTTP GET and POST requests -- a great option particularly if you're developing in a language for which we don't yet have sample code.     - [Download Python Library &amp; Sample Code &raquo;](https://github.com/ExaVault/evapi-python) - [Download PHP Library &amp; Sample Code &raquo;](https://github.com/ExaVault/evapi-php) - [Download JavaScript Library &amp; Sample Code &raquo;](https://github.com/ExaVault/evapi-javascript)  *Note: You can generate client libraries for any language using [Swagger Editor](http://editor2.swagger.io/). Just download our documentation file, past it into editor and use 'Generate Client' dropdown.*  ## Obtain Your API Key  You will need to obtain an API key for your application from the [Client Area](https://clients.exavault.com/clientarea.php?action=products) of your account.  To obtain an API key, please follow the instructions below.   + Login to the [Accounts](https://clients.exavault.com/clientarea.php?action=products) section of the Client Area.  + Use the drop down next to your desired account, and select *Manage API Keys*.  + You will be brought to the API Key management screen. Fill out the form and save to generate a new key for your app.  *NOTE: As of Oct 2017, we are in the progress of migrating customers to our next generation platform. If your account is already on our new platform, you should log into your File Manager and create your API key under Account->Developer->Manage API Keys*.  # Status Codes  The ExaVault API returns only two HTTP status codes for its responses: 200 and 500.  When the request could be successfully processed by the endpoint, the response status code will be 200, regardless of whether the requested action could be taken.  For example, the response to a getUser request for a username that does not exist in your account would have the status of 200,  indicating that the response was received and processed, but the error member of the returned response object would contain object with `message` and `code` properties.  **Result Format:**  |Success   | Error     | Results   | | ---      | :---:       |  :---:      | | 0        |  `Object` |   Empty   | | 1        |   Empty       |    `Object` or `Array`        |     When a malformed request is received, a 500 HTTP status code will be returned, indicating that the request could not be processed.  ExaVault's API does not currently support traditional REST response codes such as '201 Created' or '405 Method Not Allowed', although we intend to support such codes a future version of the API.   # File Paths  Many API calls require you to provide one or more file paths. For example, the <a href=\"#operation/moveResources\">moveResources</a> call requires both an array of source paths, **filePaths**, and a destination path, **destinationPath**. Here's a few tips for working with paths:   - File paths should always be specified as a string, using the standard Unix format: e.g. `/path/to/a/file.txt`  - File paths are always absolute _from the home directory of the logged in user_. For example, if the user **bob** had a home directory restriction of `/bob_home`, then an API call made using his login would specify a file as `/myfile.txt`, whereas an API call made using the master user ( no home directory restriction ) would specify the same file as `/bob_home/myfile.txt`.  # API Rate Limits  We rate limit the number of API calls you can make to help prevent abuse and protect system stablity. Each API key will support 500 requests per rolling five minutes. If you make more than 500 requests in a five minute period, you will receive a response with an error object for fifteen minutes.  # Webhooks  A webhook is an HTTP callback: a simple event-notification via HTTP POST. If you define webhooks for Exavault, ExaVault will POST a  message to a URL when certain things happen.     Webhooks can be used to receive a JSON object to your endpoint URL. You choose what events will trigger webhook messages to your endpoint URL.     Webhooks will attempt to send a message up to 8 times with increasing timeouts between each attempt. All webhook requests are tracked in the webhooks log.  ## Getting Started  1. Go to the Account tab inside SWFT.  2. Choose the Developer tab.  3. Configure your endpoint URL and select the events you want to trigger webhook messages.  4. Save settings.    You are all set to receive webhook callbacks on the events you selected.  ## Verification Signature  ExaVault includes a custom HTTP header, X-Exavault-Signature, with webhooks POST requests which will contain the signature for the request.  You can use the signature to verify the request for an additional level of security.  ## Generating the Signature  1. Go to Account tab inside SWFT.  2. Choose the Developer tab.  3. Obtain the verification token. This field will only be shown if you've configured your endpoint URL.  4. In your code that receives or processes the webhooks, you should concatenate the verification token with the JSON object that we sent in our      POST request and hash it with md5.     ```     md5($verificationToken.$webhooksObject);     ```  5. Compare signature that you generated to the signature provided in the X-Exavault-Signature HTTP header  ## Example JSON Response Object  ```json   {     \"accountname\": \"mycompanyname\",     \"username\": \"john\"     \"operation\": \"Upload\",     \"protocol\": \"https\",     \"path\": \"/testfolder/filename.jpg\"     \"attempt\": 1   } ```  ## Webhooks Logs  Keep track of all your webhooks requests in the Activity section of your account. You can find the following info for each request:    1. date and time - timestamp of the request.    2. endpoint url - where the webhook was sent.    3. event - what triggered the webhook.    4. status - HTTP status or curl error code.    5. attempt - how many times we tried to send this request.    6. response size - size of the response from your server.    7. details - you can check the response body if it was sent. 

    OpenAPI spec version: 1.0.1
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from __future__ import absolute_import

import sys
import os
import re

# python 2 and python 3 compatibility library
from six import iteritems

from ..configuration import Configuration
from ..api_client import ApiClient


class UserApi(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    Ref: https://github.com/swagger-api/swagger-codegen
    """

    def __init__(self, api_client=None):
        config = Configuration()
        if api_client:
            self.api_client = api_client
        else:
            if not config.api_client:
                config.api_client = ApiClient()
            self.api_client = config.api_client

    def create_user(self, api_key, access_token, username, destination_folder, email, password, role, permissions, time_zone, **kwargs):
        """
        createUser
        Adds a new user to the account. The user may be configured as an admin or standard user, and (if a standard user) may be assigned a restricted home directory and restricted permissions.  > **Notes:** - Authenticated user's role must be admin or master; standard users are not allowed to create other users. 
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.create_user(api_key, access_token, username, destination_folder, email, password, role, permissions, time_zone, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str api_key: API key required to make the API call. (required)
        :param str access_token: Access token required to make the API call. (required)
        :param str username: Username of the user to create. This should follow standard username conventions; e.g. all lowercase, no spaces, etc. We do allow email addresses as usernames. (required)
        :param str destination_folder: The path to the user's home folder. For the account root, specify `/`. Otherwise, use standard Unix path format, e.g. `/path/to/some/dir`. The user will be locked to this directory and unable to move 'up' in the account. (required)
        :param str email: The user's email address. (required)
        :param str password: The user's password. (required)
        :param str role: The user's role. Note that admin users cannot have a `destinationFolder` other than `/`, and will be setup with full permissions regardless of what you specify in the `permissions` property. (required)
        :param str permissions: A CSV string of user permissions. For example: `upload,download,list`. Note that users will be unable to see any files in the account unless you include `list` permission.   (required)
        :param str time_zone: The user's timezone, used for accurate time display within the application. See <a href='https://php.net/manual/en/timezones.php' target='blank'>this page</a> for allowed values.  (required)
        :param str nickname: An optional nickname (e.g. 'David from Sales').
        :param str expiration: Optional timestamp when the user should expire, formatted `YYYY-mm-dd hh:mm:ss`.
        :param bool locked: If true, the user's account is locked by default.
        :param bool welcome_email: If true, send a user email upon creation. The default welcome email can be configured from the settings page in your account.
        :return: Response
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('callback'):
            return self.create_user_with_http_info(api_key, access_token, username, destination_folder, email, password, role, permissions, time_zone, **kwargs)
        else:
            (data) = self.create_user_with_http_info(api_key, access_token, username, destination_folder, email, password, role, permissions, time_zone, **kwargs)
            return data

    def create_user_with_http_info(self, api_key, access_token, username, destination_folder, email, password, role, permissions, time_zone, **kwargs):
        """
        createUser
        Adds a new user to the account. The user may be configured as an admin or standard user, and (if a standard user) may be assigned a restricted home directory and restricted permissions.  > **Notes:** - Authenticated user's role must be admin or master; standard users are not allowed to create other users. 
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.create_user_with_http_info(api_key, access_token, username, destination_folder, email, password, role, permissions, time_zone, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str api_key: API key required to make the API call. (required)
        :param str access_token: Access token required to make the API call. (required)
        :param str username: Username of the user to create. This should follow standard username conventions; e.g. all lowercase, no spaces, etc. We do allow email addresses as usernames. (required)
        :param str destination_folder: The path to the user's home folder. For the account root, specify `/`. Otherwise, use standard Unix path format, e.g. `/path/to/some/dir`. The user will be locked to this directory and unable to move 'up' in the account. (required)
        :param str email: The user's email address. (required)
        :param str password: The user's password. (required)
        :param str role: The user's role. Note that admin users cannot have a `destinationFolder` other than `/`, and will be setup with full permissions regardless of what you specify in the `permissions` property. (required)
        :param str permissions: A CSV string of user permissions. For example: `upload,download,list`. Note that users will be unable to see any files in the account unless you include `list` permission.   (required)
        :param str time_zone: The user's timezone, used for accurate time display within the application. See <a href='https://php.net/manual/en/timezones.php' target='blank'>this page</a> for allowed values.  (required)
        :param str nickname: An optional nickname (e.g. 'David from Sales').
        :param str expiration: Optional timestamp when the user should expire, formatted `YYYY-mm-dd hh:mm:ss`.
        :param bool locked: If true, the user's account is locked by default.
        :param bool welcome_email: If true, send a user email upon creation. The default welcome email can be configured from the settings page in your account.
        :return: Response
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['api_key', 'access_token', 'username', 'destination_folder', 'email', 'password', 'role', 'permissions', 'time_zone', 'nickname', 'expiration', 'locked', 'welcome_email']
        all_params.append('callback')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method create_user" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'api_key' is set
        if ('api_key' not in params) or (params['api_key'] is None):
            raise ValueError("Missing the required parameter `api_key` when calling `create_user`")
        # verify the required parameter 'access_token' is set
        if ('access_token' not in params) or (params['access_token'] is None):
            raise ValueError("Missing the required parameter `access_token` when calling `create_user`")
        # verify the required parameter 'username' is set
        if ('username' not in params) or (params['username'] is None):
            raise ValueError("Missing the required parameter `username` when calling `create_user`")
        # verify the required parameter 'destination_folder' is set
        if ('destination_folder' not in params) or (params['destination_folder'] is None):
            raise ValueError("Missing the required parameter `destination_folder` when calling `create_user`")
        # verify the required parameter 'email' is set
        if ('email' not in params) or (params['email'] is None):
            raise ValueError("Missing the required parameter `email` when calling `create_user`")
        # verify the required parameter 'password' is set
        if ('password' not in params) or (params['password'] is None):
            raise ValueError("Missing the required parameter `password` when calling `create_user`")
        # verify the required parameter 'role' is set
        if ('role' not in params) or (params['role'] is None):
            raise ValueError("Missing the required parameter `role` when calling `create_user`")
        # verify the required parameter 'permissions' is set
        if ('permissions' not in params) or (params['permissions'] is None):
            raise ValueError("Missing the required parameter `permissions` when calling `create_user`")
        # verify the required parameter 'time_zone' is set
        if ('time_zone' not in params) or (params['time_zone'] is None):
            raise ValueError("Missing the required parameter `time_zone` when calling `create_user`")


        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}
        if 'api_key' in params:
            header_params['api_key'] = params['api_key']

        form_params = []
        local_var_files = {}
        if 'access_token' in params:
            form_params.append(('access_token', params['access_token']))
        if 'username' in params:
            form_params.append(('username', params['username']))
        if 'nickname' in params:
            form_params.append(('nickname', params['nickname']))
        if 'destination_folder' in params:
            form_params.append(('destinationFolder', params['destination_folder']))
        if 'email' in params:
            form_params.append(('email', params['email']))
        if 'password' in params:
            form_params.append(('password', params['password']))
        if 'role' in params:
            form_params.append(('role', params['role']))
        if 'permissions' in params:
            form_params.append(('permissions', params['permissions']))
        if 'time_zone' in params:
            form_params.append(('timeZone', params['time_zone']))
        if 'expiration' in params:
            form_params.append(('expiration', params['expiration']))
        if 'locked' in params:
            form_params.append(('locked', params['locked']))
        if 'welcome_email' in params:
            form_params.append(('welcomeEmail', params['welcome_email']))

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.\
            select_header_accept(['application/json'])

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.\
            select_header_content_type(['application/x-www-form-urlencoded'])

        # Authentication setting
        auth_settings = []

        return self.api_client.call_api('/createUser', 'POST',
                                        path_params,
                                        query_params,
                                        header_params,
                                        body=body_params,
                                        post_params=form_params,
                                        files=local_var_files,
                                        response_type='Response',
                                        auth_settings=auth_settings,
                                        callback=params.get('callback'),
                                        _return_http_data_only=params.get('_return_http_data_only'),
                                        _preload_content=params.get('_preload_content', True),
                                        _request_timeout=params.get('_request_timeout'),
                                        collection_formats=collection_formats)

    def delete_user(self, api_key, access_token, username, **kwargs):
        """
        deleteUser
        Delete a user from the account. Deleting a user does **NOT** delete any files from the account; it merely removes a user's access. If you also need to delete the user's home folder or data when you delete the user, you should make a seperate call to <a href=\"#operation/deleteResources\">deleteResources</a>. > **Notes:** - Authenticated user's role must be admin or master 
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.delete_user(api_key, access_token, username, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str api_key: API key required to make the API call. (required)
        :param str access_token: Access token required to make the API call. (required)
        :param str username: Username of the user to delete. (required)
        :return: Response
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('callback'):
            return self.delete_user_with_http_info(api_key, access_token, username, **kwargs)
        else:
            (data) = self.delete_user_with_http_info(api_key, access_token, username, **kwargs)
            return data

    def delete_user_with_http_info(self, api_key, access_token, username, **kwargs):
        """
        deleteUser
        Delete a user from the account. Deleting a user does **NOT** delete any files from the account; it merely removes a user's access. If you also need to delete the user's home folder or data when you delete the user, you should make a seperate call to <a href=\"#operation/deleteResources\">deleteResources</a>. > **Notes:** - Authenticated user's role must be admin or master 
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.delete_user_with_http_info(api_key, access_token, username, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str api_key: API key required to make the API call. (required)
        :param str access_token: Access token required to make the API call. (required)
        :param str username: Username of the user to delete. (required)
        :return: Response
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['api_key', 'access_token', 'username']
        all_params.append('callback')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method delete_user" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'api_key' is set
        if ('api_key' not in params) or (params['api_key'] is None):
            raise ValueError("Missing the required parameter `api_key` when calling `delete_user`")
        # verify the required parameter 'access_token' is set
        if ('access_token' not in params) or (params['access_token'] is None):
            raise ValueError("Missing the required parameter `access_token` when calling `delete_user`")
        # verify the required parameter 'username' is set
        if ('username' not in params) or (params['username'] is None):
            raise ValueError("Missing the required parameter `username` when calling `delete_user`")


        collection_formats = {}

        path_params = {}

        query_params = []
        if 'access_token' in params:
            query_params.append(('access_token', params['access_token']))
        if 'username' in params:
            query_params.append(('username', params['username']))

        header_params = {}
        if 'api_key' in params:
            header_params['api_key'] = params['api_key']

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.\
            select_header_accept(['application/json'])

        # Authentication setting
        auth_settings = []

        return self.api_client.call_api('/deleteUser', 'GET',
                                        path_params,
                                        query_params,
                                        header_params,
                                        body=body_params,
                                        post_params=form_params,
                                        files=local_var_files,
                                        response_type='Response',
                                        auth_settings=auth_settings,
                                        callback=params.get('callback'),
                                        _return_http_data_only=params.get('_return_http_data_only'),
                                        _preload_content=params.get('_preload_content', True),
                                        _request_timeout=params.get('_request_timeout'),
                                        collection_formats=collection_formats)

    def get_account(self, api_key, access_token, **kwargs):
        """
        getAccount
        Gets the account object and master user object for the authenticated user. Useful if you need to lookup or display information about the the account. If you need information the user you're logged in as, rather than the account and master user, see <a href=\"#operation/getCurrentUser\">getCurrentUser</a>. 
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.get_account(api_key, access_token, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str api_key: API key required to make the API call. (required)
        :param str access_token: Access token required to make the API call. (required)
        :return: AccountResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('callback'):
            return self.get_account_with_http_info(api_key, access_token, **kwargs)
        else:
            (data) = self.get_account_with_http_info(api_key, access_token, **kwargs)
            return data

    def get_account_with_http_info(self, api_key, access_token, **kwargs):
        """
        getAccount
        Gets the account object and master user object for the authenticated user. Useful if you need to lookup or display information about the the account. If you need information the user you're logged in as, rather than the account and master user, see <a href=\"#operation/getCurrentUser\">getCurrentUser</a>. 
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.get_account_with_http_info(api_key, access_token, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str api_key: API key required to make the API call. (required)
        :param str access_token: Access token required to make the API call. (required)
        :return: AccountResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['api_key', 'access_token']
        all_params.append('callback')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_account" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'api_key' is set
        if ('api_key' not in params) or (params['api_key'] is None):
            raise ValueError("Missing the required parameter `api_key` when calling `get_account`")
        # verify the required parameter 'access_token' is set
        if ('access_token' not in params) or (params['access_token'] is None):
            raise ValueError("Missing the required parameter `access_token` when calling `get_account`")


        collection_formats = {}

        path_params = {}

        query_params = []
        if 'access_token' in params:
            query_params.append(('access_token', params['access_token']))

        header_params = {}
        if 'api_key' in params:
            header_params['api_key'] = params['api_key']

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.\
            select_header_accept(['application/json'])

        # Authentication setting
        auth_settings = []

        return self.api_client.call_api('/getAccount', 'GET',
                                        path_params,
                                        query_params,
                                        header_params,
                                        body=body_params,
                                        post_params=form_params,
                                        files=local_var_files,
                                        response_type='AccountResponse',
                                        auth_settings=auth_settings,
                                        callback=params.get('callback'),
                                        _return_http_data_only=params.get('_return_http_data_only'),
                                        _preload_content=params.get('_preload_content', True),
                                        _request_timeout=params.get('_request_timeout'),
                                        collection_formats=collection_formats)

    def get_current_user(self, api_key, access_token, **kwargs):
        """
        getCurrentUser
        Gets the user object for the authenticated user. The user object contains detailed information on the user &ndash; the creation timestamp, username, nickname, associated email, and more. See the response sample, below, for full details.
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.get_current_user(api_key, access_token, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str api_key: API key required to make the API call. (required)
        :param str access_token: Access token required to make the API call. (required)
        :return: UserResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('callback'):
            return self.get_current_user_with_http_info(api_key, access_token, **kwargs)
        else:
            (data) = self.get_current_user_with_http_info(api_key, access_token, **kwargs)
            return data

    def get_current_user_with_http_info(self, api_key, access_token, **kwargs):
        """
        getCurrentUser
        Gets the user object for the authenticated user. The user object contains detailed information on the user &ndash; the creation timestamp, username, nickname, associated email, and more. See the response sample, below, for full details.
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.get_current_user_with_http_info(api_key, access_token, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str api_key: API key required to make the API call. (required)
        :param str access_token: Access token required to make the API call. (required)
        :return: UserResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['api_key', 'access_token']
        all_params.append('callback')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_current_user" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'api_key' is set
        if ('api_key' not in params) or (params['api_key'] is None):
            raise ValueError("Missing the required parameter `api_key` when calling `get_current_user`")
        # verify the required parameter 'access_token' is set
        if ('access_token' not in params) or (params['access_token'] is None):
            raise ValueError("Missing the required parameter `access_token` when calling `get_current_user`")


        collection_formats = {}

        path_params = {}

        query_params = []
        if 'access_token' in params:
            query_params.append(('access_token', params['access_token']))

        header_params = {}
        if 'api_key' in params:
            header_params['api_key'] = params['api_key']

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.\
            select_header_accept(['application/json'])

        # Authentication setting
        auth_settings = []

        return self.api_client.call_api('/getCurrentUser', 'GET',
                                        path_params,
                                        query_params,
                                        header_params,
                                        body=body_params,
                                        post_params=form_params,
                                        files=local_var_files,
                                        response_type='UserResponse',
                                        auth_settings=auth_settings,
                                        callback=params.get('callback'),
                                        _return_http_data_only=params.get('_return_http_data_only'),
                                        _preload_content=params.get('_preload_content', True),
                                        _request_timeout=params.get('_request_timeout'),
                                        collection_formats=collection_formats)

    def get_user(self, api_key, access_token, username, **kwargs):
        """
        getUser
        Get details on the specified user from your account. The user object contains detailed information on the user &ndash; the creation timestamp, username, nickname, associated email, and more. See the response sample, below, for full details.  **Notes:** - Authenticated user's role must be admin or master. 
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.get_user(api_key, access_token, username, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str api_key: API key required to make the API call. (required)
        :param str access_token: Access token required to make the API call. (required)
        :param str username: Username of the user to get. (required)
        :return: UserResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('callback'):
            return self.get_user_with_http_info(api_key, access_token, username, **kwargs)
        else:
            (data) = self.get_user_with_http_info(api_key, access_token, username, **kwargs)
            return data

    def get_user_with_http_info(self, api_key, access_token, username, **kwargs):
        """
        getUser
        Get details on the specified user from your account. The user object contains detailed information on the user &ndash; the creation timestamp, username, nickname, associated email, and more. See the response sample, below, for full details.  **Notes:** - Authenticated user's role must be admin or master. 
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.get_user_with_http_info(api_key, access_token, username, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str api_key: API key required to make the API call. (required)
        :param str access_token: Access token required to make the API call. (required)
        :param str username: Username of the user to get. (required)
        :return: UserResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['api_key', 'access_token', 'username']
        all_params.append('callback')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_user" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'api_key' is set
        if ('api_key' not in params) or (params['api_key'] is None):
            raise ValueError("Missing the required parameter `api_key` when calling `get_user`")
        # verify the required parameter 'access_token' is set
        if ('access_token' not in params) or (params['access_token'] is None):
            raise ValueError("Missing the required parameter `access_token` when calling `get_user`")
        # verify the required parameter 'username' is set
        if ('username' not in params) or (params['username'] is None):
            raise ValueError("Missing the required parameter `username` when calling `get_user`")


        collection_formats = {}

        path_params = {}

        query_params = []
        if 'access_token' in params:
            query_params.append(('access_token', params['access_token']))
        if 'username' in params:
            query_params.append(('username', params['username']))

        header_params = {}
        if 'api_key' in params:
            header_params['api_key'] = params['api_key']

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.\
            select_header_accept(['application/json'])

        # Authentication setting
        auth_settings = []

        return self.api_client.call_api('/getUser', 'GET',
                                        path_params,
                                        query_params,
                                        header_params,
                                        body=body_params,
                                        post_params=form_params,
                                        files=local_var_files,
                                        response_type='UserResponse',
                                        auth_settings=auth_settings,
                                        callback=params.get('callback'),
                                        _return_http_data_only=params.get('_return_http_data_only'),
                                        _preload_content=params.get('_preload_content', True),
                                        _request_timeout=params.get('_request_timeout'),
                                        collection_formats=collection_formats)

    def get_users(self, api_key, access_token, sort_by, **kwargs):
        """
        getUsers
        Gets array of all user objects in your account. Each element of the array will contain details on a single user.  **Notes:** - Authenticated user's role must be admin or master. 
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.get_users(api_key, access_token, sort_by, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str api_key: API key required to make the API call. (required)
        :param str access_token: Access token required to make the API call. (required)
        :param str sort_by: Sort method for the returned array. (required)
        :param str sort_order: Sort order for the returned array.
        :return: UsersResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('callback'):
            return self.get_users_with_http_info(api_key, access_token, sort_by, **kwargs)
        else:
            (data) = self.get_users_with_http_info(api_key, access_token, sort_by, **kwargs)
            return data

    def get_users_with_http_info(self, api_key, access_token, sort_by, **kwargs):
        """
        getUsers
        Gets array of all user objects in your account. Each element of the array will contain details on a single user.  **Notes:** - Authenticated user's role must be admin or master. 
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.get_users_with_http_info(api_key, access_token, sort_by, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str api_key: API key required to make the API call. (required)
        :param str access_token: Access token required to make the API call. (required)
        :param str sort_by: Sort method for the returned array. (required)
        :param str sort_order: Sort order for the returned array.
        :return: UsersResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['api_key', 'access_token', 'sort_by', 'sort_order']
        all_params.append('callback')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_users" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'api_key' is set
        if ('api_key' not in params) or (params['api_key'] is None):
            raise ValueError("Missing the required parameter `api_key` when calling `get_users`")
        # verify the required parameter 'access_token' is set
        if ('access_token' not in params) or (params['access_token'] is None):
            raise ValueError("Missing the required parameter `access_token` when calling `get_users`")
        # verify the required parameter 'sort_by' is set
        if ('sort_by' not in params) or (params['sort_by'] is None):
            raise ValueError("Missing the required parameter `sort_by` when calling `get_users`")


        collection_formats = {}

        path_params = {}

        query_params = []
        if 'access_token' in params:
            query_params.append(('access_token', params['access_token']))
        if 'sort_by' in params:
            query_params.append(('sortBy', params['sort_by']))
        if 'sort_order' in params:
            query_params.append(('sortOrder', params['sort_order']))

        header_params = {}
        if 'api_key' in params:
            header_params['api_key'] = params['api_key']

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.\
            select_header_accept(['application/json'])

        # Authentication setting
        auth_settings = []

        return self.api_client.call_api('/getUsers', 'GET',
                                        path_params,
                                        query_params,
                                        header_params,
                                        body=body_params,
                                        post_params=form_params,
                                        files=local_var_files,
                                        response_type='UsersResponse',
                                        auth_settings=auth_settings,
                                        callback=params.get('callback'),
                                        _return_http_data_only=params.get('_return_http_data_only'),
                                        _preload_content=params.get('_preload_content', True),
                                        _request_timeout=params.get('_request_timeout'),
                                        collection_formats=collection_formats)

    def update_user(self, api_key, access_token, user_id, **kwargs):
        """
        updateUser
        Updates specified user record in your account. Note that the unique key for this API call is our internal ID, and _not_ the username, as the username can be changed.   > **Notes:** - Authenticated user's role must be admin or master. 
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.update_user(api_key, access_token, user_id, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str api_key: API key required to make the API call. (required)
        :param str access_token: Access token required to make the API call. (required)
        :param int user_id: The user's ID. Note that this is our internal ID, and _not the username_. You can obtain it by calling the <a href=\"#operation/getUser\">getUser</a> method. (required)
        :param str username: Username of the user to create. This should follow standard username conventions; e.g. all lowercase, no spaces, etc. We do allow email addresses as usernames.
        :param str nickname: An optional nickname (e.g. 'David from Sales').
        :param str destination_folder: The path to the user's home folder. For the account root, specify `/`. Otherwise, use standard Unix path format, e.g. `/path/to/some/dir`. The user will be locked to this directory and unable to move 'up' in the account.
        :param str email: The user's email address.
        :param str password: The user's password.
        :param str role: The user's role. Note that admin users cannot have a `destinationFolder` other than `/`, and will be setup with full permissions regardless of what you specify in the `permissions` property.
        :param str permissions: A CSV string of user permissions. For example: `upload,download,list`. Note that users will be unable to see any files in the account unless you include `list` permission.  
        :param str time_zone: The user's timezone, used for accurate time display within the application. See <a href='https://php.net/manual/en/timezones.php' target='blank'>this page</a> for allowed values. 
        :param str expiration: Optional timestamp when the user should expire, formatted `YYYY-mm-dd hh:mm:ss`.
        :param bool locked: If true, the user's account is locked by default.
        :return: Response
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('callback'):
            return self.update_user_with_http_info(api_key, access_token, user_id, **kwargs)
        else:
            (data) = self.update_user_with_http_info(api_key, access_token, user_id, **kwargs)
            return data

    def update_user_with_http_info(self, api_key, access_token, user_id, **kwargs):
        """
        updateUser
        Updates specified user record in your account. Note that the unique key for this API call is our internal ID, and _not_ the username, as the username can be changed.   > **Notes:** - Authenticated user's role must be admin or master. 
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.update_user_with_http_info(api_key, access_token, user_id, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str api_key: API key required to make the API call. (required)
        :param str access_token: Access token required to make the API call. (required)
        :param int user_id: The user's ID. Note that this is our internal ID, and _not the username_. You can obtain it by calling the <a href=\"#operation/getUser\">getUser</a> method. (required)
        :param str username: Username of the user to create. This should follow standard username conventions; e.g. all lowercase, no spaces, etc. We do allow email addresses as usernames.
        :param str nickname: An optional nickname (e.g. 'David from Sales').
        :param str destination_folder: The path to the user's home folder. For the account root, specify `/`. Otherwise, use standard Unix path format, e.g. `/path/to/some/dir`. The user will be locked to this directory and unable to move 'up' in the account.
        :param str email: The user's email address.
        :param str password: The user's password.
        :param str role: The user's role. Note that admin users cannot have a `destinationFolder` other than `/`, and will be setup with full permissions regardless of what you specify in the `permissions` property.
        :param str permissions: A CSV string of user permissions. For example: `upload,download,list`. Note that users will be unable to see any files in the account unless you include `list` permission.  
        :param str time_zone: The user's timezone, used for accurate time display within the application. See <a href='https://php.net/manual/en/timezones.php' target='blank'>this page</a> for allowed values. 
        :param str expiration: Optional timestamp when the user should expire, formatted `YYYY-mm-dd hh:mm:ss`.
        :param bool locked: If true, the user's account is locked by default.
        :return: Response
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['api_key', 'access_token', 'user_id', 'username', 'nickname', 'destination_folder', 'email', 'password', 'role', 'permissions', 'time_zone', 'expiration', 'locked']
        all_params.append('callback')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method update_user" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'api_key' is set
        if ('api_key' not in params) or (params['api_key'] is None):
            raise ValueError("Missing the required parameter `api_key` when calling `update_user`")
        # verify the required parameter 'access_token' is set
        if ('access_token' not in params) or (params['access_token'] is None):
            raise ValueError("Missing the required parameter `access_token` when calling `update_user`")
        # verify the required parameter 'user_id' is set
        if ('user_id' not in params) or (params['user_id'] is None):
            raise ValueError("Missing the required parameter `user_id` when calling `update_user`")


        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}
        if 'api_key' in params:
            header_params['api_key'] = params['api_key']

        form_params = []
        local_var_files = {}
        if 'access_token' in params:
            form_params.append(('access_token', params['access_token']))
        if 'user_id' in params:
            form_params.append(('userId', params['user_id']))
        if 'username' in params:
            form_params.append(('username', params['username']))
        if 'nickname' in params:
            form_params.append(('nickname', params['nickname']))
        if 'destination_folder' in params:
            form_params.append(('destinationFolder', params['destination_folder']))
        if 'email' in params:
            form_params.append(('email', params['email']))
        if 'password' in params:
            form_params.append(('password', params['password']))
        if 'role' in params:
            form_params.append(('role', params['role']))
        if 'permissions' in params:
            form_params.append(('permissions', params['permissions']))
        if 'time_zone' in params:
            form_params.append(('timeZone', params['time_zone']))
        if 'expiration' in params:
            form_params.append(('expiration', params['expiration']))
        if 'locked' in params:
            form_params.append(('locked', params['locked']))

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.\
            select_header_accept(['application/json'])

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.\
            select_header_content_type(['application/x-www-form-urlencoded'])

        # Authentication setting
        auth_settings = []

        return self.api_client.call_api('/updateUser', 'POST',
                                        path_params,
                                        query_params,
                                        header_params,
                                        body=body_params,
                                        post_params=form_params,
                                        files=local_var_files,
                                        response_type='Response',
                                        auth_settings=auth_settings,
                                        callback=params.get('callback'),
                                        _return_http_data_only=params.get('_return_http_data_only'),
                                        _preload_content=params.get('_preload_content', True),
                                        _request_timeout=params.get('_request_timeout'),
                                        collection_formats=collection_formats)

    def user_available(self, api_key, access_token, username, **kwargs):
        """
        userAvailable
        Returns true if requested username has not already been taken in the system. Note that usernames are global in our system; if one account has claimed the username 'bobsmith' then no other account may use that username.
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.user_available(api_key, access_token, username, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str api_key: API key required to make the API call. (required)
        :param str access_token: Access token required to make the API call. (required)
        :param str username: Username to check. (required)
        :return: AvailableUserResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('callback'):
            return self.user_available_with_http_info(api_key, access_token, username, **kwargs)
        else:
            (data) = self.user_available_with_http_info(api_key, access_token, username, **kwargs)
            return data

    def user_available_with_http_info(self, api_key, access_token, username, **kwargs):
        """
        userAvailable
        Returns true if requested username has not already been taken in the system. Note that usernames are global in our system; if one account has claimed the username 'bobsmith' then no other account may use that username.
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.user_available_with_http_info(api_key, access_token, username, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str api_key: API key required to make the API call. (required)
        :param str access_token: Access token required to make the API call. (required)
        :param str username: Username to check. (required)
        :return: AvailableUserResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['api_key', 'access_token', 'username']
        all_params.append('callback')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method user_available" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'api_key' is set
        if ('api_key' not in params) or (params['api_key'] is None):
            raise ValueError("Missing the required parameter `api_key` when calling `user_available`")
        # verify the required parameter 'access_token' is set
        if ('access_token' not in params) or (params['access_token'] is None):
            raise ValueError("Missing the required parameter `access_token` when calling `user_available`")
        # verify the required parameter 'username' is set
        if ('username' not in params) or (params['username'] is None):
            raise ValueError("Missing the required parameter `username` when calling `user_available`")


        collection_formats = {}

        path_params = {}

        query_params = []
        if 'access_token' in params:
            query_params.append(('access_token', params['access_token']))
        if 'username' in params:
            query_params.append(('username', params['username']))

        header_params = {}
        if 'api_key' in params:
            header_params['api_key'] = params['api_key']

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.\
            select_header_accept(['application/json'])

        # Authentication setting
        auth_settings = []

        return self.api_client.call_api('/userAvailable', 'GET',
                                        path_params,
                                        query_params,
                                        header_params,
                                        body=body_params,
                                        post_params=form_params,
                                        files=local_var_files,
                                        response_type='AvailableUserResponse',
                                        auth_settings=auth_settings,
                                        callback=params.get('callback'),
                                        _return_http_data_only=params.get('_return_http_data_only'),
                                        _preload_content=params.get('_preload_content', True),
                                        _request_timeout=params.get('_request_timeout'),
                                        collection_formats=collection_formats)
