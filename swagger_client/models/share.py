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


class Share(object):
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
        'name': 'str',
        'has_password': 'bool',
        'public': 'bool',
        'access_mode': 'str',
        'access_description': 'str',
        'embed': 'bool',
        'hash': 'str',
        'owner_hash': 'str',
        'expiration': 'str',
        'expired': 'bool',
        'resent': 'str',
        'owner': 'int',
        'owner_username': 'str',
        'type': 'str',
        'require_email': 'bool',
        'file_drop_create_folders': 'bool',
        'paths': 'list[str]',
        'recipients': 'list[ShareRecipient]',
        'recipients_with_owner': 'list[ShareRecipient]',
        'messages': 'list[Message]',
        'inherited': 'bool',
        'status': 'int',
        'has_notification': 'bool',
        'notification': 'str',
        'created': 'str',
        'modified': 'str'
    }

    attribute_map = {
        'id': 'id',
        'name': 'name',
        'has_password': 'hasPassword',
        'public': 'public',
        'access_mode': 'accessMode',
        'access_description': 'accessDescription',
        'embed': 'embed',
        'hash': 'hash',
        'owner_hash': 'ownerHash',
        'expiration': 'expiration',
        'expired': 'expired',
        'resent': 'resent',
        'owner': 'owner',
        'owner_username': 'ownerUsername',
        'type': 'type',
        'require_email': 'requireEmail',
        'file_drop_create_folders': 'fileDropCreateFolders',
        'paths': 'paths',
        'recipients': 'recipients',
        'recipients_with_owner': 'recipientsWithOwner',
        'messages': 'messages',
        'inherited': 'inherited',
        'status': 'status',
        'has_notification': 'hasNotification',
        'notification': 'notification',
        'created': 'created',
        'modified': 'modified'
    }

    def __init__(self, id=None, name=None, has_password=None, public=None, access_mode=None, access_description=None, embed=None, hash=None, owner_hash=None, expiration=None, expired=None, resent=None, owner=None, owner_username=None, type=None, require_email=None, file_drop_create_folders=None, paths=None, recipients=None, recipients_with_owner=None, messages=None, inherited=None, status=None, has_notification=None, notification=None, created=None, modified=None):
        """
        Share - a model defined in Swagger
        """

        self._id = None
        self._name = None
        self._has_password = None
        self._public = None
        self._access_mode = None
        self._access_description = None
        self._embed = None
        self._hash = None
        self._owner_hash = None
        self._expiration = None
        self._expired = None
        self._resent = None
        self._owner = None
        self._owner_username = None
        self._type = None
        self._require_email = None
        self._file_drop_create_folders = None
        self._paths = None
        self._recipients = None
        self._recipients_with_owner = None
        self._messages = None
        self._inherited = None
        self._status = None
        self._has_notification = None
        self._notification = None
        self._created = None
        self._modified = None

        if id is not None:
          self.id = id
        if name is not None:
          self.name = name
        if has_password is not None:
          self.has_password = has_password
        if public is not None:
          self.public = public
        if access_mode is not None:
          self.access_mode = access_mode
        if access_description is not None:
          self.access_description = access_description
        if embed is not None:
          self.embed = embed
        if hash is not None:
          self.hash = hash
        if owner_hash is not None:
          self.owner_hash = owner_hash
        if expiration is not None:
          self.expiration = expiration
        if expired is not None:
          self.expired = expired
        if resent is not None:
          self.resent = resent
        if owner is not None:
          self.owner = owner
        if owner_username is not None:
          self.owner_username = owner_username
        if type is not None:
          self.type = type
        if require_email is not None:
          self.require_email = require_email
        if file_drop_create_folders is not None:
          self.file_drop_create_folders = file_drop_create_folders
        if paths is not None:
          self.paths = paths
        if recipients is not None:
          self.recipients = recipients
        if recipients_with_owner is not None:
          self.recipients_with_owner = recipients_with_owner
        if messages is not None:
          self.messages = messages
        if inherited is not None:
          self.inherited = inherited
        if status is not None:
          self.status = status
        if has_notification is not None:
          self.has_notification = has_notification
        if notification is not None:
          self.notification = notification
        if created is not None:
          self.created = created
        if modified is not None:
          self.modified = modified

    @property
    def id(self):
        """
        Gets the id of this Share.
        ID of the share.

        :return: The id of this Share.
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """
        Sets the id of this Share.
        ID of the share.

        :param id: The id of this Share.
        :type: int
        """

        self._id = id

    @property
    def name(self):
        """
        Gets the name of this Share.
        Share name.

        :return: The name of this Share.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """
        Sets the name of this Share.
        Share name.

        :param name: The name of this Share.
        :type: str
        """

        self._name = name

    @property
    def has_password(self):
        """
        Gets the has_password of this Share.
        True if the share has password.

        :return: The has_password of this Share.
        :rtype: bool
        """
        return self._has_password

    @has_password.setter
    def has_password(self, has_password):
        """
        Sets the has_password of this Share.
        True if the share has password.

        :param has_password: The has_password of this Share.
        :type: bool
        """

        self._has_password = has_password

    @property
    def public(self):
        """
        Gets the public of this Share.
        True if the share has a public url.

        :return: The public of this Share.
        :rtype: bool
        """
        return self._public

    @public.setter
    def public(self, public):
        """
        Sets the public of this Share.
        True if the share has a public url.

        :param public: The public of this Share.
        :type: bool
        """

        self._public = public

    @property
    def access_mode(self):
        """
        Gets the access_mode of this Share.
        Access rights for the share.

        :return: The access_mode of this Share.
        :rtype: str
        """
        return self._access_mode

    @access_mode.setter
    def access_mode(self, access_mode):
        """
        Sets the access_mode of this Share.
        Access rights for the share.

        :param access_mode: The access_mode of this Share.
        :type: str
        """
        allowed_values = ["upload", "download", "download_upload", "download_upload_modify_delete"]
        if access_mode not in allowed_values:
            raise ValueError(
                "Invalid value for `access_mode` ({0}), must be one of {1}"
                .format(access_mode, allowed_values)
            )

        self._access_mode = access_mode

    @property
    def access_description(self):
        """
        Gets the access_description of this Share.
        Description of the share access rights.

        :return: The access_description of this Share.
        :rtype: str
        """
        return self._access_description

    @access_description.setter
    def access_description(self, access_description):
        """
        Sets the access_description of this Share.
        Description of the share access rights.

        :param access_description: The access_description of this Share.
        :type: str
        """

        self._access_description = access_description

    @property
    def embed(self):
        """
        Gets the embed of this Share.
        True if share can be embedded.

        :return: The embed of this Share.
        :rtype: bool
        """
        return self._embed

    @embed.setter
    def embed(self, embed):
        """
        Sets the embed of this Share.
        True if share can be embedded.

        :param embed: The embed of this Share.
        :type: bool
        """

        self._embed = embed

    @property
    def hash(self):
        """
        Gets the hash of this Share.
        Share hash.

        :return: The hash of this Share.
        :rtype: str
        """
        return self._hash

    @hash.setter
    def hash(self, hash):
        """
        Sets the hash of this Share.
        Share hash.

        :param hash: The hash of this Share.
        :type: str
        """

        self._hash = hash

    @property
    def owner_hash(self):
        """
        Gets the owner_hash of this Share.
        Share owner's hash.

        :return: The owner_hash of this Share.
        :rtype: str
        """
        return self._owner_hash

    @owner_hash.setter
    def owner_hash(self, owner_hash):
        """
        Sets the owner_hash of this Share.
        Share owner's hash.

        :param owner_hash: The owner_hash of this Share.
        :type: str
        """

        self._owner_hash = owner_hash

    @property
    def expiration(self):
        """
        Gets the expiration of this Share.
        Expiration date of the share.

        :return: The expiration of this Share.
        :rtype: str
        """
        return self._expiration

    @expiration.setter
    def expiration(self, expiration):
        """
        Sets the expiration of this Share.
        Expiration date of the share.

        :param expiration: The expiration of this Share.
        :type: str
        """

        self._expiration = expiration

    @property
    def expired(self):
        """
        Gets the expired of this Share.
        True if the share has expired.

        :return: The expired of this Share.
        :rtype: bool
        """
        return self._expired

    @expired.setter
    def expired(self, expired):
        """
        Sets the expired of this Share.
        True if the share has expired.

        :param expired: The expired of this Share.
        :type: bool
        """

        self._expired = expired

    @property
    def resent(self):
        """
        Gets the resent of this Share.
        Invitations resent date. Can be `null` if resent never happened.

        :return: The resent of this Share.
        :rtype: str
        """
        return self._resent

    @resent.setter
    def resent(self, resent):
        """
        Sets the resent of this Share.
        Invitations resent date. Can be `null` if resent never happened.

        :param resent: The resent of this Share.
        :type: str
        """

        self._resent = resent

    @property
    def owner(self):
        """
        Gets the owner of this Share.
        ID of the share owner.

        :return: The owner of this Share.
        :rtype: int
        """
        return self._owner

    @owner.setter
    def owner(self, owner):
        """
        Sets the owner of this Share.
        ID of the share owner.

        :param owner: The owner of this Share.
        :type: int
        """

        self._owner = owner

    @property
    def owner_username(self):
        """
        Gets the owner_username of this Share.
        Username of share owner.

        :return: The owner_username of this Share.
        :rtype: str
        """
        return self._owner_username

    @owner_username.setter
    def owner_username(self, owner_username):
        """
        Sets the owner_username of this Share.
        Username of share owner.

        :param owner_username: The owner_username of this Share.
        :type: str
        """

        self._owner_username = owner_username

    @property
    def type(self):
        """
        Gets the type of this Share.
        Type of share.

        :return: The type of this Share.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """
        Sets the type of this Share.
        Type of share.

        :param type: The type of this Share.
        :type: str
        """
        allowed_values = ["shared_folder", "send", "receive"]
        if type not in allowed_values:
            raise ValueError(
                "Invalid value for `type` ({0}), must be one of {1}"
                .format(type, allowed_values)
            )

        self._type = type

    @property
    def require_email(self):
        """
        Gets the require_email of this Share.
        True if share requires email to access.

        :return: The require_email of this Share.
        :rtype: bool
        """
        return self._require_email

    @require_email.setter
    def require_email(self, require_email):
        """
        Sets the require_email of this Share.
        True if share requires email to access.

        :param require_email: The require_email of this Share.
        :type: bool
        """

        self._require_email = require_email

    @property
    def file_drop_create_folders(self):
        """
        Gets the file_drop_create_folders of this Share.
        Flag to show if separate folders should be created for each file upload to receive folder.

        :return: The file_drop_create_folders of this Share.
        :rtype: bool
        """
        return self._file_drop_create_folders

    @file_drop_create_folders.setter
    def file_drop_create_folders(self, file_drop_create_folders):
        """
        Sets the file_drop_create_folders of this Share.
        Flag to show if separate folders should be created for each file upload to receive folder.

        :param file_drop_create_folders: The file_drop_create_folders of this Share.
        :type: bool
        """

        self._file_drop_create_folders = file_drop_create_folders

    @property
    def paths(self):
        """
        Gets the paths of this Share.
        Path to the shared resource in your account.

        :return: The paths of this Share.
        :rtype: list[str]
        """
        return self._paths

    @paths.setter
    def paths(self, paths):
        """
        Sets the paths of this Share.
        Path to the shared resource in your account.

        :param paths: The paths of this Share.
        :type: list[str]
        """

        self._paths = paths

    @property
    def recipients(self):
        """
        Gets the recipients of this Share.
        Array of recipients.

        :return: The recipients of this Share.
        :rtype: list[ShareRecipient]
        """
        return self._recipients

    @recipients.setter
    def recipients(self, recipients):
        """
        Sets the recipients of this Share.
        Array of recipients.

        :param recipients: The recipients of this Share.
        :type: list[ShareRecipient]
        """

        self._recipients = recipients

    @property
    def recipients_with_owner(self):
        """
        Gets the recipients_with_owner of this Share.
        Array of recipients with owner.

        :return: The recipients_with_owner of this Share.
        :rtype: list[ShareRecipient]
        """
        return self._recipients_with_owner

    @recipients_with_owner.setter
    def recipients_with_owner(self, recipients_with_owner):
        """
        Sets the recipients_with_owner of this Share.
        Array of recipients with owner.

        :param recipients_with_owner: The recipients_with_owner of this Share.
        :type: list[ShareRecipient]
        """

        self._recipients_with_owner = recipients_with_owner

    @property
    def messages(self):
        """
        Gets the messages of this Share.
        Array of invitation messages.

        :return: The messages of this Share.
        :rtype: list[Message]
        """
        return self._messages

    @messages.setter
    def messages(self, messages):
        """
        Sets the messages of this Share.
        Array of invitation messages.

        :param messages: The messages of this Share.
        :type: list[Message]
        """

        self._messages = messages

    @property
    def inherited(self):
        """
        Gets the inherited of this Share.
        True if share inherited from parent folder.

        :return: The inherited of this Share.
        :rtype: bool
        """
        return self._inherited

    @inherited.setter
    def inherited(self, inherited):
        """
        Sets the inherited of this Share.
        True if share inherited from parent folder.

        :param inherited: The inherited of this Share.
        :type: bool
        """

        self._inherited = inherited

    @property
    def status(self):
        """
        Gets the status of this Share.
        Share activity status. Can be active (1) or deactivated (0).

        :return: The status of this Share.
        :rtype: int
        """
        return self._status

    @status.setter
    def status(self, status):
        """
        Sets the status of this Share.
        Share activity status. Can be active (1) or deactivated (0).

        :param status: The status of this Share.
        :type: int
        """
        allowed_values = [0, 1]
        if status not in allowed_values:
            raise ValueError(
                "Invalid value for `status` ({0}), must be one of {1}"
                .format(status, allowed_values)
            )

        self._status = status

    @property
    def has_notification(self):
        """
        Gets the has_notification of this Share.
        True if share has notification.

        :return: The has_notification of this Share.
        :rtype: bool
        """
        return self._has_notification

    @has_notification.setter
    def has_notification(self, has_notification):
        """
        Sets the has_notification of this Share.
        True if share has notification.

        :param has_notification: The has_notification of this Share.
        :type: bool
        """

        self._has_notification = has_notification

    @property
    def notification(self):
        """
        Gets the notification of this Share.
        Notification object if share has one.

        :return: The notification of this Share.
        :rtype: str
        """
        return self._notification

    @notification.setter
    def notification(self, notification):
        """
        Sets the notification of this Share.
        Notification object if share has one.

        :param notification: The notification of this Share.
        :type: str
        """

        self._notification = notification

    @property
    def created(self):
        """
        Gets the created of this Share.
        Timestamp of share creation.

        :return: The created of this Share.
        :rtype: str
        """
        return self._created

    @created.setter
    def created(self, created):
        """
        Sets the created of this Share.
        Timestamp of share creation.

        :param created: The created of this Share.
        :type: str
        """

        self._created = created

    @property
    def modified(self):
        """
        Gets the modified of this Share.
        Timestamp of share modification. Can be `null` if it wasn't modified.

        :return: The modified of this Share.
        :rtype: str
        """
        return self._modified

    @modified.setter
    def modified(self, modified):
        """
        Sets the modified of this Share.
        Timestamp of share modification. Can be `null` if it wasn't modified.

        :param modified: The modified of this Share.
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
        if not isinstance(other, Share):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
