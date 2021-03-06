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

class AccountAllowedIpRanges(object):
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
        'ip_start': 'str',
        'ip_end': 'str'
    }

    attribute_map = {
        'ip_start': 'ipStart',
        'ip_end': 'ipEnd'
    }

    def __init__(self, ip_start=None, ip_end=None):  # noqa: E501
        """AccountAllowedIpRanges - a model defined in Swagger"""  # noqa: E501
        self._ip_start = None
        self._ip_end = None
        self.discriminator = None
        if ip_start is not None:
            self.ip_start = ip_start
        if ip_end is not None:
            self.ip_end = ip_end

    @property
    def ip_start(self):
        """Gets the ip_start of this AccountAllowedIpRanges.  # noqa: E501


        :return: The ip_start of this AccountAllowedIpRanges.  # noqa: E501
        :rtype: str
        """
        return self._ip_start

    @ip_start.setter
    def ip_start(self, ip_start):
        """Sets the ip_start of this AccountAllowedIpRanges.


        :param ip_start: The ip_start of this AccountAllowedIpRanges.  # noqa: E501
        :type: str
        """

        self._ip_start = ip_start

    @property
    def ip_end(self):
        """Gets the ip_end of this AccountAllowedIpRanges.  # noqa: E501


        :return: The ip_end of this AccountAllowedIpRanges.  # noqa: E501
        :rtype: str
        """
        return self._ip_end

    @ip_end.setter
    def ip_end(self, ip_end):
        """Sets the ip_end of this AccountAllowedIpRanges.


        :param ip_end: The ip_end of this AccountAllowedIpRanges.  # noqa: E501
        :type: str
        """

        self._ip_end = ip_end

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
        if issubclass(AccountAllowedIpRanges, dict):
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
        if not isinstance(other, AccountAllowedIpRanges):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
