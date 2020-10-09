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


class Body(object):
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
        'name': 'str',
        'emails': 'list[str]'
    }

    attribute_map = {
        'name': 'name',
        'emails': 'emails'
    }

    def __init__(self, name=None, emails=None):  # noqa: E501
        """Body - a model defined in Swagger"""  # noqa: E501
        self._name = None
        self._emails = None
        self.discriminator = None
        self.name = name
        self.emails = emails

    @property
    def name(self):
        """Gets the name of this Body.  # noqa: E501

        Name of the email list.   # noqa: E501

        :return: The name of this Body.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this Body.

        Name of the email list.   # noqa: E501

        :param name: The name of this Body.  # noqa: E501
        :type: str
        """
        if name is None:
            raise ValueError("Invalid value for `name`, must not be `None`")  # noqa: E501

        self._name = name

    @property
    def emails(self):
        """Gets the emails of this Body.  # noqa: E501

        Array of email addresses to include in the email list.   # noqa: E501

        :return: The emails of this Body.  # noqa: E501
        :rtype: list[str]
        """
        return self._emails

    @emails.setter
    def emails(self, emails):
        """Sets the emails of this Body.

        Array of email addresses to include in the email list.   # noqa: E501

        :param emails: The emails of this Body.  # noqa: E501
        :type: list[str]
        """
        if emails is None:
            raise ValueError("Invalid value for `emails`, must not be `None`")  # noqa: E501

        self._emails = emails

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
        if issubclass(Body, dict):
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
        if not isinstance(other, Body):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
