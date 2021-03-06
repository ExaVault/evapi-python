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

class NotificationAttributes(object):
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
        'user_id': 'str',
        'type': 'str',
        'path': 'str',
        'name': 'str',
        'action': 'str',
        'usernames': 'list[str]',
        'recipients': 'list[NotificationRecipient]',
        'send_email': 'bool',
        'readable_description': 'str',
        'readable_description_without_path': 'str',
        'share_id': 'str',
        'message': 'str',
        'created': 'datetime',
        'modified': 'datetime'
    }

    attribute_map = {
        'user_id': 'userId',
        'type': 'type',
        'path': 'path',
        'name': 'name',
        'action': 'action',
        'usernames': 'usernames',
        'recipients': 'recipients',
        'send_email': 'sendEmail',
        'readable_description': 'readableDescription',
        'readable_description_without_path': 'readableDescriptionWithoutPath',
        'share_id': 'shareId',
        'message': 'message',
        'created': 'created',
        'modified': 'modified'
    }

    def __init__(self, user_id=None, type=None, path=None, name=None, action=None, usernames=None, recipients=None, send_email=None, readable_description=None, readable_description_without_path=None, share_id=None, message=None, created=None, modified=None):  # noqa: E501
        """NotificationAttributes - a model defined in Swagger"""  # noqa: E501
        self._user_id = None
        self._type = None
        self._path = None
        self._name = None
        self._action = None
        self._usernames = None
        self._recipients = None
        self._send_email = None
        self._readable_description = None
        self._readable_description_without_path = None
        self._share_id = None
        self._message = None
        self._created = None
        self._modified = None
        self.discriminator = None
        if user_id is not None:
            self.user_id = user_id
        if type is not None:
            self.type = type
        if path is not None:
            self.path = path
        if name is not None:
            self.name = name
        if action is not None:
            self.action = action
        if usernames is not None:
            self.usernames = usernames
        if recipients is not None:
            self.recipients = recipients
        if send_email is not None:
            self.send_email = send_email
        if readable_description is not None:
            self.readable_description = readable_description
        if readable_description_without_path is not None:
            self.readable_description_without_path = readable_description_without_path
        if share_id is not None:
            self.share_id = share_id
        if message is not None:
            self.message = message
        if created is not None:
            self.created = created
        if modified is not None:
            self.modified = modified

    @property
    def user_id(self):
        """Gets the user_id of this NotificationAttributes.  # noqa: E501

        ID of the user that the notification belongs to.  # noqa: E501

        :return: The user_id of this NotificationAttributes.  # noqa: E501
        :rtype: str
        """
        return self._user_id

    @user_id.setter
    def user_id(self, user_id):
        """Sets the user_id of this NotificationAttributes.

        ID of the user that the notification belongs to.  # noqa: E501

        :param user_id: The user_id of this NotificationAttributes.  # noqa: E501
        :type: str
        """

        self._user_id = user_id

    @property
    def type(self):
        """Gets the type of this NotificationAttributes.  # noqa: E501

        Type of the resource the notification is attached to.   # noqa: E501

        :return: The type of this NotificationAttributes.  # noqa: E501
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this NotificationAttributes.

        Type of the resource the notification is attached to.   # noqa: E501

        :param type: The type of this NotificationAttributes.  # noqa: E501
        :type: str
        """
        allowed_values = ["file", "folder", "shared_folder", "send_receipt", "share_receipt", "file_drop"]  # noqa: E501
        if type not in allowed_values:
            raise ValueError(
                "Invalid value for `type` ({0}), must be one of {1}"  # noqa: E501
                .format(type, allowed_values)
            )

        self._type = type

    @property
    def path(self):
        """Gets the path of this NotificationAttributes.  # noqa: E501

        Path to the item that the notification is set on.  # noqa: E501

        :return: The path of this NotificationAttributes.  # noqa: E501
        :rtype: str
        """
        return self._path

    @path.setter
    def path(self, path):
        """Sets the path of this NotificationAttributes.

        Path to the item that the notification is set on.  # noqa: E501

        :param path: The path of this NotificationAttributes.  # noqa: E501
        :type: str
        """

        self._path = path

    @property
    def name(self):
        """Gets the name of this NotificationAttributes.  # noqa: E501

        Name of the item that the notification is set on.  # noqa: E501

        :return: The name of this NotificationAttributes.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this NotificationAttributes.

        Name of the item that the notification is set on.  # noqa: E501

        :param name: The name of this NotificationAttributes.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def action(self):
        """Gets the action of this NotificationAttributes.  # noqa: E501

        Action that triggers notification.  # noqa: E501

        :return: The action of this NotificationAttributes.  # noqa: E501
        :rtype: str
        """
        return self._action

    @action.setter
    def action(self, action):
        """Sets the action of this NotificationAttributes.

        Action that triggers notification.  # noqa: E501

        :param action: The action of this NotificationAttributes.  # noqa: E501
        :type: str
        """
        allowed_values = ["upload", "download", "delete", "all"]  # noqa: E501
        if action not in allowed_values:
            raise ValueError(
                "Invalid value for `action` ({0}), must be one of {1}"  # noqa: E501
                .format(action, allowed_values)
            )

        self._action = action

    @property
    def usernames(self):
        """Gets the usernames of this NotificationAttributes.  # noqa: E501

        Detail on which users can trigger the notification.  # noqa: E501

        :return: The usernames of this NotificationAttributes.  # noqa: E501
        :rtype: list[str]
        """
        return self._usernames

    @usernames.setter
    def usernames(self, usernames):
        """Sets the usernames of this NotificationAttributes.

        Detail on which users can trigger the notification.  # noqa: E501

        :param usernames: The usernames of this NotificationAttributes.  # noqa: E501
        :type: list[str]
        """

        self._usernames = usernames

    @property
    def recipients(self):
        """Gets the recipients of this NotificationAttributes.  # noqa: E501

        Notification recipients.  # noqa: E501

        :return: The recipients of this NotificationAttributes.  # noqa: E501
        :rtype: list[NotificationRecipient]
        """
        return self._recipients

    @recipients.setter
    def recipients(self, recipients):
        """Sets the recipients of this NotificationAttributes.

        Notification recipients.  # noqa: E501

        :param recipients: The recipients of this NotificationAttributes.  # noqa: E501
        :type: list[NotificationRecipient]
        """

        self._recipients = recipients

    @property
    def send_email(self):
        """Gets the send_email of this NotificationAttributes.  # noqa: E501

        Whether or not an email will send when the notification is triggered.  # noqa: E501

        :return: The send_email of this NotificationAttributes.  # noqa: E501
        :rtype: bool
        """
        return self._send_email

    @send_email.setter
    def send_email(self, send_email):
        """Sets the send_email of this NotificationAttributes.

        Whether or not an email will send when the notification is triggered.  # noqa: E501

        :param send_email: The send_email of this NotificationAttributes.  # noqa: E501
        :type: bool
        """

        self._send_email = send_email

    @property
    def readable_description(self):
        """Gets the readable_description of this NotificationAttributes.  # noqa: E501

        Human readable description of the notification.  # noqa: E501

        :return: The readable_description of this NotificationAttributes.  # noqa: E501
        :rtype: str
        """
        return self._readable_description

    @readable_description.setter
    def readable_description(self, readable_description):
        """Sets the readable_description of this NotificationAttributes.

        Human readable description of the notification.  # noqa: E501

        :param readable_description: The readable_description of this NotificationAttributes.  # noqa: E501
        :type: str
        """

        self._readable_description = readable_description

    @property
    def readable_description_without_path(self):
        """Gets the readable_description_without_path of this NotificationAttributes.  # noqa: E501

        Human readable description of the notification without item path.  # noqa: E501

        :return: The readable_description_without_path of this NotificationAttributes.  # noqa: E501
        :rtype: str
        """
        return self._readable_description_without_path

    @readable_description_without_path.setter
    def readable_description_without_path(self, readable_description_without_path):
        """Sets the readable_description_without_path of this NotificationAttributes.

        Human readable description of the notification without item path.  # noqa: E501

        :param readable_description_without_path: The readable_description_without_path of this NotificationAttributes.  # noqa: E501
        :type: str
        """

        self._readable_description_without_path = readable_description_without_path

    @property
    def share_id(self):
        """Gets the share_id of this NotificationAttributes.  # noqa: E501

        ID of the share that the notification belogns to.  # noqa: E501

        :return: The share_id of this NotificationAttributes.  # noqa: E501
        :rtype: str
        """
        return self._share_id

    @share_id.setter
    def share_id(self, share_id):
        """Sets the share_id of this NotificationAttributes.

        ID of the share that the notification belogns to.  # noqa: E501

        :param share_id: The share_id of this NotificationAttributes.  # noqa: E501
        :type: str
        """

        self._share_id = share_id

    @property
    def message(self):
        """Gets the message of this NotificationAttributes.  # noqa: E501

        Custom message that will be sent to the notification recipients.  # noqa: E501

        :return: The message of this NotificationAttributes.  # noqa: E501
        :rtype: str
        """
        return self._message

    @message.setter
    def message(self, message):
        """Sets the message of this NotificationAttributes.

        Custom message that will be sent to the notification recipients.  # noqa: E501

        :param message: The message of this NotificationAttributes.  # noqa: E501
        :type: str
        """

        self._message = message

    @property
    def created(self):
        """Gets the created of this NotificationAttributes.  # noqa: E501

        Timestamp of notifiction creation.  # noqa: E501

        :return: The created of this NotificationAttributes.  # noqa: E501
        :rtype: datetime
        """
        return self._created

    @created.setter
    def created(self, created):
        """Sets the created of this NotificationAttributes.

        Timestamp of notifiction creation.  # noqa: E501

        :param created: The created of this NotificationAttributes.  # noqa: E501
        :type: datetime
        """

        self._created = created

    @property
    def modified(self):
        """Gets the modified of this NotificationAttributes.  # noqa: E501

        Timestamp of notification modification.  # noqa: E501

        :return: The modified of this NotificationAttributes.  # noqa: E501
        :rtype: datetime
        """
        return self._modified

    @modified.setter
    def modified(self, modified):
        """Sets the modified of this NotificationAttributes.

        Timestamp of notification modification.  # noqa: E501

        :param modified: The modified of this NotificationAttributes.  # noqa: E501
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
        if issubclass(NotificationAttributes, dict):
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
        if not isinstance(other, NotificationAttributes):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
