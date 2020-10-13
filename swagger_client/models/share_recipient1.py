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

class ShareRecipient1(object):
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
        'share_id': 'str',
        'type': 'str',
        'hash': 'str',
        'email': 'str',
        'sent': 'bool',
        'received': 'bool',
        'created': 'datetime'
    }

    attribute_map = {
        'id': 'id',
        'share_id': 'shareId',
        'type': 'type',
        'hash': 'hash',
        'email': 'email',
        'sent': 'sent',
        'received': 'received',
        'created': 'created'
    }

    def __init__(self, id=None, share_id=None, type=None, hash=None, email=None, sent=None, received=None, created=None):  # noqa: E501
        """ShareRecipient1 - a model defined in Swagger"""  # noqa: E501
        self._id = None
        self._share_id = None
        self._type = None
        self._hash = None
        self._email = None
        self._sent = None
        self._received = None
        self._created = None
        self.discriminator = None
        if id is not None:
            self.id = id
        if share_id is not None:
            self.share_id = share_id
        if type is not None:
            self.type = type
        if hash is not None:
            self.hash = hash
        if email is not None:
            self.email = email
        if sent is not None:
            self.sent = sent
        if received is not None:
            self.received = received
        if created is not None:
            self.created = created

    @property
    def id(self):
        """Gets the id of this ShareRecipient1.  # noqa: E501

        ID of the recipient.  # noqa: E501

        :return: The id of this ShareRecipient1.  # noqa: E501
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this ShareRecipient1.

        ID of the recipient.  # noqa: E501

        :param id: The id of this ShareRecipient1.  # noqa: E501
        :type: int
        """

        self._id = id

    @property
    def share_id(self):
        """Gets the share_id of this ShareRecipient1.  # noqa: E501

        ID of the share that the recipoient belongs to.  # noqa: E501

        :return: The share_id of this ShareRecipient1.  # noqa: E501
        :rtype: str
        """
        return self._share_id

    @share_id.setter
    def share_id(self, share_id):
        """Sets the share_id of this ShareRecipient1.

        ID of the share that the recipoient belongs to.  # noqa: E501

        :param share_id: The share_id of this ShareRecipient1.  # noqa: E501
        :type: str
        """

        self._share_id = share_id

    @property
    def type(self):
        """Gets the type of this ShareRecipient1.  # noqa: E501

        Type of the recipient.  # noqa: E501

        :return: The type of this ShareRecipient1.  # noqa: E501
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this ShareRecipient1.

        Type of the recipient.  # noqa: E501

        :param type: The type of this ShareRecipient1.  # noqa: E501
        :type: str
        """
        allowed_values = ["owner", "direct"]  # noqa: E501
        if type not in allowed_values:
            raise ValueError(
                "Invalid value for `type` ({0}), must be one of {1}"  # noqa: E501
                .format(type, allowed_values)
            )

        self._type = type

    @property
    def hash(self):
        """Gets the hash of this ShareRecipient1.  # noqa: E501

        Share hash.  # noqa: E501

        :return: The hash of this ShareRecipient1.  # noqa: E501
        :rtype: str
        """
        return self._hash

    @hash.setter
    def hash(self, hash):
        """Sets the hash of this ShareRecipient1.

        Share hash.  # noqa: E501

        :param hash: The hash of this ShareRecipient1.  # noqa: E501
        :type: str
        """

        self._hash = hash

    @property
    def email(self):
        """Gets the email of this ShareRecipient1.  # noqa: E501

        Recipient email address.  # noqa: E501

        :return: The email of this ShareRecipient1.  # noqa: E501
        :rtype: str
        """
        return self._email

    @email.setter
    def email(self, email):
        """Sets the email of this ShareRecipient1.

        Recipient email address.  # noqa: E501

        :param email: The email of this ShareRecipient1.  # noqa: E501
        :type: str
        """

        self._email = email

    @property
    def sent(self):
        """Gets the sent of this ShareRecipient1.  # noqa: E501

        Set to true if invite email was sent; false otherwise.  # noqa: E501

        :return: The sent of this ShareRecipient1.  # noqa: E501
        :rtype: bool
        """
        return self._sent

    @sent.setter
    def sent(self, sent):
        """Sets the sent of this ShareRecipient1.

        Set to true if invite email was sent; false otherwise.  # noqa: E501

        :param sent: The sent of this ShareRecipient1.  # noqa: E501
        :type: bool
        """

        self._sent = sent

    @property
    def received(self):
        """Gets the received of this ShareRecipient1.  # noqa: E501

        Set to true if recipient has accessed the share. Note this is set to true when the recipient clicks the link to access the share; not when they download a file.  # noqa: E501

        :return: The received of this ShareRecipient1.  # noqa: E501
        :rtype: bool
        """
        return self._received

    @received.setter
    def received(self, received):
        """Sets the received of this ShareRecipient1.

        Set to true if recipient has accessed the share. Note this is set to true when the recipient clicks the link to access the share; not when they download a file.  # noqa: E501

        :param received: The received of this ShareRecipient1.  # noqa: E501
        :type: bool
        """

        self._received = received

    @property
    def created(self):
        """Gets the created of this ShareRecipient1.  # noqa: E501

        Timestamp of adding recipient to the share.  # noqa: E501

        :return: The created of this ShareRecipient1.  # noqa: E501
        :rtype: datetime
        """
        return self._created

    @created.setter
    def created(self, created):
        """Sets the created of this ShareRecipient1.

        Timestamp of adding recipient to the share.  # noqa: E501

        :param created: The created of this ShareRecipient1.  # noqa: E501
        :type: datetime
        """

        self._created = created

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
        if issubclass(ShareRecipient1, dict):
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
        if not isinstance(other, ShareRecipient1):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
