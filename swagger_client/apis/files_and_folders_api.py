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


class FilesAndFoldersApi(object):
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

    def check_files_exist(self, api_key, access_token, file_paths, **kwargs):
        """
        checkFilesExist
        Check if any of the file/folder paths in the input array exist in your account. This is particularly useful if you are uploading files and want to present the user with a dialog asking them if they want to overwrite existing files, as the <a href=\"#operation/getUploadFileUrl\">getUploadFileUrl</a> call overwrites files by default.
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.check_files_exist(api_key, access_token, file_paths, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str api_key: API key required to make the API call. (required)
        :param str access_token: Access token required to make the API call. (required)
        :param list[str] file_paths: Array containing file/folder paths to check. (required)
        :return: ExistingResourcesResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('callback'):
            return self.check_files_exist_with_http_info(api_key, access_token, file_paths, **kwargs)
        else:
            (data) = self.check_files_exist_with_http_info(api_key, access_token, file_paths, **kwargs)
            return data

    def check_files_exist_with_http_info(self, api_key, access_token, file_paths, **kwargs):
        """
        checkFilesExist
        Check if any of the file/folder paths in the input array exist in your account. This is particularly useful if you are uploading files and want to present the user with a dialog asking them if they want to overwrite existing files, as the <a href=\"#operation/getUploadFileUrl\">getUploadFileUrl</a> call overwrites files by default.
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.check_files_exist_with_http_info(api_key, access_token, file_paths, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str api_key: API key required to make the API call. (required)
        :param str access_token: Access token required to make the API call. (required)
        :param list[str] file_paths: Array containing file/folder paths to check. (required)
        :return: ExistingResourcesResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['api_key', 'access_token', 'file_paths']
        all_params.append('callback')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method check_files_exist" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'api_key' is set
        if ('api_key' not in params) or (params['api_key'] is None):
            raise ValueError("Missing the required parameter `api_key` when calling `check_files_exist`")
        # verify the required parameter 'access_token' is set
        if ('access_token' not in params) or (params['access_token'] is None):
            raise ValueError("Missing the required parameter `access_token` when calling `check_files_exist`")
        # verify the required parameter 'file_paths' is set
        if ('file_paths' not in params) or (params['file_paths'] is None):
            raise ValueError("Missing the required parameter `file_paths` when calling `check_files_exist`")


        collection_formats = {}

        path_params = {}

        query_params = []
        if 'access_token' in params:
            query_params.append(('access_token', params['access_token']))
        if 'file_paths' in params:
            query_params.append(('filePaths[]', params['file_paths']))
            collection_formats['filePaths[]'] = 'multi'

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

        return self.api_client.call_api('/checkFilesExist', 'GET',
                                        path_params,
                                        query_params,
                                        header_params,
                                        body=body_params,
                                        post_params=form_params,
                                        files=local_var_files,
                                        response_type='ExistingResourcesResponse',
                                        auth_settings=auth_settings,
                                        callback=params.get('callback'),
                                        _return_http_data_only=params.get('_return_http_data_only'),
                                        _preload_content=params.get('_preload_content', True),
                                        _request_timeout=params.get('_request_timeout'),
                                        collection_formats=collection_formats)

    def copy_resources(self, api_key, access_token, file_paths, destination_path, **kwargs):
        """
        copyResources
        Copies a set of exisiting files/folders (provided by an array **filePaths**) to the requested **destinationPath** in your account. In the **filePaths** array, you may specify paths pointing files/folders throughout the account, but everything will be copied to the  root of the **destinationPath**.  **Notes:** - Authenticated user should have modify permission. 
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.copy_resources(api_key, access_token, file_paths, destination_path, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str api_key: API key required to make the API call. (required)
        :param str access_token: Access token required to make the API call. (required)
        :param list[str] file_paths: Array containing file/folder paths to copy. (required)
        :param str destination_path: Remote destination path to copy files/folders to. (required)
        :return: ModifiedResourcesResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('callback'):
            return self.copy_resources_with_http_info(api_key, access_token, file_paths, destination_path, **kwargs)
        else:
            (data) = self.copy_resources_with_http_info(api_key, access_token, file_paths, destination_path, **kwargs)
            return data

    def copy_resources_with_http_info(self, api_key, access_token, file_paths, destination_path, **kwargs):
        """
        copyResources
        Copies a set of exisiting files/folders (provided by an array **filePaths**) to the requested **destinationPath** in your account. In the **filePaths** array, you may specify paths pointing files/folders throughout the account, but everything will be copied to the  root of the **destinationPath**.  **Notes:** - Authenticated user should have modify permission. 
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.copy_resources_with_http_info(api_key, access_token, file_paths, destination_path, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str api_key: API key required to make the API call. (required)
        :param str access_token: Access token required to make the API call. (required)
        :param list[str] file_paths: Array containing file/folder paths to copy. (required)
        :param str destination_path: Remote destination path to copy files/folders to. (required)
        :return: ModifiedResourcesResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['api_key', 'access_token', 'file_paths', 'destination_path']
        all_params.append('callback')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method copy_resources" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'api_key' is set
        if ('api_key' not in params) or (params['api_key'] is None):
            raise ValueError("Missing the required parameter `api_key` when calling `copy_resources`")
        # verify the required parameter 'access_token' is set
        if ('access_token' not in params) or (params['access_token'] is None):
            raise ValueError("Missing the required parameter `access_token` when calling `copy_resources`")
        # verify the required parameter 'file_paths' is set
        if ('file_paths' not in params) or (params['file_paths'] is None):
            raise ValueError("Missing the required parameter `file_paths` when calling `copy_resources`")
        # verify the required parameter 'destination_path' is set
        if ('destination_path' not in params) or (params['destination_path'] is None):
            raise ValueError("Missing the required parameter `destination_path` when calling `copy_resources`")


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
        if 'file_paths' in params:
            # EV add [] to filePath 
            form_params.append(('filePaths[]', params['file_paths']))
            collection_formats['filePaths[]'] = 'multi'
        if 'destination_path' in params:
            form_params.append(('destinationPath', params['destination_path']))

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.\
            select_header_accept(['application/json'])

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.\
            select_header_content_type(['application/x-www-form-urlencoded'])

        # Authentication setting
        auth_settings = []

        return self.api_client.call_api('/copyResources', 'POST',
                                        path_params,
                                        query_params,
                                        header_params,
                                        body=body_params,
                                        post_params=form_params,
                                        files=local_var_files,
                                        response_type='ModifiedResourcesResponse',
                                        auth_settings=auth_settings,
                                        callback=params.get('callback'),
                                        _return_http_data_only=params.get('_return_http_data_only'),
                                        _preload_content=params.get('_preload_content', True),
                                        _request_timeout=params.get('_request_timeout'),
                                        collection_formats=collection_formats)

    def create_folder(self, api_key, access_token, folder_name, path, **kwargs):
        """
        createFolder
        Create a new folder at the specified path. > **Notes:** - Authenticated user should have modify permission. 
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.create_folder(api_key, access_token, folder_name, path, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str api_key: API key required to make the API call. (required)
        :param str access_token: Access token required to make the API call. (required)
        :param str folder_name: Name of the folder to create. (required)
        :param str path: Where to create the folder. Use **/** to create a folder in the user's home directory. (required)
        :return: Response
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('callback'):
            return self.create_folder_with_http_info(api_key, access_token, folder_name, path, **kwargs)
        else:
            (data) = self.create_folder_with_http_info(api_key, access_token, folder_name, path, **kwargs)
            return data

    def create_folder_with_http_info(self, api_key, access_token, folder_name, path, **kwargs):
        """
        createFolder
        Create a new folder at the specified path. > **Notes:** - Authenticated user should have modify permission. 
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.create_folder_with_http_info(api_key, access_token, folder_name, path, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str api_key: API key required to make the API call. (required)
        :param str access_token: Access token required to make the API call. (required)
        :param str folder_name: Name of the folder to create. (required)
        :param str path: Where to create the folder. Use **/** to create a folder in the user's home directory. (required)
        :return: Response
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['api_key', 'access_token', 'folder_name', 'path']
        all_params.append('callback')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method create_folder" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'api_key' is set
        if ('api_key' not in params) or (params['api_key'] is None):
            raise ValueError("Missing the required parameter `api_key` when calling `create_folder`")
        # verify the required parameter 'access_token' is set
        if ('access_token' not in params) or (params['access_token'] is None):
            raise ValueError("Missing the required parameter `access_token` when calling `create_folder`")
        # verify the required parameter 'folder_name' is set
        if ('folder_name' not in params) or (params['folder_name'] is None):
            raise ValueError("Missing the required parameter `folder_name` when calling `create_folder`")
        # verify the required parameter 'path' is set
        if ('path' not in params) or (params['path'] is None):
            raise ValueError("Missing the required parameter `path` when calling `create_folder`")


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
        if 'folder_name' in params:
            form_params.append(('folderName', params['folder_name']))
        if 'path' in params:
            form_params.append(('path', params['path']))

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.\
            select_header_accept(['application/json'])

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.\
            select_header_content_type(['application/x-www-form-urlencoded'])

        # Authentication setting
        auth_settings = []

        return self.api_client.call_api('/createFolder', 'POST',
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

    def delete_resources(self, api_key, access_token, file_paths, **kwargs):
        """
        deleteResources
        Delete the files/folders located at a given set of paths. Note that this call performs the delete **immediately**, and it is irreversible. We strongly recommend that you confirm your user's intention to delete file(s) before issuing this API call.  **Notes:** - Authenticated user should have delete permission. 
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.delete_resources(api_key, access_token, file_paths, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str api_key: API key required to make the API call. (required)
        :param str access_token: Access token required to make the API call. (required)
        :param list[str] file_paths: Array containing paths of the files or folder to delete. (required)
        :return: DeletedResourcesResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('callback'):
            return self.delete_resources_with_http_info(api_key, access_token, file_paths, **kwargs)
        else:
            (data) = self.delete_resources_with_http_info(api_key, access_token, file_paths, **kwargs)
            return data

    def delete_resources_with_http_info(self, api_key, access_token, file_paths, **kwargs):
        """
        deleteResources
        Delete the files/folders located at a given set of paths. Note that this call performs the delete **immediately**, and it is irreversible. We strongly recommend that you confirm your user's intention to delete file(s) before issuing this API call.  **Notes:** - Authenticated user should have delete permission. 
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.delete_resources_with_http_info(api_key, access_token, file_paths, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str api_key: API key required to make the API call. (required)
        :param str access_token: Access token required to make the API call. (required)
        :param list[str] file_paths: Array containing paths of the files or folder to delete. (required)
        :return: DeletedResourcesResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['api_key', 'access_token', 'file_paths']
        all_params.append('callback')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method delete_resources" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'api_key' is set
        if ('api_key' not in params) or (params['api_key'] is None):
            raise ValueError("Missing the required parameter `api_key` when calling `delete_resources`")
        # verify the required parameter 'access_token' is set
        if ('access_token' not in params) or (params['access_token'] is None):
            raise ValueError("Missing the required parameter `access_token` when calling `delete_resources`")
        # verify the required parameter 'file_paths' is set
        if ('file_paths' not in params) or (params['file_paths'] is None):
            raise ValueError("Missing the required parameter `file_paths` when calling `delete_resources`")


        collection_formats = {}

        path_params = {}

        query_params = []
        if 'access_token' in params:
            query_params.append(('access_token', params['access_token']))
        if 'file_paths' in params:
            query_params.append(('filePaths[]', params['file_paths']))
            collection_formats['filePaths[]'] = 'multi'

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

        return self.api_client.call_api('/deleteResources', 'GET',
                                        path_params,
                                        query_params,
                                        header_params,
                                        body=body_params,
                                        post_params=form_params,
                                        files=local_var_files,
                                        response_type='DeletedResourcesResponse',
                                        auth_settings=auth_settings,
                                        callback=params.get('callback'),
                                        _return_http_data_only=params.get('_return_http_data_only'),
                                        _preload_content=params.get('_preload_content', True),
                                        _request_timeout=params.get('_request_timeout'),
                                        collection_formats=collection_formats)

    def get_download_file_url(self, api_key, access_token, file_paths, **kwargs):
        """
        getDownloadFileUrl
        Returns an unique URL for a file download.  To download a file from ExaVault, you first request a download URL from our API using this API call. You then make an HTTP GET request to get the actual file contents using the download URL. The download URL will contain a link to an ExaVault storage server where the file is located, and a unique access token &ndash; valid for only one use and thirty (30) seconds &ndash; which allows you to download the file.  **Notes:** - Authenticated user should have download permission. 
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.get_download_file_url(api_key, access_token, file_paths, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str api_key: API key required to make the API call. (required)
        :param str access_token: Access token required to make the API call. (required)
        :param str file_paths: Path of file to be downloaded. (required)
        :param str download_name: The name of the file to be downloaded.
        :return: UrlResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('callback'):
            return self.get_download_file_url_with_http_info(api_key, access_token, file_paths, **kwargs)
        else:
            (data) = self.get_download_file_url_with_http_info(api_key, access_token, file_paths, **kwargs)
            return data

    def get_download_file_url_with_http_info(self, api_key, access_token, file_paths, **kwargs):
        """
        getDownloadFileUrl
        Returns an unique URL for a file download.  To download a file from ExaVault, you first request a download URL from our API using this API call. You then make an HTTP GET request to get the actual file contents using the download URL. The download URL will contain a link to an ExaVault storage server where the file is located, and a unique access token &ndash; valid for only one use and thirty (30) seconds &ndash; which allows you to download the file.  **Notes:** - Authenticated user should have download permission. 
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.get_download_file_url_with_http_info(api_key, access_token, file_paths, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str api_key: API key required to make the API call. (required)
        :param str access_token: Access token required to make the API call. (required)
        :param str file_paths: Path of file to be downloaded. (required)
        :param str download_name: The name of the file to be downloaded.
        :return: UrlResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['api_key', 'access_token', 'file_paths', 'download_name']
        all_params.append('callback')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_download_file_url" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'api_key' is set
        if ('api_key' not in params) or (params['api_key'] is None):
            raise ValueError("Missing the required parameter `api_key` when calling `get_download_file_url`")
        # verify the required parameter 'access_token' is set
        if ('access_token' not in params) or (params['access_token'] is None):
            raise ValueError("Missing the required parameter `access_token` when calling `get_download_file_url`")
        # verify the required parameter 'file_paths' is set
        if ('file_paths' not in params) or (params['file_paths'] is None):
            raise ValueError("Missing the required parameter `file_paths` when calling `get_download_file_url`")


        collection_formats = {}

        path_params = {}

        query_params = []
        if 'access_token' in params:
            query_params.append(('access_token', params['access_token']))
        if 'file_paths' in params:
            query_params.append(('filePaths', params['file_paths']))
        if 'download_name' in params:
            query_params.append(('downloadName', params['download_name']))

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

        return self.api_client.call_api('/getDownloadFileUrl', 'GET',
                                        path_params,
                                        query_params,
                                        header_params,
                                        body=body_params,
                                        post_params=form_params,
                                        files=local_var_files,
                                        response_type='UrlResponse',
                                        auth_settings=auth_settings,
                                        callback=params.get('callback'),
                                        _return_http_data_only=params.get('_return_http_data_only'),
                                        _preload_content=params.get('_preload_content', True),
                                        _request_timeout=params.get('_request_timeout'),
                                        collection_formats=collection_formats)

    def get_folders(self, api_key, access_token, path, **kwargs):
        """
        getFolders
        Gets the list of folder objects for a specified path. This is similar to <a href=\"#operation/getResourceList\">getResourceList</a>, but returns only folders and is simpler and more perfomrant if you only need to get a list of folders at a given path. > **Notes:** - Authenticated user should have list permission. 
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.get_folders(api_key, access_token, path, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str api_key: API key required to make the API call. (required)
        :param str access_token: Access token required to make the API call. (required)
        :param str path: Path to get folders for. (required)
        :return: ResourcePropertiesResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('callback'):
            return self.get_folders_with_http_info(api_key, access_token, path, **kwargs)
        else:
            (data) = self.get_folders_with_http_info(api_key, access_token, path, **kwargs)
            return data

    def get_folders_with_http_info(self, api_key, access_token, path, **kwargs):
        """
        getFolders
        Gets the list of folder objects for a specified path. This is similar to <a href=\"#operation/getResourceList\">getResourceList</a>, but returns only folders and is simpler and more perfomrant if you only need to get a list of folders at a given path. > **Notes:** - Authenticated user should have list permission. 
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.get_folders_with_http_info(api_key, access_token, path, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str api_key: API key required to make the API call. (required)
        :param str access_token: Access token required to make the API call. (required)
        :param str path: Path to get folders for. (required)
        :return: ResourcePropertiesResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['api_key', 'access_token', 'path']
        all_params.append('callback')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_folders" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'api_key' is set
        if ('api_key' not in params) or (params['api_key'] is None):
            raise ValueError("Missing the required parameter `api_key` when calling `get_folders`")
        # verify the required parameter 'access_token' is set
        if ('access_token' not in params) or (params['access_token'] is None):
            raise ValueError("Missing the required parameter `access_token` when calling `get_folders`")
        # verify the required parameter 'path' is set
        if ('path' not in params) or (params['path'] is None):
            raise ValueError("Missing the required parameter `path` when calling `get_folders`")


        collection_formats = {}

        path_params = {}

        query_params = []
        if 'access_token' in params:
            query_params.append(('access_token', params['access_token']))
        if 'path' in params:
            query_params.append(('path', params['path']))

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

        return self.api_client.call_api('/getFolders', 'GET',
                                        path_params,
                                        query_params,
                                        header_params,
                                        body=body_params,
                                        post_params=form_params,
                                        files=local_var_files,
                                        response_type='ResourcePropertiesResponse',
                                        auth_settings=auth_settings,
                                        callback=params.get('callback'),
                                        _return_http_data_only=params.get('_return_http_data_only'),
                                        _preload_content=params.get('_preload_content', True),
                                        _request_timeout=params.get('_request_timeout'),
                                        collection_formats=collection_formats)

    def get_resource_list(self, api_key, access_token, path, **kwargs):
        """
        getResourceList
        Get a listing of files/folders for the specified path.   You can use this API call to get information about all files and folders at a specified path. By default, the API returns basic metadata on each file/folder. An optional 'detailed' parameter forces the return of additional metadata. As with all API calls, the path should be the full path relative to the user's home directory (e.g. `/myfiles/some_folder`).  **Notes:** - Authenticated user should have list permission. 
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.get_resource_list(api_key, access_token, path, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str api_key: API key required to make the API call. (required)
        :param str access_token: Access token required to make the API call. (required)
        :param str path: Path to get listing of resources for. (required)
        :param str sort_by: Sort method. Use in conjunction with **sort_order**, below.
        :param str sort_order: Sort order.
        :param int offset: Determines which item to start on for pagination. Use zero (0) to start at the beginning of the list.
        :param int limit: The number of files to limit the result. Cannot be set higher than 100. If you have more than one hundred files in your directory, make multiple calls to **getResourceList**, incrementing the **offset** parameter, above.
        :param bool detailed: If true, returns sharedFolder, notifications or other objects associated with specified path. You should only set this paramter to true if you need the additional details, as the API call is less perfomant when it is enabled.
        :param str pattern: Regex string. If not null, perform a search with specified pattern.
        :return: ResourceResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('callback'):
            return self.get_resource_list_with_http_info(api_key, access_token, path, **kwargs)
        else:
            (data) = self.get_resource_list_with_http_info(api_key, access_token, path, **kwargs)
            return data

    def get_resource_list_with_http_info(self, api_key, access_token, path, **kwargs):
        """
        getResourceList
        Get a listing of files/folders for the specified path.   You can use this API call to get information about all files and folders at a specified path. By default, the API returns basic metadata on each file/folder. An optional 'detailed' parameter forces the return of additional metadata. As with all API calls, the path should be the full path relative to the user's home directory (e.g. `/myfiles/some_folder`).  **Notes:** - Authenticated user should have list permission. 
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.get_resource_list_with_http_info(api_key, access_token, path, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str api_key: API key required to make the API call. (required)
        :param str access_token: Access token required to make the API call. (required)
        :param str path: Path to get listing of resources for. (required)
        :param str sort_by: Sort method. Use in conjunction with **sort_order**, below.
        :param str sort_order: Sort order.
        :param int offset: Determines which item to start on for pagination. Use zero (0) to start at the beginning of the list.
        :param int limit: The number of files to limit the result. Cannot be set higher than 100. If you have more than one hundred files in your directory, make multiple calls to **getResourceList**, incrementing the **offset** parameter, above.
        :param bool detailed: If true, returns sharedFolder, notifications or other objects associated with specified path. You should only set this paramter to true if you need the additional details, as the API call is less perfomant when it is enabled.
        :param str pattern: Regex string. If not null, perform a search with specified pattern.
        :return: ResourceResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['api_key', 'access_token', 'path', 'sort_by', 'sort_order', 'offset', 'limit', 'detailed', 'pattern']
        all_params.append('callback')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_resource_list" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'api_key' is set
        if ('api_key' not in params) or (params['api_key'] is None):
            raise ValueError("Missing the required parameter `api_key` when calling `get_resource_list`")
        # verify the required parameter 'access_token' is set
        if ('access_token' not in params) or (params['access_token'] is None):
            raise ValueError("Missing the required parameter `access_token` when calling `get_resource_list`")
        # verify the required parameter 'path' is set
        if ('path' not in params) or (params['path'] is None):
            raise ValueError("Missing the required parameter `path` when calling `get_resource_list`")


        collection_formats = {}

        path_params = {}

        query_params = []
        if 'access_token' in params:
            query_params.append(('access_token', params['access_token']))
        if 'path' in params:
            query_params.append(('path', params['path']))
        if 'sort_by' in params:
            query_params.append(('sortBy', params['sort_by']))
        if 'sort_order' in params:
            query_params.append(('sortOrder', params['sort_order']))
        if 'offset' in params:
            query_params.append(('offset', params['offset']))
        if 'limit' in params:
            query_params.append(('limit', params['limit']))
        if 'detailed' in params:
            query_params.append(('detailed', params['detailed']))
        if 'pattern' in params:
            query_params.append(('pattern', params['pattern']))

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

        return self.api_client.call_api('/getResourceList', 'GET',
                                        path_params,
                                        query_params,
                                        header_params,
                                        body=body_params,
                                        post_params=form_params,
                                        files=local_var_files,
                                        response_type='ResourceResponse',
                                        auth_settings=auth_settings,
                                        callback=params.get('callback'),
                                        _return_http_data_only=params.get('_return_http_data_only'),
                                        _preload_content=params.get('_preload_content', True),
                                        _request_timeout=params.get('_request_timeout'),
                                        collection_formats=collection_formats)

    def get_resource_properties(self, api_key, access_token, file_paths, **kwargs):
        """
        getResourceProperties
        Gets metadata for each of the specified file/folder paths, including things like upload date, size and type. For the full list of returned properties, see the response syntax, below. > **Notes:** - Authenticated user should have list permission. 
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.get_resource_properties(api_key, access_token, file_paths, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str api_key: API key required to make the API call. (required)
        :param str access_token: Access token required to make the API call. (required)
        :param list[str] file_paths: Array containing paths of the files or folder to get metadata for. (required)
        :return: ResourcePropertiesResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('callback'):
            return self.get_resource_properties_with_http_info(api_key, access_token, file_paths, **kwargs)
        else:
            (data) = self.get_resource_properties_with_http_info(api_key, access_token, file_paths, **kwargs)
            return data

    def get_resource_properties_with_http_info(self, api_key, access_token, file_paths, **kwargs):
        """
        getResourceProperties
        Gets metadata for each of the specified file/folder paths, including things like upload date, size and type. For the full list of returned properties, see the response syntax, below. > **Notes:** - Authenticated user should have list permission. 
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.get_resource_properties_with_http_info(api_key, access_token, file_paths, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str api_key: API key required to make the API call. (required)
        :param str access_token: Access token required to make the API call. (required)
        :param list[str] file_paths: Array containing paths of the files or folder to get metadata for. (required)
        :return: ResourcePropertiesResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['api_key', 'access_token', 'file_paths']
        all_params.append('callback')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_resource_properties" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'api_key' is set
        if ('api_key' not in params) or (params['api_key'] is None):
            raise ValueError("Missing the required parameter `api_key` when calling `get_resource_properties`")
        # verify the required parameter 'access_token' is set
        if ('access_token' not in params) or (params['access_token'] is None):
            raise ValueError("Missing the required parameter `access_token` when calling `get_resource_properties`")
        # verify the required parameter 'file_paths' is set
        if ('file_paths' not in params) or (params['file_paths'] is None):
            raise ValueError("Missing the required parameter `file_paths` when calling `get_resource_properties`")


        collection_formats = {}

        path_params = {}

        query_params = []
        if 'access_token' in params:
            query_params.append(('access_token', params['access_token']))
        if 'file_paths' in params:
            query_params.append(('filePaths[]', params['file_paths']))
            collection_formats['filePaths[]'] = 'multi'

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

        return self.api_client.call_api('/getResourceProperties', 'GET',
                                        path_params,
                                        query_params,
                                        header_params,
                                        body=body_params,
                                        post_params=form_params,
                                        files=local_var_files,
                                        response_type='ResourcePropertiesResponse',
                                        auth_settings=auth_settings,
                                        callback=params.get('callback'),
                                        _return_http_data_only=params.get('_return_http_data_only'),
                                        _preload_content=params.get('_preload_content', True),
                                        _request_timeout=params.get('_request_timeout'),
                                        collection_formats=collection_formats)

    def get_upload_file_url(self, api_key, access_token, file_size, destination_path, **kwargs):
        """
        getUploadFileUrl
        Returns an unique URL for handling file uploads.  To upload a file to ExaVault, you first request an upload URL from our API using this API call. You then make an HTTP POST request to that url to put the file on the server. The upload URL will contain a link to an ExaVault storage server where the file can be stored, and a unique access token &ndash; valid for only one use and thirty (30) seconds &ndash; which allows you to upload the file.  **Notes:** - Authenticated user should have upload premission. 
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.get_upload_file_url(api_key, access_token, file_size, destination_path, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str api_key: API key required to make the API call. (required)
        :param str access_token: Access token required to make the API call. (required)
        :param int file_size: Size of the file to upload, in bytes. (required)
        :param str destination_path: Path relative to account's home directory, including file name. (required)
        :param bool allow_overwrite: True if the file should be overwritten, false if different file names should be generated. Call <a href=\"#operation/checkFilesExist\">checkFilesExist</a> first if you need to determine whether or not a file with the same name already exists. 
        :param bool resume: True if upload resume is supported, false if it isn't.
        :return: UrlResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('callback'):
            return self.get_upload_file_url_with_http_info(api_key, access_token, file_size, destination_path, **kwargs)
        else:
            (data) = self.get_upload_file_url_with_http_info(api_key, access_token, file_size, destination_path, **kwargs)
            return data

    def get_upload_file_url_with_http_info(self, api_key, access_token, file_size, destination_path, **kwargs):
        """
        getUploadFileUrl
        Returns an unique URL for handling file uploads.  To upload a file to ExaVault, you first request an upload URL from our API using this API call. You then make an HTTP POST request to that url to put the file on the server. The upload URL will contain a link to an ExaVault storage server where the file can be stored, and a unique access token &ndash; valid for only one use and thirty (30) seconds &ndash; which allows you to upload the file.  **Notes:** - Authenticated user should have upload premission. 
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.get_upload_file_url_with_http_info(api_key, access_token, file_size, destination_path, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str api_key: API key required to make the API call. (required)
        :param str access_token: Access token required to make the API call. (required)
        :param int file_size: Size of the file to upload, in bytes. (required)
        :param str destination_path: Path relative to account's home directory, including file name. (required)
        :param bool allow_overwrite: True if the file should be overwritten, false if different file names should be generated. Call <a href=\"#operation/checkFilesExist\">checkFilesExist</a> first if you need to determine whether or not a file with the same name already exists. 
        :param bool resume: True if upload resume is supported, false if it isn't.
        :return: UrlResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['api_key', 'access_token', 'file_size', 'destination_path', 'allow_overwrite', 'resume']
        all_params.append('callback')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_upload_file_url" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'api_key' is set
        if ('api_key' not in params) or (params['api_key'] is None):
            raise ValueError("Missing the required parameter `api_key` when calling `get_upload_file_url`")
        # verify the required parameter 'access_token' is set
        if ('access_token' not in params) or (params['access_token'] is None):
            raise ValueError("Missing the required parameter `access_token` when calling `get_upload_file_url`")
        # verify the required parameter 'file_size' is set
        if ('file_size' not in params) or (params['file_size'] is None):
            raise ValueError("Missing the required parameter `file_size` when calling `get_upload_file_url`")
        # verify the required parameter 'destination_path' is set
        if ('destination_path' not in params) or (params['destination_path'] is None):
            raise ValueError("Missing the required parameter `destination_path` when calling `get_upload_file_url`")


        collection_formats = {}

        path_params = {}

        query_params = []
        if 'access_token' in params:
            query_params.append(('access_token', params['access_token']))
        if 'file_size' in params:
            query_params.append(('fileSize', params['file_size']))
        if 'destination_path' in params:
            query_params.append(('destinationPath', params['destination_path']))
        if 'allow_overwrite' in params:
            query_params.append(('allowOverwrite', params['allow_overwrite']))
        if 'resume' in params:
            query_params.append(('resume', params['resume']))

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

        return self.api_client.call_api('/getUploadFileUrl', 'GET',
                                        path_params,
                                        query_params,
                                        header_params,
                                        body=body_params,
                                        post_params=form_params,
                                        files=local_var_files,
                                        response_type='UrlResponse',
                                        auth_settings=auth_settings,
                                        callback=params.get('callback'),
                                        _return_http_data_only=params.get('_return_http_data_only'),
                                        _preload_content=params.get('_preload_content', True),
                                        _request_timeout=params.get('_request_timeout'),
                                        collection_formats=collection_formats)

    def move_resources(self, api_key, access_token, file_paths, destination_path, **kwargs):
        """
        moveResources
        Moves a set of exisiting files/folders (provided by an array **filePaths**) to the requested **destinationPath** in your account. In the **filePaths** array, you may specify paths pointing files/folders throughout the account, but everything will be moved to the  root of the **destinationPath**.  **Notes:** - Authenticated user should have modify permission. 
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.move_resources(api_key, access_token, file_paths, destination_path, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str api_key: API key required to make the API call. (required)
        :param str access_token: Access token required to make the API call. (required)
        :param list[str] file_paths: Array containing file/folder paths to move. (required)
        :param str destination_path: Remote destination path to move files/folders to. (required)
        :return: ModifiedResourcesResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('callback'):
            return self.move_resources_with_http_info(api_key, access_token, file_paths, destination_path, **kwargs)
        else:
            (data) = self.move_resources_with_http_info(api_key, access_token, file_paths, destination_path, **kwargs)
            return data

    def move_resources_with_http_info(self, api_key, access_token, file_paths, destination_path, **kwargs):
        """
        moveResources
        Moves a set of exisiting files/folders (provided by an array **filePaths**) to the requested **destinationPath** in your account. In the **filePaths** array, you may specify paths pointing files/folders throughout the account, but everything will be moved to the  root of the **destinationPath**.  **Notes:** - Authenticated user should have modify permission. 
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.move_resources_with_http_info(api_key, access_token, file_paths, destination_path, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str api_key: API key required to make the API call. (required)
        :param str access_token: Access token required to make the API call. (required)
        :param list[str] file_paths: Array containing file/folder paths to move. (required)
        :param str destination_path: Remote destination path to move files/folders to. (required)
        :return: ModifiedResourcesResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['api_key', 'access_token', 'file_paths', 'destination_path']
        all_params.append('callback')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method move_resources" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'api_key' is set
        if ('api_key' not in params) or (params['api_key'] is None):
            raise ValueError("Missing the required parameter `api_key` when calling `move_resources`")
        # verify the required parameter 'access_token' is set
        if ('access_token' not in params) or (params['access_token'] is None):
            raise ValueError("Missing the required parameter `access_token` when calling `move_resources`")
        # verify the required parameter 'file_paths' is set
        if ('file_paths' not in params) or (params['file_paths'] is None):
            raise ValueError("Missing the required parameter `file_paths` when calling `move_resources`")
        # verify the required parameter 'destination_path' is set
        if ('destination_path' not in params) or (params['destination_path'] is None):
            raise ValueError("Missing the required parameter `destination_path` when calling `move_resources`")


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
        if 'file_paths' in params:
            # EV add [] to filePath
            form_params.append(('filePaths[]', params['file_paths']))
            collection_formats['filePaths[]'] = 'multi'
        if 'destination_path' in params:
            form_params.append(('destinationPath', params['destination_path']))

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.\
            select_header_accept(['application/json'])

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.\
            select_header_content_type(['application/x-www-form-urlencoded'])

        # Authentication setting
        auth_settings = []

        return self.api_client.call_api('/moveResources', 'POST',
                                        path_params,
                                        query_params,
                                        header_params,
                                        body=body_params,
                                        post_params=form_params,
                                        files=local_var_files,
                                        response_type='ModifiedResourcesResponse',
                                        auth_settings=auth_settings,
                                        callback=params.get('callback'),
                                        _return_http_data_only=params.get('_return_http_data_only'),
                                        _preload_content=params.get('_preload_content', True),
                                        _request_timeout=params.get('_request_timeout'),
                                        collection_formats=collection_formats)

    def preview_file(self, api_key, access_token, path, size, **kwargs):
        """
        previewFile
        Returns a resized image of the specified document for supported file types.  Image data returned is encoded in base64 format and can be viewed using the `<img>` element.   ```<img src='data:image/jpeg;base64' + results.image/>```  **Notes:** - Supported files types are `'jpg'`, `'jpeg'`, `'gif'`, `'png'`, `'bmp'`, `'pdf'`, `'psd'`, `'doc'` 
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.preview_file(api_key, access_token, path, size, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str api_key: API key required to make the API call. (required)
        :param str access_token: Access token required to make the API call. (required)
        :param str path: Path of the image relative to the user's home directory. (required)
        :param str size: The size of the image. (required)
        :param int width: Overrides sizes. Sets to a specific width.
        :param int height: Overrides sizes. Sets to a specific height.
        :param int page: Page number for the `.pdf` or `.doc` files.
        :return: PreviewFileResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('callback'):
            return self.preview_file_with_http_info(api_key, access_token, path, size, **kwargs)
        else:
            (data) = self.preview_file_with_http_info(api_key, access_token, path, size, **kwargs)
            return data

    def preview_file_with_http_info(self, api_key, access_token, path, size, **kwargs):
        """
        previewFile
        Returns a resized image of the specified document for supported file types.  Image data returned is encoded in base64 format and can be viewed using the `<img>` element.   ```<img src='data:image/jpeg;base64' + results.image/>```  **Notes:** - Supported files types are `'jpg'`, `'jpeg'`, `'gif'`, `'png'`, `'bmp'`, `'pdf'`, `'psd'`, `'doc'` 
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.preview_file_with_http_info(api_key, access_token, path, size, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str api_key: API key required to make the API call. (required)
        :param str access_token: Access token required to make the API call. (required)
        :param str path: Path of the image relative to the user's home directory. (required)
        :param str size: The size of the image. (required)
        :param int width: Overrides sizes. Sets to a specific width.
        :param int height: Overrides sizes. Sets to a specific height.
        :param int page: Page number for the `.pdf` or `.doc` files.
        :return: PreviewFileResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['api_key', 'access_token', 'path', 'size', 'width', 'height', 'page']
        all_params.append('callback')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method preview_file" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'api_key' is set
        if ('api_key' not in params) or (params['api_key'] is None):
            raise ValueError("Missing the required parameter `api_key` when calling `preview_file`")
        # verify the required parameter 'access_token' is set
        if ('access_token' not in params) or (params['access_token'] is None):
            raise ValueError("Missing the required parameter `access_token` when calling `preview_file`")
        # verify the required parameter 'path' is set
        if ('path' not in params) or (params['path'] is None):
            raise ValueError("Missing the required parameter `path` when calling `preview_file`")
        # verify the required parameter 'size' is set
        if ('size' not in params) or (params['size'] is None):
            raise ValueError("Missing the required parameter `size` when calling `preview_file`")


        collection_formats = {}

        path_params = {}

        query_params = []
        if 'access_token' in params:
            query_params.append(('access_token', params['access_token']))
        if 'path' in params:
            query_params.append(('path', params['path']))
        if 'size' in params:
            query_params.append(('size', params['size']))
        if 'width' in params:
            query_params.append(('width', params['width']))
        if 'height' in params:
            query_params.append(('height', params['height']))
        if 'page' in params:
            query_params.append(('page', params['page']))

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

        return self.api_client.call_api('/previewFile', 'GET',
                                        path_params,
                                        query_params,
                                        header_params,
                                        body=body_params,
                                        post_params=form_params,
                                        files=local_var_files,
                                        response_type='PreviewFileResponse',
                                        auth_settings=auth_settings,
                                        callback=params.get('callback'),
                                        _return_http_data_only=params.get('_return_http_data_only'),
                                        _preload_content=params.get('_preload_content', True),
                                        _request_timeout=params.get('_request_timeout'),
                                        collection_formats=collection_formats)

    def rename_resource(self, api_key, access_token, file_path, new_name, **kwargs):
        """
        renameResource
        Rename a file or folder at the specified path. > **Notes:** - Authenticated user should have modify permission. 
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.rename_resource(api_key, access_token, file_path, new_name, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str api_key: API key required to make the API call. (required)
        :param str access_token: Access token required to make the API call. (required)
        :param str file_path: Remote path of the file or folder to rename. (required)
        :param str new_name: The new name of the file or folder. (required)
        :return: Response
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('callback'):
            return self.rename_resource_with_http_info(api_key, access_token, file_path, new_name, **kwargs)
        else:
            (data) = self.rename_resource_with_http_info(api_key, access_token, file_path, new_name, **kwargs)
            return data

    def rename_resource_with_http_info(self, api_key, access_token, file_path, new_name, **kwargs):
        """
        renameResource
        Rename a file or folder at the specified path. > **Notes:** - Authenticated user should have modify permission. 
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.rename_resource_with_http_info(api_key, access_token, file_path, new_name, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str api_key: API key required to make the API call. (required)
        :param str access_token: Access token required to make the API call. (required)
        :param str file_path: Remote path of the file or folder to rename. (required)
        :param str new_name: The new name of the file or folder. (required)
        :return: Response
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['api_key', 'access_token', 'file_path', 'new_name']
        all_params.append('callback')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method rename_resource" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'api_key' is set
        if ('api_key' not in params) or (params['api_key'] is None):
            raise ValueError("Missing the required parameter `api_key` when calling `rename_resource`")
        # verify the required parameter 'access_token' is set
        if ('access_token' not in params) or (params['access_token'] is None):
            raise ValueError("Missing the required parameter `access_token` when calling `rename_resource`")
        # verify the required parameter 'file_path' is set
        if ('file_path' not in params) or (params['file_path'] is None):
            raise ValueError("Missing the required parameter `file_path` when calling `rename_resource`")
        # verify the required parameter 'new_name' is set
        if ('new_name' not in params) or (params['new_name'] is None):
            raise ValueError("Missing the required parameter `new_name` when calling `rename_resource`")


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
        if 'file_path' in params:
            form_params.append(('filePath', params['file_path']))
        if 'new_name' in params:
            form_params.append(('newName', params['new_name']))

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.\
            select_header_accept(['application/json'])

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.\
            select_header_content_type(['application/x-www-form-urlencoded'])

        # Authentication setting
        auth_settings = []

        return self.api_client.call_api('/renameResource', 'POST',
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
