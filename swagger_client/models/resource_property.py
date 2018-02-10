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


class ResourceProperty(object):
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
        'file_count': 'int',
        'extension': 'str',
        'name': 'str',
        'created_by': 'str',
        'upload_date': 'str',
        'parent': 'str',
        'path': 'str',
        'shares': 'list[Share]',
        'notification_settings': 'str',
        'size': 'int',
        'previewable': 'bool',
        'direct_file': 'str',
        'type': 'str'
    }

    attribute_map = {
        'file_count': 'fileCount',
        'extension': 'extension',
        'name': 'name',
        'created_by': 'createdBy',
        'upload_date': 'uploadDate',
        'parent': 'parent',
        'path': 'path',
        'shares': 'shares',
        'notification_settings': 'notificationSettings',
        'size': 'size',
        'previewable': 'previewable',
        'direct_file': 'directFile',
        'type': 'type'
    }

    def __init__(self, file_count=None, extension=None, name=None, created_by=None, upload_date=None, parent=None, path=None, shares=None, notification_settings=None, size=None, previewable=None, direct_file=None, type=None):
        """
        ResourceProperty - a model defined in Swagger
        """

        self._file_count = None
        self._extension = None
        self._name = None
        self._created_by = None
        self._upload_date = None
        self._parent = None
        self._path = None
        self._shares = None
        self._notification_settings = None
        self._size = None
        self._previewable = None
        self._direct_file = None
        self._type = None

        if file_count is not None:
          self.file_count = file_count
        if extension is not None:
          self.extension = extension
        if name is not None:
          self.name = name
        if created_by is not None:
          self.created_by = created_by
        if upload_date is not None:
          self.upload_date = upload_date
        if parent is not None:
          self.parent = parent
        if path is not None:
          self.path = path
        if shares is not None:
          self.shares = shares
        if notification_settings is not None:
          self.notification_settings = notification_settings
        if size is not None:
          self.size = size
        if previewable is not None:
          self.previewable = previewable
        if direct_file is not None:
          self.direct_file = direct_file
        if type is not None:
          self.type = type

    @property
    def file_count(self):
        """
        Gets the file_count of this ResourceProperty.
        Count of files in resource. Property exists only if resource `type` is folder.

        :return: The file_count of this ResourceProperty.
        :rtype: int
        """
        return self._file_count

    @file_count.setter
    def file_count(self, file_count):
        """
        Sets the file_count of this ResourceProperty.
        Count of files in resource. Property exists only if resource `type` is folder.

        :param file_count: The file_count of this ResourceProperty.
        :type: int
        """

        self._file_count = file_count

    @property
    def extension(self):
        """
        Gets the extension of this ResourceProperty.
        Resource extension. Property exists only if resource `type` is file.

        :return: The extension of this ResourceProperty.
        :rtype: str
        """
        return self._extension

    @extension.setter
    def extension(self, extension):
        """
        Sets the extension of this ResourceProperty.
        Resource extension. Property exists only if resource `type` is file.

        :param extension: The extension of this ResourceProperty.
        :type: str
        """

        self._extension = extension

    @property
    def name(self):
        """
        Gets the name of this ResourceProperty.
        Resource name, e.g. the name of the file or folder.

        :return: The name of this ResourceProperty.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """
        Sets the name of this ResourceProperty.
        Resource name, e.g. the name of the file or folder.

        :param name: The name of this ResourceProperty.
        :type: str
        """

        self._name = name

    @property
    def created_by(self):
        """
        Gets the created_by of this ResourceProperty.
        Username of the creator.

        :return: The created_by of this ResourceProperty.
        :rtype: str
        """
        return self._created_by

    @created_by.setter
    def created_by(self, created_by):
        """
        Sets the created_by of this ResourceProperty.
        Username of the creator.

        :param created_by: The created_by of this ResourceProperty.
        :type: str
        """

        self._created_by = created_by

    @property
    def upload_date(self):
        """
        Gets the upload_date of this ResourceProperty.
        Timestamp of resource upload or creation.

        :return: The upload_date of this ResourceProperty.
        :rtype: str
        """
        return self._upload_date

    @upload_date.setter
    def upload_date(self, upload_date):
        """
        Sets the upload_date of this ResourceProperty.
        Timestamp of resource upload or creation.

        :param upload_date: The upload_date of this ResourceProperty.
        :type: str
        """

        self._upload_date = upload_date

    @property
    def parent(self):
        """
        Gets the parent of this ResourceProperty.
        Parent path of the resource.

        :return: The parent of this ResourceProperty.
        :rtype: str
        """
        return self._parent

    @parent.setter
    def parent(self, parent):
        """
        Sets the parent of this ResourceProperty.
        Parent path of the resource.

        :param parent: The parent of this ResourceProperty.
        :type: str
        """

        self._parent = parent

    @property
    def path(self):
        """
        Gets the path of this ResourceProperty.
        Full path to the resource.

        :return: The path of this ResourceProperty.
        :rtype: str
        """
        return self._path

    @path.setter
    def path(self, path):
        """
        Sets the path of this ResourceProperty.
        Full path to the resource.

        :param path: The path of this ResourceProperty.
        :type: str
        """

        self._path = path

    @property
    def shares(self):
        """
        Gets the shares of this ResourceProperty.
        Associated shares array.

        :return: The shares of this ResourceProperty.
        :rtype: list[Share]
        """
        return self._shares

    @shares.setter
    def shares(self, shares):
        """
        Sets the shares of this ResourceProperty.
        Associated shares array.

        :param shares: The shares of this ResourceProperty.
        :type: list[Share]
        """

        self._shares = shares

    @property
    def notification_settings(self):
        """
        Gets the notification_settings of this ResourceProperty.
        Associated  notificactions array.

        :return: The notification_settings of this ResourceProperty.
        :rtype: str
        """
        return self._notification_settings

    @notification_settings.setter
    def notification_settings(self, notification_settings):
        """
        Sets the notification_settings of this ResourceProperty.
        Associated  notificactions array.

        :param notification_settings: The notification_settings of this ResourceProperty.
        :type: str
        """

        self._notification_settings = notification_settings

    @property
    def size(self):
        """
        Gets the size of this ResourceProperty.
        Resource size.

        :return: The size of this ResourceProperty.
        :rtype: int
        """
        return self._size

    @size.setter
    def size(self, size):
        """
        Sets the size of this ResourceProperty.
        Resource size.

        :param size: The size of this ResourceProperty.
        :type: int
        """

        self._size = size

    @property
    def previewable(self):
        """
        Gets the previewable of this ResourceProperty.
        Can resource be previewed. Property equals `null` if resource `type` is folder.

        :return: The previewable of this ResourceProperty.
        :rtype: bool
        """
        return self._previewable

    @previewable.setter
    def previewable(self, previewable):
        """
        Sets the previewable of this ResourceProperty.
        Can resource be previewed. Property equals `null` if resource `type` is folder.

        :param previewable: The previewable of this ResourceProperty.
        :type: bool
        """

        self._previewable = previewable

    @property
    def direct_file(self):
        """
        Gets the direct_file of this ResourceProperty.
        Associated direct file objects.

        :return: The direct_file of this ResourceProperty.
        :rtype: str
        """
        return self._direct_file

    @direct_file.setter
    def direct_file(self, direct_file):
        """
        Sets the direct_file of this ResourceProperty.
        Associated direct file objects.

        :param direct_file: The direct_file of this ResourceProperty.
        :type: str
        """

        self._direct_file = direct_file

    @property
    def type(self):
        """
        Gets the type of this ResourceProperty.
        Type of the resource.

        :return: The type of this ResourceProperty.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """
        Sets the type of this ResourceProperty.
        Type of the resource.

        :param type: The type of this ResourceProperty.
        :type: str
        """
        allowed_values = ["file", "folder"]
        if type not in allowed_values:
            raise ValueError(
                "Invalid value for `type` ({0}), must be one of {1}"
                .format(type, allowed_values)
            )

        self._type = type

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
        if not isinstance(other, ResourceProperty):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
