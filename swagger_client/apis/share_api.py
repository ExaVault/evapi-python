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


class ShareApi(object):
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

    def create_share(self, api_key, access_token, type, name, file_paths, access_mode, **kwargs):
        """
        createShare
        Creates a new share object for the given path in your account. We support three types of shares:   - A **shared folder** allows you to let outside parties access a folder in your account (including any files and nested subfolders) using just a link. Shared folders can be restricted; e.g. with an expiration date, password, download-only, etc. Shared folders are 'live'; if someone makes a change to a file in your shared folder, it will be immediately reflected in your account, and vice-versa.   - A **file send** lets you send one or more files via an easy download link. File sends are different than shared folders because file sends are 'point in time' -- the recipient will get the files as you sent them. If you later make a change to the source file, it will not be updated for the recipient.   - A **recieve folder** lets you recieve files into your account. You can either send users a link, or optionally drop an upload widget on your website.   **Notes:** - Authenticated user requires share permission. 
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.create_share(api_key, access_token, type, name, file_paths, access_mode, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str api_key: API key required to make the API call. (required)
        :param str access_token: Access token required to make the API call. (required)
        :param str type: The type of share to create. See above for a description of each. (required)
        :param str name: Name of the share. (required)
        :param list[str] file_paths: Array of strings containing the file paths to share. (required)
        :param str access_mode: Type of permissions share recipients have. (required)
        :param str subject: Share message subject (for email invitations).
        :param str message: Share message contents (for email invitations).
        :param list[str] emails: Array of strings for email recipients (for email invitations).
        :param list[str] cc_email: Array of strings for CC email recipients (for email invitations).
        :param bool require_email: Requires a user to enter their email address to access. If set true, isPublic must also be set true.  Please note that emails are not validated; we simply log the email in the share activity.  If you want a share to be invite only (e.g. restricted access to only invited email addresses) you should set this to false, and pass the set of email addresses via the `emails` paramater. 
        :param bool embed: Allows user to embed a widget with the share.
        :param bool is_public: True if share has a public URL. If false, the only way to access the share will be via the personalized URL sent via the email invite process.
        :param str password: If not null, value of password is required to access this share.
        :param str expiration: The timestamp the current share should expire, formatted `YYYY-mm-dd hh:mm:ss`.
        :param bool has_notification: True if the user should be notified about activity on this share.
        :param list[str] notification_emails: An array of recipients who should receive notification emails.
        :param bool file_drop_create_folders: If true, all receive folder submissions will be uploaded separate folders (only applicable for the `receive` share type).
        :return: ShareResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('callback'):
            return self.create_share_with_http_info(api_key, access_token, type, name, file_paths, access_mode, **kwargs)
        else:
            (data) = self.create_share_with_http_info(api_key, access_token, type, name, file_paths, access_mode, **kwargs)
            return data

    def create_share_with_http_info(self, api_key, access_token, type, name, file_paths, access_mode, **kwargs):
        """
        createShare
        Creates a new share object for the given path in your account. We support three types of shares:   - A **shared folder** allows you to let outside parties access a folder in your account (including any files and nested subfolders) using just a link. Shared folders can be restricted; e.g. with an expiration date, password, download-only, etc. Shared folders are 'live'; if someone makes a change to a file in your shared folder, it will be immediately reflected in your account, and vice-versa.   - A **file send** lets you send one or more files via an easy download link. File sends are different than shared folders because file sends are 'point in time' -- the recipient will get the files as you sent them. If you later make a change to the source file, it will not be updated for the recipient.   - A **recieve folder** lets you recieve files into your account. You can either send users a link, or optionally drop an upload widget on your website.   **Notes:** - Authenticated user requires share permission. 
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.create_share_with_http_info(api_key, access_token, type, name, file_paths, access_mode, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str api_key: API key required to make the API call. (required)
        :param str access_token: Access token required to make the API call. (required)
        :param str type: The type of share to create. See above for a description of each. (required)
        :param str name: Name of the share. (required)
        :param list[str] file_paths: Array of strings containing the file paths to share. (required)
        :param str access_mode: Type of permissions share recipients have. (required)
        :param str subject: Share message subject (for email invitations).
        :param str message: Share message contents (for email invitations).
        :param list[str] emails: Array of strings for email recipients (for email invitations).
        :param list[str] cc_email: Array of strings for CC email recipients (for email invitations).
        :param bool require_email: Requires a user to enter their email address to access. If set true, isPublic must also be set true.  Please note that emails are not validated; we simply log the email in the share activity.  If you want a share to be invite only (e.g. restricted access to only invited email addresses) you should set this to false, and pass the set of email addresses via the `emails` paramater. 
        :param bool embed: Allows user to embed a widget with the share.
        :param bool is_public: True if share has a public URL. If false, the only way to access the share will be via the personalized URL sent via the email invite process.
        :param str password: If not null, value of password is required to access this share.
        :param str expiration: The timestamp the current share should expire, formatted `YYYY-mm-dd hh:mm:ss`.
        :param bool has_notification: True if the user should be notified about activity on this share.
        :param list[str] notification_emails: An array of recipients who should receive notification emails.
        :param bool file_drop_create_folders: If true, all receive folder submissions will be uploaded separate folders (only applicable for the `receive` share type).
        :return: ShareResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['api_key', 'access_token', 'type', 'name', 'file_paths', 'access_mode', 'subject', 'message', 'emails', 'cc_email', 'require_email', 'embed', 'is_public', 'password', 'expiration', 'has_notification', 'notification_emails', 'file_drop_create_folders']
        all_params.append('callback')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method create_share" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'api_key' is set
        if ('api_key' not in params) or (params['api_key'] is None):
            raise ValueError("Missing the required parameter `api_key` when calling `create_share`")
        # verify the required parameter 'access_token' is set
        if ('access_token' not in params) or (params['access_token'] is None):
            raise ValueError("Missing the required parameter `access_token` when calling `create_share`")
        # verify the required parameter 'type' is set
        if ('type' not in params) or (params['type'] is None):
            raise ValueError("Missing the required parameter `type` when calling `create_share`")
        # verify the required parameter 'name' is set
        if ('name' not in params) or (params['name'] is None):
            raise ValueError("Missing the required parameter `name` when calling `create_share`")
        # verify the required parameter 'file_paths' is set
        if ('file_paths' not in params) or (params['file_paths'] is None):
            raise ValueError("Missing the required parameter `file_paths` when calling `create_share`")
        # verify the required parameter 'access_mode' is set
        if ('access_mode' not in params) or (params['access_mode'] is None):
            raise ValueError("Missing the required parameter `access_mode` when calling `create_share`")


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
        if 'type' in params:
            form_params.append(('type', params['type']))
        if 'name' in params:
            form_params.append(('name', params['name']))
        if 'file_paths' in params:
            form_params.append(('filePaths', params['file_paths']))
            collection_formats['filePaths'] = 'multi'
        if 'access_mode' in params:
            form_params.append(('accessMode', params['access_mode']))
        if 'subject' in params:
            form_params.append(('subject', params['subject']))
        if 'message' in params:
            form_params.append(('message', params['message']))
        if 'emails' in params:
            form_params.append(('emails', params['emails']))
            collection_formats['emails'] = 'multi'
        if 'cc_email' in params:
            form_params.append(('ccEmail', params['cc_email']))
            collection_formats['ccEmail'] = 'multi'
        if 'require_email' in params:
            form_params.append(('requireEmail', params['require_email']))
        if 'embed' in params:
            form_params.append(('embed', params['embed']))
        if 'is_public' in params:
            form_params.append(('isPublic', params['is_public']))
        if 'password' in params:
            form_params.append(('password', params['password']))
        if 'expiration' in params:
            form_params.append(('expiration', params['expiration']))
        if 'has_notification' in params:
            form_params.append(('hasNotification', params['has_notification']))
        if 'notification_emails' in params:
            form_params.append(('notificationEmails', params['notification_emails']))
            collection_formats['notificationEmails'] = 'multi'
        if 'file_drop_create_folders' in params:
            form_params.append(('fileDropCreateFolders', params['file_drop_create_folders']))

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.\
            select_header_accept(['application/json'])

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.\
            select_header_content_type(['application/x-www-form-urlencoded'])

        # Authentication setting
        auth_settings = []

        return self.api_client.call_api('/createShare', 'POST',
                                        path_params,
                                        query_params,
                                        header_params,
                                        body=body_params,
                                        post_params=form_params,
                                        files=local_var_files,
                                        response_type='ShareResponse',
                                        auth_settings=auth_settings,
                                        callback=params.get('callback'),
                                        _return_http_data_only=params.get('_return_http_data_only'),
                                        _preload_content=params.get('_preload_content', True),
                                        _request_timeout=params.get('_request_timeout'),
                                        collection_formats=collection_formats)

    def delete_share(self, api_key, access_token, id, **kwargs):
        """
        deleteShare
        Delete a share. Deleting a share does not remove the underlying files for `shared_folder` and `recieve` share types; it merely removes the access URL. Delating a `send` share type does remove the associated files, as files that have been sent are _only_ associated with the share, and aren't stored anywhere else in the account. > **Notes:**  - Authenticated user's role must be admin or master, or user must be the owner of the specified share.  
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.delete_share(api_key, access_token, id, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str api_key: API key required to make the API call. (required)
        :param str access_token: Access token required to make the API call. (required)
        :param int id: ID of the share to delete. Use <a href=\"#operation/getShares\">getShares</a> if you need to lookup an ID. (required)
        :return: Response
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('callback'):
            return self.delete_share_with_http_info(api_key, access_token, id, **kwargs)
        else:
            (data) = self.delete_share_with_http_info(api_key, access_token, id, **kwargs)
            return data

    def delete_share_with_http_info(self, api_key, access_token, id, **kwargs):
        """
        deleteShare
        Delete a share. Deleting a share does not remove the underlying files for `shared_folder` and `recieve` share types; it merely removes the access URL. Delating a `send` share type does remove the associated files, as files that have been sent are _only_ associated with the share, and aren't stored anywhere else in the account. > **Notes:**  - Authenticated user's role must be admin or master, or user must be the owner of the specified share.  
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.delete_share_with_http_info(api_key, access_token, id, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str api_key: API key required to make the API call. (required)
        :param str access_token: Access token required to make the API call. (required)
        :param int id: ID of the share to delete. Use <a href=\"#operation/getShares\">getShares</a> if you need to lookup an ID. (required)
        :return: Response
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['api_key', 'access_token', 'id']
        all_params.append('callback')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method delete_share" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'api_key' is set
        if ('api_key' not in params) or (params['api_key'] is None):
            raise ValueError("Missing the required parameter `api_key` when calling `delete_share`")
        # verify the required parameter 'access_token' is set
        if ('access_token' not in params) or (params['access_token'] is None):
            raise ValueError("Missing the required parameter `access_token` when calling `delete_share`")
        # verify the required parameter 'id' is set
        if ('id' not in params) or (params['id'] is None):
            raise ValueError("Missing the required parameter `id` when calling `delete_share`")


        collection_formats = {}

        path_params = {}

        query_params = []
        if 'access_token' in params:
            query_params.append(('access_token', params['access_token']))
        if 'id' in params:
            query_params.append(('id', params['id']))

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

        return self.api_client.call_api('/deleteShare', 'GET',
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

    def get_share(self, api_key, access_token, id, **kwargs):
        """
        getShare
        Returns a share object specified by a given share ID.   **Notes:** - Authenticated user should be the owner of the specified share. 
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.get_share(api_key, access_token, id, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str api_key: API key required to make the API call. (required)
        :param str access_token: Access token required to make the API call. (required)
        :param int id: ID of the requested share. Note this is our internal ID, not the share hash. Use <a href=\"#operation/getShares\">getShares</a> if you need to lookup an ID. (required)
        :return: ShareResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('callback'):
            return self.get_share_with_http_info(api_key, access_token, id, **kwargs)
        else:
            (data) = self.get_share_with_http_info(api_key, access_token, id, **kwargs)
            return data

    def get_share_with_http_info(self, api_key, access_token, id, **kwargs):
        """
        getShare
        Returns a share object specified by a given share ID.   **Notes:** - Authenticated user should be the owner of the specified share. 
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.get_share_with_http_info(api_key, access_token, id, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str api_key: API key required to make the API call. (required)
        :param str access_token: Access token required to make the API call. (required)
        :param int id: ID of the requested share. Note this is our internal ID, not the share hash. Use <a href=\"#operation/getShares\">getShares</a> if you need to lookup an ID. (required)
        :return: ShareResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['api_key', 'access_token', 'id']
        all_params.append('callback')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_share" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'api_key' is set
        if ('api_key' not in params) or (params['api_key'] is None):
            raise ValueError("Missing the required parameter `api_key` when calling `get_share`")
        # verify the required parameter 'access_token' is set
        if ('access_token' not in params) or (params['access_token'] is None):
            raise ValueError("Missing the required parameter `access_token` when calling `get_share`")
        # verify the required parameter 'id' is set
        if ('id' not in params) or (params['id'] is None):
            raise ValueError("Missing the required parameter `id` when calling `get_share`")


        collection_formats = {}

        path_params = {}

        query_params = []
        if 'access_token' in params:
            query_params.append(('access_token', params['access_token']))
        if 'id' in params:
            query_params.append(('id', params['id']))

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

        return self.api_client.call_api('/getShare', 'GET',
                                        path_params,
                                        query_params,
                                        header_params,
                                        body=body_params,
                                        post_params=form_params,
                                        files=local_var_files,
                                        response_type='ShareResponse',
                                        auth_settings=auth_settings,
                                        callback=params.get('callback'),
                                        _return_http_data_only=params.get('_return_http_data_only'),
                                        _preload_content=params.get('_preload_content', True),
                                        _request_timeout=params.get('_request_timeout'),
                                        collection_formats=collection_formats)

    def get_shares(self, api_key, access_token, sort_by, sort_order, **kwargs):
        """
        getShares
        Returns array of all share objects that the authenticated user has access to. Sorting and filtering options allow you to limit the returned list.  **Notes:**  - Authenticated user requires share permission.  - To get share objects with type `send`, authenticated user's role must be admin or master. 
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.get_shares(api_key, access_token, sort_by, sort_order, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str api_key: API key required to make the API call. (required)
        :param str access_token: Access token required to make the API call. (required)
        :param str sort_by: Sort method. (required)
        :param str sort_order: Sort order. (required)
        :param str type: The type of share to return. If no argument specified, will return all shares of all types.
        :param str filter: Filter by the provided search terms.
        :param str include: Filter returned shares. You can get all shares in the account, only active ones or shares you own.
        :param int offset: Start position of results to return, for pagination. Defaults to zero (0).
        :param int limit: Maximum number of shares to return.
        :return: SharesResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('callback'):
            return self.get_shares_with_http_info(api_key, access_token, sort_by, sort_order, **kwargs)
        else:
            (data) = self.get_shares_with_http_info(api_key, access_token, sort_by, sort_order, **kwargs)
            return data

    def get_shares_with_http_info(self, api_key, access_token, sort_by, sort_order, **kwargs):
        """
        getShares
        Returns array of all share objects that the authenticated user has access to. Sorting and filtering options allow you to limit the returned list.  **Notes:**  - Authenticated user requires share permission.  - To get share objects with type `send`, authenticated user's role must be admin or master. 
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.get_shares_with_http_info(api_key, access_token, sort_by, sort_order, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str api_key: API key required to make the API call. (required)
        :param str access_token: Access token required to make the API call. (required)
        :param str sort_by: Sort method. (required)
        :param str sort_order: Sort order. (required)
        :param str type: The type of share to return. If no argument specified, will return all shares of all types.
        :param str filter: Filter by the provided search terms.
        :param str include: Filter returned shares. You can get all shares in the account, only active ones or shares you own.
        :param int offset: Start position of results to return, for pagination. Defaults to zero (0).
        :param int limit: Maximum number of shares to return.
        :return: SharesResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['api_key', 'access_token', 'sort_by', 'sort_order', 'type', 'filter', 'include', 'offset', 'limit']
        all_params.append('callback')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_shares" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'api_key' is set
        if ('api_key' not in params) or (params['api_key'] is None):
            raise ValueError("Missing the required parameter `api_key` when calling `get_shares`")
        # verify the required parameter 'access_token' is set
        if ('access_token' not in params) or (params['access_token'] is None):
            raise ValueError("Missing the required parameter `access_token` when calling `get_shares`")
        # verify the required parameter 'sort_by' is set
        if ('sort_by' not in params) or (params['sort_by'] is None):
            raise ValueError("Missing the required parameter `sort_by` when calling `get_shares`")
        # verify the required parameter 'sort_order' is set
        if ('sort_order' not in params) or (params['sort_order'] is None):
            raise ValueError("Missing the required parameter `sort_order` when calling `get_shares`")


        collection_formats = {}

        path_params = {}

        query_params = []
        if 'access_token' in params:
            query_params.append(('access_token', params['access_token']))
        if 'type' in params:
            query_params.append(('type', params['type']))
        if 'sort_by' in params:
            query_params.append(('sortBy', params['sort_by']))
        if 'sort_order' in params:
            query_params.append(('sortOrder', params['sort_order']))
        if 'filter' in params:
            query_params.append(('filter', params['filter']))
        if 'include' in params:
            query_params.append(('include', params['include']))
        if 'offset' in params:
            query_params.append(('offset', params['offset']))
        if 'limit' in params:
            query_params.append(('limit', params['limit']))

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

        return self.api_client.call_api('/getShares', 'GET',
                                        path_params,
                                        query_params,
                                        header_params,
                                        body=body_params,
                                        post_params=form_params,
                                        files=local_var_files,
                                        response_type='SharesResponse',
                                        auth_settings=auth_settings,
                                        callback=params.get('callback'),
                                        _return_http_data_only=params.get('_return_http_data_only'),
                                        _preload_content=params.get('_preload_content', True),
                                        _request_timeout=params.get('_request_timeout'),
                                        collection_formats=collection_formats)

    def update_share(self, api_key, access_token, id, **kwargs):
        """
        updateShare
        Update an existing share object by specified ID. Note that it is not possible to change the type of share once it has been created; if you need to (for example) convert a shared folder to a recieve folder, you must first delete the shared folder and then create a new recieve folder.  **Notes:** - Authenticated user's role must be admin or master, or the authenticated user must be the owner of the specified share. 
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.update_share(api_key, access_token, id, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str api_key: API key required to make the API call. (required)
        :param str access_token: Access token required to make the API call. (required)
        :param int id: ID of the share to update. Use <a href=\"#operation/getShares\">getShares</a> if you need to lookup an ID. (required)
        :param str name: Name of the share.
        :param list[str] file_paths: Array of strings containing the file paths to share.
        :param str access_mode: Type of permissions share recipients have.
        :param str subject: Share message subject (for email invitations).
        :param str message: Share message contents (for email invitations).
        :param list[str] emails: Array of strings for email recipients (for email invitations).
        :param list[str] cc_email: Array of strings for CC email recipients (for email invitations).
        :param bool require_email: Requires a user to enter their email address to access. If set true, isPublic must also be set true.  Please note that emails are not validated; we simply log the email in the share activity.  If you want a share to be invite only (e.g. restricted access to only invited email addresses) you should set this to false, and pass the set of email addresses via the `emails` paramater. 
        :param bool embed: Allows user to embed a widget with the share.
        :param bool is_public: True if share has a public URL. If false, the only way to access the share will be via the personalized URL sent via the email invite process.
        :param str password: If not null, value of password is required to access this share.
        :param str expiration: The timestamp the current share should expire, formatted `YYYY-mm-dd hh:mm:ss`.
        :param bool has_notification: True if the user should be notified about activity on this share.
        :param list[str] notification_emails: An array of recipients who should receive notification emails.
        :param bool file_drop_create_folders: If true, all receive folder submissions will be uploaded separate folders (only applicable for the `receive` share type).
        :return: Response
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('callback'):
            return self.update_share_with_http_info(api_key, access_token, id, **kwargs)
        else:
            (data) = self.update_share_with_http_info(api_key, access_token, id, **kwargs)
            return data

    def update_share_with_http_info(self, api_key, access_token, id, **kwargs):
        """
        updateShare
        Update an existing share object by specified ID. Note that it is not possible to change the type of share once it has been created; if you need to (for example) convert a shared folder to a recieve folder, you must first delete the shared folder and then create a new recieve folder.  **Notes:** - Authenticated user's role must be admin or master, or the authenticated user must be the owner of the specified share. 
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.update_share_with_http_info(api_key, access_token, id, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str api_key: API key required to make the API call. (required)
        :param str access_token: Access token required to make the API call. (required)
        :param int id: ID of the share to update. Use <a href=\"#operation/getShares\">getShares</a> if you need to lookup an ID. (required)
        :param str name: Name of the share.
        :param list[str] file_paths: Array of strings containing the file paths to share.
        :param str access_mode: Type of permissions share recipients have.
        :param str subject: Share message subject (for email invitations).
        :param str message: Share message contents (for email invitations).
        :param list[str] emails: Array of strings for email recipients (for email invitations).
        :param list[str] cc_email: Array of strings for CC email recipients (for email invitations).
        :param bool require_email: Requires a user to enter their email address to access. If set true, isPublic must also be set true.  Please note that emails are not validated; we simply log the email in the share activity.  If you want a share to be invite only (e.g. restricted access to only invited email addresses) you should set this to false, and pass the set of email addresses via the `emails` paramater. 
        :param bool embed: Allows user to embed a widget with the share.
        :param bool is_public: True if share has a public URL. If false, the only way to access the share will be via the personalized URL sent via the email invite process.
        :param str password: If not null, value of password is required to access this share.
        :param str expiration: The timestamp the current share should expire, formatted `YYYY-mm-dd hh:mm:ss`.
        :param bool has_notification: True if the user should be notified about activity on this share.
        :param list[str] notification_emails: An array of recipients who should receive notification emails.
        :param bool file_drop_create_folders: If true, all receive folder submissions will be uploaded separate folders (only applicable for the `receive` share type).
        :return: Response
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['api_key', 'access_token', 'id', 'name', 'file_paths', 'access_mode', 'subject', 'message', 'emails', 'cc_email', 'require_email', 'embed', 'is_public', 'password', 'expiration', 'has_notification', 'notification_emails', 'file_drop_create_folders']
        all_params.append('callback')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method update_share" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'api_key' is set
        if ('api_key' not in params) or (params['api_key'] is None):
            raise ValueError("Missing the required parameter `api_key` when calling `update_share`")
        # verify the required parameter 'access_token' is set
        if ('access_token' not in params) or (params['access_token'] is None):
            raise ValueError("Missing the required parameter `access_token` when calling `update_share`")
        # verify the required parameter 'id' is set
        if ('id' not in params) or (params['id'] is None):
            raise ValueError("Missing the required parameter `id` when calling `update_share`")


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
        if 'id' in params:
            form_params.append(('id', params['id']))
        if 'name' in params:
            form_params.append(('name', params['name']))
        if 'file_paths' in params:
            form_params.append(('filePaths', params['file_paths']))
            collection_formats['filePaths'] = 'multi'
        if 'access_mode' in params:
            form_params.append(('accessMode', params['access_mode']))
        if 'subject' in params:
            form_params.append(('subject', params['subject']))
        if 'message' in params:
            form_params.append(('message', params['message']))
        if 'emails' in params:
            form_params.append(('emails', params['emails']))
            collection_formats['emails'] = 'multi'
        if 'cc_email' in params:
            form_params.append(('ccEmail', params['cc_email']))
            collection_formats['ccEmail'] = 'multi'
        if 'require_email' in params:
            form_params.append(('requireEmail', params['require_email']))
        if 'embed' in params:
            form_params.append(('embed', params['embed']))
        if 'is_public' in params:
            form_params.append(('isPublic', params['is_public']))
        if 'password' in params:
            form_params.append(('password', params['password']))
        if 'expiration' in params:
            form_params.append(('expiration', params['expiration']))
        if 'has_notification' in params:
            form_params.append(('hasNotification', params['has_notification']))
        if 'notification_emails' in params:
            form_params.append(('notificationEmails', params['notification_emails']))
            collection_formats['notificationEmails'] = 'multi'
        if 'file_drop_create_folders' in params:
            form_params.append(('fileDropCreateFolders', params['file_drop_create_folders']))

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.\
            select_header_accept(['application/json'])

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.\
            select_header_content_type(['application/x-www-form-urlencoded'])

        # Authentication setting
        auth_settings = []

        return self.api_client.call_api('/updateShare', 'POST',
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
