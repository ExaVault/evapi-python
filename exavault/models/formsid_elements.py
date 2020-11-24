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

class FormsidElements(object):
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
        'name': 'str',
        'order': 'int',
        'type': 'str',
        'settings': 'FormsidSettings'
    }

    attribute_map = {
        'id': 'id',
        'name': 'name',
        'order': 'order',
        'type': 'type',
        'settings': 'settings'
    }

    def __init__(self, id=None, name=None, order=None, type=None, settings=None):  # noqa: E501
        """FormsidElements - a model defined in Swagger"""  # noqa: E501
        self._id = None
        self._name = None
        self._order = None
        self._type = None
        self._settings = None
        self.discriminator = None
        if id is not None:
            self.id = id
        if name is not None:
            self.name = name
        if order is not None:
            self.order = order
        if type is not None:
            self.type = type
        if settings is not None:
            self.settings = settings

    @property
    def id(self):
        """Gets the id of this FormsidElements.  # noqa: E501

        ID of the form element. If you're adding a new element to the form, do not include this field.  # noqa: E501

        :return: The id of this FormsidElements.  # noqa: E501
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this FormsidElements.

        ID of the form element. If you're adding a new element to the form, do not include this field.  # noqa: E501

        :param id: The id of this FormsidElements.  # noqa: E501
        :type: int
        """

        self._id = id

    @property
    def name(self):
        """Gets the name of this FormsidElements.  # noqa: E501

        Name of the form element.  # noqa: E501

        :return: The name of this FormsidElements.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this FormsidElements.

        Name of the form element.  # noqa: E501

        :param name: The name of this FormsidElements.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def order(self):
        """Gets the order of this FormsidElements.  # noqa: E501

        The order the fields will be displayed to the recipient. Starts at 0.   # noqa: E501

        :return: The order of this FormsidElements.  # noqa: E501
        :rtype: int
        """
        return self._order

    @order.setter
    def order(self, order):
        """Sets the order of this FormsidElements.

        The order the fields will be displayed to the recipient. Starts at 0.   # noqa: E501

        :param order: The order of this FormsidElements.  # noqa: E501
        :type: int
        """

        self._order = order

    @property
    def type(self):
        """Gets the type of this FormsidElements.  # noqa: E501

        Type of form field to use.  # noqa: E501

        :return: The type of this FormsidElements.  # noqa: E501
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this FormsidElements.

        Type of form field to use.  # noqa: E501

        :param type: The type of this FormsidElements.  # noqa: E501
        :type: str
        """
        allowed_values = ["name", "email", "text", "textarea", "upload_area"]  # noqa: E501
        if type not in allowed_values:
            raise ValueError(
                "Invalid value for `type` ({0}), must be one of {1}"  # noqa: E501
                .format(type, allowed_values)
            )

        self._type = type

    @property
    def settings(self):
        """Gets the settings of this FormsidElements.  # noqa: E501


        :return: The settings of this FormsidElements.  # noqa: E501
        :rtype: FormsidSettings
        """
        return self._settings

    @settings.setter
    def settings(self, settings):
        """Sets the settings of this FormsidElements.


        :param settings: The settings of this FormsidElements.  # noqa: E501
        :type: FormsidSettings
        """

        self._settings = settings

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
        if issubclass(FormsidElements, dict):
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
        if not isinstance(other, FormsidElements):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
