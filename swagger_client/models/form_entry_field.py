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

class FormEntryField(object):
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
        'value': 'str',
        'order': 'int'
    }

    attribute_map = {
        'name': 'name',
        'value': 'value',
        'order': 'order'
    }

    def __init__(self, name=None, value=None, order=None):  # noqa: E501
        """FormEntryField - a model defined in Swagger"""  # noqa: E501
        self._name = None
        self._value = None
        self._order = None
        self.discriminator = None
        if name is not None:
            self.name = name
        if value is not None:
            self.value = value
        if order is not None:
            self.order = order

    @property
    def name(self):
        """Gets the name of this FormEntryField.  # noqa: E501

        Field name  # noqa: E501

        :return: The name of this FormEntryField.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this FormEntryField.

        Field name  # noqa: E501

        :param name: The name of this FormEntryField.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def value(self):
        """Gets the value of this FormEntryField.  # noqa: E501

        Field value  # noqa: E501

        :return: The value of this FormEntryField.  # noqa: E501
        :rtype: str
        """
        return self._value

    @value.setter
    def value(self, value):
        """Sets the value of this FormEntryField.

        Field value  # noqa: E501

        :param value: The value of this FormEntryField.  # noqa: E501
        :type: str
        """

        self._value = value

    @property
    def order(self):
        """Gets the order of this FormEntryField.  # noqa: E501

        Field order in the form  # noqa: E501

        :return: The order of this FormEntryField.  # noqa: E501
        :rtype: int
        """
        return self._order

    @order.setter
    def order(self, order):
        """Sets the order of this FormEntryField.

        Field order in the form  # noqa: E501

        :param order: The order of this FormEntryField.  # noqa: E501
        :type: int
        """

        self._order = order

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
        if issubclass(FormEntryField, dict):
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
        if not isinstance(other, FormEntryField):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
