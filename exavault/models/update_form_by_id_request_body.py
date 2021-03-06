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

class UpdateFormByIdRequestBody(object):
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
        'form_description': 'str',
        'submit_button_text': 'str',
        'success_message': 'str',
        'elements': 'list[FormsidElements]',
        'css_styles': 'str'
    }

    attribute_map = {
        'form_description': 'formDescription',
        'submit_button_text': 'submitButtonText',
        'success_message': 'successMessage',
        'elements': 'elements',
        'css_styles': 'cssStyles'
    }

    def __init__(self, form_description=None, submit_button_text=None, success_message=None, elements=None, css_styles=None):  # noqa: E501
        """UpdateFormByIdRequestBody - a model defined in Swagger"""  # noqa: E501
        self._form_description = None
        self._submit_button_text = None
        self._success_message = None
        self._elements = None
        self._css_styles = None
        self.discriminator = None
        if form_description is not None:
            self.form_description = form_description
        if submit_button_text is not None:
            self.submit_button_text = submit_button_text
        if success_message is not None:
            self.success_message = success_message
        if elements is not None:
            self.elements = elements
        if css_styles is not None:
            self.css_styles = css_styles

    @property
    def form_description(self):
        """Gets the form_description of this UpdateFormByIdRequestBody.  # noqa: E501

        Set a description for the form that will be visible to recipients.   # noqa: E501

        :return: The form_description of this UpdateFormByIdRequestBody.  # noqa: E501
        :rtype: str
        """
        return self._form_description

    @form_description.setter
    def form_description(self, form_description):
        """Sets the form_description of this UpdateFormByIdRequestBody.

        Set a description for the form that will be visible to recipients.   # noqa: E501

        :param form_description: The form_description of this UpdateFormByIdRequestBody.  # noqa: E501
        :type: str
        """

        self._form_description = form_description

    @property
    def submit_button_text(self):
        """Gets the submit_button_text of this UpdateFormByIdRequestBody.  # noqa: E501

        Text to be displayed on the submission button.  # noqa: E501

        :return: The submit_button_text of this UpdateFormByIdRequestBody.  # noqa: E501
        :rtype: str
        """
        return self._submit_button_text

    @submit_button_text.setter
    def submit_button_text(self, submit_button_text):
        """Sets the submit_button_text of this UpdateFormByIdRequestBody.

        Text to be displayed on the submission button.  # noqa: E501

        :param submit_button_text: The submit_button_text of this UpdateFormByIdRequestBody.  # noqa: E501
        :type: str
        """

        self._submit_button_text = submit_button_text

    @property
    def success_message(self):
        """Gets the success_message of this UpdateFormByIdRequestBody.  # noqa: E501

        Text to be displayed when a recipient has submitted the form.   # noqa: E501

        :return: The success_message of this UpdateFormByIdRequestBody.  # noqa: E501
        :rtype: str
        """
        return self._success_message

    @success_message.setter
    def success_message(self, success_message):
        """Sets the success_message of this UpdateFormByIdRequestBody.

        Text to be displayed when a recipient has submitted the form.   # noqa: E501

        :param success_message: The success_message of this UpdateFormByIdRequestBody.  # noqa: E501
        :type: str
        """

        self._success_message = success_message

    @property
    def elements(self):
        """Gets the elements of this UpdateFormByIdRequestBody.  # noqa: E501


        :return: The elements of this UpdateFormByIdRequestBody.  # noqa: E501
        :rtype: list[FormsidElements]
        """
        return self._elements

    @elements.setter
    def elements(self, elements):
        """Sets the elements of this UpdateFormByIdRequestBody.


        :param elements: The elements of this UpdateFormByIdRequestBody.  # noqa: E501
        :type: list[FormsidElements]
        """

        self._elements = elements

    @property
    def css_styles(self):
        """Gets the css_styles of this UpdateFormByIdRequestBody.  # noqa: E501


        :return: The css_styles of this UpdateFormByIdRequestBody.  # noqa: E501
        :rtype: str
        """
        return self._css_styles

    @css_styles.setter
    def css_styles(self, css_styles):
        """Sets the css_styles of this UpdateFormByIdRequestBody.


        :param css_styles: The css_styles of this UpdateFormByIdRequestBody.  # noqa: E501
        :type: str
        """

        self._css_styles = css_styles

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
        if issubclass(UpdateFormByIdRequestBody, dict):
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
        if not isinstance(other, UpdateFormByIdRequestBody):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
