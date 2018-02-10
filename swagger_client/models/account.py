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


class Account(object):
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
        'username': 'str',
        'max_users': 'int',
        'user_count': 'int',
        'master_account': 'User',
        'status': 'int',
        'branding': 'bool',
        'custom_domain': 'bool',
        'plan_code': 'str',
        'package_id': 'int',
        'disk_quota_limit': 'int',
        'bandwidth_quota_limit': 'int',
        'disk_quota_used': 'int',
        'bandwidth_quota_used': 'int',
        'quota_notice_enabled': 'int',
        'quota_notice_threshold': 'int',
        'redirect': 'str',
        'secure_only': 'bool',
        'complex_passwords': 'bool',
        'show_referral_links': 'bool',
        'external_domains': 'str',
        'allowed_ip': 'str',
        'callback_settings': 'CallbackSettings',
        'free_trial': 'bool',
        'applied_trial': 'str',
        'client_id': 'int',
        'welcome_email_content': 'str',
        'welcome_email_subject': 'str',
        'custom_signature': 'str',
        'created': 'str',
        'modified': 'str'
    }

    attribute_map = {
        'id': 'id',
        'username': 'username',
        'max_users': 'maxUsers',
        'user_count': 'userCount',
        'master_account': 'masterAccount',
        'status': 'status',
        'branding': 'branding',
        'custom_domain': 'customDomain',
        'plan_code': 'planCode',
        'package_id': 'packageId',
        'disk_quota_limit': 'diskQuotaLimit',
        'bandwidth_quota_limit': 'bandwidthQuotaLimit',
        'disk_quota_used': 'diskQuotaUsed',
        'bandwidth_quota_used': 'bandwidthQuotaUsed',
        'quota_notice_enabled': 'quotaNoticeEnabled',
        'quota_notice_threshold': 'quotaNoticeThreshold',
        'redirect': 'redirect',
        'secure_only': 'secureOnly',
        'complex_passwords': 'complexPasswords',
        'show_referral_links': 'showReferralLinks',
        'external_domains': 'externalDomains',
        'allowed_ip': 'allowedIp',
        'callback_settings': 'callbackSettings',
        'free_trial': 'freeTrial',
        'applied_trial': 'appliedTrial',
        'client_id': 'clientId',
        'welcome_email_content': 'welcomeEmailContent',
        'welcome_email_subject': 'welcomeEmailSubject',
        'custom_signature': 'customSignature',
        'created': 'created',
        'modified': 'modified'
    }

    def __init__(self, id=None, username=None, max_users=None, user_count=None, master_account=None, status=None, branding=None, custom_domain=None, plan_code=None, package_id=None, disk_quota_limit=None, bandwidth_quota_limit=None, disk_quota_used=None, bandwidth_quota_used=None, quota_notice_enabled=None, quota_notice_threshold=None, redirect=None, secure_only=None, complex_passwords=None, show_referral_links=None, external_domains=None, allowed_ip=None, callback_settings=None, free_trial=None, applied_trial=None, client_id=None, welcome_email_content=None, welcome_email_subject=None, custom_signature=None, created=None, modified=None):
        """
        Account - a model defined in Swagger
        """

        self._id = None
        self._username = None
        self._max_users = None
        self._user_count = None
        self._master_account = None
        self._status = None
        self._branding = None
        self._custom_domain = None
        self._plan_code = None
        self._package_id = None
        self._disk_quota_limit = None
        self._bandwidth_quota_limit = None
        self._disk_quota_used = None
        self._bandwidth_quota_used = None
        self._quota_notice_enabled = None
        self._quota_notice_threshold = None
        self._redirect = None
        self._secure_only = None
        self._complex_passwords = None
        self._show_referral_links = None
        self._external_domains = None
        self._allowed_ip = None
        self._callback_settings = None
        self._free_trial = None
        self._applied_trial = None
        self._client_id = None
        self._welcome_email_content = None
        self._welcome_email_subject = None
        self._custom_signature = None
        self._created = None
        self._modified = None

        if id is not None:
          self.id = id
        if username is not None:
          self.username = username
        if max_users is not None:
          self.max_users = max_users
        if user_count is not None:
          self.user_count = user_count
        if master_account is not None:
          self.master_account = master_account
        if status is not None:
          self.status = status
        if branding is not None:
          self.branding = branding
        if custom_domain is not None:
          self.custom_domain = custom_domain
        if plan_code is not None:
          self.plan_code = plan_code
        if package_id is not None:
          self.package_id = package_id
        if disk_quota_limit is not None:
          self.disk_quota_limit = disk_quota_limit
        if bandwidth_quota_limit is not None:
          self.bandwidth_quota_limit = bandwidth_quota_limit
        if disk_quota_used is not None:
          self.disk_quota_used = disk_quota_used
        if bandwidth_quota_used is not None:
          self.bandwidth_quota_used = bandwidth_quota_used
        if quota_notice_enabled is not None:
          self.quota_notice_enabled = quota_notice_enabled
        if quota_notice_threshold is not None:
          self.quota_notice_threshold = quota_notice_threshold
        if redirect is not None:
          self.redirect = redirect
        if secure_only is not None:
          self.secure_only = secure_only
        if complex_passwords is not None:
          self.complex_passwords = complex_passwords
        if show_referral_links is not None:
          self.show_referral_links = show_referral_links
        if external_domains is not None:
          self.external_domains = external_domains
        if allowed_ip is not None:
          self.allowed_ip = allowed_ip
        if callback_settings is not None:
          self.callback_settings = callback_settings
        if free_trial is not None:
          self.free_trial = free_trial
        if applied_trial is not None:
          self.applied_trial = applied_trial
        if client_id is not None:
          self.client_id = client_id
        if welcome_email_content is not None:
          self.welcome_email_content = welcome_email_content
        if welcome_email_subject is not None:
          self.welcome_email_subject = welcome_email_subject
        if custom_signature is not None:
          self.custom_signature = custom_signature
        if created is not None:
          self.created = created
        if modified is not None:
          self.modified = modified

    @property
    def id(self):
        """
        Gets the id of this Account.
        ID of the account.

        :return: The id of this Account.
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """
        Sets the id of this Account.
        ID of the account.

        :param id: The id of this Account.
        :type: int
        """

        self._id = id

    @property
    def username(self):
        """
        Gets the username of this Account.
        Name of the account.

        :return: The username of this Account.
        :rtype: str
        """
        return self._username

    @username.setter
    def username(self, username):
        """
        Sets the username of this Account.
        Name of the account.

        :param username: The username of this Account.
        :type: str
        """

        self._username = username

    @property
    def max_users(self):
        """
        Gets the max_users of this Account.
        Maximum number of users the account can have. This can be increased by contacting ExaVault Support.

        :return: The max_users of this Account.
        :rtype: int
        """
        return self._max_users

    @max_users.setter
    def max_users(self, max_users):
        """
        Sets the max_users of this Account.
        Maximum number of users the account can have. This can be increased by contacting ExaVault Support.

        :param max_users: The max_users of this Account.
        :type: int
        """

        self._max_users = max_users

    @property
    def user_count(self):
        """
        Gets the user_count of this Account.
        Current number of users on the account.

        :return: The user_count of this Account.
        :rtype: int
        """
        return self._user_count

    @user_count.setter
    def user_count(self, user_count):
        """
        Sets the user_count of this Account.
        Current number of users on the account.

        :param user_count: The user_count of this Account.
        :type: int
        """

        self._user_count = user_count

    @property
    def master_account(self):
        """
        Gets the master_account of this Account.
        Master user object.

        :return: The master_account of this Account.
        :rtype: User
        """
        return self._master_account

    @master_account.setter
    def master_account(self, master_account):
        """
        Sets the master_account of this Account.
        Master user object.

        :param master_account: The master_account of this Account.
        :type: User
        """

        self._master_account = master_account

    @property
    def status(self):
        """
        Gets the status of this Account.
        Account status flag. A one (1) means the account is active; zero (0) means it is suspended.

        :return: The status of this Account.
        :rtype: int
        """
        return self._status

    @status.setter
    def status(self, status):
        """
        Sets the status of this Account.
        Account status flag. A one (1) means the account is active; zero (0) means it is suspended.

        :param status: The status of this Account.
        :type: int
        """
        allowed_values = [1, 0]
        if status not in allowed_values:
            raise ValueError(
                "Invalid value for `status` ({0}), must be one of {1}"
                .format(status, allowed_values)
            )

        self._status = status

    @property
    def branding(self):
        """
        Gets the branding of this Account.
        Branding flag. Set to `true` if the account has branding functionality enabled.

        :return: The branding of this Account.
        :rtype: bool
        """
        return self._branding

    @branding.setter
    def branding(self, branding):
        """
        Sets the branding of this Account.
        Branding flag. Set to `true` if the account has branding functionality enabled.

        :param branding: The branding of this Account.
        :type: bool
        """

        self._branding = branding

    @property
    def custom_domain(self):
        """
        Gets the custom_domain of this Account.
        Custom domain flag. Set to `true` if account has custom domain functionality enabled.

        :return: The custom_domain of this Account.
        :rtype: bool
        """
        return self._custom_domain

    @custom_domain.setter
    def custom_domain(self, custom_domain):
        """
        Sets the custom_domain of this Account.
        Custom domain flag. Set to `true` if account has custom domain functionality enabled.

        :param custom_domain: The custom_domain of this Account.
        :type: bool
        """

        self._custom_domain = custom_domain

    @property
    def plan_code(self):
        """
        Gets the plan_code of this Account.
        Code of the plan account is signed up for.

        :return: The plan_code of this Account.
        :rtype: str
        """
        return self._plan_code

    @plan_code.setter
    def plan_code(self, plan_code):
        """
        Sets the plan_code of this Account.
        Code of the plan account is signed up for.

        :param plan_code: The plan_code of this Account.
        :type: str
        """

        self._plan_code = plan_code

    @property
    def package_id(self):
        """
        Gets the package_id of this Account.
        Internal ID of the package that the account is signed for.

        :return: The package_id of this Account.
        :rtype: int
        """
        return self._package_id

    @package_id.setter
    def package_id(self, package_id):
        """
        Sets the package_id of this Account.
        Internal ID of the package that the account is signed for.

        :param package_id: The package_id of this Account.
        :type: int
        """

        self._package_id = package_id

    @property
    def disk_quota_limit(self):
        """
        Gets the disk_quota_limit of this Account.
        Amount of disk space that the account has available to it. This may be increased by upgrading to a larger plan.

        :return: The disk_quota_limit of this Account.
        :rtype: int
        """
        return self._disk_quota_limit

    @disk_quota_limit.setter
    def disk_quota_limit(self, disk_quota_limit):
        """
        Sets the disk_quota_limit of this Account.
        Amount of disk space that the account has available to it. This may be increased by upgrading to a larger plan.

        :param disk_quota_limit: The disk_quota_limit of this Account.
        :type: int
        """

        self._disk_quota_limit = disk_quota_limit

    @property
    def bandwidth_quota_limit(self):
        """
        Gets the bandwidth_quota_limit of this Account.
        Amount of bandwidth that the account has available before a warning is generated. All ExaVault accounts include unlimited bandwidth, but we flag high-bandwidth users.

        :return: The bandwidth_quota_limit of this Account.
        :rtype: int
        """
        return self._bandwidth_quota_limit

    @bandwidth_quota_limit.setter
    def bandwidth_quota_limit(self, bandwidth_quota_limit):
        """
        Sets the bandwidth_quota_limit of this Account.
        Amount of bandwidth that the account has available before a warning is generated. All ExaVault accounts include unlimited bandwidth, but we flag high-bandwidth users.

        :param bandwidth_quota_limit: The bandwidth_quota_limit of this Account.
        :type: int
        """

        self._bandwidth_quota_limit = bandwidth_quota_limit

    @property
    def disk_quota_used(self):
        """
        Gets the disk_quota_used of this Account.
        Amount of disk space currently in use.

        :return: The disk_quota_used of this Account.
        :rtype: int
        """
        return self._disk_quota_used

    @disk_quota_used.setter
    def disk_quota_used(self, disk_quota_used):
        """
        Sets the disk_quota_used of this Account.
        Amount of disk space currently in use.

        :param disk_quota_used: The disk_quota_used of this Account.
        :type: int
        """

        self._disk_quota_used = disk_quota_used

    @property
    def bandwidth_quota_used(self):
        """
        Gets the bandwidth_quota_used of this Account.
        Amount of bandwidth used by this account in the last billing period.

        :return: The bandwidth_quota_used of this Account.
        :rtype: int
        """
        return self._bandwidth_quota_used

    @bandwidth_quota_used.setter
    def bandwidth_quota_used(self, bandwidth_quota_used):
        """
        Sets the bandwidth_quota_used of this Account.
        Amount of bandwidth used by this account in the last billing period.

        :param bandwidth_quota_used: The bandwidth_quota_used of this Account.
        :type: int
        """

        self._bandwidth_quota_used = bandwidth_quota_used

    @property
    def quota_notice_enabled(self):
        """
        Gets the quota_notice_enabled of this Account.
        Should a quota warning be sent to the account owner when a threshold level of space utilization is reached?

        :return: The quota_notice_enabled of this Account.
        :rtype: int
        """
        return self._quota_notice_enabled

    @quota_notice_enabled.setter
    def quota_notice_enabled(self, quota_notice_enabled):
        """
        Sets the quota_notice_enabled of this Account.
        Should a quota warning be sent to the account owner when a threshold level of space utilization is reached?

        :param quota_notice_enabled: The quota_notice_enabled of this Account.
        :type: int
        """

        self._quota_notice_enabled = quota_notice_enabled

    @property
    def quota_notice_threshold(self):
        """
        Gets the quota_notice_threshold of this Account.
        Treshold that triggers a quota notification.

        :return: The quota_notice_threshold of this Account.
        :rtype: int
        """
        return self._quota_notice_threshold

    @quota_notice_threshold.setter
    def quota_notice_threshold(self, quota_notice_threshold):
        """
        Sets the quota_notice_threshold of this Account.
        Treshold that triggers a quota notification.

        :param quota_notice_threshold: The quota_notice_threshold of this Account.
        :type: int
        """

        self._quota_notice_threshold = quota_notice_threshold

    @property
    def redirect(self):
        """
        Gets the redirect of this Account.
        Internal flag indicating which version of our web interface will be used.

        :return: The redirect of this Account.
        :rtype: str
        """
        return self._redirect

    @redirect.setter
    def redirect(self, redirect):
        """
        Sets the redirect of this Account.
        Internal flag indicating which version of our web interface will be used.

        :param redirect: The redirect of this Account.
        :type: str
        """
        allowed_values = ["swft", "app"]
        if redirect not in allowed_values:
            raise ValueError(
                "Invalid value for `redirect` ({0}), must be one of {1}"
                .format(redirect, allowed_values)
            )

        self._redirect = redirect

    @property
    def secure_only(self):
        """
        Gets the secure_only of this Account.
        Flag to indicate whether the account disables connections via insecure protocols (e.g. FTP).

        :return: The secure_only of this Account.
        :rtype: bool
        """
        return self._secure_only

    @secure_only.setter
    def secure_only(self, secure_only):
        """
        Sets the secure_only of this Account.
        Flag to indicate whether the account disables connections via insecure protocols (e.g. FTP).

        :param secure_only: The secure_only of this Account.
        :type: bool
        """

        self._secure_only = secure_only

    @property
    def complex_passwords(self):
        """
        Gets the complex_passwords of this Account.
        Flag to indicate whether the account requires complex passwords.

        :return: The complex_passwords of this Account.
        :rtype: bool
        """
        return self._complex_passwords

    @complex_passwords.setter
    def complex_passwords(self, complex_passwords):
        """
        Sets the complex_passwords of this Account.
        Flag to indicate whether the account requires complex passwords.

        :param complex_passwords: The complex_passwords of this Account.
        :type: bool
        """

        self._complex_passwords = complex_passwords

    @property
    def show_referral_links(self):
        """
        Gets the show_referral_links of this Account.
        Flag to indicate showing of referrals links in the account.

        :return: The show_referral_links of this Account.
        :rtype: bool
        """
        return self._show_referral_links

    @show_referral_links.setter
    def show_referral_links(self, show_referral_links):
        """
        Sets the show_referral_links of this Account.
        Flag to indicate showing of referrals links in the account.

        :param show_referral_links: The show_referral_links of this Account.
        :type: bool
        """

        self._show_referral_links = show_referral_links

    @property
    def external_domains(self):
        """
        Gets the external_domains of this Account.
        Custom domain used to brand this account.

        :return: The external_domains of this Account.
        :rtype: str
        """
        return self._external_domains

    @external_domains.setter
    def external_domains(self, external_domains):
        """
        Sets the external_domains of this Account.
        Custom domain used to brand this account.

        :param external_domains: The external_domains of this Account.
        :type: str
        """

        self._external_domains = external_domains

    @property
    def allowed_ip(self):
        """
        Gets the allowed_ip of this Account.
        Range of IP addresses allowed to access this account.

        :return: The allowed_ip of this Account.
        :rtype: str
        """
        return self._allowed_ip

    @allowed_ip.setter
    def allowed_ip(self, allowed_ip):
        """
        Sets the allowed_ip of this Account.
        Range of IP addresses allowed to access this account.

        :param allowed_ip: The allowed_ip of this Account.
        :type: str
        """

        self._allowed_ip = allowed_ip

    @property
    def callback_settings(self):
        """
        Gets the callback_settings of this Account.
        Callback settings of the account.

        :return: The callback_settings of this Account.
        :rtype: CallbackSettings
        """
        return self._callback_settings

    @callback_settings.setter
    def callback_settings(self, callback_settings):
        """
        Sets the callback_settings of this Account.
        Callback settings of the account.

        :param callback_settings: The callback_settings of this Account.
        :type: CallbackSettings
        """

        self._callback_settings = callback_settings

    @property
    def free_trial(self):
        """
        Gets the free_trial of this Account.
        Flag indicates if free trial enabled.

        :return: The free_trial of this Account.
        :rtype: bool
        """
        return self._free_trial

    @free_trial.setter
    def free_trial(self, free_trial):
        """
        Sets the free_trial of this Account.
        Flag indicates if free trial enabled.

        :param free_trial: The free_trial of this Account.
        :type: bool
        """

        self._free_trial = free_trial

    @property
    def applied_trial(self):
        """
        Gets the applied_trial of this Account.
        Free trial description.

        :return: The applied_trial of this Account.
        :rtype: str
        """
        return self._applied_trial

    @applied_trial.setter
    def applied_trial(self, applied_trial):
        """
        Sets the applied_trial of this Account.
        Free trial description.

        :param applied_trial: The applied_trial of this Account.
        :type: str
        """

        self._applied_trial = applied_trial

    @property
    def client_id(self):
        """
        Gets the client_id of this Account.
        ID of the account in our client system.

        :return: The client_id of this Account.
        :rtype: int
        """
        return self._client_id

    @client_id.setter
    def client_id(self, client_id):
        """
        Sets the client_id of this Account.
        ID of the account in our client system.

        :param client_id: The client_id of this Account.
        :type: int
        """

        self._client_id = client_id

    @property
    def welcome_email_content(self):
        """
        Gets the welcome_email_content of this Account.
        Content of welcome email each new user will receive.

        :return: The welcome_email_content of this Account.
        :rtype: str
        """
        return self._welcome_email_content

    @welcome_email_content.setter
    def welcome_email_content(self, welcome_email_content):
        """
        Sets the welcome_email_content of this Account.
        Content of welcome email each new user will receive.

        :param welcome_email_content: The welcome_email_content of this Account.
        :type: str
        """

        self._welcome_email_content = welcome_email_content

    @property
    def welcome_email_subject(self):
        """
        Gets the welcome_email_subject of this Account.
        Subject of welcome email each new user will receive.

        :return: The welcome_email_subject of this Account.
        :rtype: str
        """
        return self._welcome_email_subject

    @welcome_email_subject.setter
    def welcome_email_subject(self, welcome_email_subject):
        """
        Sets the welcome_email_subject of this Account.
        Subject of welcome email each new user will receive.

        :param welcome_email_subject: The welcome_email_subject of this Account.
        :type: str
        """

        self._welcome_email_subject = welcome_email_subject

    @property
    def custom_signature(self):
        """
        Gets the custom_signature of this Account.
        Custom signature for all account emails users or recipients will receive.

        :return: The custom_signature of this Account.
        :rtype: str
        """
        return self._custom_signature

    @custom_signature.setter
    def custom_signature(self, custom_signature):
        """
        Sets the custom_signature of this Account.
        Custom signature for all account emails users or recipients will receive.

        :param custom_signature: The custom_signature of this Account.
        :type: str
        """

        self._custom_signature = custom_signature

    @property
    def created(self):
        """
        Gets the created of this Account.
        Timestamp of account creation.

        :return: The created of this Account.
        :rtype: str
        """
        return self._created

    @created.setter
    def created(self, created):
        """
        Sets the created of this Account.
        Timestamp of account creation.

        :param created: The created of this Account.
        :type: str
        """

        self._created = created

    @property
    def modified(self):
        """
        Gets the modified of this Account.
        Timestamp of account modification.

        :return: The modified of this Account.
        :rtype: str
        """
        return self._modified

    @modified.setter
    def modified(self, modified):
        """
        Sets the modified of this Account.
        Timestamp of account modification.

        :param modified: The modified of this Account.
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
        if not isinstance(other, Account):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
