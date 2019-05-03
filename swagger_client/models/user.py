# coding: utf-8

"""
    ExaVault API

    # Introduction  Welcome to the ExaVault API documentation. Our API lets you control nearly all aspects of your ExaVault account programatically, from uploading and downloading files to creating and managing shares and notifications. Our API supports both GET and POST operations.  Capabilities of the API include:  - Uploading and downloading files. - Managing files and folders; including standard operations like move, copy and delete. - Getting information about activity occuring in your account. - Creating, updating and deleting users. - Creating and managing shares, including download-only shares and recieve folders.  - Setting up and managing notifications.  ## The API Endpoint  The ExaVault API is located at: https://api.exavault.com/v1.2/  # Testing w/ Postman  We've made it easy for you to test our API before you start full-scale development. Download [Postman](https://www.getpostman.com/) or the [Postman Chrome Extension](https://chrome.google.com/webstore/detail/postman/fhbjgbiflinjbdggehcddcbncdddomop?hl=en), and then download our Postman collection, below. [Obtain your API key](#section/Code-Libraries-and-Sample-PHP-Code/Obtain-your-API-key) and you'll be able to interact with your ExaVault account immediately, so you can better understand what the capabilities of the API are.  <div class=\"postman-run-button\" data-postman-action=\"collection/import\" data-postman-var-1=\"e13395afc6278ce1555f\"></div>  ![ExaVault API Postman Colletion Usage](/images/postman.png)  If you'd prefer to skip Postman and start working with code directly, take a look at the sample code below.    # Code Libraries & Sample PHP Code  Once you're ready for full-scale development, we recommend looking at our code libraries available on [GitHub](https://github.com/ExaVault). We offer code libraries for [Python](https://github.com/ExaVault/evapi-python), [PHP](https://github.com/ExaVault/evapi-php) and [JavaScript](https://github.com/ExaVault/evapi-javascript).  While we recommend using our libraries, you're welcome to interact directly with our API via HTTP GET and POST requests -- a great option particularly if you're developing in a language for which we don't yet have sample code.     - [Download Python Library &amp; Sample Code &raquo;](https://github.com/ExaVault/evapi-python) - [Download PHP Library &amp; Sample Code &raquo;](https://github.com/ExaVault/evapi-php) - [Download JavaScript Library &amp; Sample Code &raquo;](https://github.com/ExaVault/evapi-javascript)  *Note: You can generate client libraries for any language using [Swagger Editor](http://editor2.swagger.io/). Just download our documentation file, past it into editor and use 'Generate Client' dropdown.*  ## Obtain Your API Key  You will need to obtain an API key for your application from the [Client Area](https://clients.exavault.com/clientarea.php?action=products) of your account.  To obtain an API key, please follow the instructions below.   + Login to the [Accounts](https://clients.exavault.com/clientarea.php?action=products) section of the Client Area.  + Use the drop down next to your desired account, and select *Manage API Keys*.  + You will be brought to the API Key management screen. Fill out the form and save to generate a new key for your app.  *NOTE: As of Oct 2017, we are in the progress of migrating customers to our next generation platform. If your account is already on our new platform, you should log into your File Manager and create your API key under Account->Developer->Manage API Keys*.  # Status Codes  The ExaVault API returns only two HTTP status codes for its responses: 200 and 500.  When the request could be successfully processed by the endpoint, the response status code will be 200, regardless of whether the requested action could be taken.  For example, the response to a getUser request for a username that does not exist in your account would have the status of 200,  indicating that the response was received and processed, but the error member of the returned response object would contain object with `message` and `code` properties.  **Result Format:**  |Success   | Error     | Results   | | ---      | :---:       |  :---:      | | 0        |  `Object` |   Empty   | | 1        |   Empty       |    `Object` or `Array`        |     When a malformed request is received, a 500 HTTP status code will be returned, indicating that the request could not be processed.  ExaVault's API does not currently support traditional REST response codes such as '201 Created' or '405 Method Not Allowed', although we intend to support such codes a future version of the API.   # File Paths  Many API calls require you to provide one or more file paths. For example, the <a href=\"#operation/moveResources\">moveResources</a> call requires both an array of source paths, **filePaths**, and a destination path, **destinationPath**. Here's a few tips for working with paths:   - File paths should always be specified as a string, using the standard Unix format: e.g. `/path/to/a/file.txt`  - File paths are always absolute _from the home directory of the logged in user_. For example, if the user **bob** had a home directory restriction of `/bob_home`, then an API call made using his login would specify a file as `/myfile.txt`, whereas an API call made using the master user ( no home directory restriction ) would specify the same file as `/bob_home/myfile.txt`.  # API Rate Limits  We rate limit the number of API calls you can make to help prevent abuse and protect system stablity. Each API key will support 500 requests per rolling five minutes. If you make more than 500 requests in a five minute period, you will receive a response with an error object for fifteen minutes.  # Webhooks  A webhook is an HTTP callback: a simple event-notification via HTTP POST. If you define webhooks for Exavault, ExaVault will POST a  message to a URL when certain things happen.     Webhooks can be used to receive a JSON object to your endpoint URL. You choose what events will trigger webhook messages to your endpoint URL.     Webhooks will attempt to send a message up to 8 times with increasing timeouts between each attempt. All webhook requests are tracked in the webhooks log.  ## Getting Started  1. Go to the Account tab inside SWFT.  2. Choose the Developer tab.  3. Configure your endpoint URL and select the events you want to trigger webhook messages.  4. Save settings.    You are all set to receive webhook callbacks on the events you selected.  ## Verification Signature  ExaVault includes a custom HTTP header, X-Exavault-Signature, with webhooks POST requests which will contain the signature for the request.  You can use the signature to verify the request for an additional level of security.  ## Generating the Signature  1. Go to Account tab inside SWFT.  2. Choose the Developer tab.  3. Obtain the verification token. This field will only be shown if you've configured your endpoint URL.  4. In your code that receives or processes the webhooks, you should concatenate the verification token with the JSON object that we sent in our      POST request and hash it with md5.     ```     md5($verificationToken.$webhooksObject);     ```  5. Compare signature that you generated to the signature provided in the X-Exavault-Signature HTTP header  ## Example JSON Response Object  ```json   {     \"accountname\": \"mycompanyname\",     \"username\": \"john\"     \"operation\": \"Upload\",     \"protocol\": \"https\",     \"path\": \"/testfolder/filename.jpg\"     \"attempt\": 1   } ```  ## Webhooks Logs  Keep track of all your webhooks requests in the Activity section of your account. You can find the following info for each request:    1. date and time - timestamp of the request.    2. endpoint url - where the webhook was sent.    3. event - what triggered the webhook.    4. status - HTTP status or curl error code.    5. attempt - how many times we tried to send this request.    6. response size - size of the response from your server.    7. details - you can check the response body if it was sent. 

    OpenAPI spec version: 1.0.1
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from pprint import pformat
from six import iteritems
import re


class User(object):
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
        'gid': 'int',
        'status': 'int',
        'expiration': 'str',
        'created': 'str',
        'modified': 'str',
        'access_timestamp': 'str',
        'id': 'int',
        'owning_account_id': 'int',
        'username': 'str',
        'nickname': 'str',
        'email': 'str',
        'home_dir': 'str',
        'download': 'bool',
        'upload': 'bool',
        'modify': 'bool',
        'delete': 'bool',
        'list': 'bool',
        'change_password': 'bool',
        'share': 'bool',
        'notification': 'bool',
        'role': 'str',
        'time_zone': 'str'
    }

    attribute_map = {
        'gid': 'gid',
        'status': 'status',
        'expiration': 'expiration',
        'created': 'created',
        'modified': 'modified',
        'access_timestamp': 'accessTimestamp',
        'id': 'id',
        'owning_account_id': 'owningAccountId',
        'username': 'username',
        'nickname': 'nickname',
        'email': 'email',
        'home_dir': 'homeDir',
        'download': 'download',
        'upload': 'upload',
        'modify': 'modify',
        'delete': 'delete',
        'list': 'list',
        'change_password': 'changePassword',
        'share': 'share',
        'notification': 'notification',
        'role': 'role',
        'time_zone': 'timeZone'
    }

    def __init__(self, gid=None, status=None, expiration=None, created=None, modified=None, access_timestamp=None, id=None, owning_account_id=None, username=None, nickname=None, email=None, home_dir=None, download=None, upload=None, modify=None, delete=None, list=None, change_password=None, share=None, notification=None, role=None, time_zone=None):
        """
        User - a model defined in Swagger
        """

        self._gid = None
        self._status = None
        self._expiration = None
        self._created = None
        self._modified = None
        self._access_timestamp = None
        self._id = None
        self._owning_account_id = None
        self._username = None
        self._nickname = None
        self._email = None
        self._home_dir = None
        self._download = None
        self._upload = None
        self._modify = None
        self._delete = None
        self._list = None
        self._change_password = None
        self._share = None
        self._notification = None
        self._role = None
        self._time_zone = None

        if gid is not None:
          self.gid = gid
        if status is not None:
          self.status = status
        if expiration is not None:
          self.expiration = expiration
        if created is not None:
          self.created = created
        if modified is not None:
          self.modified = modified
        if access_timestamp is not None:
          self.access_timestamp = access_timestamp
        if id is not None:
          self.id = id
        if owning_account_id is not None:
          self.owning_account_id = owning_account_id
        if username is not None:
          self.username = username
        if nickname is not None:
          self.nickname = nickname
        if email is not None:
          self.email = email
        if home_dir is not None:
          self.home_dir = home_dir
        if download is not None:
          self.download = download
        if upload is not None:
          self.upload = upload
        if modify is not None:
          self.modify = modify
        if delete is not None:
          self.delete = delete
        if list is not None:
          self.list = list
        if change_password is not None:
          self.change_password = change_password
        if share is not None:
          self.share = share
        if notification is not None:
          self.notification = notification
        if role is not None:
          self.role = role
        if time_zone is not None:
          self.time_zone = time_zone

    @property
    def gid(self):
        """
        Gets the gid of this User.
        GID of the user.

        :return: The gid of this User.
        :rtype: int
        """
        return self._gid

    @gid.setter
    def gid(self, gid):
        """
        Sets the gid of this User.
        GID of the user.

        :param gid: The gid of this User.
        :type: int
        """

        self._gid = gid

    @property
    def status(self):
        """
        Gets the status of this User.
        Indicates user activity status.

        :return: The status of this User.
        :rtype: int
        """
        return self._status

    @status.setter
    def status(self, status):
        """
        Sets the status of this User.
        Indicates user activity status.

        :param status: The status of this User.
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
    def expiration(self):
        """
        Gets the expiration of this User.
        Timestamp of user expiration.

        :return: The expiration of this User.
        :rtype: str
        """
        return self._expiration

    @expiration.setter
    def expiration(self, expiration):
        """
        Sets the expiration of this User.
        Timestamp of user expiration.

        :param expiration: The expiration of this User.
        :type: str
        """

        self._expiration = expiration

    @property
    def created(self):
        """
        Gets the created of this User.
        Timestamp of user creation.

        :return: The created of this User.
        :rtype: str
        """
        return self._created

    @created.setter
    def created(self, created):
        """
        Sets the created of this User.
        Timestamp of user creation.

        :param created: The created of this User.
        :type: str
        """

        self._created = created

    @property
    def modified(self):
        """
        Gets the modified of this User.
        Timestamp of user modification.

        :return: The modified of this User.
        :rtype: str
        """
        return self._modified

    @modified.setter
    def modified(self, modified):
        """
        Sets the modified of this User.
        Timestamp of user modification.

        :param modified: The modified of this User.
        :type: str
        """

        self._modified = modified

    @property
    def access_timestamp(self):
        """
        Gets the access_timestamp of this User.
        Timestamp of user accesing the account.

        :return: The access_timestamp of this User.
        :rtype: str
        """
        return self._access_timestamp

    @access_timestamp.setter
    def access_timestamp(self, access_timestamp):
        """
        Sets the access_timestamp of this User.
        Timestamp of user accesing the account.

        :param access_timestamp: The access_timestamp of this User.
        :type: str
        """

        self._access_timestamp = access_timestamp

    @property
    def id(self):
        """
        Gets the id of this User.
        ID of the user.

        :return: The id of this User.
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """
        Sets the id of this User.
        ID of the user.

        :param id: The id of this User.
        :type: int
        """

        self._id = id

    @property
    def owning_account_id(self):
        """
        Gets the owning_account_id of this User.
        ID of the account this user belongs to.

        :return: The owning_account_id of this User.
        :rtype: int
        """
        return self._owning_account_id

    @owning_account_id.setter
    def owning_account_id(self, owning_account_id):
        """
        Sets the owning_account_id of this User.
        ID of the account this user belongs to.

        :param owning_account_id: The owning_account_id of this User.
        :type: int
        """

        self._owning_account_id = owning_account_id

    @property
    def username(self):
        """
        Gets the username of this User.
        Username of the user.

        :return: The username of this User.
        :rtype: str
        """
        return self._username

    @username.setter
    def username(self, username):
        """
        Sets the username of this User.
        Username of the user.

        :param username: The username of this User.
        :type: str
        """

        self._username = username

    @property
    def nickname(self):
        """
        Gets the nickname of this User.
        Nickname of the user.

        :return: The nickname of this User.
        :rtype: str
        """
        return self._nickname

    @nickname.setter
    def nickname(self, nickname):
        """
        Sets the nickname of this User.
        Nickname of the user.

        :param nickname: The nickname of this User.
        :type: str
        """

        self._nickname = nickname

    @property
    def email(self):
        """
        Gets the email of this User.
        Email address of the user.

        :return: The email of this User.
        :rtype: str
        """
        return self._email

    @email.setter
    def email(self, email):
        """
        Sets the email of this User.
        Email address of the user.

        :param email: The email of this User.
        :type: str
        """

        self._email = email

    @property
    def home_dir(self):
        """
        Gets the home_dir of this User.
        Path to the user's home folder.

        :return: The home_dir of this User.
        :rtype: str
        """
        return self._home_dir

    @home_dir.setter
    def home_dir(self, home_dir):
        """
        Sets the home_dir of this User.
        Path to the user's home folder.

        :param home_dir: The home_dir of this User.
        :type: str
        """

        self._home_dir = home_dir

    @property
    def download(self):
        """
        Gets the download of this User.
        Download permission flag.

        :return: The download of this User.
        :rtype: bool
        """
        return self._download

    @download.setter
    def download(self, download):
        """
        Sets the download of this User.
        Download permission flag.

        :param download: The download of this User.
        :type: bool
        """

        self._download = download

    @property
    def upload(self):
        """
        Gets the upload of this User.
        Upload permission flag.

        :return: The upload of this User.
        :rtype: bool
        """
        return self._upload

    @upload.setter
    def upload(self, upload):
        """
        Sets the upload of this User.
        Upload permission flag.

        :param upload: The upload of this User.
        :type: bool
        """

        self._upload = upload

    @property
    def modify(self):
        """
        Gets the modify of this User.
        Modify permission flag.

        :return: The modify of this User.
        :rtype: bool
        """
        return self._modify

    @modify.setter
    def modify(self, modify):
        """
        Sets the modify of this User.
        Modify permission flag.

        :param modify: The modify of this User.
        :type: bool
        """

        self._modify = modify

    @property
    def delete(self):
        """
        Gets the delete of this User.
        Delete permission flag.

        :return: The delete of this User.
        :rtype: bool
        """
        return self._delete

    @delete.setter
    def delete(self, delete):
        """
        Sets the delete of this User.
        Delete permission flag.

        :param delete: The delete of this User.
        :type: bool
        """

        self._delete = delete

    @property
    def list(self):
        """
        Gets the list of this User.
        View files permission flag.

        :return: The list of this User.
        :rtype: bool
        """
        return self._list

    @list.setter
    def list(self, list):
        """
        Sets the list of this User.
        View files permission flag.

        :param list: The list of this User.
        :type: bool
        """

        self._list = list

    @property
    def change_password(self):
        """
        Gets the change_password of this User.
        Change permission flag.

        :return: The change_password of this User.
        :rtype: bool
        """
        return self._change_password

    @change_password.setter
    def change_password(self, change_password):
        """
        Sets the change_password of this User.
        Change permission flag.

        :param change_password: The change_password of this User.
        :type: bool
        """

        self._change_password = change_password

    @property
    def share(self):
        """
        Gets the share of this User.
        Share folders permission flag.

        :return: The share of this User.
        :rtype: bool
        """
        return self._share

    @share.setter
    def share(self, share):
        """
        Sets the share of this User.
        Share folders permission flag.

        :param share: The share of this User.
        :type: bool
        """

        self._share = share

    @property
    def notification(self):
        """
        Gets the notification of this User.
        Create notifications permission flag.

        :return: The notification of this User.
        :rtype: bool
        """
        return self._notification

    @notification.setter
    def notification(self, notification):
        """
        Sets the notification of this User.
        Create notifications permission flag.

        :param notification: The notification of this User.
        :type: bool
        """

        self._notification = notification

    @property
    def role(self):
        """
        Gets the role of this User.
        User's role.

        :return: The role of this User.
        :rtype: str
        """
        return self._role

    @role.setter
    def role(self, role):
        """
        Sets the role of this User.
        User's role.

        :param role: The role of this User.
        :type: str
        """

        self._role = role

    @property
    def time_zone(self):
        """
        Gets the time_zone of this User.
        User's timezone.

        :return: The time_zone of this User.
        :rtype: str
        """
        return self._time_zone

    @time_zone.setter
    def time_zone(self, time_zone):
        """
        Sets the time_zone of this User.
        User's timezone.

        :param time_zone: The time_zone of this User.
        :type: str
        """

        self._time_zone = time_zone

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
        if not isinstance(other, User):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
