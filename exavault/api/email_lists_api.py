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


class EmailListsApi(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    Ref: https://github.com/swagger-api/swagger-codegen
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def add_email_list(self, ev_api_key, ev_access_token, **kwargs):  # noqa: E501
        """Create new email list  # noqa: E501

        Create a new email list. Among other things, email lists can be used to send files or share folders with a group of email addresses at once.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.add_email_list(ev_api_key, ev_access_token, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str ev_api_key: API Key required to make the API call. (required)
        :param str ev_access_token: Access token required to make the API call. (required)
        :param AddEmailListRequestBody body:
        :return: EmailListResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.add_email_list_with_http_info(ev_api_key, ev_access_token, **kwargs)  # noqa: E501
        else:
            (data) = self.add_email_list_with_http_info(ev_api_key, ev_access_token, **kwargs)  # noqa: E501
            return data

    def add_email_list_with_http_info(self, ev_api_key, ev_access_token, **kwargs):  # noqa: E501
        """Create new email list  # noqa: E501

        Create a new email list. Among other things, email lists can be used to send files or share folders with a group of email addresses at once.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.add_email_list_with_http_info(ev_api_key, ev_access_token, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str ev_api_key: API Key required to make the API call. (required)
        :param str ev_access_token: Access token required to make the API call. (required)
        :param AddEmailListRequestBody body:
        :return: EmailListResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['ev_api_key', 'ev_access_token', 'body']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method add_email_list" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'ev_api_key' is set
        if ('ev_api_key' not in params or
                params['ev_api_key'] is None):
            raise ValueError("Missing the required parameter `ev_api_key` when calling `add_email_list`")  # noqa: E501
        # verify the required parameter 'ev_access_token' is set
        if ('ev_access_token' not in params or
                params['ev_access_token'] is None):
            raise ValueError("Missing the required parameter `ev_access_token` when calling `add_email_list`")  # noqa: E501

        collection_formats = {}

        path_params = {}

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
            '/email-lists', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='EmailListResponse',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def delete_email_list_by_id(self, ev_api_key, ev_access_token, id, **kwargs):  # noqa: E501
        """Delete an email group with given id  # noqa: E501

        Permanently delete an email group. This action is not reversable. We recommend making a user confirm this action before sending the API call.   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.delete_email_list_by_id(ev_api_key, ev_access_token, id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str ev_api_key: API Key required to make the API call. (required)
        :param str ev_access_token: Access token required to make the API call. (required)
        :param int id: ID of the email list to delete (required)
        :return: EmptyResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.delete_email_list_by_id_with_http_info(ev_api_key, ev_access_token, id, **kwargs)  # noqa: E501
        else:
            (data) = self.delete_email_list_by_id_with_http_info(ev_api_key, ev_access_token, id, **kwargs)  # noqa: E501
            return data

    def delete_email_list_by_id_with_http_info(self, ev_api_key, ev_access_token, id, **kwargs):  # noqa: E501
        """Delete an email group with given id  # noqa: E501

        Permanently delete an email group. This action is not reversable. We recommend making a user confirm this action before sending the API call.   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.delete_email_list_by_id_with_http_info(ev_api_key, ev_access_token, id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str ev_api_key: API Key required to make the API call. (required)
        :param str ev_access_token: Access token required to make the API call. (required)
        :param int id: ID of the email list to delete (required)
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
                    " to method delete_email_list_by_id" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'ev_api_key' is set
        if ('ev_api_key' not in params or
                params['ev_api_key'] is None):
            raise ValueError("Missing the required parameter `ev_api_key` when calling `delete_email_list_by_id`")  # noqa: E501
        # verify the required parameter 'ev_access_token' is set
        if ('ev_access_token' not in params or
                params['ev_access_token'] is None):
            raise ValueError("Missing the required parameter `ev_access_token` when calling `delete_email_list_by_id`")  # noqa: E501
        # verify the required parameter 'id' is set
        if ('id' not in params or
                params['id'] is None):
            raise ValueError("Missing the required parameter `id` when calling `delete_email_list_by_id`")  # noqa: E501

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
            '/email-lists/{id}', 'DELETE',
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

    def get_email_list_by_id(self, ev_api_key, ev_access_token, id, **kwargs):  # noqa: E501
        """Get individual email group  # noqa: E501

        Retrieve all the details of a specifc email list including it's name, when it was created and all the email addresses that belong to the group.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_email_list_by_id(ev_api_key, ev_access_token, id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str ev_api_key: API Key required to make the API call. (required)
        :param str ev_access_token: Access token required to make the API call. (required)
        :param int id: ID of the email list to return. (required)
        :param str include: Related record types to include in the response. Valid option is `ownerUser`
        :return: EmailListResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.get_email_list_by_id_with_http_info(ev_api_key, ev_access_token, id, **kwargs)  # noqa: E501
        else:
            (data) = self.get_email_list_by_id_with_http_info(ev_api_key, ev_access_token, id, **kwargs)  # noqa: E501
            return data

    def get_email_list_by_id_with_http_info(self, ev_api_key, ev_access_token, id, **kwargs):  # noqa: E501
        """Get individual email group  # noqa: E501

        Retrieve all the details of a specifc email list including it's name, when it was created and all the email addresses that belong to the group.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_email_list_by_id_with_http_info(ev_api_key, ev_access_token, id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str ev_api_key: API Key required to make the API call. (required)
        :param str ev_access_token: Access token required to make the API call. (required)
        :param int id: ID of the email list to return. (required)
        :param str include: Related record types to include in the response. Valid option is `ownerUser`
        :return: EmailListResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['ev_api_key', 'ev_access_token', 'id', 'include']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_email_list_by_id" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'ev_api_key' is set
        if ('ev_api_key' not in params or
                params['ev_api_key'] is None):
            raise ValueError("Missing the required parameter `ev_api_key` when calling `get_email_list_by_id`")  # noqa: E501
        # verify the required parameter 'ev_access_token' is set
        if ('ev_access_token' not in params or
                params['ev_access_token'] is None):
            raise ValueError("Missing the required parameter `ev_access_token` when calling `get_email_list_by_id`")  # noqa: E501
        # verify the required parameter 'id' is set
        if ('id' not in params or
                params['id'] is None):
            raise ValueError("Missing the required parameter `id` when calling `get_email_list_by_id`")  # noqa: E501

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
            '/email-lists/{id}', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='EmailListResponse',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def get_email_lists(self, ev_api_key, ev_access_token, **kwargs):  # noqa: E501
        """Get all email groups  # noqa: E501

        List all email groups for authenticated user  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_email_lists(ev_api_key, ev_access_token, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str ev_api_key: API Key required to make the API call. (required)
        :param str ev_access_token: Access token required to make the API call. (required)
        :param str include: Related record types to include in the response. Valid option is `ownerUser`
        :return: EmailListCollectionResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.get_email_lists_with_http_info(ev_api_key, ev_access_token, **kwargs)  # noqa: E501
        else:
            (data) = self.get_email_lists_with_http_info(ev_api_key, ev_access_token, **kwargs)  # noqa: E501
            return data

    def get_email_lists_with_http_info(self, ev_api_key, ev_access_token, **kwargs):  # noqa: E501
        """Get all email groups  # noqa: E501

        List all email groups for authenticated user  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_email_lists_with_http_info(ev_api_key, ev_access_token, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str ev_api_key: API Key required to make the API call. (required)
        :param str ev_access_token: Access token required to make the API call. (required)
        :param str include: Related record types to include in the response. Valid option is `ownerUser`
        :return: EmailListCollectionResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['ev_api_key', 'ev_access_token', 'include']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_email_lists" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'ev_api_key' is set
        if ('ev_api_key' not in params or
                params['ev_api_key'] is None):
            raise ValueError("Missing the required parameter `ev_api_key` when calling `get_email_lists`")  # noqa: E501
        # verify the required parameter 'ev_access_token' is set
        if ('ev_access_token' not in params or
                params['ev_access_token'] is None):
            raise ValueError("Missing the required parameter `ev_access_token` when calling `get_email_lists`")  # noqa: E501

        collection_formats = {}

        path_params = {}

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
            '/email-lists', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='EmailListCollectionResponse',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def update_email_list_by_id(self, ev_api_key, ev_access_token, id, **kwargs):  # noqa: E501
        """Update an email group  # noqa: E501

        Add or remove emails from an email list that can be used to send and share files with groups.   **Notes**  *This call will **replace** your current email list in its entirety.* If you want to keep any existing emails on the list, be sure to submit the call with any current emails you want to keep on the list.    # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.update_email_list_by_id(ev_api_key, ev_access_token, id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str ev_api_key: API Key required to make the API call. (required)
        :param str ev_access_token: Access token required to make the API call. (required)
        :param int id: ID of the email list to update. (required)
        :param UpdateEmailListRequestBody body:
        :return: EmailListResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.update_email_list_by_id_with_http_info(ev_api_key, ev_access_token, id, **kwargs)  # noqa: E501
        else:
            (data) = self.update_email_list_by_id_with_http_info(ev_api_key, ev_access_token, id, **kwargs)  # noqa: E501
            return data

    def update_email_list_by_id_with_http_info(self, ev_api_key, ev_access_token, id, **kwargs):  # noqa: E501
        """Update an email group  # noqa: E501

        Add or remove emails from an email list that can be used to send and share files with groups.   **Notes**  *This call will **replace** your current email list in its entirety.* If you want to keep any existing emails on the list, be sure to submit the call with any current emails you want to keep on the list.    # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.update_email_list_by_id_with_http_info(ev_api_key, ev_access_token, id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str ev_api_key: API Key required to make the API call. (required)
        :param str ev_access_token: Access token required to make the API call. (required)
        :param int id: ID of the email list to update. (required)
        :param UpdateEmailListRequestBody body:
        :return: EmailListResponse
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
                    " to method update_email_list_by_id" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'ev_api_key' is set
        if ('ev_api_key' not in params or
                params['ev_api_key'] is None):
            raise ValueError("Missing the required parameter `ev_api_key` when calling `update_email_list_by_id`")  # noqa: E501
        # verify the required parameter 'ev_access_token' is set
        if ('ev_access_token' not in params or
                params['ev_access_token'] is None):
            raise ValueError("Missing the required parameter `ev_access_token` when calling `update_email_list_by_id`")  # noqa: E501
        # verify the required parameter 'id' is set
        if ('id' not in params or
                params['id'] is None):
            raise ValueError("Missing the required parameter `id` when calling `update_email_list_by_id`")  # noqa: E501

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
            '/email-lists/{id}', 'PATCH',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='EmailListResponse',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)
