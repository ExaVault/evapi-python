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


class NotificationApi(object):
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

    def create_notification(self, api_key, access_token, type, path, action, usernames, send_email, **kwargs):
        """
        createNotification
        Create a new notification for the given path in the current account. Notifications can be sent via email or webhook. To enable email, pass an array of email addresses to the `emails` parameter of this call. To enable webhooks, setup the webhook callback URL in your account settings.   **Notes:** - Authenticated user requires notification permission. 
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.create_notification(api_key, access_token, type, path, action, usernames, send_email, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str api_key: API key required to make the API call. (required)
        :param str access_token: Access token required to make the API call. (required)
        :param str type: Type of resource you're setting the notification on. (required)
        :param str path: Full path of file/folder where the notification is set. (required)
        :param str action: Type of action to filter on. Notifications will only be fired for the given type of action. (required)
        :param list[str] usernames: Determines which users should trigger the notification. Either one of the values above, or an array of usernames. (required)
        :param bool send_email: Set to true if the user should be notified by email when the notification is triggered. (required)
        :param list[str] emails: Email addresses to send the notification to. If not specified, sends to the authenticated user.
        :return: NotificationResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('callback'):
            return self.create_notification_with_http_info(api_key, access_token, type, path, action, usernames, send_email, **kwargs)
        else:
            (data) = self.create_notification_with_http_info(api_key, access_token, type, path, action, usernames, send_email, **kwargs)
            return data

    def create_notification_with_http_info(self, api_key, access_token, type, path, action, usernames, send_email, **kwargs):
        """
        createNotification
        Create a new notification for the given path in the current account. Notifications can be sent via email or webhook. To enable email, pass an array of email addresses to the `emails` parameter of this call. To enable webhooks, setup the webhook callback URL in your account settings.   **Notes:** - Authenticated user requires notification permission. 
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.create_notification_with_http_info(api_key, access_token, type, path, action, usernames, send_email, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str api_key: API key required to make the API call. (required)
        :param str access_token: Access token required to make the API call. (required)
        :param str type: Type of resource you're setting the notification on. (required)
        :param str path: Full path of file/folder where the notification is set. (required)
        :param str action: Type of action to filter on. Notifications will only be fired for the given type of action. (required)
        :param list[str] usernames: Determines which users should trigger the notification. Either one of the values above, or an array of usernames. (required)
        :param bool send_email: Set to true if the user should be notified by email when the notification is triggered. (required)
        :param list[str] emails: Email addresses to send the notification to. If not specified, sends to the authenticated user.
        :return: NotificationResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['api_key', 'access_token', 'type', 'path', 'action', 'usernames', 'send_email', 'emails']
        all_params.append('callback')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method create_notification" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'api_key' is set
        if ('api_key' not in params) or (params['api_key'] is None):
            raise ValueError("Missing the required parameter `api_key` when calling `create_notification`")
        # verify the required parameter 'access_token' is set
        if ('access_token' not in params) or (params['access_token'] is None):
            raise ValueError("Missing the required parameter `access_token` when calling `create_notification`")
        # verify the required parameter 'type' is set
        if ('type' not in params) or (params['type'] is None):
            raise ValueError("Missing the required parameter `type` when calling `create_notification`")
        # verify the required parameter 'path' is set
        if ('path' not in params) or (params['path'] is None):
            raise ValueError("Missing the required parameter `path` when calling `create_notification`")
        # verify the required parameter 'action' is set
        if ('action' not in params) or (params['action'] is None):
            raise ValueError("Missing the required parameter `action` when calling `create_notification`")
        # verify the required parameter 'usernames' is set
        if ('usernames' not in params) or (params['usernames'] is None):
            raise ValueError("Missing the required parameter `usernames` when calling `create_notification`")
        # verify the required parameter 'send_email' is set
        if ('send_email' not in params) or (params['send_email'] is None):
            raise ValueError("Missing the required parameter `send_email` when calling `create_notification`")


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
        if 'path' in params:
            form_params.append(('path', params['path']))
        if 'action' in params:
            form_params.append(('action', params['action']))
        if 'usernames' in params:
            form_params.append(('usernames', params['usernames']))
            collection_formats['usernames'] = 'multi'
        if 'send_email' in params:
            form_params.append(('sendEmail', params['send_email']))
        if 'emails' in params:
            form_params.append(('emails', params['emails']))
            collection_formats['emails'] = 'multi'

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.\
            select_header_accept(['application/json'])

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.\
            select_header_content_type(['application/x-www-form-urlencoded'])

        # Authentication setting
        auth_settings = []

        return self.api_client.call_api('/createNotification', 'POST',
                                        path_params,
                                        query_params,
                                        header_params,
                                        body=body_params,
                                        post_params=form_params,
                                        files=local_var_files,
                                        response_type='NotificationResponse',
                                        auth_settings=auth_settings,
                                        callback=params.get('callback'),
                                        _return_http_data_only=params.get('_return_http_data_only'),
                                        _preload_content=params.get('_preload_content', True),
                                        _request_timeout=params.get('_request_timeout'),
                                        collection_formats=collection_formats)

    def delete_notification(self, api_key, access_token, id, **kwargs):
        """
        deleteNotification
        Deletes the specified notification. Note that deleting a notification _only_ deletes the notification &ndash; it does not delete any underlying files or folders. > **Notes:** - Authenticated usee requires notification permission.  - Authenticated user should be the owner of the specified notification. 
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.delete_notification(api_key, access_token, id, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str api_key: API key required to make the API call. (required)
        :param str access_token: Access token required to make the API call. (required)
        :param int id: ID of the notification to delete. Use <a href=\"#operation/getNotifications\">getNotifications</a> if you need to lookup an ID. (required)
        :return: Response
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('callback'):
            return self.delete_notification_with_http_info(api_key, access_token, id, **kwargs)
        else:
            (data) = self.delete_notification_with_http_info(api_key, access_token, id, **kwargs)
            return data

    def delete_notification_with_http_info(self, api_key, access_token, id, **kwargs):
        """
        deleteNotification
        Deletes the specified notification. Note that deleting a notification _only_ deletes the notification &ndash; it does not delete any underlying files or folders. > **Notes:** - Authenticated usee requires notification permission.  - Authenticated user should be the owner of the specified notification. 
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.delete_notification_with_http_info(api_key, access_token, id, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str api_key: API key required to make the API call. (required)
        :param str access_token: Access token required to make the API call. (required)
        :param int id: ID of the notification to delete. Use <a href=\"#operation/getNotifications\">getNotifications</a> if you need to lookup an ID. (required)
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
                    " to method delete_notification" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'api_key' is set
        if ('api_key' not in params) or (params['api_key'] is None):
            raise ValueError("Missing the required parameter `api_key` when calling `delete_notification`")
        # verify the required parameter 'access_token' is set
        if ('access_token' not in params) or (params['access_token'] is None):
            raise ValueError("Missing the required parameter `access_token` when calling `delete_notification`")
        # verify the required parameter 'id' is set
        if ('id' not in params) or (params['id'] is None):
            raise ValueError("Missing the required parameter `id` when calling `delete_notification`")


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

        return self.api_client.call_api('/deleteNotification', 'GET',
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

    def get_notification(self, api_key, access_token, id, **kwargs):
        """
        getNotification
        Returns the specified notification object.  **Notes:** - Authenticated user should be the owner of the specified notification 
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.get_notification(api_key, access_token, id, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str api_key: API key required to make the API call. (required)
        :param str access_token: Access token required to make the API call. (required)
        :param int id: ID of the notification. Use <a href=\"#operation/getNotifications\">getNotifications</a> if you need to lookup an ID. (required)
        :return: NotificationResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('callback'):
            return self.get_notification_with_http_info(api_key, access_token, id, **kwargs)
        else:
            (data) = self.get_notification_with_http_info(api_key, access_token, id, **kwargs)
            return data

    def get_notification_with_http_info(self, api_key, access_token, id, **kwargs):
        """
        getNotification
        Returns the specified notification object.  **Notes:** - Authenticated user should be the owner of the specified notification 
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.get_notification_with_http_info(api_key, access_token, id, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str api_key: API key required to make the API call. (required)
        :param str access_token: Access token required to make the API call. (required)
        :param int id: ID of the notification. Use <a href=\"#operation/getNotifications\">getNotifications</a> if you need to lookup an ID. (required)
        :return: NotificationResponse
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
                    " to method get_notification" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'api_key' is set
        if ('api_key' not in params) or (params['api_key'] is None):
            raise ValueError("Missing the required parameter `api_key` when calling `get_notification`")
        # verify the required parameter 'access_token' is set
        if ('access_token' not in params) or (params['access_token'] is None):
            raise ValueError("Missing the required parameter `access_token` when calling `get_notification`")
        # verify the required parameter 'id' is set
        if ('id' not in params) or (params['id'] is None):
            raise ValueError("Missing the required parameter `id` when calling `get_notification`")


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

        return self.api_client.call_api('/getNotification', 'GET',
                                        path_params,
                                        query_params,
                                        header_params,
                                        body=body_params,
                                        post_params=form_params,
                                        files=local_var_files,
                                        response_type='NotificationResponse',
                                        auth_settings=auth_settings,
                                        callback=params.get('callback'),
                                        _return_http_data_only=params.get('_return_http_data_only'),
                                        _preload_content=params.get('_preload_content', True),
                                        _request_timeout=params.get('_request_timeout'),
                                        collection_formats=collection_formats)

    def get_notifications(self, api_key, access_token, type, **kwargs):
        """
        getNotifications
        Returns array of all notification objects owned by the authenticated user. You can use sorting and filtering to limit the returned list.  **Notes:** - Autheticated user should have notification permission 
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.get_notifications(api_key, access_token, type, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str api_key: API key required to make the API call. (required)
        :param str access_token: Access token required to make the API call. (required)
        :param str type: Type of notification to filter on. (required)
        :param str sort_by: Sort method.
        :param str sort_order: Sort order.
        :param str filter: Filter by the provided search terms.
        :return: NotificationsResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('callback'):
            return self.get_notifications_with_http_info(api_key, access_token, type, **kwargs)
        else:
            (data) = self.get_notifications_with_http_info(api_key, access_token, type, **kwargs)
            return data

    def get_notifications_with_http_info(self, api_key, access_token, type, **kwargs):
        """
        getNotifications
        Returns array of all notification objects owned by the authenticated user. You can use sorting and filtering to limit the returned list.  **Notes:** - Autheticated user should have notification permission 
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.get_notifications_with_http_info(api_key, access_token, type, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str api_key: API key required to make the API call. (required)
        :param str access_token: Access token required to make the API call. (required)
        :param str type: Type of notification to filter on. (required)
        :param str sort_by: Sort method.
        :param str sort_order: Sort order.
        :param str filter: Filter by the provided search terms.
        :return: NotificationsResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['api_key', 'access_token', 'type', 'sort_by', 'sort_order', 'filter']
        all_params.append('callback')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_notifications" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'api_key' is set
        if ('api_key' not in params) or (params['api_key'] is None):
            raise ValueError("Missing the required parameter `api_key` when calling `get_notifications`")
        # verify the required parameter 'access_token' is set
        if ('access_token' not in params) or (params['access_token'] is None):
            raise ValueError("Missing the required parameter `access_token` when calling `get_notifications`")
        # verify the required parameter 'type' is set
        if ('type' not in params) or (params['type'] is None):
            raise ValueError("Missing the required parameter `type` when calling `get_notifications`")


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

        return self.api_client.call_api('/getNotifications', 'GET',
                                        path_params,
                                        query_params,
                                        header_params,
                                        body=body_params,
                                        post_params=form_params,
                                        files=local_var_files,
                                        response_type='NotificationsResponse',
                                        auth_settings=auth_settings,
                                        callback=params.get('callback'),
                                        _return_http_data_only=params.get('_return_http_data_only'),
                                        _preload_content=params.get('_preload_content', True),
                                        _request_timeout=params.get('_request_timeout'),
                                        collection_formats=collection_formats)

    def update_notification(self, api_key, **kwargs):
        """
        updateNotification
        Update an existing notification object.  **Notes:** - Authenticated user should have notification permission.  - Authenticated user should be the owner of the specified notification. 
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.update_notification(api_key, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str api_key: API key required to make the API call. (required)
        :param UpdateNotification update_notification:
        :return: Response
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('callback'):
            return self.update_notification_with_http_info(api_key, **kwargs)
        else:
            (data) = self.update_notification_with_http_info(api_key, **kwargs)
            return data

    def update_notification_with_http_info(self, api_key, **kwargs):
        """
        updateNotification
        Update an existing notification object.  **Notes:** - Authenticated user should have notification permission.  - Authenticated user should be the owner of the specified notification. 
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.update_notification_with_http_info(api_key, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str api_key: API key required to make the API call. (required)
        :param UpdateNotification update_notification:
        :return: Response
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['api_key', 'update_notification']
        all_params.append('callback')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method update_notification" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'api_key' is set
        if ('api_key' not in params) or (params['api_key'] is None):
            raise ValueError("Missing the required parameter `api_key` when calling `update_notification`")


        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}
        if 'api_key' in params:
            header_params['api_key'] = params['api_key']

        form_params = []
        local_var_files = {}

        body_params = None
        if 'update_notification' in params:
            body_params = params['update_notification']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.\
            select_header_accept(['application/json'])

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.\
            select_header_content_type(['application/x-www-form-urlencoded'])

        # Authentication setting
        auth_settings = []

        return self.api_client.call_api('/updateNotification', 'POST',
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
