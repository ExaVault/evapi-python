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

class NotificationRecipient(object):
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
        'notification_id': 'int',
        'email': 'str',
        'created': 'datetime',
        'modified': 'datetime'
    }

    attribute_map = {
        'id': 'id',
        'notification_id': 'notificationId',
        'email': 'email',
        'created': 'created',
        'modified': 'modified'
    }

    def __init__(self, id=None, notification_id=None, email=None, created=None, modified=None):  # noqa: E501
        """NotificationRecipient - a model defined in Swagger"""  # noqa: E501
        self._id = None
        self._notification_id = None
        self._email = None
        self._created = None
        self._modified = None
        self.discriminator = None
        if id is not None:
            self.id = id
        if notification_id is not None:
            self.notification_id = notification_id
        if email is not None:
            self.email = email
        if created is not None:
            self.created = created
        if modified is not None:
            self.modified = modified

    @property
    def id(self):
        """Gets the id of this NotificationRecipient.  # noqa: E501

        ID of the recipient.  # noqa: E501

        :return: The id of this NotificationRecipient.  # noqa: E501
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this NotificationRecipient.

        ID of the recipient.  # noqa: E501

        :param id: The id of this NotificationRecipient.  # noqa: E501
        :type: int
        """

        self._id = id

    @property
    def notification_id(self):
        """Gets the notification_id of this NotificationRecipient.  # noqa: E501

        ID of the notification that the recipient belongs to.  # noqa: E501

        :return: The notification_id of this NotificationRecipient.  # noqa: E501
        :rtype: int
        """
        return self._notification_id

    @notification_id.setter
    def notification_id(self, notification_id):
        """Sets the notification_id of this NotificationRecipient.

        ID of the notification that the recipient belongs to.  # noqa: E501

        :param notification_id: The notification_id of this NotificationRecipient.  # noqa: E501
        :type: int
        """

        self._notification_id = notification_id

    @property
    def email(self):
        """Gets the email of this NotificationRecipient.  # noqa: E501

        Recipient email.  # noqa: E501

        :return: The email of this NotificationRecipient.  # noqa: E501
        :rtype: str
        """
        return self._email

    @email.setter
    def email(self, email):
        """Sets the email of this NotificationRecipient.

        Recipient email.  # noqa: E501

        :param email: The email of this NotificationRecipient.  # noqa: E501
        :type: str
        """

        self._email = email

    @property
    def created(self):
        """Gets the created of this NotificationRecipient.  # noqa: E501

        Timestamp of adding notification recipient.  # noqa: E501

        :return: The created of this NotificationRecipient.  # noqa: E501
        :rtype: datetime
        """
        return self._created

    @created.setter
    def created(self, created):
        """Sets the created of this NotificationRecipient.

        Timestamp of adding notification recipient.  # noqa: E501

        :param created: The created of this NotificationRecipient.  # noqa: E501
        :type: datetime
        """

        self._created = created

    @property
    def modified(self):
        """Gets the modified of this NotificationRecipient.  # noqa: E501

        Timestamp of notification recipient modification.  # noqa: E501

        :return: The modified of this NotificationRecipient.  # noqa: E501
        :rtype: datetime
        """
        return self._modified

    @modified.setter
    def modified(self, modified):
        """Sets the modified of this NotificationRecipient.

        Timestamp of notification recipient modification.  # noqa: E501

        :param modified: The modified of this NotificationRecipient.  # noqa: E501
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
        if issubclass(NotificationRecipient, dict):
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
        if not isinstance(other, NotificationRecipient):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
