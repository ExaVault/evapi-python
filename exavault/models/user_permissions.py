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

class UserPermissions(object):
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
        'download': 'bool',
        'upload': 'bool',
        'modify': 'bool',
        'delete': 'bool',
        'list': 'bool',
        'change_password': 'bool',
        'share': 'bool',
        'notification': 'bool',
        'view_form_data': 'bool',
        'delete_form_data': 'bool'
    }

    attribute_map = {
        'download': 'download',
        'upload': 'upload',
        'modify': 'modify',
        'delete': 'delete',
        'list': 'list',
        'change_password': 'changePassword',
        'share': 'share',
        'notification': 'notification',
        'view_form_data': 'viewFormData',
        'delete_form_data': 'deleteFormData'
    }

    def __init__(self, download=None, upload=None, modify=None, delete=None, list=None, change_password=None, share=None, notification=None, view_form_data=None, delete_form_data=None):  # noqa: E501
        """UserPermissions - a model defined in Swagger"""  # noqa: E501
        self._download = None
        self._upload = None
        self._modify = None
        self._delete = None
        self._list = None
        self._change_password = None
        self._share = None
        self._notification = None
        self._view_form_data = None
        self._delete_form_data = None
        self.discriminator = None
        self.download = download
        self.upload = upload
        self.modify = modify
        self.delete = delete
        self.list = list
        self.change_password = change_password
        self.share = share
        self.notification = notification
        self.view_form_data = view_form_data
        self.delete_form_data = delete_form_data

    @property
    def download(self):
        """Gets the download of this UserPermissions.  # noqa: E501

        Download permission flag  # noqa: E501

        :return: The download of this UserPermissions.  # noqa: E501
        :rtype: bool
        """
        return self._download

    @download.setter
    def download(self, download):
        """Sets the download of this UserPermissions.

        Download permission flag  # noqa: E501

        :param download: The download of this UserPermissions.  # noqa: E501
        :type: bool
        """
        if download is None:
            raise ValueError("Invalid value for `download`, must not be `None`")  # noqa: E501

        self._download = download

    @property
    def upload(self):
        """Gets the upload of this UserPermissions.  # noqa: E501

        Upload permission flag  # noqa: E501

        :return: The upload of this UserPermissions.  # noqa: E501
        :rtype: bool
        """
        return self._upload

    @upload.setter
    def upload(self, upload):
        """Sets the upload of this UserPermissions.

        Upload permission flag  # noqa: E501

        :param upload: The upload of this UserPermissions.  # noqa: E501
        :type: bool
        """
        if upload is None:
            raise ValueError("Invalid value for `upload`, must not be `None`")  # noqa: E501

        self._upload = upload

    @property
    def modify(self):
        """Gets the modify of this UserPermissions.  # noqa: E501

        Modify permission flag  # noqa: E501

        :return: The modify of this UserPermissions.  # noqa: E501
        :rtype: bool
        """
        return self._modify

    @modify.setter
    def modify(self, modify):
        """Sets the modify of this UserPermissions.

        Modify permission flag  # noqa: E501

        :param modify: The modify of this UserPermissions.  # noqa: E501
        :type: bool
        """
        if modify is None:
            raise ValueError("Invalid value for `modify`, must not be `None`")  # noqa: E501

        self._modify = modify

    @property
    def delete(self):
        """Gets the delete of this UserPermissions.  # noqa: E501

        Delete permission flag  # noqa: E501

        :return: The delete of this UserPermissions.  # noqa: E501
        :rtype: bool
        """
        return self._delete

    @delete.setter
    def delete(self, delete):
        """Sets the delete of this UserPermissions.

        Delete permission flag  # noqa: E501

        :param delete: The delete of this UserPermissions.  # noqa: E501
        :type: bool
        """
        if delete is None:
            raise ValueError("Invalid value for `delete`, must not be `None`")  # noqa: E501

        self._delete = delete

    @property
    def list(self):
        """Gets the list of this UserPermissions.  # noqa: E501

        View folder contents permission flag  # noqa: E501

        :return: The list of this UserPermissions.  # noqa: E501
        :rtype: bool
        """
        return self._list

    @list.setter
    def list(self, list):
        """Sets the list of this UserPermissions.

        View folder contents permission flag  # noqa: E501

        :param list: The list of this UserPermissions.  # noqa: E501
        :type: bool
        """
        if list is None:
            raise ValueError("Invalid value for `list`, must not be `None`")  # noqa: E501

        self._list = list

    @property
    def change_password(self):
        """Gets the change_password of this UserPermissions.  # noqa: E501

        Change (own) password permission flag  # noqa: E501

        :return: The change_password of this UserPermissions.  # noqa: E501
        :rtype: bool
        """
        return self._change_password

    @change_password.setter
    def change_password(self, change_password):
        """Sets the change_password of this UserPermissions.

        Change (own) password permission flag  # noqa: E501

        :param change_password: The change_password of this UserPermissions.  # noqa: E501
        :type: bool
        """
        if change_password is None:
            raise ValueError("Invalid value for `change_password`, must not be `None`")  # noqa: E501

        self._change_password = change_password

    @property
    def share(self):
        """Gets the share of this UserPermissions.  # noqa: E501

        Sharing permission flag  # noqa: E501

        :return: The share of this UserPermissions.  # noqa: E501
        :rtype: bool
        """
        return self._share

    @share.setter
    def share(self, share):
        """Sets the share of this UserPermissions.

        Sharing permission flag  # noqa: E501

        :param share: The share of this UserPermissions.  # noqa: E501
        :type: bool
        """
        if share is None:
            raise ValueError("Invalid value for `share`, must not be `None`")  # noqa: E501

        self._share = share

    @property
    def notification(self):
        """Gets the notification of this UserPermissions.  # noqa: E501

        Notifications permission flag  # noqa: E501

        :return: The notification of this UserPermissions.  # noqa: E501
        :rtype: bool
        """
        return self._notification

    @notification.setter
    def notification(self, notification):
        """Sets the notification of this UserPermissions.

        Notifications permission flag  # noqa: E501

        :param notification: The notification of this UserPermissions.  # noqa: E501
        :type: bool
        """
        if notification is None:
            raise ValueError("Invalid value for `notification`, must not be `None`")  # noqa: E501

        self._notification = notification

    @property
    def view_form_data(self):
        """Gets the view_form_data of this UserPermissions.  # noqa: E501

        Access Form Data permission flag. If true, user can view submissions that have been stored for a receive folder. This includes any data submitted in the receive folder form.  # noqa: E501

        :return: The view_form_data of this UserPermissions.  # noqa: E501
        :rtype: bool
        """
        return self._view_form_data

    @view_form_data.setter
    def view_form_data(self, view_form_data):
        """Sets the view_form_data of this UserPermissions.

        Access Form Data permission flag. If true, user can view submissions that have been stored for a receive folder. This includes any data submitted in the receive folder form.  # noqa: E501

        :param view_form_data: The view_form_data of this UserPermissions.  # noqa: E501
        :type: bool
        """
        if view_form_data is None:
            raise ValueError("Invalid value for `view_form_data`, must not be `None`")  # noqa: E501

        self._view_form_data = view_form_data

    @property
    def delete_form_data(self):
        """Gets the delete_form_data of this UserPermissions.  # noqa: E501

        Delete form data permission flag. If true, user can remove data that was submitted for a receive folder. This applies only to data submitted in the receive folder form, not the actual files uploaded.  # noqa: E501

        :return: The delete_form_data of this UserPermissions.  # noqa: E501
        :rtype: bool
        """
        return self._delete_form_data

    @delete_form_data.setter
    def delete_form_data(self, delete_form_data):
        """Sets the delete_form_data of this UserPermissions.

        Delete form data permission flag. If true, user can remove data that was submitted for a receive folder. This applies only to data submitted in the receive folder form, not the actual files uploaded.  # noqa: E501

        :param delete_form_data: The delete_form_data of this UserPermissions.  # noqa: E501
        :type: bool
        """
        if delete_form_data is None:
            raise ValueError("Invalid value for `delete_form_data`, must not be `None`")  # noqa: E501

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
        if issubclass(UserPermissions, dict):
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
        if not isinstance(other, UserPermissions):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
