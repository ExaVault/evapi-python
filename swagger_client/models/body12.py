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


class Body12(object):
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
        'resources': 'list[str]',
        'parent_resource': 'str'
    }

    attribute_map = {
        'resources': 'resources',
        'parent_resource': 'parentResource'
    }

    def __init__(self, resources=None, parent_resource=None):  # noqa: E501
        """Body12 - a model defined in Swagger"""  # noqa: E501
        self._resources = None
        self._parent_resource = None
        self.discriminator = None
        self.resources = resources
        self.parent_resource = parent_resource

    @property
    def resources(self):
        """Gets the resources of this Body12.  # noqa: E501

        Resource identifier(s) of items to be copied to a new location  # noqa: E501

        :return: The resources of this Body12.  # noqa: E501
        :rtype: list[str]
        """
        return self._resources

    @resources.setter
    def resources(self, resources):
        """Sets the resources of this Body12.

        Resource identifier(s) of items to be copied to a new location  # noqa: E501

        :param resources: The resources of this Body12.  # noqa: E501
        :type: list[str]
        """
        if resources is None:
            raise ValueError("Invalid value for `resources`, must not be `None`")  # noqa: E501

        self._resources = resources

    @property
    def parent_resource(self):
        """Gets the parent_resource of this Body12.  # noqa: E501

        Resource identifier for folder where items will be copied to.  # noqa: E501

        :return: The parent_resource of this Body12.  # noqa: E501
        :rtype: str
        """
        return self._parent_resource

    @parent_resource.setter
    def parent_resource(self, parent_resource):
        """Sets the parent_resource of this Body12.

        Resource identifier for folder where items will be copied to.  # noqa: E501

        :param parent_resource: The parent_resource of this Body12.  # noqa: E501
        :type: str
        """
        if parent_resource is None:
            raise ValueError("Invalid value for `parent_resource`, must not be `None`")  # noqa: E501

        self._parent_resource = parent_resource

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
        if issubclass(Body12, dict):
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
        if not isinstance(other, Body12):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
