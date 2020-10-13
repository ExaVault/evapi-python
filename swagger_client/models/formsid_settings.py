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

class FormsidSettings(object):
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
        'is_required': 'bool',
        'sender_email': 'bool',
        'use_as_folder_name': 'bool'
    }

    attribute_map = {
        'is_required': 'isRequired',
        'sender_email': 'senderEmail',
        'use_as_folder_name': 'useAsFolderName'
    }

    def __init__(self, is_required=None, sender_email=None, use_as_folder_name=None):  # noqa: E501
        """FormsidSettings - a model defined in Swagger"""  # noqa: E501
        self._is_required = None
        self._sender_email = None
        self._use_as_folder_name = None
        self.discriminator = None
        if is_required is not None:
            self.is_required = is_required
        if sender_email is not None:
            self.sender_email = sender_email
        if use_as_folder_name is not None:
            self.use_as_folder_name = use_as_folder_name

    @property
    def is_required(self):
        """Gets the is_required of this FormsidSettings.  # noqa: E501

        True is the form element is required for submission.   # noqa: E501

        :return: The is_required of this FormsidSettings.  # noqa: E501
        :rtype: bool
        """
        return self._is_required

    @is_required.setter
    def is_required(self, is_required):
        """Sets the is_required of this FormsidSettings.

        True is the form element is required for submission.   # noqa: E501

        :param is_required: The is_required of this FormsidSettings.  # noqa: E501
        :type: bool
        """

        self._is_required = is_required

    @property
    def sender_email(self):
        """Gets the sender_email of this FormsidSettings.  # noqa: E501


        :return: The sender_email of this FormsidSettings.  # noqa: E501
        :rtype: bool
        """
        return self._sender_email

    @sender_email.setter
    def sender_email(self, sender_email):
        """Sets the sender_email of this FormsidSettings.


        :param sender_email: The sender_email of this FormsidSettings.  # noqa: E501
        :type: bool
        """

        self._sender_email = sender_email

    @property
    def use_as_folder_name(self):
        """Gets the use_as_folder_name of this FormsidSettings.  # noqa: E501

        True if the submitted response should be used as the name for the new folder.   # noqa: E501

        :return: The use_as_folder_name of this FormsidSettings.  # noqa: E501
        :rtype: bool
        """
        return self._use_as_folder_name

    @use_as_folder_name.setter
    def use_as_folder_name(self, use_as_folder_name):
        """Sets the use_as_folder_name of this FormsidSettings.

        True if the submitted response should be used as the name for the new folder.   # noqa: E501

        :param use_as_folder_name: The use_as_folder_name of this FormsidSettings.  # noqa: E501
        :type: bool
        """

        self._use_as_folder_name = use_as_folder_name

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
        if issubclass(FormsidSettings, dict):
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
        if not isinstance(other, FormsidSettings):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other