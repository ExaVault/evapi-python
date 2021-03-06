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

class ShareMessageAttributes(object):
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
        'subject': 'str',
        'body': 'str',
        'created': 'datetime',
        'modified': 'datetime'
    }

    attribute_map = {
        'subject': 'subject',
        'body': 'body',
        'created': 'created',
        'modified': 'modified'
    }

    def __init__(self, subject=None, body=None, created=None, modified=None):  # noqa: E501
        """ShareMessageAttributes - a model defined in Swagger"""  # noqa: E501
        self._subject = None
        self._body = None
        self._created = None
        self._modified = None
        self.discriminator = None
        if subject is not None:
            self.subject = subject
        if body is not None:
            self.body = body
        if created is not None:
            self.created = created
        if modified is not None:
            self.modified = modified

    @property
    def subject(self):
        """Gets the subject of this ShareMessageAttributes.  # noqa: E501

        Message subject.  # noqa: E501

        :return: The subject of this ShareMessageAttributes.  # noqa: E501
        :rtype: str
        """
        return self._subject

    @subject.setter
    def subject(self, subject):
        """Sets the subject of this ShareMessageAttributes.

        Message subject.  # noqa: E501

        :param subject: The subject of this ShareMessageAttributes.  # noqa: E501
        :type: str
        """

        self._subject = subject

    @property
    def body(self):
        """Gets the body of this ShareMessageAttributes.  # noqa: E501

        Message text.  # noqa: E501

        :return: The body of this ShareMessageAttributes.  # noqa: E501
        :rtype: str
        """
        return self._body

    @body.setter
    def body(self, body):
        """Sets the body of this ShareMessageAttributes.

        Message text.  # noqa: E501

        :param body: The body of this ShareMessageAttributes.  # noqa: E501
        :type: str
        """

        self._body = body

    @property
    def created(self):
        """Gets the created of this ShareMessageAttributes.  # noqa: E501

        Timestamp of message creation.  # noqa: E501

        :return: The created of this ShareMessageAttributes.  # noqa: E501
        :rtype: datetime
        """
        return self._created

    @created.setter
    def created(self, created):
        """Sets the created of this ShareMessageAttributes.

        Timestamp of message creation.  # noqa: E501

        :param created: The created of this ShareMessageAttributes.  # noqa: E501
        :type: datetime
        """

        self._created = created

    @property
    def modified(self):
        """Gets the modified of this ShareMessageAttributes.  # noqa: E501

        Timestamp of message modification.  # noqa: E501

        :return: The modified of this ShareMessageAttributes.  # noqa: E501
        :rtype: datetime
        """
        return self._modified

    @modified.setter
    def modified(self, modified):
        """Sets the modified of this ShareMessageAttributes.

        Timestamp of message modification.  # noqa: E501

        :param modified: The modified of this ShareMessageAttributes.  # noqa: E501
        :type: datetime
        """

        self._modified = modified

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
        if issubclass(ShareMessageAttributes, dict):
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
        if not isinstance(other, ShareMessageAttributes):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
