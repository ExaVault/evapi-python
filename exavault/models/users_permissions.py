# coding: utf-8

"""
    ExaVault API

    See our API reference documentation at https://www.exavault.com/developer/api-docs/  # noqa: E501

    OpenAPI spec version: 2.0
    Contact: support@exavault.com
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

import pprint
import re  # noqa: F401

import six

class UsersPermissions(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """
    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'list': 'bool',
        'download': 'bool',
        'upload': 'bool',
        'modify': 'bool',
        'delete': 'bool',
        'change_password': 'bool',
        'share': 'bool',
        'notification': 'bool',
        'view_form_data': 'bool',
        'delete_form_data': 'bool'
    }

    attribute_map = {
        'list': 'list',
        'download': 'download',
        'upload': 'upload',
        'modify': 'modify',
        'delete': 'delete',
        'change_password': 'changePassword',
        'share': 'share',
        'notification': 'notification',
        'view_form_data': 'viewFormData',
        'delete_form_data': 'deleteFormData'
    }

    def __init__(self, list=None, download=None, upload=None, modify=None, delete=None, change_password=None, share=None, notification=None, view_form_data=None, delete_form_data=None):  # noqa: E501
        """UsersPermissions - a model defined in Swagger"""  # noqa: E501
        self._list = None
        self._download = None
        self._upload = None
        self._modify = None
        self._delete = None
        self._change_password = None
        self._share = None
        self._notification = None
        self._view_form_data = None
        self._delete_form_data = None
        self.discriminator = None
        if list is not None:
            self.list = list
        if download is not None:
            self.download = download
        if upload is not None:
            self.upload = upload
        if modify is not None:
            self.modify = modify
        if delete is not None:
            self.delete = delete
        if change_password is not None:
            self.change_password = change_password
        if share is not None:
            self.share = share
        if notification is not None:
            self.notification = notification
        if view_form_data is not None:
            self.view_form_data = view_form_data
        if delete_form_data is not None:
            self.delete_form_data = delete_form_data

    @property
    def list(self):
        """Gets the list of this UsersPermissions.  # noqa: E501


        :return: The list of this UsersPermissions.  # noqa: E501
        :rtype: bool
        """
        return self._list

    @list.setter
    def list(self, list):
        """Sets the list of this UsersPermissions.


        :param list: The list of this UsersPermissions.  # noqa: E501
        :type: bool
        """

        self._list = list

    @property
    def download(self):
        """Gets the download of this UsersPermissions.  # noqa: E501


        :return: The download of this UsersPermissions.  # noqa: E501
        :rtype: bool
        """
        return self._download

    @download.setter
    def download(self, download):
        """Sets the download of this UsersPermissions.


        :param download: The download of this UsersPermissions.  # noqa: E501
        :type: bool
        """

        self._download = download

    @property
    def upload(self):
        """Gets the upload of this UsersPermissions.  # noqa: E501


        :return: The upload of this UsersPermissions.  # noqa: E501
        :rtype: bool
        """
        return self._upload

    @upload.setter
    def upload(self, upload):
        """Sets the upload of this UsersPermissions.


        :param upload: The upload of this UsersPermissions.  # noqa: E501
        :type: bool
        """

        self._upload = upload

    @property
    def modify(self):
        """Gets the modify of this UsersPermissions.  # noqa: E501


        :return: The modify of this UsersPermissions.  # noqa: E501
        :rtype: bool
        """
        return self._modify

    @modify.setter
    def modify(self, modify):
        """Sets the modify of this UsersPermissions.


        :param modify: The modify of this UsersPermissions.  # noqa: E501
        :type: bool
        """

        self._modify = modify

    @property
    def delete(self):
        """Gets the delete of this UsersPermissions.  # noqa: E501


        :return: The delete of this UsersPermissions.  # noqa: E501
        :rtype: bool
        """
        return self._delete

    @delete.setter
    def delete(self, delete):
        """Sets the delete of this UsersPermissions.


        :param delete: The delete of this UsersPermissions.  # noqa: E501
        :type: bool
        """

        self._delete = delete

    @property
    def change_password(self):
        """Gets the change_password of this UsersPermissions.  # noqa: E501


        :return: The change_password of this UsersPermissions.  # noqa: E501
        :rtype: bool
        """
        return self._change_password

    @change_password.setter
    def change_password(self, change_password):
        """Sets the change_password of this UsersPermissions.


        :param change_password: The change_password of this UsersPermissions.  # noqa: E501
        :type: bool
        """

        self._change_password = change_password

    @property
    def share(self):
        """Gets the share of this UsersPermissions.  # noqa: E501


        :return: The share of this UsersPermissions.  # noqa: E501
        :rtype: bool
        """
        return self._share

    @share.setter
    def share(self, share):
        """Sets the share of this UsersPermissions.


        :param share: The share of this UsersPermissions.  # noqa: E501
        :type: bool
        """

        self._share = share

    @property
    def notification(self):
        """Gets the notification of this UsersPermissions.  # noqa: E501


        :return: The notification of this UsersPermissions.  # noqa: E501
        :rtype: bool
        """
        return self._notification

    @notification.setter
    def notification(self, notification):
        """Sets the notification of this UsersPermissions.


        :param notification: The notification of this UsersPermissions.  # noqa: E501
        :type: bool
        """

        self._notification = notification

    @property
    def view_form_data(self):
        """Gets the view_form_data of this UsersPermissions.  # noqa: E501


        :return: The view_form_data of this UsersPermissions.  # noqa: E501
        :rtype: bool
        """
        return self._view_form_data

    @view_form_data.setter
    def view_form_data(self, view_form_data):
        """Sets the view_form_data of this UsersPermissions.


        :param view_form_data: The view_form_data of this UsersPermissions.  # noqa: E501
        :type: bool
        """

        self._view_form_data = view_form_data

    @property
    def delete_form_data(self):
        """Gets the delete_form_data of this UsersPermissions.  # noqa: E501


        :return: The delete_form_data of this UsersPermissions.  # noqa: E501
        :rtype: bool
        """
        return self._delete_form_data

    @delete_form_data.setter
    def delete_form_data(self, delete_form_data):
        """Sets the delete_form_data of this UsersPermissions.


        :param delete_form_data: The delete_form_data of this UsersPermissions.  # noqa: E501
        :type: bool
        """

        self._delete_form_data = delete_form_data

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.swagger_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                result[attr] = value
        if issubclass(UsersPermissions, dict):
            for key, value in self.items():
                result[key] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, UsersPermissions):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other