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

class WebhooksActivityEntry(object):
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
        'id': 'int',
        'type': 'str',
        'attributes': 'WebhooksActivityEntryAttributes'
    }

    attribute_map = {
        'id': 'id',
        'type': 'type',
        'attributes': 'attributes'
    }

    def __init__(self, id=None, type=None, attributes=None):  # noqa: E501
        """WebhooksActivityEntry - a model defined in Swagger"""  # noqa: E501
        self._id = None
        self._type = None
        self._attributes = None
        self.discriminator = None
        if id is not None:
            self.id = id
        if type is not None:
            self.type = type
        if attributes is not None:
            self.attributes = attributes

    @property
    def id(self):
        """Gets the id of this WebhooksActivityEntry.  # noqa: E501


        :return: The id of this WebhooksActivityEntry.  # noqa: E501
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this WebhooksActivityEntry.


        :param id: The id of this WebhooksActivityEntry.  # noqa: E501
        :type: int
        """

        self._id = id

    @property
    def type(self):
        """Gets the type of this WebhooksActivityEntry.  # noqa: E501


        :return: The type of this WebhooksActivityEntry.  # noqa: E501
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this WebhooksActivityEntry.


        :param type: The type of this WebhooksActivityEntry.  # noqa: E501
        :type: str
        """
        allowed_values = ["webhookActivity"]  # noqa: E501
        if type not in allowed_values:
            raise ValueError(
                "Invalid value for `type` ({0}), must be one of {1}"  # noqa: E501
                .format(type, allowed_values)
            )

        self._type = type

    @property
    def attributes(self):
        """Gets the attributes of this WebhooksActivityEntry.  # noqa: E501


        :return: The attributes of this WebhooksActivityEntry.  # noqa: E501
        :rtype: WebhooksActivityEntryAttributes
        """
        return self._attributes

    @attributes.setter
    def attributes(self, attributes):
        """Sets the attributes of this WebhooksActivityEntry.


        :param attributes: The attributes of this WebhooksActivityEntry.  # noqa: E501
        :type: WebhooksActivityEntryAttributes
        """

        self._attributes = attributes

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
        if issubclass(WebhooksActivityEntry, dict):
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
        if not isinstance(other, WebhooksActivityEntry):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
