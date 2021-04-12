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

class PlanDetails(object):
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
        'storage_add_on': 'int',
        'ip_whitelist': 'bool',
        'user_expiration': 'bool',
        'user_import': 'bool',
        'custom_domain': 'bool',
        'custom_name': 'bool',
        'color_schema': 'bool',
        'api_keys': 'int',
        'api_tokens': 'int',
        'ssh_keys': 'int',
        'direct_links': 'bool',
        'sharing_options': 'list[str]',
        'webhook_options': 'PlanDetailsWebhookOptions',
        'unlimited_users': 'bool'
    }

    attribute_map = {
        'storage_add_on': 'storageAddOn',
        'ip_whitelist': 'ipWhitelist',
        'user_expiration': 'userExpiration',
        'user_import': 'userImport',
        'custom_domain': 'customDomain',
        'custom_name': 'customName',
        'color_schema': 'colorSchema',
        'api_keys': 'apiKeys',
        'api_tokens': 'apiTokens',
        'ssh_keys': 'sshKeys',
        'direct_links': 'directLinks',
        'sharing_options': 'sharingOptions',
        'webhook_options': 'webhookOptions',
        'unlimited_users': 'unlimitedUsers'
    }

    def __init__(self, storage_add_on=None, ip_whitelist=None, user_expiration=None, user_import=None, custom_domain=None, custom_name=None, color_schema=None, api_keys=None, api_tokens=None, ssh_keys=None, direct_links=None, sharing_options=None, webhook_options=None, unlimited_users=None):  # noqa: E501
        """PlanDetails - a model defined in Swagger"""  # noqa: E501
        self._storage_add_on = None
        self._ip_whitelist = None
        self._user_expiration = None
        self._user_import = None
        self._custom_domain = None
        self._custom_name = None
        self._color_schema = None
        self._api_keys = None
        self._api_tokens = None
        self._ssh_keys = None
        self._direct_links = None
        self._sharing_options = None
        self._webhook_options = None
        self._unlimited_users = None
        self.discriminator = None
        if storage_add_on is not None:
            self.storage_add_on = storage_add_on
        if ip_whitelist is not None:
            self.ip_whitelist = ip_whitelist
        if user_expiration is not None:
            self.user_expiration = user_expiration
        if user_import is not None:
            self.user_import = user_import
        if custom_domain is not None:
            self.custom_domain = custom_domain
        if custom_name is not None:
            self.custom_name = custom_name
        if color_schema is not None:
            self.color_schema = color_schema
        if api_keys is not None:
            self.api_keys = api_keys
        if api_tokens is not None:
            self.api_tokens = api_tokens
        if ssh_keys is not None:
            self.ssh_keys = ssh_keys
        if direct_links is not None:
            self.direct_links = direct_links
        if sharing_options is not None:
            self.sharing_options = sharing_options
        if webhook_options is not None:
            self.webhook_options = webhook_options
        if unlimited_users is not None:
            self.unlimited_users = unlimited_users

    @property
    def storage_add_on(self):
        """Gets the storage_add_on of this PlanDetails.  # noqa: E501


        :return: The storage_add_on of this PlanDetails.  # noqa: E501
        :rtype: int
        """
        return self._storage_add_on

    @storage_add_on.setter
    def storage_add_on(self, storage_add_on):
        """Sets the storage_add_on of this PlanDetails.


        :param storage_add_on: The storage_add_on of this PlanDetails.  # noqa: E501
        :type: int
        """

        self._storage_add_on = storage_add_on

    @property
    def ip_whitelist(self):
        """Gets the ip_whitelist of this PlanDetails.  # noqa: E501


        :return: The ip_whitelist of this PlanDetails.  # noqa: E501
        :rtype: bool
        """
        return self._ip_whitelist

    @ip_whitelist.setter
    def ip_whitelist(self, ip_whitelist):
        """Sets the ip_whitelist of this PlanDetails.


        :param ip_whitelist: The ip_whitelist of this PlanDetails.  # noqa: E501
        :type: bool
        """

        self._ip_whitelist = ip_whitelist

    @property
    def user_expiration(self):
        """Gets the user_expiration of this PlanDetails.  # noqa: E501


        :return: The user_expiration of this PlanDetails.  # noqa: E501
        :rtype: bool
        """
        return self._user_expiration

    @user_expiration.setter
    def user_expiration(self, user_expiration):
        """Sets the user_expiration of this PlanDetails.


        :param user_expiration: The user_expiration of this PlanDetails.  # noqa: E501
        :type: bool
        """

        self._user_expiration = user_expiration

    @property
    def user_import(self):
        """Gets the user_import of this PlanDetails.  # noqa: E501


        :return: The user_import of this PlanDetails.  # noqa: E501
        :rtype: bool
        """
        return self._user_import

    @user_import.setter
    def user_import(self, user_import):
        """Sets the user_import of this PlanDetails.


        :param user_import: The user_import of this PlanDetails.  # noqa: E501
        :type: bool
        """

        self._user_import = user_import

    @property
    def custom_domain(self):
        """Gets the custom_domain of this PlanDetails.  # noqa: E501


        :return: The custom_domain of this PlanDetails.  # noqa: E501
        :rtype: bool
        """
        return self._custom_domain

    @custom_domain.setter
    def custom_domain(self, custom_domain):
        """Sets the custom_domain of this PlanDetails.


        :param custom_domain: The custom_domain of this PlanDetails.  # noqa: E501
        :type: bool
        """

        self._custom_domain = custom_domain

    @property
    def custom_name(self):
        """Gets the custom_name of this PlanDetails.  # noqa: E501


        :return: The custom_name of this PlanDetails.  # noqa: E501
        :rtype: bool
        """
        return self._custom_name

    @custom_name.setter
    def custom_name(self, custom_name):
        """Sets the custom_name of this PlanDetails.


        :param custom_name: The custom_name of this PlanDetails.  # noqa: E501
        :type: bool
        """

        self._custom_name = custom_name

    @property
    def color_schema(self):
        """Gets the color_schema of this PlanDetails.  # noqa: E501


        :return: The color_schema of this PlanDetails.  # noqa: E501
        :rtype: bool
        """
        return self._color_schema

    @color_schema.setter
    def color_schema(self, color_schema):
        """Sets the color_schema of this PlanDetails.


        :param color_schema: The color_schema of this PlanDetails.  # noqa: E501
        :type: bool
        """

        self._color_schema = color_schema

    @property
    def api_keys(self):
        """Gets the api_keys of this PlanDetails.  # noqa: E501


        :return: The api_keys of this PlanDetails.  # noqa: E501
        :rtype: int
        """
        return self._api_keys

    @api_keys.setter
    def api_keys(self, api_keys):
        """Sets the api_keys of this PlanDetails.


        :param api_keys: The api_keys of this PlanDetails.  # noqa: E501
        :type: int
        """

        self._api_keys = api_keys

    @property
    def api_tokens(self):
        """Gets the api_tokens of this PlanDetails.  # noqa: E501


        :return: The api_tokens of this PlanDetails.  # noqa: E501
        :rtype: int
        """
        return self._api_tokens

    @api_tokens.setter
    def api_tokens(self, api_tokens):
        """Sets the api_tokens of this PlanDetails.


        :param api_tokens: The api_tokens of this PlanDetails.  # noqa: E501
        :type: int
        """

        self._api_tokens = api_tokens

    @property
    def ssh_keys(self):
        """Gets the ssh_keys of this PlanDetails.  # noqa: E501


        :return: The ssh_keys of this PlanDetails.  # noqa: E501
        :rtype: int
        """
        return self._ssh_keys

    @ssh_keys.setter
    def ssh_keys(self, ssh_keys):
        """Sets the ssh_keys of this PlanDetails.


        :param ssh_keys: The ssh_keys of this PlanDetails.  # noqa: E501
        :type: int
        """

        self._ssh_keys = ssh_keys

    @property
    def direct_links(self):
        """Gets the direct_links of this PlanDetails.  # noqa: E501


        :return: The direct_links of this PlanDetails.  # noqa: E501
        :rtype: bool
        """
        return self._direct_links

    @direct_links.setter
    def direct_links(self, direct_links):
        """Sets the direct_links of this PlanDetails.


        :param direct_links: The direct_links of this PlanDetails.  # noqa: E501
        :type: bool
        """

        self._direct_links = direct_links

    @property
    def sharing_options(self):
        """Gets the sharing_options of this PlanDetails.  # noqa: E501


        :return: The sharing_options of this PlanDetails.  # noqa: E501
        :rtype: list[str]
        """
        return self._sharing_options

    @sharing_options.setter
    def sharing_options(self, sharing_options):
        """Sets the sharing_options of this PlanDetails.


        :param sharing_options: The sharing_options of this PlanDetails.  # noqa: E501
        :type: list[str]
        """

        self._sharing_options = sharing_options

    @property
    def webhook_options(self):
        """Gets the webhook_options of this PlanDetails.  # noqa: E501


        :return: The webhook_options of this PlanDetails.  # noqa: E501
        :rtype: PlanDetailsWebhookOptions
        """
        return self._webhook_options

    @webhook_options.setter
    def webhook_options(self, webhook_options):
        """Sets the webhook_options of this PlanDetails.


        :param webhook_options: The webhook_options of this PlanDetails.  # noqa: E501
        :type: PlanDetailsWebhookOptions
        """

        self._webhook_options = webhook_options

    @property
    def unlimited_users(self):
        """Gets the unlimited_users of this PlanDetails.  # noqa: E501


        :return: The unlimited_users of this PlanDetails.  # noqa: E501
        :rtype: bool
        """
        return self._unlimited_users

    @unlimited_users.setter
    def unlimited_users(self, unlimited_users):
        """Sets the unlimited_users of this PlanDetails.


        :param unlimited_users: The unlimited_users of this PlanDetails.  # noqa: E501
        :type: bool
        """

        self._unlimited_users = unlimited_users

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
        if issubclass(PlanDetails, dict):
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
        if not isinstance(other, PlanDetails):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
