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


class UserAttributes(object):
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
        'status': 'int',
        'expiration': 'str',
        'created': 'datetime',
        'modified': 'datetime',
        'access_timestamp': 'str',
        'account_name': 'str',
        'username': 'str',
        'nickname': 'str',
        'email': 'str',
        'home_dir': 'str',
        'permissions': 'UserPermissions',
        'role': 'str',
        'time_zone': 'str',
        'onboarding': 'bool',
        'first_login': 'bool'
    }

    attribute_map = {
        'status': 'status',
        'expiration': 'expiration',
        'created': 'created',
        'modified': 'modified',
        'access_timestamp': 'accessTimestamp',
        'account_name': 'accountName',
        'username': 'username',
        'nickname': 'nickname',
        'email': 'email',
        'home_dir': 'homeDir',
        'permissions': 'permissions',
        'role': 'role',
        'time_zone': 'timeZone',
        'onboarding': 'onboarding',
        'first_login': 'firstLogin'
    }

    def __init__(self, status=None, expiration=None, created=None, modified=None, access_timestamp=None, account_name=None, username=None, nickname=None, email=None, home_dir=None, permissions=None, role=None, time_zone=None, onboarding=None, first_login=None):  # noqa: E501
        """UserAttributes - a model defined in Swagger"""  # noqa: E501
        self._status = None
        self._expiration = None
        self._created = None
        self._modified = None
        self._access_timestamp = None
        self._account_name = None
        self._username = None
        self._nickname = None
        self._email = None
        self._home_dir = None
        self._permissions = None
        self._role = None
        self._time_zone = None
        self._onboarding = None
        self._first_login = None
        self.discriminator = None
        self.status = status
        if expiration is not None:
            self.expiration = expiration
        self.created = created
        self.modified = modified
        if access_timestamp is not None:
            self.access_timestamp = access_timestamp
        self.account_name = account_name
        self.username = username
        self.nickname = nickname
        if email is not None:
            self.email = email
        self.home_dir = home_dir
        self.permissions = permissions
        self.role = role
        self.time_zone = time_zone
        self.onboarding = onboarding
        if first_login is not None:
            self.first_login = first_login

    @property
    def status(self):
        """Gets the status of this UserAttributes.  # noqa: E501

        Indicates user activity status. `0` means the user is locked and cannot log in. `1` means the user is active and can log in.  # noqa: E501

        :return: The status of this UserAttributes.  # noqa: E501
        :rtype: int
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this UserAttributes.

        Indicates user activity status. `0` means the user is locked and cannot log in. `1` means the user is active and can log in.  # noqa: E501

        :param status: The status of this UserAttributes.  # noqa: E501
        :type: int
        """
        if status is None:
            raise ValueError("Invalid value for `status`, must not be `None`")  # noqa: E501
        allowed_values = [0, 1]  # noqa: E501
        if status not in allowed_values:
            raise ValueError(
                "Invalid value for `status` ({0}), must be one of {1}"  # noqa: E501
                .format(status, allowed_values)
            )

        self._status = status

    @property
    def expiration(self):
        """Gets the expiration of this UserAttributes.  # noqa: E501

        Timestamp of user expiration.  # noqa: E501

        :return: The expiration of this UserAttributes.  # noqa: E501
        :rtype: str
        """
        return self._expiration

    @expiration.setter
    def expiration(self, expiration):
        """Sets the expiration of this UserAttributes.

        Timestamp of user expiration.  # noqa: E501

        :param expiration: The expiration of this UserAttributes.  # noqa: E501
        :type: str
        """

        self._expiration = expiration

    @property
    def created(self):
        """Gets the created of this UserAttributes.  # noqa: E501

        Timestamp of user creation.  # noqa: E501

        :return: The created of this UserAttributes.  # noqa: E501
        :rtype: datetime
        """
        return self._created

    @created.setter
    def created(self, created):
        """Sets the created of this UserAttributes.

        Timestamp of user creation.  # noqa: E501

        :param created: The created of this UserAttributes.  # noqa: E501
        :type: datetime
        """
        if created is None:
            raise ValueError("Invalid value for `created`, must not be `None`")  # noqa: E501

        self._created = created

    @property
    def modified(self):
        """Gets the modified of this UserAttributes.  # noqa: E501

        Timestamp of user modification.  # noqa: E501

        :return: The modified of this UserAttributes.  # noqa: E501
        :rtype: datetime
        """
        return self._modified

    @modified.setter
    def modified(self, modified):
        """Sets the modified of this UserAttributes.

        Timestamp of user modification.  # noqa: E501

        :param modified: The modified of this UserAttributes.  # noqa: E501
        :type: datetime
        """
        if modified is None:
            raise ValueError("Invalid value for `modified`, must not be `None`")  # noqa: E501

        self._modified = modified

    @property
    def access_timestamp(self):
        """Gets the access_timestamp of this UserAttributes.  # noqa: E501

        Timestamp of most recent successful user login.  # noqa: E501

        :return: The access_timestamp of this UserAttributes.  # noqa: E501
        :rtype: str
        """
        return self._access_timestamp

    @access_timestamp.setter
    def access_timestamp(self, access_timestamp):
        """Sets the access_timestamp of this UserAttributes.

        Timestamp of most recent successful user login.  # noqa: E501

        :param access_timestamp: The access_timestamp of this UserAttributes.  # noqa: E501
        :type: str
        """

        self._access_timestamp = access_timestamp

    @property
    def account_name(self):
        """Gets the account_name of this UserAttributes.  # noqa: E501

        Name of the account this user belongs to.  # noqa: E501

        :return: The account_name of this UserAttributes.  # noqa: E501
        :rtype: str
        """
        return self._account_name

    @account_name.setter
    def account_name(self, account_name):
        """Sets the account_name of this UserAttributes.

        Name of the account this user belongs to.  # noqa: E501

        :param account_name: The account_name of this UserAttributes.  # noqa: E501
        :type: str
        """
        if account_name is None:
            raise ValueError("Invalid value for `account_name`, must not be `None`")  # noqa: E501

        self._account_name = account_name

    @property
    def username(self):
        """Gets the username of this UserAttributes.  # noqa: E501

        Username of the user.  # noqa: E501

        :return: The username of this UserAttributes.  # noqa: E501
        :rtype: str
        """
        return self._username

    @username.setter
    def username(self, username):
        """Sets the username of this UserAttributes.

        Username of the user.  # noqa: E501

        :param username: The username of this UserAttributes.  # noqa: E501
        :type: str
        """
        if username is None:
            raise ValueError("Invalid value for `username`, must not be `None`")  # noqa: E501

        self._username = username

    @property
    def nickname(self):
        """Gets the nickname of this UserAttributes.  # noqa: E501

        Nickname of the user.  # noqa: E501

        :return: The nickname of this UserAttributes.  # noqa: E501
        :rtype: str
        """
        return self._nickname

    @nickname.setter
    def nickname(self, nickname):
        """Sets the nickname of this UserAttributes.

        Nickname of the user.  # noqa: E501

        :param nickname: The nickname of this UserAttributes.  # noqa: E501
        :type: str
        """
        if nickname is None:
            raise ValueError("Invalid value for `nickname`, must not be `None`")  # noqa: E501

        self._nickname = nickname

    @property
    def email(self):
        """Gets the email of this UserAttributes.  # noqa: E501

        Email address of the user.  # noqa: E501

        :return: The email of this UserAttributes.  # noqa: E501
        :rtype: str
        """
        return self._email

    @email.setter
    def email(self, email):
        """Sets the email of this UserAttributes.

        Email address of the user.  # noqa: E501

        :param email: The email of this UserAttributes.  # noqa: E501
        :type: str
        """

        self._email = email

    @property
    def home_dir(self):
        """Gets the home_dir of this UserAttributes.  # noqa: E501

        Path to the user's home folder.  # noqa: E501

        :return: The home_dir of this UserAttributes.  # noqa: E501
        :rtype: str
        """
        return self._home_dir

    @home_dir.setter
    def home_dir(self, home_dir):
        """Sets the home_dir of this UserAttributes.

        Path to the user's home folder.  # noqa: E501

        :param home_dir: The home_dir of this UserAttributes.  # noqa: E501
        :type: str
        """
        if home_dir is None:
            raise ValueError("Invalid value for `home_dir`, must not be `None`")  # noqa: E501

        self._home_dir = home_dir

    @property
    def permissions(self):
        """Gets the permissions of this UserAttributes.  # noqa: E501


        :return: The permissions of this UserAttributes.  # noqa: E501
        :rtype: UserPermissions
        """
        return self._permissions

    @permissions.setter
    def permissions(self, permissions):
        """Sets the permissions of this UserAttributes.


        :param permissions: The permissions of this UserAttributes.  # noqa: E501
        :type: UserPermissions
        """
        if permissions is None:
            raise ValueError("Invalid value for `permissions`, must not be `None`")  # noqa: E501

        self._permissions = permissions

    @property
    def role(self):
        """Gets the role of this UserAttributes.  # noqa: E501

        User's access level  # noqa: E501

        :return: The role of this UserAttributes.  # noqa: E501
        :rtype: str
        """
        return self._role

    @role.setter
    def role(self, role):
        """Sets the role of this UserAttributes.

        User's access level  # noqa: E501

        :param role: The role of this UserAttributes.  # noqa: E501
        :type: str
        """
        if role is None:
            raise ValueError("Invalid value for `role`, must not be `None`")  # noqa: E501
        allowed_values = ["user", "admin", "master"]  # noqa: E501
        if role not in allowed_values:
            raise ValueError(
                "Invalid value for `role` ({0}), must be one of {1}"  # noqa: E501
                .format(role, allowed_values)
            )

        self._role = role

    @property
    def time_zone(self):
        """Gets the time_zone of this UserAttributes.  # noqa: E501

        User's timezone. See <a href='https://php.net/manual/en/timezones.php' target='blank'>this page</a> for allowed values.  # noqa: E501

        :return: The time_zone of this UserAttributes.  # noqa: E501
        :rtype: str
        """
        return self._time_zone

    @time_zone.setter
    def time_zone(self, time_zone):
        """Sets the time_zone of this UserAttributes.

        User's timezone. See <a href='https://php.net/manual/en/timezones.php' target='blank'>this page</a> for allowed values.  # noqa: E501

        :param time_zone: The time_zone of this UserAttributes.  # noqa: E501
        :type: str
        """
        if time_zone is None:
            raise ValueError("Invalid value for `time_zone`, must not be `None`")  # noqa: E501

        self._time_zone = time_zone

    @property
    def onboarding(self):
        """Gets the onboarding of this UserAttributes.  # noqa: E501

        Whether the onboarding help system is enabled for this user. `true` means that additional help popups are displayed in the web application for this user.  # noqa: E501

        :return: The onboarding of this UserAttributes.  # noqa: E501
        :rtype: bool
        """
        return self._onboarding

    @onboarding.setter
    def onboarding(self, onboarding):
        """Sets the onboarding of this UserAttributes.

        Whether the onboarding help system is enabled for this user. `true` means that additional help popups are displayed in the web application for this user.  # noqa: E501

        :param onboarding: The onboarding of this UserAttributes.  # noqa: E501
        :type: bool
        """
        if onboarding is None:
            raise ValueError("Invalid value for `onboarding`, must not be `None`")  # noqa: E501

        self._onboarding = onboarding

    @property
    def first_login(self):
        """Gets the first_login of this UserAttributes.  # noqa: E501

        `true` if the user has logged into the system.  # noqa: E501

        :return: The first_login of this UserAttributes.  # noqa: E501
        :rtype: bool
        """
        return self._first_login

    @first_login.setter
    def first_login(self, first_login):
        """Sets the first_login of this UserAttributes.

        `true` if the user has logged into the system.  # noqa: E501

        :param first_login: The first_login of this UserAttributes.  # noqa: E501
        :type: bool
        """

        self._first_login = first_login

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
        if issubclass(UserAttributes, dict):
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
        if not isinstance(other, UserAttributes):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
