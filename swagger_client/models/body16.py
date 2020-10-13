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

class Body16(object):
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
        'type': 'str',
        'name': 'str',
        'resources': 'list[str]',
        'access_mode': 'list[str]',
        'embed': 'bool',
        'recipients': 'list[SharesRecipients]',
        'expiration': 'datetime',
        'has_notification': 'bool',
        'is_public': 'bool',
        'message': 'str',
        'notification_emails': 'list[str]',
        'password': 'str',
        'require_email': 'bool',
        'subject': 'str',
        'file_drop_create_folders': 'bool',
        'sending_local_files': 'bool'
    }

    attribute_map = {
        'type': 'type',
        'name': 'name',
        'resources': 'resources',
        'access_mode': 'accessMode',
        'embed': 'embed',
        'recipients': 'recipients',
        'expiration': 'expiration',
        'has_notification': 'hasNotification',
        'is_public': 'isPublic',
        'message': 'message',
        'notification_emails': 'notificationEmails',
        'password': 'password',
        'require_email': 'requireEmail',
        'subject': 'subject',
        'file_drop_create_folders': 'fileDropCreateFolders',
        'sending_local_files': 'sendingLocalFiles'
    }

    def __init__(self, type=None, name=None, resources=None, access_mode=None, embed=None, recipients=None, expiration=None, has_notification=None, is_public=None, message=None, notification_emails=None, password=None, require_email=None, subject=None, file_drop_create_folders=None, sending_local_files=None):  # noqa: E501
        """Body16 - a model defined in Swagger"""  # noqa: E501
        self._type = None
        self._name = None
        self._resources = None
        self._access_mode = None
        self._embed = None
        self._recipients = None
        self._expiration = None
        self._has_notification = None
        self._is_public = None
        self._message = None
        self._notification_emails = None
        self._password = None
        self._require_email = None
        self._subject = None
        self._file_drop_create_folders = None
        self._sending_local_files = None
        self.discriminator = None
        self.type = type
        self.name = name
        if resources is not None:
            self.resources = resources
        self.access_mode = access_mode
        if embed is not None:
            self.embed = embed
        if recipients is not None:
            self.recipients = recipients
        if expiration is not None:
            self.expiration = expiration
        if has_notification is not None:
            self.has_notification = has_notification
        if is_public is not None:
            self.is_public = is_public
        if message is not None:
            self.message = message
        if notification_emails is not None:
            self.notification_emails = notification_emails
        if password is not None:
            self.password = password
        if require_email is not None:
            self.require_email = require_email
        if subject is not None:
            self.subject = subject
        if file_drop_create_folders is not None:
            self.file_drop_create_folders = file_drop_create_folders
        if sending_local_files is not None:
            self.sending_local_files = sending_local_files

    @property
    def type(self):
        """Gets the type of this Body16.  # noqa: E501

        The type of share to create. See above for a description of each.  # noqa: E501

        :return: The type of this Body16.  # noqa: E501
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this Body16.

        The type of share to create. See above for a description of each.  # noqa: E501

        :param type: The type of this Body16.  # noqa: E501
        :type: str
        """
        if type is None:
            raise ValueError("Invalid value for `type`, must not be `None`")  # noqa: E501
        allowed_values = ["shared_folder", "receive", "send"]  # noqa: E501
        if type not in allowed_values:
            raise ValueError(
                "Invalid value for `type` ({0}), must be one of {1}"  # noqa: E501
                .format(type, allowed_values)
            )

        self._type = type

    @property
    def name(self):
        """Gets the name of this Body16.  # noqa: E501

        A name for the share. This will be visible on the page that recipients visit.   # noqa: E501

        :return: The name of this Body16.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this Body16.

        A name for the share. This will be visible on the page that recipients visit.   # noqa: E501

        :param name: The name of this Body16.  # noqa: E501
        :type: str
        """
        if name is None:
            raise ValueError("Invalid value for `name`, must not be `None`")  # noqa: E501

        self._name = name

    @property
    def resources(self):
        """Gets the resources of this Body16.  # noqa: E501

        Array of resources for this share. See details on [how to specify resources](#section/Identifying-Resources) above.  **shared_folder** and **receive** shares must have only one `resource`, which is a directory that does not have a current share attached.  **send** shares may have multiple `resource` parameters. You can also leave this parameter null if you are planning to upload files to the send. If you are planning to upload files to the send that are not yet in your account, you will also need to call the [POST /shares/complete-send/{id}](#operation/completeDirectSend) endpoint to finish the send operation.   # noqa: E501

        :return: The resources of this Body16.  # noqa: E501
        :rtype: list[str]
        """
        return self._resources

    @resources.setter
    def resources(self, resources):
        """Sets the resources of this Body16.

        Array of resources for this share. See details on [how to specify resources](#section/Identifying-Resources) above.  **shared_folder** and **receive** shares must have only one `resource`, which is a directory that does not have a current share attached.  **send** shares may have multiple `resource` parameters. You can also leave this parameter null if you are planning to upload files to the send. If you are planning to upload files to the send that are not yet in your account, you will also need to call the [POST /shares/complete-send/{id}](#operation/completeDirectSend) endpoint to finish the send operation.   # noqa: E501

        :param resources: The resources of this Body16.  # noqa: E501
        :type: list[str]
        """

        self._resources = resources

    @property
    def access_mode(self):
        """Gets the access_mode of this Body16.  # noqa: E501

        Array of permissions that describes what people can do when they visit the share. Valid options are `upload` `download` `modify` and `delete`  Not all permissions work with all shares - **receive** shares must always have the permission to **upload** and never provide a method for visitors to **download**.  If you are creating a share of type **send** and plan to upload files from your own computer before completing the send with [POST /shares/complete-send/{id}](#operation/completeDirectSend), use the access mode **upload**  # noqa: E501

        :return: The access_mode of this Body16.  # noqa: E501
        :rtype: list[str]
        """
        return self._access_mode

    @access_mode.setter
    def access_mode(self, access_mode):
        """Sets the access_mode of this Body16.

        Array of permissions that describes what people can do when they visit the share. Valid options are `upload` `download` `modify` and `delete`  Not all permissions work with all shares - **receive** shares must always have the permission to **upload** and never provide a method for visitors to **download**.  If you are creating a share of type **send** and plan to upload files from your own computer before completing the send with [POST /shares/complete-send/{id}](#operation/completeDirectSend), use the access mode **upload**  # noqa: E501

        :param access_mode: The access_mode of this Body16.  # noqa: E501
        :type: list[str]
        """
        if access_mode is None:
            raise ValueError("Invalid value for `access_mode`, must not be `None`")  # noqa: E501

        self._access_mode = access_mode

    @property
    def embed(self):
        """Gets the embed of this Body16.  # noqa: E501

        Whether this share can be embedded within a web page.  # noqa: E501

        :return: The embed of this Body16.  # noqa: E501
        :rtype: bool
        """
        return self._embed

    @embed.setter
    def embed(self, embed):
        """Sets the embed of this Body16.

        Whether this share can be embedded within a web page.  # noqa: E501

        :param embed: The embed of this Body16.  # noqa: E501
        :type: bool
        """

        self._embed = embed

    @property
    def recipients(self):
        """Gets the recipients of this Body16.  # noqa: E501

        People you want to invite to the share. **Note**: unless you also set the `subject` and `message` for the new share, invitation emails will not be sent to these recipients.  # noqa: E501

        :return: The recipients of this Body16.  # noqa: E501
        :rtype: list[SharesRecipients]
        """
        return self._recipients

    @recipients.setter
    def recipients(self, recipients):
        """Sets the recipients of this Body16.

        People you want to invite to the share. **Note**: unless you also set the `subject` and `message` for the new share, invitation emails will not be sent to these recipients.  # noqa: E501

        :param recipients: The recipients of this Body16.  # noqa: E501
        :type: list[SharesRecipients]
        """

        self._recipients = recipients

    @property
    def expiration(self):
        """Gets the expiration of this Body16.  # noqa: E501

        Expiration date for the share. If someone attempts to use the share after this date, they will receive an error that the share is not available.  # noqa: E501

        :return: The expiration of this Body16.  # noqa: E501
        :rtype: datetime
        """
        return self._expiration

    @expiration.setter
    def expiration(self, expiration):
        """Sets the expiration of this Body16.

        Expiration date for the share. If someone attempts to use the share after this date, they will receive an error that the share is not available.  # noqa: E501

        :param expiration: The expiration of this Body16.  # noqa: E501
        :type: datetime
        """

        self._expiration = expiration

    @property
    def has_notification(self):
        """Gets the has_notification of this Body16.  # noqa: E501

        Whether delivery receipts should be sent.  # noqa: E501

        :return: The has_notification of this Body16.  # noqa: E501
        :rtype: bool
        """
        return self._has_notification

    @has_notification.setter
    def has_notification(self, has_notification):
        """Sets the has_notification of this Body16.

        Whether delivery receipts should be sent.  # noqa: E501

        :param has_notification: The has_notification of this Body16.  # noqa: E501
        :type: bool
        """

        self._has_notification = has_notification

    @property
    def is_public(self):
        """Gets the is_public of this Body16.  # noqa: E501

        Whether someone can visit the share without following a personalized recipient link.  # noqa: E501

        :return: The is_public of this Body16.  # noqa: E501
        :rtype: bool
        """
        return self._is_public

    @is_public.setter
    def is_public(self, is_public):
        """Sets the is_public of this Body16.

        Whether someone can visit the share without following a personalized recipient link.  # noqa: E501

        :param is_public: The is_public of this Body16.  # noqa: E501
        :type: bool
        """

        self._is_public = is_public

    @property
    def message(self):
        """Gets the message of this Body16.  # noqa: E501

        The message to be included in email invitations for your recipients. Ignored if you have not also provided `recipients` and `subject`  # noqa: E501

        :return: The message of this Body16.  # noqa: E501
        :rtype: str
        """
        return self._message

    @message.setter
    def message(self, message):
        """Sets the message of this Body16.

        The message to be included in email invitations for your recipients. Ignored if you have not also provided `recipients` and `subject`  # noqa: E501

        :param message: The message of this Body16.  # noqa: E501
        :type: str
        """

        self._message = message

    @property
    def notification_emails(self):
        """Gets the notification_emails of this Body16.  # noqa: E501

        Emails that will receive delivery receipts for this share. `hasNotification` must be **true** for delivery receipts will be sent.  # noqa: E501

        :return: The notification_emails of this Body16.  # noqa: E501
        :rtype: list[str]
        """
        return self._notification_emails

    @notification_emails.setter
    def notification_emails(self, notification_emails):
        """Sets the notification_emails of this Body16.

        Emails that will receive delivery receipts for this share. `hasNotification` must be **true** for delivery receipts will be sent.  # noqa: E501

        :param notification_emails: The notification_emails of this Body16.  # noqa: E501
        :type: list[str]
        """

        self._notification_emails = notification_emails

    @property
    def password(self):
        """Gets the password of this Body16.  # noqa: E501

        Set a password for recipients to access the share. All recipients will use the same password.  # noqa: E501

        :return: The password of this Body16.  # noqa: E501
        :rtype: str
        """
        return self._password

    @password.setter
    def password(self, password):
        """Sets the password of this Body16.

        Set a password for recipients to access the share. All recipients will use the same password.  # noqa: E501

        :param password: The password of this Body16.  # noqa: E501
        :type: str
        """

        self._password = password

    @property
    def require_email(self):
        """Gets the require_email of this Body16.  # noqa: E501

        True if recipients must provide their email to view the share.  # noqa: E501

        :return: The require_email of this Body16.  # noqa: E501
        :rtype: bool
        """
        return self._require_email

    @require_email.setter
    def require_email(self, require_email):
        """Sets the require_email of this Body16.

        True if recipients must provide their email to view the share.  # noqa: E501

        :param require_email: The require_email of this Body16.  # noqa: E501
        :type: bool
        """

        self._require_email = require_email

    @property
    def subject(self):
        """Gets the subject of this Body16.  # noqa: E501

        Subject to use on emails inviting recipients to the share. Ignored if you have not also provided `recipients` and a `message`  # noqa: E501

        :return: The subject of this Body16.  # noqa: E501
        :rtype: str
        """
        return self._subject

    @subject.setter
    def subject(self, subject):
        """Sets the subject of this Body16.

        Subject to use on emails inviting recipients to the share. Ignored if you have not also provided `recipients` and a `message`  # noqa: E501

        :param subject: The subject of this Body16.  # noqa: E501
        :type: str
        """

        self._subject = subject

    @property
    def file_drop_create_folders(self):
        """Gets the file_drop_create_folders of this Body16.  # noqa: E501

        Only used for **receive** shares. If true, uploads will be automatically placed into sub-folders of the folder, named after the chosen field on your form.   # noqa: E501

        :return: The file_drop_create_folders of this Body16.  # noqa: E501
        :rtype: bool
        """
        return self._file_drop_create_folders

    @file_drop_create_folders.setter
    def file_drop_create_folders(self, file_drop_create_folders):
        """Sets the file_drop_create_folders of this Body16.

        Only used for **receive** shares. If true, uploads will be automatically placed into sub-folders of the folder, named after the chosen field on your form.   # noqa: E501

        :param file_drop_create_folders: The file_drop_create_folders of this Body16.  # noqa: E501
        :type: bool
        """

        self._file_drop_create_folders = file_drop_create_folders

    @property
    def sending_local_files(self):
        """Gets the sending_local_files of this Body16.  # noqa: E501

        Use this only for **send** shares. Flag to indicate that you are going to upload additional files from your computer to the share. If this is **true**, you will also need to use the [POST /shares/complete-send/{id}](#operation/completeDirectSend) call to finish setting up your share after the files are uploaded.  # noqa: E501

        :return: The sending_local_files of this Body16.  # noqa: E501
        :rtype: bool
        """
        return self._sending_local_files

    @sending_local_files.setter
    def sending_local_files(self, sending_local_files):
        """Sets the sending_local_files of this Body16.

        Use this only for **send** shares. Flag to indicate that you are going to upload additional files from your computer to the share. If this is **true**, you will also need to use the [POST /shares/complete-send/{id}](#operation/completeDirectSend) call to finish setting up your share after the files are uploaded.  # noqa: E501

        :param sending_local_files: The sending_local_files of this Body16.  # noqa: E501
        :type: bool
        """

        self._sending_local_files = sending_local_files

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
        if issubclass(Body16, dict):
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
        if not isinstance(other, Body16):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other