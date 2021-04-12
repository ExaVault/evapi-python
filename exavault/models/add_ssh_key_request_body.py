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

class AddSSHKeyRequestBody(object):
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
        'user_id': 'int',
        'public_key': 'str'
    }

    attribute_map = {
        'user_id': 'userId',
        'public_key': 'publicKey'
    }

    def __init__(self, user_id=None, public_key=None):  # noqa: E501
        """AddSSHKeyRequestBody - a model defined in Swagger"""  # noqa: E501
        self._user_id = None
        self._public_key = None
        self.discriminator = None
        self.user_id = user_id
        self.public_key = public_key

    @property
    def user_id(self):
        """Gets the user_id of this AddSSHKeyRequestBody.  # noqa: E501

        ID of the user to assign the new key to.   # noqa: E501

        :return: The user_id of this AddSSHKeyRequestBody.  # noqa: E501
        :rtype: int
        """
        return self._user_id

    @user_id.setter
    def user_id(self, user_id):
        """Sets the user_id of this AddSSHKeyRequestBody.

        ID of the user to assign the new key to.   # noqa: E501

        :param user_id: The user_id of this AddSSHKeyRequestBody.  # noqa: E501
        :type: int
        """
        if user_id is None:
            raise ValueError("Invalid value for `user_id`, must not be `None`")  # noqa: E501

        self._user_id = user_id

    @property
    def public_key(self):
        """Gets the public_key of this AddSSHKeyRequestBody.  # noqa: E501

        Public Key to provide ExaVault. You can provide the Public Key as formatted from the ssh-keygen command or a standard rfc-4716 format.   # noqa: E501

        :return: The public_key of this AddSSHKeyRequestBody.  # noqa: E501
        :rtype: str
        """
        return self._public_key

    @public_key.setter
    def public_key(self, public_key):
        """Sets the public_key of this AddSSHKeyRequestBody.

        Public Key to provide ExaVault. You can provide the Public Key as formatted from the ssh-keygen command or a standard rfc-4716 format.   # noqa: E501

        :param public_key: The public_key of this AddSSHKeyRequestBody.  # noqa: E501
        :type: str
        """
        if public_key is None:
            raise ValueError("Invalid value for `public_key`, must not be `None`")  # noqa: E501

        self._public_key = public_key

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
        if issubclass(AddSSHKeyRequestBody, dict):
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
        if not isinstance(other, AddSSHKeyRequestBody):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
