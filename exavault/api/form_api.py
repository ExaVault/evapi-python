# coding: utf-8

"""
    ExaVault API

    See our API reference documentation at https://www.exavault.com/developer/api-docs/  # noqa: E501

    OpenAPI spec version: 2.0
    Contact: support@exavault.com
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

from __future__ import absolute_import

import re  # noqa: F401

# python 2 and python 3 compatibility library
import six

from exavault.api_client import ApiClient


class FormApi(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    Ref: https://github.com/swagger-api/swagger-codegen
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def delete_form_message_by_id(self, ev_api_key, ev_access_token, id, **kwargs):  # noqa: E501
        """Delete a receive form submission  # noqa: E501

        Deletes a form submission entry, which represents one time that a visitor filled out the form and uploaded files. This deletes only the record of the submission (the date, the values entered in the form and the names of the files uploaded by the visitor).The share and any associated file resources will not be deleted by this.   **Notes**:  - Use the [GET /form/entries/{formId}](#operation/getFormMessageById) to list the submissions and obtain the ID of the entry you want to delete - You must have the [DeleteFormData permission](/docs/account/04-users/00-introduction#managing-user-roles-and-permissions) in order to use this operation - It is not possible to un-delete data that is removed in this way   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.delete_form_message_by_id(ev_api_key, ev_access_token, id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str ev_api_key: API Key required to make the API call.  (required)
        :param str ev_access_token: Access token required to make the API call. (required)
        :param str id: ID of the entry to be deleted data for (required)
        :return: EmptyResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.delete_form_message_by_id_with_http_info(ev_api_key, ev_access_token, id, **kwargs)  # noqa: E501
        else:
            (data) = self.delete_form_message_by_id_with_http_info(ev_api_key, ev_access_token, id, **kwargs)  # noqa: E501
            return data

    def delete_form_message_by_id_with_http_info(self, ev_api_key, ev_access_token, id, **kwargs):  # noqa: E501
        """Delete a receive form submission  # noqa: E501

        Deletes a form submission entry, which represents one time that a visitor filled out the form and uploaded files. This deletes only the record of the submission (the date, the values entered in the form and the names of the files uploaded by the visitor).The share and any associated file resources will not be deleted by this.   **Notes**:  - Use the [GET /form/entries/{formId}](#operation/getFormMessageById) to list the submissions and obtain the ID of the entry you want to delete - You must have the [DeleteFormData permission](/docs/account/04-users/00-introduction#managing-user-roles-and-permissions) in order to use this operation - It is not possible to un-delete data that is removed in this way   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.delete_form_message_by_id_with_http_info(ev_api_key, ev_access_token, id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str ev_api_key: API Key required to make the API call.  (required)
        :param str ev_access_token: Access token required to make the API call. (required)
        :param str id: ID of the entry to be deleted data for (required)
        :return: EmptyResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['ev_api_key', 'ev_access_token', 'id']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method delete_form_message_by_id" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'ev_api_key' is set
        if ('ev_api_key' not in params or
                params['ev_api_key'] is None):
            raise ValueError("Missing the required parameter `ev_api_key` when calling `delete_form_message_by_id`")  # noqa: E501
        # verify the required parameter 'ev_access_token' is set
        if ('ev_access_token' not in params or
                params['ev_access_token'] is None):
            raise ValueError("Missing the required parameter `ev_access_token` when calling `delete_form_message_by_id`")  # noqa: E501
        # verify the required parameter 'id' is set
        if ('id' not in params or
                params['id'] is None):
            raise ValueError("Missing the required parameter `id` when calling `delete_form_message_by_id`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'id' in params:
            path_params['id'] = params['id']  # noqa: E501

        query_params = []

        header_params = {}
        if 'ev_api_key' in params:
            header_params['ev-api-key'] = params['ev_api_key']  # noqa: E501
        if 'ev_access_token' in params:
            header_params['ev-access-token'] = params['ev_access_token']  # noqa: E501

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/forms/entries/{id}', 'DELETE',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='EmptyResponse',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def get_form_by_id(self, id, ev_api_key, ev_access_token, **kwargs):  # noqa: E501
        """Get receive folder form by Id  # noqa: E501

        Returns the [file upload form](/docs/account/05-file-sharing/05-form-builder) assigned to a [receive folder](/docs/account/05-file-sharing/04-receive-folders). The form details will return all the input fields and their settings.   Use the `include` parameter (with the value **share**) to also retrieve the details of the associated receive folder.   **Note**  If you prefer to find a form by its shareHash, you can use the [GET /forms](#operation/getFormByShareHash) endpoint instead.    # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_form_by_id(id, ev_api_key, ev_access_token, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param int id: Form unique ID number. (required)
        :param str ev_api_key: API key required to make the API call. (required)
        :param str ev_access_token: Access Token required to make the API call. (required)
        :param str include: Enter \"**share**\" to get information about associated receive folder.
        :return: FormResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.get_form_by_id_with_http_info(id, ev_api_key, ev_access_token, **kwargs)  # noqa: E501
        else:
            (data) = self.get_form_by_id_with_http_info(id, ev_api_key, ev_access_token, **kwargs)  # noqa: E501
            return data

    def get_form_by_id_with_http_info(self, id, ev_api_key, ev_access_token, **kwargs):  # noqa: E501
        """Get receive folder form by Id  # noqa: E501

        Returns the [file upload form](/docs/account/05-file-sharing/05-form-builder) assigned to a [receive folder](/docs/account/05-file-sharing/04-receive-folders). The form details will return all the input fields and their settings.   Use the `include` parameter (with the value **share**) to also retrieve the details of the associated receive folder.   **Note**  If you prefer to find a form by its shareHash, you can use the [GET /forms](#operation/getFormByShareHash) endpoint instead.    # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_form_by_id_with_http_info(id, ev_api_key, ev_access_token, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param int id: Form unique ID number. (required)
        :param str ev_api_key: API key required to make the API call. (required)
        :param str ev_access_token: Access Token required to make the API call. (required)
        :param str include: Enter \"**share**\" to get information about associated receive folder.
        :return: FormResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['id', 'ev_api_key', 'ev_access_token', 'include']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_form_by_id" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'id' is set
        if ('id' not in params or
                params['id'] is None):
            raise ValueError("Missing the required parameter `id` when calling `get_form_by_id`")  # noqa: E501
        # verify the required parameter 'ev_api_key' is set
        if ('ev_api_key' not in params or
                params['ev_api_key'] is None):
            raise ValueError("Missing the required parameter `ev_api_key` when calling `get_form_by_id`")  # noqa: E501
        # verify the required parameter 'ev_access_token' is set
        if ('ev_access_token' not in params or
                params['ev_access_token'] is None):
            raise ValueError("Missing the required parameter `ev_access_token` when calling `get_form_by_id`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'id' in params:
            path_params['id'] = params['id']  # noqa: E501

        query_params = []
        if 'include' in params:
            query_params.append(('include', params['include']))  # noqa: E501

        header_params = {}
        if 'ev_api_key' in params:
            header_params['ev-api-key'] = params['ev_api_key']  # noqa: E501
        if 'ev_access_token' in params:
            header_params['ev-access-token'] = params['ev_access_token']  # noqa: E501

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/forms/{id}', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='FormResponse',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def get_form_by_share_hash(self, ev_api_key, ev_access_token, share_hash, **kwargs):  # noqa: E501
        """Get receive folder form settings  # noqa: E501

        Get the information for the [file upload form](/docs/account/05-file-sharing/05-form-builder) assigned to a [receive folder](/docs/account/05-file-sharing/04-receive-folders) by its shareHash. The form details will return all the input field settings and the CSS for the form.  Use the `include` parameter (with the value **share**) to also get the details of the associated receive folder.  **Note**  - If you prefer to find a form by its ID, you can use the [GET /forms/{id}](#operation/getFormById) endpoint instead.    # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_form_by_share_hash(ev_api_key, ev_access_token, share_hash, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str ev_api_key: API key required to make the API call. (required)
        :param str ev_access_token: Access Token required to make the API call. (required)
        :param str share_hash: Share hash to retrieve the form for. (required)
        :param str include: Related record types to include in the response. Valid option is **share**
        :return: FormResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.get_form_by_share_hash_with_http_info(ev_api_key, ev_access_token, share_hash, **kwargs)  # noqa: E501
        else:
            (data) = self.get_form_by_share_hash_with_http_info(ev_api_key, ev_access_token, share_hash, **kwargs)  # noqa: E501
            return data

    def get_form_by_share_hash_with_http_info(self, ev_api_key, ev_access_token, share_hash, **kwargs):  # noqa: E501
        """Get receive folder form settings  # noqa: E501

        Get the information for the [file upload form](/docs/account/05-file-sharing/05-form-builder) assigned to a [receive folder](/docs/account/05-file-sharing/04-receive-folders) by its shareHash. The form details will return all the input field settings and the CSS for the form.  Use the `include` parameter (with the value **share**) to also get the details of the associated receive folder.  **Note**  - If you prefer to find a form by its ID, you can use the [GET /forms/{id}](#operation/getFormById) endpoint instead.    # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_form_by_share_hash_with_http_info(ev_api_key, ev_access_token, share_hash, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str ev_api_key: API key required to make the API call. (required)
        :param str ev_access_token: Access Token required to make the API call. (required)
        :param str share_hash: Share hash to retrieve the form for. (required)
        :param str include: Related record types to include in the response. Valid option is **share**
        :return: FormResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['ev_api_key', 'ev_access_token', 'share_hash', 'include']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_form_by_share_hash" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'ev_api_key' is set
        if ('ev_api_key' not in params or
                params['ev_api_key'] is None):
            raise ValueError("Missing the required parameter `ev_api_key` when calling `get_form_by_share_hash`")  # noqa: E501
        # verify the required parameter 'ev_access_token' is set
        if ('ev_access_token' not in params or
                params['ev_access_token'] is None):
            raise ValueError("Missing the required parameter `ev_access_token` when calling `get_form_by_share_hash`")  # noqa: E501
        # verify the required parameter 'share_hash' is set
        if ('share_hash' not in params or
                params['share_hash'] is None):
            raise ValueError("Missing the required parameter `share_hash` when calling `get_form_by_share_hash`")  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'share_hash' in params:
            query_params.append(('shareHash', params['share_hash']))  # noqa: E501
        if 'include' in params:
            query_params.append(('include', params['include']))  # noqa: E501

        header_params = {}
        if 'ev_api_key' in params:
            header_params['ev-api-key'] = params['ev_api_key']  # noqa: E501
        if 'ev_access_token' in params:
            header_params['ev-access-token'] = params['ev_access_token']  # noqa: E501

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/forms', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='FormResponse',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def get_form_entries(self, ev_api_key, ev_access_token, id, **kwargs):  # noqa: E501
        """Get form data entries for a receive  # noqa: E501

        Returns the form data entries for a specific form for a receive. Optional parameters can be included in the call to manage larger data sets.   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_form_entries(ev_api_key, ev_access_token, id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str ev_api_key: API Key required to make the API call.  (required)
        :param str ev_access_token: Access token required to make the API call. (required)
        :param str id: ID of the form to retrieve entries for. (required)
        :param int limit: Limit of records to be returned (for pagination)
        :param int offset: Current offset of records (for pagination)
        :return: FormEntryResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.get_form_entries_with_http_info(ev_api_key, ev_access_token, id, **kwargs)  # noqa: E501
        else:
            (data) = self.get_form_entries_with_http_info(ev_api_key, ev_access_token, id, **kwargs)  # noqa: E501
            return data

    def get_form_entries_with_http_info(self, ev_api_key, ev_access_token, id, **kwargs):  # noqa: E501
        """Get form data entries for a receive  # noqa: E501

        Returns the form data entries for a specific form for a receive. Optional parameters can be included in the call to manage larger data sets.   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_form_entries_with_http_info(ev_api_key, ev_access_token, id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str ev_api_key: API Key required to make the API call.  (required)
        :param str ev_access_token: Access token required to make the API call. (required)
        :param str id: ID of the form to retrieve entries for. (required)
        :param int limit: Limit of records to be returned (for pagination)
        :param int offset: Current offset of records (for pagination)
        :return: FormEntryResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['ev_api_key', 'ev_access_token', 'id', 'limit', 'offset']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_form_entries" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'ev_api_key' is set
        if ('ev_api_key' not in params or
                params['ev_api_key'] is None):
            raise ValueError("Missing the required parameter `ev_api_key` when calling `get_form_entries`")  # noqa: E501
        # verify the required parameter 'ev_access_token' is set
        if ('ev_access_token' not in params or
                params['ev_access_token'] is None):
            raise ValueError("Missing the required parameter `ev_access_token` when calling `get_form_entries`")  # noqa: E501
        # verify the required parameter 'id' is set
        if ('id' not in params or
                params['id'] is None):
            raise ValueError("Missing the required parameter `id` when calling `get_form_entries`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'id' in params:
            path_params['id'] = params['id']  # noqa: E501

        query_params = []
        if 'limit' in params:
            query_params.append(('limit', params['limit']))  # noqa: E501
        if 'offset' in params:
            query_params.append(('offset', params['offset']))  # noqa: E501

        header_params = {}
        if 'ev_api_key' in params:
            header_params['ev-api-key'] = params['ev_api_key']  # noqa: E501
        if 'ev_access_token' in params:
            header_params['ev-access-token'] = params['ev_access_token']  # noqa: E501

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/forms/entries/{id}', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='FormEntryResponse',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def update_form_by_id(self, ev_api_key, ev_access_token, id, **kwargs):  # noqa: E501
        """Updates a form with given parameters  # noqa: E501

        Add, update, or delete a form's parameters. This will alter how your users/customers will see and interact with the form when sending you files.   **Notes**  *This call will **replace** your current form in its entirety.* If you want to keep any existing elements unchanged, be sure to submit the call with an element's current settings to preserve them.                            # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.update_form_by_id(ev_api_key, ev_access_token, id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str ev_api_key: API Key required to make the API call. (required)
        :param str ev_access_token: Access token required to make the API call. (required)
        :param int id: Form unique ID number. (required)
        :param Body2 body:
        :return: FormResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.update_form_by_id_with_http_info(ev_api_key, ev_access_token, id, **kwargs)  # noqa: E501
        else:
            (data) = self.update_form_by_id_with_http_info(ev_api_key, ev_access_token, id, **kwargs)  # noqa: E501
            return data

    def update_form_by_id_with_http_info(self, ev_api_key, ev_access_token, id, **kwargs):  # noqa: E501
        """Updates a form with given parameters  # noqa: E501

        Add, update, or delete a form's parameters. This will alter how your users/customers will see and interact with the form when sending you files.   **Notes**  *This call will **replace** your current form in its entirety.* If you want to keep any existing elements unchanged, be sure to submit the call with an element's current settings to preserve them.                            # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.update_form_by_id_with_http_info(ev_api_key, ev_access_token, id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str ev_api_key: API Key required to make the API call. (required)
        :param str ev_access_token: Access token required to make the API call. (required)
        :param int id: Form unique ID number. (required)
        :param Body2 body:
        :return: FormResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['ev_api_key', 'ev_access_token', 'id', 'body']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method update_form_by_id" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'ev_api_key' is set
        if ('ev_api_key' not in params or
                params['ev_api_key'] is None):
            raise ValueError("Missing the required parameter `ev_api_key` when calling `update_form_by_id`")  # noqa: E501
        # verify the required parameter 'ev_access_token' is set
        if ('ev_access_token' not in params or
                params['ev_access_token'] is None):
            raise ValueError("Missing the required parameter `ev_access_token` when calling `update_form_by_id`")  # noqa: E501
        # verify the required parameter 'id' is set
        if ('id' not in params or
                params['id'] is None):
            raise ValueError("Missing the required parameter `id` when calling `update_form_by_id`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'id' in params:
            path_params['id'] = params['id']  # noqa: E501

        query_params = []

        header_params = {}
        if 'ev_api_key' in params:
            header_params['ev-api-key'] = params['ev_api_key']  # noqa: E501
        if 'ev_access_token' in params:
            header_params['ev-access-token'] = params['ev_access_token']  # noqa: E501

        form_params = []
        local_var_files = {}

        body_params = None
        if 'body' in params:
            body_params = params['body']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/forms/{id}', 'PATCH',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='FormResponse',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)
