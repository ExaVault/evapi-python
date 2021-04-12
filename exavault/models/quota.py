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

class Quota(object):
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
        'disk_limit': 'int',
        'disk_used': 'int',
        'notice_enabled': 'bool',
        'notice_threshold': 'int',
        'bandwidth_limit': 'int',
        'bandwidth_used': 'int',
        'transactions_limit': 'int',
        'transactions_notice_enabled': 'bool',
        'transactions_notice_threshold': 'int'
    }

    attribute_map = {
        'disk_limit': 'diskLimit',
        'disk_used': 'diskUsed',
        'notice_enabled': 'noticeEnabled',
        'notice_threshold': 'noticeThreshold',
        'bandwidth_limit': 'bandwidthLimit',
        'bandwidth_used': 'bandwidthUsed',
        'transactions_limit': 'transactionsLimit',
        'transactions_notice_enabled': 'transactionsNoticeEnabled',
        'transactions_notice_threshold': 'transactionsNoticeThreshold'
    }

    def __init__(self, disk_limit=None, disk_used=None, notice_enabled=None, notice_threshold=None, bandwidth_limit=None, bandwidth_used=None, transactions_limit=None, transactions_notice_enabled=None, transactions_notice_threshold=None):  # noqa: E501
        """Quota - a model defined in Swagger"""  # noqa: E501
        self._disk_limit = None
        self._disk_used = None
        self._notice_enabled = None
        self._notice_threshold = None
        self._bandwidth_limit = None
        self._bandwidth_used = None
        self._transactions_limit = None
        self._transactions_notice_enabled = None
        self._transactions_notice_threshold = None
        self.discriminator = None
        if disk_limit is not None:
            self.disk_limit = disk_limit
        if disk_used is not None:
            self.disk_used = disk_used
        if notice_enabled is not None:
            self.notice_enabled = notice_enabled
        if notice_threshold is not None:
            self.notice_threshold = notice_threshold
        if bandwidth_limit is not None:
            self.bandwidth_limit = bandwidth_limit
        if bandwidth_used is not None:
            self.bandwidth_used = bandwidth_used
        if transactions_limit is not None:
            self.transactions_limit = transactions_limit
        if transactions_notice_enabled is not None:
            self.transactions_notice_enabled = transactions_notice_enabled
        if transactions_notice_threshold is not None:
            self.transactions_notice_threshold = transactions_notice_threshold

    @property
    def disk_limit(self):
        """Gets the disk_limit of this Quota.  # noqa: E501

        Amount of disk space that the account has available to it. This may be increased by upgrading to a larger plan.  # noqa: E501

        :return: The disk_limit of this Quota.  # noqa: E501
        :rtype: int
        """
        return self._disk_limit

    @disk_limit.setter
    def disk_limit(self, disk_limit):
        """Sets the disk_limit of this Quota.

        Amount of disk space that the account has available to it. This may be increased by upgrading to a larger plan.  # noqa: E501

        :param disk_limit: The disk_limit of this Quota.  # noqa: E501
        :type: int
        """

        self._disk_limit = disk_limit

    @property
    def disk_used(self):
        """Gets the disk_used of this Quota.  # noqa: E501

        Amount of disk space currently in use.  # noqa: E501

        :return: The disk_used of this Quota.  # noqa: E501
        :rtype: int
        """
        return self._disk_used

    @disk_used.setter
    def disk_used(self, disk_used):
        """Sets the disk_used of this Quota.

        Amount of disk space currently in use.  # noqa: E501

        :param disk_used: The disk_used of this Quota.  # noqa: E501
        :type: int
        """

        self._disk_used = disk_used

    @property
    def notice_enabled(self):
        """Gets the notice_enabled of this Quota.  # noqa: E501

        Should a quota warning be sent to the account owner when a threshold level of space utilization is reached?  # noqa: E501

        :return: The notice_enabled of this Quota.  # noqa: E501
        :rtype: bool
        """
        return self._notice_enabled

    @notice_enabled.setter
    def notice_enabled(self, notice_enabled):
        """Sets the notice_enabled of this Quota.

        Should a quota warning be sent to the account owner when a threshold level of space utilization is reached?  # noqa: E501

        :param notice_enabled: The notice_enabled of this Quota.  # noqa: E501
        :type: bool
        """

        self._notice_enabled = notice_enabled

    @property
    def notice_threshold(self):
        """Gets the notice_threshold of this Quota.  # noqa: E501

        Treshold that triggers a quota notification. This represents the \"percent full\" your account must be before the quota notification is generated.  # noqa: E501

        :return: The notice_threshold of this Quota.  # noqa: E501
        :rtype: int
        """
        return self._notice_threshold

    @notice_threshold.setter
    def notice_threshold(self, notice_threshold):
        """Sets the notice_threshold of this Quota.

        Treshold that triggers a quota notification. This represents the \"percent full\" your account must be before the quota notification is generated.  # noqa: E501

        :param notice_threshold: The notice_threshold of this Quota.  # noqa: E501
        :type: int
        """

        self._notice_threshold = notice_threshold

    @property
    def bandwidth_limit(self):
        """Gets the bandwidth_limit of this Quota.  # noqa: E501

        Total number of bytes that can be transferred per month.  # noqa: E501

        :return: The bandwidth_limit of this Quota.  # noqa: E501
        :rtype: int
        """
        return self._bandwidth_limit

    @bandwidth_limit.setter
    def bandwidth_limit(self, bandwidth_limit):
        """Sets the bandwidth_limit of this Quota.

        Total number of bytes that can be transferred per month.  # noqa: E501

        :param bandwidth_limit: The bandwidth_limit of this Quota.  # noqa: E501
        :type: int
        """

        self._bandwidth_limit = bandwidth_limit

    @property
    def bandwidth_used(self):
        """Gets the bandwidth_used of this Quota.  # noqa: E501

        Number of bytes transferred this month.  # noqa: E501

        :return: The bandwidth_used of this Quota.  # noqa: E501
        :rtype: int
        """
        return self._bandwidth_used

    @bandwidth_used.setter
    def bandwidth_used(self, bandwidth_used):
        """Sets the bandwidth_used of this Quota.

        Number of bytes transferred this month.  # noqa: E501

        :param bandwidth_used: The bandwidth_used of this Quota.  # noqa: E501
        :type: int
        """

        self._bandwidth_used = bandwidth_used

    @property
    def transactions_limit(self):
        """Gets the transactions_limit of this Quota.  # noqa: E501

        Total number of transactions allowed in a 24-hour period.  # noqa: E501

        :return: The transactions_limit of this Quota.  # noqa: E501
        :rtype: int
        """
        return self._transactions_limit

    @transactions_limit.setter
    def transactions_limit(self, transactions_limit):
        """Sets the transactions_limit of this Quota.

        Total number of transactions allowed in a 24-hour period.  # noqa: E501

        :param transactions_limit: The transactions_limit of this Quota.  # noqa: E501
        :type: int
        """

        self._transactions_limit = transactions_limit

    @property
    def transactions_notice_enabled(self):
        """Gets the transactions_notice_enabled of this Quota.  # noqa: E501

        Whether an email should be sent to the account owner up to once per day if transaction usage exceeds `transactionsNoticeThreshold` value.  # noqa: E501

        :return: The transactions_notice_enabled of this Quota.  # noqa: E501
        :rtype: bool
        """
        return self._transactions_notice_enabled

    @transactions_notice_enabled.setter
    def transactions_notice_enabled(self, transactions_notice_enabled):
        """Sets the transactions_notice_enabled of this Quota.

        Whether an email should be sent to the account owner up to once per day if transaction usage exceeds `transactionsNoticeThreshold` value.  # noqa: E501

        :param transactions_notice_enabled: The transactions_notice_enabled of this Quota.  # noqa: E501
        :type: bool
        """

        self._transactions_notice_enabled = transactions_notice_enabled

    @property
    def transactions_notice_threshold(self):
        """Gets the transactions_notice_threshold of this Quota.  # noqa: E501

        Percent of daily transactions limit that will trigger an email if activity exceeds it.  # noqa: E501

        :return: The transactions_notice_threshold of this Quota.  # noqa: E501
        :rtype: int
        """
        return self._transactions_notice_threshold

    @transactions_notice_threshold.setter
    def transactions_notice_threshold(self, transactions_notice_threshold):
        """Sets the transactions_notice_threshold of this Quota.

        Percent of daily transactions limit that will trigger an email if activity exceeds it.  # noqa: E501

        :param transactions_notice_threshold: The transactions_notice_threshold of this Quota.  # noqa: E501
        :type: int
        """

        self._transactions_notice_threshold = transactions_notice_threshold

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
        if issubclass(Quota, dict):
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
        if not isinstance(other, Quota):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
