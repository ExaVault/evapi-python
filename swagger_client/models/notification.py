# coding: utf-8

"""
    ExaVault API

    # Introduction  Welcome to the ExaVault API documentation. Our API lets you control nearly all aspects of your ExaVault account programatically, from uploading and downloading files to creating and managing shares and notifications. Our API supports both GET and POST operations.  Capabilities of the API include:  - Uploading and downloading files. - Managing files and folders; including standard operations like move, copy and delete. - Getting information about activity occuring in your account. - Creating, updating and deleting users. - Creating and managing shares, including download-only shares and recieve folders.  - Setting up and managing notifications.  ## The API Endpoint  The ExaVault API is located at: https://api.exavault.com/v1/  # Testing w/ Postman  We've made it easy for you to test our API before you start full-scale development. Download [Postman](https://www.getpostman.com/) or the [Postman Chrome Extension](https://chrome.google.com/webstore/detail/postman/fhbjgbiflinjbdggehcddcbncdddomop?hl=en), and then download our Postman collection, below. [Obtain your API key](#section/Code-Libraries-and-Sample-PHP-Code/Obtain-your-API-key) and you'll be able to interact with your ExaVault account immediately, so you can better understand what the capabilities of the API are.  <div class=\"postman-run-button\" data-postman-action=\"collection/import\" data-postman-var-1=\"e13395afc6278ce1555f\"></div>  ![ExaVault API Postman Colletion Usage](/images/postman.png)  If you'd prefer to skip Postman and start working with code directly, take a look at the sample code below.    # Code Libraries & Sample PHP Code  Once you're ready for full-scale development, we recommend looking at our code libraries available on [GitHub](https://github.com/ExaVault). We offer code libraries for [Python](https://github.com/ExaVault/evapi-python), [PHP](https://github.com/ExaVault/evapi-php) and [JavaScript](https://github.com/ExaVault/evapi-javascript).  While we recommend using our libraries, you're welcome to interact directly with our API via HTTP GET and POST requests -- a great option particularly if you're developing in a language for which we don't yet have sample code.     - [Download Python Library &amp; Sample Code &raquo;](https://github.com/ExaVault/evapi-python) - [Download PHP Library &amp; Sample Code &raquo;](https://github.com/ExaVault/evapi-php) - [Download JavaScript Library &amp; Sample Code &raquo;](https://github.com/ExaVault/evapi-javascript)  *Note: You can generate client libraries for any language using [Swagger Editor](http://editor2.swagger.io/). Just download our documentation file, past it into editor and use 'Generate Client' dropdown.*  ## Obtain Your API Key  You will need to obtain an API key for your application from the [Client Area](https://clients.exavault.com/clientarea.php?action=products) of your account.  To obtain an API key, please follow the instructions below.   + Login to the [Accounts](https://clients.exavault.com/clientarea.php?action=products) section of the Client Area.  + Use the drop down next to your desired account, and select *Manage API Keys*.  + You will be brought to the API Key management screen. Fill out the form and save to generate a new key for your app.  *NOTE: As of Oct 2017, we are in the progress of migrating customers to our next generation platform. If your account is already on our new platform, you should log into your File Manager and create your API key under Account->Developer->Manage API Keys*.  # Status Codes  The ExaVault API returns only two HTTP status codes for its responses: 200 and 500.  When the request could be successfully processed by the endpoint, the response status code will be 200, regardless of whether the requested action could be taken.  For example, the response to a getUser request for a username that does not exist in your account would have the status of 200,  indicating that the response was received and processed, but the error member of the returned response object would contain object with `message` and `code` properties.  **Result Format:**  |Success   | Error     | Results   | | ---      | :---:       |  :---:      | | 0        |  `Object` |   Empty   | | 1        |   Empty       |    `Object` or `Array`        |     When a malformed request is received, a 500 HTTP status code will be returned, indicating that the request could not be processed.  ExaVault's API does not currently support traditional REST response codes such as '201 Created' or '405 Method Not Allowed', although we intend to support such codes a future version of the API.   # File Paths  Many API calls require you to provide one or more file paths. For example, the <a href=\"#operation/moveResources\">moveResources</a> call requires both an array of source paths, **filePaths**, and a destination path, **destinationPath**. Here's a few tips for working with paths:   - File paths should always be specified as a string, using the standard Unix format: e.g. `/path/to/a/file.txt`  - File paths are always absolute _from the home directory of the logged in user_. For example, if the user **bob** had a home directory restriction of `/bob_home`, then an API call made using his login would specify a file as `/myfile.txt`, whereas an API call made using the master user ( no home directory restriction ) would specify the same file as `/bob_home/myfile.txt`.  # API Rate Limits  We rate limit the number of API calls you can make to help prevent abuse and protect system stablity. Each API key will support 500 requests per rolling five minutes. If you make more than 500 requests in a five minute period, you will receive a response with an error object for fifteen minutes.  # Webhooks  A webhook is an HTTP callback: a simple event-notification via HTTP POST. If you define webhooks for Exavault, ExaVault will POST a  message to a URL when certain things happen.     Webhooks can be used to receive a JSON object to your endpoint URL. You choose what events will trigger webhook messages to your endpoint URL.     Webhooks will attempt to send a message up to 8 times with increasing timeouts between each attempt. All webhook requests are tracked in the webhooks log.  ## Getting Started  1. Go to the Account tab inside SWFT.  2. Choose the Developer tab.  3. Configure your endpoint URL and select the events you want to trigger webhook messages.  4. Save settings.    You are all set to receive webhook callbacks on the events you selected.  ## Verification Signature  ExaVault includes a custom HTTP header, X-Exavault-Signature, with webhooks POST requests which will contain the signature for the request.  You can use the signature to verify the request for an additional level of security.  ## Generating the Signature  1. Go to Account tab inside SWFT.  2. Choose the Developer tab.  3. Obtain the verification token. This field will only be shown if you've configured your endpoint URL.  4. In your code that receives or processes the webhooks, you should concatenate the verification token with the JSON object that we sent in our      POST request and hash it with md5.     ```     md5($verificationToken.$webhooksObject);     ```  5. Compare signature that you generated to the signature provided in the X-Exavault-Signature HTTP header  ## Example JSON Response Object  ```json   {     \"accountname\": \"mycompanyname\",     \"username\": \"john\"     \"operation\": \"Upload\",     \"protocol\": \"https\",     \"path\": \"/testfolder/filename.jpg\"     \"attempt\": 1   } ```  ## Webhooks Logs  Keep track of all your webhooks requests in the Activity section of your account. You can find the following info for each request:    1. date and time - timestamp of the request.    2. endpoint url - where the webhook was sent.    3. event - what triggered the webhook.    4. status - HTTP status or curl error code.    5. attempt - how many times we tried to send this request.    6. response size - size of the response from your server.    7. details - you can check the response body if it was sent. 

    OpenAPI spec version: 1.0.1
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from pprint import pformat
from six import iteritems
import re


class Notification(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
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
        'user_id': 'str',
        'type': 'str',
        'path': 'str',
        'name': 'str',
        'action': 'str',
        'usernames': 'list[str]',
        'recipients': 'list[NotificationRecipient]',
        'recipient_emails': 'list[str]',
        'send_email': 'str',
        'readable_description': 'str',
        'readable_description_without_path': 'str',
        'share_id': 'str',
        'message': 'str',
        'created': 'str',
        'modified': 'str'
    }

    attribute_map = {
        'id': 'id',
        'user_id': 'userId',
        'type': 'type',
        'path': 'path',
        'name': 'name',
        'action': 'action',
        'usernames': 'usernames',
        'recipients': 'recipients',
        'recipient_emails': 'recipientEmails',
        'send_email': 'sendEmail',
        'readable_description': 'readableDescription',
        'readable_description_without_path': 'readableDescriptionWithoutPath',
        'share_id': 'shareId',
        'message': 'message',
        'created': 'created',
        'modified': 'modified'
    }

    def __init__(self, id=None, user_id=None, type=None, path=None, name=None, action=None, usernames=None, recipients=None, recipient_emails=None, send_email=None, readable_description=None, readable_description_without_path=None, share_id=None, message=None, created=None, modified=None):
        """
        Notification - a model defined in Swagger
        """

        self._id = None
        self._user_id = None
        self._type = None
        self._path = None
        self._name = None
        self._action = None
        self._usernames = None
        self._recipients = None
        self._recipient_emails = None
        self._send_email = None
        self._readable_description = None
        self._readable_description_without_path = None
        self._share_id = None
        self._message = None
        self._created = None
        self._modified = None

        if id is not None:
          self.id = id
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
        if recipient_emails is not None:
          self.recipient_emails = recipient_emails
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
    def id(self):
        """
        Gets the id of this Notification.
        ID of the notification.

        :return: The id of this Notification.
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """
        Sets the id of this Notification.
        ID of the notification.

        :param id: The id of this Notification.
        :type: int
        """

        self._id = id

    @property
    def user_id(self):
        """
        Gets the user_id of this Notification.
        ID of the user that the notification belongs to.

        :return: The user_id of this Notification.
        :rtype: str
        """
        return self._user_id

    @user_id.setter
    def user_id(self, user_id):
        """
        Sets the user_id of this Notification.
        ID of the user that the notification belongs to.

        :param user_id: The user_id of this Notification.
        :type: str
        """

        self._user_id = user_id

    @property
    def type(self):
        """
        Gets the type of this Notification.
        Notification type.

        :return: The type of this Notification.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """
        Sets the type of this Notification.
        Notification type.

        :param type: The type of this Notification.
        :type: str
        """
        allowed_values = ["file", "folder", "shared_folder", "send_receipt", "share_receipt", "file_drop"]
        if type not in allowed_values:
            raise ValueError(
                "Invalid value for `type` ({0}), must be one of {1}"
                .format(type, allowed_values)
            )

        self._type = type

    @property
    def path(self):
        """
        Gets the path of this Notification.
        Path to the item that the notification is set on.

        :return: The path of this Notification.
        :rtype: str
        """
        return self._path

    @path.setter
    def path(self, path):
        """
        Sets the path of this Notification.
        Path to the item that the notification is set on.

        :param path: The path of this Notification.
        :type: str
        """

        self._path = path

    @property
    def name(self):
        """
        Gets the name of this Notification.
        Name of the item that the notification is set on.

        :return: The name of this Notification.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """
        Sets the name of this Notification.
        Name of the item that the notification is set on.

        :param name: The name of this Notification.
        :type: str
        """

        self._name = name

    @property
    def action(self):
        """
        Gets the action of this Notification.
        Action that triggers notification.

        :return: The action of this Notification.
        :rtype: str
        """
        return self._action

    @action.setter
    def action(self, action):
        """
        Sets the action of this Notification.
        Action that triggers notification.

        :param action: The action of this Notification.
        :type: str
        """
        allowed_values = ["upload", "download", "delete", "all"]
        if action not in allowed_values:
            raise ValueError(
                "Invalid value for `action` ({0}), must be one of {1}"
                .format(action, allowed_values)
            )

        self._action = action

    @property
    def usernames(self):
        """
        Gets the usernames of this Notification.
        Detail on which users can trigger the notification.

        :return: The usernames of this Notification.
        :rtype: list[str]
        """
        return self._usernames

    @usernames.setter
    def usernames(self, usernames):
        """
        Sets the usernames of this Notification.
        Detail on which users can trigger the notification.

        :param usernames: The usernames of this Notification.
        :type: list[str]
        """

        self._usernames = usernames

    @property
    def recipients(self):
        """
        Gets the recipients of this Notification.
        Notification recipients.

        :return: The recipients of this Notification.
        :rtype: list[NotificationRecipient]
        """
        return self._recipients

    @recipients.setter
    def recipients(self, recipients):
        """
        Sets the recipients of this Notification.
        Notification recipients.

        :param recipients: The recipients of this Notification.
        :type: list[NotificationRecipient]
        """

        self._recipients = recipients

    @property
    def recipient_emails(self):
        """
        Gets the recipient_emails of this Notification.
        Email addresses of all recipients.

        :return: The recipient_emails of this Notification.
        :rtype: list[str]
        """
        return self._recipient_emails

    @recipient_emails.setter
    def recipient_emails(self, recipient_emails):
        """
        Sets the recipient_emails of this Notification.
        Email addresses of all recipients.

        :param recipient_emails: The recipient_emails of this Notification.
        :type: list[str]
        """

        self._recipient_emails = recipient_emails

    @property
    def send_email(self):
        """
        Gets the send_email of this Notification.
        Send email when the notification is triggered.

        :return: The send_email of this Notification.
        :rtype: str
        """
        return self._send_email

    @send_email.setter
    def send_email(self, send_email):
        """
        Sets the send_email of this Notification.
        Send email when the notification is triggered.

        :param send_email: The send_email of this Notification.
        :type: str
        """
        allowed_values = ["0", "1"]
        if send_email not in allowed_values:
            raise ValueError(
                "Invalid value for `send_email` ({0}), must be one of {1}"
                .format(send_email, allowed_values)
            )

        self._send_email = send_email

    @property
    def readable_description(self):
        """
        Gets the readable_description of this Notification.
        Human readable description of the notification.

        :return: The readable_description of this Notification.
        :rtype: str
        """
        return self._readable_description

    @readable_description.setter
    def readable_description(self, readable_description):
        """
        Sets the readable_description of this Notification.
        Human readable description of the notification.

        :param readable_description: The readable_description of this Notification.
        :type: str
        """

        self._readable_description = readable_description

    @property
    def readable_description_without_path(self):
        """
        Gets the readable_description_without_path of this Notification.
        Human readable description of the notification without item path.

        :return: The readable_description_without_path of this Notification.
        :rtype: str
        """
        return self._readable_description_without_path

    @readable_description_without_path.setter
    def readable_description_without_path(self, readable_description_without_path):
        """
        Sets the readable_description_without_path of this Notification.
        Human readable description of the notification without item path.

        :param readable_description_without_path: The readable_description_without_path of this Notification.
        :type: str
        """

        self._readable_description_without_path = readable_description_without_path

    @property
    def share_id(self):
        """
        Gets the share_id of this Notification.
        ID of the share that the notification belogns to.

        :return: The share_id of this Notification.
        :rtype: str
        """
        return self._share_id

    @share_id.setter
    def share_id(self, share_id):
        """
        Sets the share_id of this Notification.
        ID of the share that the notification belogns to.

        :param share_id: The share_id of this Notification.
        :type: str
        """

        self._share_id = share_id

    @property
    def message(self):
        """
        Gets the message of this Notification.
        Custom message that will be sent to the notification recipients.

        :return: The message of this Notification.
        :rtype: str
        """
        return self._message

    @message.setter
    def message(self, message):
        """
        Sets the message of this Notification.
        Custom message that will be sent to the notification recipients.

        :param message: The message of this Notification.
        :type: str
        """

        self._message = message

    @property
    def created(self):
        """
        Gets the created of this Notification.
        Timestamp of notifiction creation.

        :return: The created of this Notification.
        :rtype: str
        """
        return self._created

    @created.setter
    def created(self, created):
        """
        Sets the created of this Notification.
        Timestamp of notifiction creation.

        :param created: The created of this Notification.
        :type: str
        """

        self._created = created

    @property
    def modified(self):
        """
        Gets the modified of this Notification.
        Timestamp of notification modification.

        :return: The modified of this Notification.
        :rtype: str
        """
        return self._modified

    @modified.setter
    def modified(self, modified):
        """
        Sets the modified of this Notification.
        Timestamp of notification modification.

        :param modified: The modified of this Notification.
        :type: str
        """

        self._modified = modified

    def to_dict(self):
        """
        Returns the model properties as a dict
        """
        result = {}

        for attr, _ in iteritems(self.swagger_types):
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

        return result

    def to_str(self):
        """
        Returns the string representation of the model
        """
        return pformat(self.to_dict())

    def __repr__(self):
        """
        For `print` and `pprint`
        """
        return self.to_str()

    def __eq__(self, other):
        """
        Returns true if both objects are equal
        """
        if not isinstance(other, Notification):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
