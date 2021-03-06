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

class AddFolderRequestBody(object):
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
        'path': 'str',
        'name': 'str',
        'parent_resource': 'str'
    }

    attribute_map = {
        'path': 'path',
        'name': 'name',
        'parent_resource': 'parentResource'
    }

    def __init__(self, path=None, name=None, parent_resource=None):  # noqa: E501
        """AddFolderRequestBody - a model defined in Swagger"""  # noqa: E501
        self._path = None
        self._name = None
        self._parent_resource = None
        self.discriminator = None
        if path is not None:
            self.path = path
        if name is not None:
            self.name = name
        if parent_resource is not None:
            self.parent_resource = parent_resource

    @property
    def path(self):
        """Gets the path of this AddFolderRequestBody.  # noqa: E501

        Fully-qualified path to the new folder including folder's name  # noqa: E501

        :return: The path of this AddFolderRequestBody.  # noqa: E501
        :rtype: str
        """
        return self._path

    @path.setter
    def path(self, path):
        """Sets the path of this AddFolderRequestBody.

        Fully-qualified path to the new folder including folder's name  # noqa: E501

        :param path: The path of this AddFolderRequestBody.  # noqa: E501
        :type: str
        """

        self._path = path

    @property
    def name(self):
        """Gets the name of this AddFolderRequestBody.  # noqa: E501

        Name of the folder to create. Required if **path** is not used  # noqa: E501

        :return: The name of this AddFolderRequestBody.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this AddFolderRequestBody.

        Name of the folder to create. Required if **path** is not used  # noqa: E501

        :param name: The name of this AddFolderRequestBody.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def parent_resource(self):
        """Gets the parent_resource of this AddFolderRequestBody.  # noqa: E501

        Resource identifier where to create a folder. Required if **path** is not used  # noqa: E501

        :return: The parent_resource of this AddFolderRequestBody.  # noqa: E501
        :rtype: str
        """
        return self._parent_resource

    @parent_resource.setter
    def parent_resource(self, parent_resource):
        """Sets the parent_resource of this AddFolderRequestBody.

        Resource identifier where to create a folder. Required if **path** is not used  # noqa: E501

        :param parent_resource: The parent_resource of this AddFolderRequestBody.  # noqa: E501
        :type: str
        """

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
        if issubclass(AddFolderRequestBody, dict):
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
        if not isinstance(other, AddFolderRequestBody):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
