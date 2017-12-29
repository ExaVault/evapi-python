# coding: utf-8

"""
    ExaVault API

    # Introduction  Welcome to the ExaVault API documentation. Our API lets you control nearly all aspects of your ExaVault account programatically, from uploading and downloading files to creating and managing shares and notifications. Our API supports both GET and POST operations.  Capabilities of the API include:  - Uploading and downloading files. - Managing files and folders; including standard operations like move, copy and delete. - Getting information about activity occuring in your account. - Creating, updating and deleting users. - Creating and managing shares, including download-only shares and recieve folders.  - Setting up and managing notifications.  ## The API Endpoint  The ExaVault API is located at: https://api.exavault.com/v1/  # Testing w/ Postman  We've made it easy for you to test our API before you start full-scale development. Download [Postman](https://www.getpostman.com/) or the [Postman Chrome Extension](https://chrome.google.com/webstore/detail/postman/fhbjgbiflinjbdggehcddcbncdddomop?hl=en), and then download our Postman collection, below. [Obtain your API key](#section/Code-Libraries-and-Sample-PHP-Code/Obtain-your-API-key) and you'll be able to interact with your ExaVault account immediately, so you can better understand what the capabilities of the API are.  <div class=\"postman-run-button\" data-postman-action=\"collection/import\" data-postman-var-1=\"e13395afc6278ce1555f\"></div>  ![ExaVault API Postman Colletion Usage](/images/postman.png)  If you'd prefer to skip Postman and start working with code directly, take a look at the sample code below.    # Code Libraries & Sample PHP Code  Once you're ready for full-scale development, we recommend looking at our code libraries available on [GitHub](https://github.com/ExaVault). We offer code libraries for [Python](https://github.com/ExaVault/evapi-python), [PHP](https://github.com/ExaVault/evapi-php), [C#](https://github.com/ExaVault/evapi-csharp), and [Java](https://github.com/ExaVault/evapi-java).  While we recommend using our libraries, you're welcome to interact directly with our API via HTTP GET and POST requests -- a great option particularly if you're developing in a language for which we don't yet have sample code.     - [Download Python Libraries &raquo;](https://github.com/ExaVault/evapi-python) - [Download PHP Libraries &raquo;](https://github.com/ExaVault/evapi-php) - [Download C# Libraries &raquo;](https://github.com/ExaVault/evapi-csharp) - [Download Java Libraries &raquo;](https://github.com/ExaVault/evapi-java)  ## Obtain your API key  You will need to obtain an API key for your application from the [Client Area](https://clients.exavault.com/clientarea.php?action=products) of your account.  To obtain an API key, please follow the instructions below.   + Login to the [Accounts](https://clients.exavault.com/clientarea.php?action=products) section of the Client Area.  + Use the drop down next to your desired account, and select *Manage API Keys*.  + You will be brought to the API Key management screen. Fill out the form and save to generate a new key for your app.  *NOTE: As of Oct 2017, we are in the progress of migrating customers to our next generation platform. If your account is already on our new platform, you should log into your File Manager and create your API key under Account->Developer->Manage API Keys*.  ## Example: Setting the API key  To get started, you will want to add your custom API key to your application config. Here is an example using PHP, which makes use of our sample PHP library:  ```php    require_once('V1Api.php');   require_once('APIClient.php');   $apiKey = 'myaccountname-XXXXXXXXXXXXXXXX';   $apiUrl = 'https://api.exavault.com'   ``` ## Example: Authenticating  Once your API key is in place, you will likely want to authenticate so that you can begin uploading and downloading files, creating users, and all that other fun stuff.  ```php    // create a new instance of the ExaVault API library class   $api = new V1Api( new APIClient($apiKey, $apiUrl) );     $accessToken = null;    // call the authenticateUser method, passing your username and password   $response = $api->authenticateUser('yourusername', 'yourpassword');    // save this result for later, we will need it to logout   $loginSuccess = $response->success;    // if authentication was successful, store the access token   // obtained via the response body in the API instance.    if ($loginSuccess) {       $accessToken = $response->results->accessToken;    } else {       // Handle the error...   }  ```  ## Example: Uploading a file   ```php    // set the local and remote paths   $localPath = '/path/of/your/local/file';   $remotePath = '/path/on/remote/host';    // get the file size located at the local path   $filesize = filesize($localPath);    // get the upload URL from the Evapi object   $uploadResults = $api->getUploadFileUrl($accessToken, $filesize, $remotePath, true);    // if we were able to successfully get the upload URL, start   // uploading. Otherwise, print an error message.    if($uploadResults->success) {     // initialize a new curl session by passing the uploadFileUrl     $uploadUrl = $uploadResults->results->url;     $ch = curl_init($uploadUrl);      // create the open file handle     $handle = fopen($localPath, 'r');      // set the HTTP POST header, indicating the size of file to be uploaded     $header = array('X_File_Size: ' . $filesize,                     'Content-Type: multipart/form-data',                     'Content-Length: '' . $filesize,     );      // PHP uses curl for sending HTTP requests. If using a different language     // you will likely do this differently      curl_setopt($ch, CURLOPT_POST, true);  // perform upload via http post     curl_setopt($ch, CURLOPT_HTTPHEADER, $header);  // specify the header     curl_setopt($ch, CURLOPT_RETURNTRANSFER, 1);  // return string of result     curl_setopt($ch, CURLOPT_INFILE, $handle);  // specify size of file to upload     curl_setopt($ch, CURLOPT_SSLVERSION, 1);  // specify TLS 1.0     curl_setopt($ch, CURLOPT_SSL_VERIFYHOST, 2);  // verify common name with specified hostname     curl_setopt($ch, CURLOPT_SSL_VERIFYPEER, true); // verify certificate of remote peer      $result = curl_exec($ch);   // upload the file, get back result     $result = json_decode($result, true); // convert result to an array     curl_close($ch);  // close the curl session     fclose($handle);   // close the open file handle      if ($result['success']) {       // Your upload was successful!     } else {       // Wah-wah. Your upload failed for some reason.     }    } else {     // Wah-wah. Your upload failed for some reason.   }  ```  ## Example: Downloading a file  Downloading, like the upload process, first requires obtaining an appropriate download URL and then making a separate HTTP request to the API.   ```php    // set the filename   $filename = \"file.txt\";    // set the local path of the file to download to   $localPath = \"/path/to/local/\" . $filename;    // set the remote path where the file is located   $remotePath = \"/path/to/remote/\" . $filename;    // call the getDownloadFileUrl method on the API object instance   $downloadResults = $api->getDownloadFileUrl($accessToken, $remotePath);        if($downloadResults->success) {        // get the download URL and initialize a new curl session       $downloadUrl = $downloadResults->results->url;       $ch = curl_init($downloadUrl);        // set the file handle to the appropriate path       $handle = fopen($localPath, 'w');        // set the cURL options       curl_setopt($ch, CURLOPT_RETURNTRANSFER, true);       curl_setopt($ch, CURLOPT_FILE, $handle);       curl_setopt($ch, CURLOPT_SSLVERSION, 1);       curl_setopt($ch, CURLOPT_SSL_VERIFYHOST, 2);       curl_setopt($ch, CURLOPT_SSL_VERIFYPEER, true);               $result = curl_exec($ch);       $result = json_decode($result, true);       curl_close($ch);       fclose($handle);        if ($result) {           // Download successful!       } else {           // Oops, there was an error.       }   } else {       // Oops, there was an error.   }  ```  ## Example: Logging Out  Logging out of the API is very simple. The only thing that is required is to check to see if we were logged in in the first place; if yes then log out.  ```php    // logout only if login was successful   if ($loginResult) {       $api->logoutUser($accessToken);   }  ```  # Status Codes  The ExaVault API returns only two HTTP status codes for its responses: 200 and 500.  When the request could be successfully processed by the endpoint, the response status code will be 200, regardless of whether the requested action could be taken.  For example, the response to a getUser request for a username that does not exist in your account would have the status of 200,  indicating that the response was received and processed, but the error member of the returned response object would contain object with `message` and `code` properties.  **Result Format:**  |Success   | Error     | Results   | | ---      | :---:       |  :---:      | | 0        |  `Object` |   Empty   | | 1        |   Empty       |    `Object` or `Array`        |     When a malformed request is received, a 500 HTTP status code will be returned, indicating that the request could not be processed.  ExaVault's API does not currently support traditional REST response codes such as '201 Created' or '405 Method Not Allowed', although we intend to support such codes a future version of the API.   # File Paths  Many API calls require you to provide one or more file paths. For example, the <a href=\"#operation/moveResources\">moveResources</a> call requires both an array of source paths, **filePaths**, and a destination path, **destinationPath**. Here's a few tips for working with paths:   - File paths should always be specified as a string, using the standard Unix format: e.g. `/path/to/a/file.txt`  - File paths are always absolute _from the home directory of the logged in user_. For example, if the user **bob** had a home directory restriction of `/bob_home`, then an API call made using his login would specify a file as `/myfile.txt`, whereas an API call made using the master user ( no home directory restriction ) would specify the same file as `/bob_home/myfile.txt`.  # API Rate Limits  We rate limit the number of API calls you can make to help prevent abuse and protect system stablity. Each API key will support 500 requests per rolling five minutes. If you make more than 500 requests in a five minute period, you will receive a response with an error object for fifteen minutes.  # Webhooks  A webhook is an HTTP callback: a simple event-notification via HTTP POST. If you define webhooks for Exavault, ExaVault will POST a  message to a URL when certain things happen.     Webhooks can be used to receive a JSON object to your endpoint URL. You choose what events will trigger webhook messages to your endpoint URL.     Webhooks will attempt to send a message up to 8 times with increasing timeouts between each attempt. All webhook requests are tracked in the webhooks log.  ## Getting started  1. Go to the Account tab inside SWFT.  2. Choose the Developer tab.  3. Configure your endpoint URL and select the events you want to trigger webhook messages.  4. Save settings.    You are all set to receive webhook callbacks on the events you selected.  ## Verification Signature  ExaVault includes a custom HTTP header, X-Exavault-Signature, with webhooks POST requests which will contain the signature for the request.  You can use the signature to verify the request for an additional level of security.  ## Generating the Signature  1. Go to Account tab inside SWFT.  2. Choose the Developer tab.  3. Obtain the verification token. This field will only be shown if you've configured your endpoint URL.  4. In your code that receives or processes the webhooks, you should concatenate the verification token with the JSON object that we sent in our      POST request and hash it with md5.     ```     md5($verificationToken.$webhooksObject);     ```  5. Compare signature that you generated to the signature provided in the X-Exavault-Signature HTTP header  ## Example JSON Response Object  ```json   {     \"accountname\": \"mycompanyname\",     \"username\": \"john\"     \"operation\": \"Upload\",     \"protocol\": \"https\",     \"path\": \"/testfolder/filename.jpg\"     \"attempt\": 1   } ```  ## Webhooks Logs  Keep track of all your webhooks requests in the Activity section of your account. You can find the following info for each request:    1. date and time - timestamp of the request.    2. endpoint url - where the webhook was sent.    3. event - what triggered the webhook.    4. status - HTTP status or curl error code.    5. attempt - how many times we tried to send this request.    6. response size - size of the response from your server.    7. details - you can check the response body if it was sent. 

    OpenAPI spec version: 1.0.1
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from pprint import pformat
from six import iteritems
import re


class CallbackSettings(object):
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
        'account_id': 'str',
        'endpoint_url': 'str',
        'token': 'str',
        'upload': 'str',
        'download': 'str',
        'delete': 'str',
        'create_folder': 'str',
        'rename': 'str',
        'move': 'str',
        'copy': 'str',
        'compress': 'str',
        'extract': 'str',
        'share_folder': 'str',
        'send_files': 'str',
        'receive_files': 'str',
        'update_share': 'str',
        'update_receive': 'str',
        'delete_send': 'str',
        'delete_receive': 'str',
        'delete_share': 'str',
        'create_notification': 'str',
        'update_notification': 'str',
        'delete_notification': 'str',
        'create_user': 'str',
        'update_user': 'str',
        'delete_user': 'str',
        'user_connect': 'str',
        'user_disconnect': 'str'
    }

    attribute_map = {
        'account_id': 'accountId',
        'endpoint_url': 'endpointUrl',
        'token': 'token',
        'upload': 'upload',
        'download': 'download',
        'delete': 'delete',
        'create_folder': 'createFolder',
        'rename': 'rename',
        'move': 'move',
        'copy': 'copy',
        'compress': 'compress',
        'extract': 'extract',
        'share_folder': 'shareFolder',
        'send_files': 'sendFiles',
        'receive_files': 'receiveFiles',
        'update_share': 'updateShare',
        'update_receive': 'updateReceive',
        'delete_send': 'deleteSend',
        'delete_receive': 'deleteReceive',
        'delete_share': 'deleteShare',
        'create_notification': 'createNotification',
        'update_notification': 'updateNotification',
        'delete_notification': 'deleteNotification',
        'create_user': 'createUser',
        'update_user': 'updateUser',
        'delete_user': 'deleteUser',
        'user_connect': 'userConnect',
        'user_disconnect': 'userDisconnect'
    }

    def __init__(self, account_id=None, endpoint_url=None, token=None, upload=None, download=None, delete=None, create_folder=None, rename=None, move=None, copy=None, compress=None, extract=None, share_folder=None, send_files=None, receive_files=None, update_share=None, update_receive=None, delete_send=None, delete_receive=None, delete_share=None, create_notification=None, update_notification=None, delete_notification=None, create_user=None, update_user=None, delete_user=None, user_connect=None, user_disconnect=None):
        """
        CallbackSettings - a model defined in Swagger
        """

        self._account_id = None
        self._endpoint_url = None
        self._token = None
        self._upload = None
        self._download = None
        self._delete = None
        self._create_folder = None
        self._rename = None
        self._move = None
        self._copy = None
        self._compress = None
        self._extract = None
        self._share_folder = None
        self._send_files = None
        self._receive_files = None
        self._update_share = None
        self._update_receive = None
        self._delete_send = None
        self._delete_receive = None
        self._delete_share = None
        self._create_notification = None
        self._update_notification = None
        self._delete_notification = None
        self._create_user = None
        self._update_user = None
        self._delete_user = None
        self._user_connect = None
        self._user_disconnect = None

        if account_id is not None:
          self.account_id = account_id
        if endpoint_url is not None:
          self.endpoint_url = endpoint_url
        if token is not None:
          self.token = token
        if upload is not None:
          self.upload = upload
        if download is not None:
          self.download = download
        if delete is not None:
          self.delete = delete
        if create_folder is not None:
          self.create_folder = create_folder
        if rename is not None:
          self.rename = rename
        if move is not None:
          self.move = move
        if copy is not None:
          self.copy = copy
        if compress is not None:
          self.compress = compress
        if extract is not None:
          self.extract = extract
        if share_folder is not None:
          self.share_folder = share_folder
        if send_files is not None:
          self.send_files = send_files
        if receive_files is not None:
          self.receive_files = receive_files
        if update_share is not None:
          self.update_share = update_share
        if update_receive is not None:
          self.update_receive = update_receive
        if delete_send is not None:
          self.delete_send = delete_send
        if delete_receive is not None:
          self.delete_receive = delete_receive
        if delete_share is not None:
          self.delete_share = delete_share
        if create_notification is not None:
          self.create_notification = create_notification
        if update_notification is not None:
          self.update_notification = update_notification
        if delete_notification is not None:
          self.delete_notification = delete_notification
        if create_user is not None:
          self.create_user = create_user
        if update_user is not None:
          self.update_user = update_user
        if delete_user is not None:
          self.delete_user = delete_user
        if user_connect is not None:
          self.user_connect = user_connect
        if user_disconnect is not None:
          self.user_disconnect = user_disconnect

    @property
    def account_id(self):
        """
        Gets the account_id of this CallbackSettings.
        ID of the account these settings belongs to.

        :return: The account_id of this CallbackSettings.
        :rtype: str
        """
        return self._account_id

    @account_id.setter
    def account_id(self, account_id):
        """
        Sets the account_id of this CallbackSettings.
        ID of the account these settings belongs to.

        :param account_id: The account_id of this CallbackSettings.
        :type: str
        """

        self._account_id = account_id

    @property
    def endpoint_url(self):
        """
        Gets the endpoint_url of this CallbackSettings.
        Where callback settings object sent to.

        :return: The endpoint_url of this CallbackSettings.
        :rtype: str
        """
        return self._endpoint_url

    @endpoint_url.setter
    def endpoint_url(self, endpoint_url):
        """
        Sets the endpoint_url of this CallbackSettings.
        Where callback settings object sent to.

        :param endpoint_url: The endpoint_url of this CallbackSettings.
        :type: str
        """

        self._endpoint_url = endpoint_url

    @property
    def token(self):
        """
        Gets the token of this CallbackSettings.
        Verification token for the request authentication.

        :return: The token of this CallbackSettings.
        :rtype: str
        """
        return self._token

    @token.setter
    def token(self, token):
        """
        Sets the token of this CallbackSettings.
        Verification token for the request authentication.

        :param token: The token of this CallbackSettings.
        :type: str
        """

        self._token = token

    @property
    def upload(self):
        """
        Gets the upload of this CallbackSettings.
        Trigger callback on upload.

        :return: The upload of this CallbackSettings.
        :rtype: str
        """
        return self._upload

    @upload.setter
    def upload(self, upload):
        """
        Sets the upload of this CallbackSettings.
        Trigger callback on upload.

        :param upload: The upload of this CallbackSettings.
        :type: str
        """

        self._upload = upload

    @property
    def download(self):
        """
        Gets the download of this CallbackSettings.
        Trigger callback on download.

        :return: The download of this CallbackSettings.
        :rtype: str
        """
        return self._download

    @download.setter
    def download(self, download):
        """
        Sets the download of this CallbackSettings.
        Trigger callback on download.

        :param download: The download of this CallbackSettings.
        :type: str
        """

        self._download = download

    @property
    def delete(self):
        """
        Gets the delete of this CallbackSettings.
        Trigger callback on delete.

        :return: The delete of this CallbackSettings.
        :rtype: str
        """
        return self._delete

    @delete.setter
    def delete(self, delete):
        """
        Sets the delete of this CallbackSettings.
        Trigger callback on delete.

        :param delete: The delete of this CallbackSettings.
        :type: str
        """

        self._delete = delete

    @property
    def create_folder(self):
        """
        Gets the create_folder of this CallbackSettings.
        Trigger callback on fodler create.

        :return: The create_folder of this CallbackSettings.
        :rtype: str
        """
        return self._create_folder

    @create_folder.setter
    def create_folder(self, create_folder):
        """
        Sets the create_folder of this CallbackSettings.
        Trigger callback on fodler create.

        :param create_folder: The create_folder of this CallbackSettings.
        :type: str
        """

        self._create_folder = create_folder

    @property
    def rename(self):
        """
        Gets the rename of this CallbackSettings.
        Trigger callback on rename.

        :return: The rename of this CallbackSettings.
        :rtype: str
        """
        return self._rename

    @rename.setter
    def rename(self, rename):
        """
        Sets the rename of this CallbackSettings.
        Trigger callback on rename.

        :param rename: The rename of this CallbackSettings.
        :type: str
        """

        self._rename = rename

    @property
    def move(self):
        """
        Gets the move of this CallbackSettings.
        Trigger callback on move.

        :return: The move of this CallbackSettings.
        :rtype: str
        """
        return self._move

    @move.setter
    def move(self, move):
        """
        Sets the move of this CallbackSettings.
        Trigger callback on move.

        :param move: The move of this CallbackSettings.
        :type: str
        """

        self._move = move

    @property
    def copy(self):
        """
        Gets the copy of this CallbackSettings.
        Trigger callback on copy.

        :return: The copy of this CallbackSettings.
        :rtype: str
        """
        return self._copy

    @copy.setter
    def copy(self, copy):
        """
        Sets the copy of this CallbackSettings.
        Trigger callback on copy.

        :param copy: The copy of this CallbackSettings.
        :type: str
        """

        self._copy = copy

    @property
    def compress(self):
        """
        Gets the compress of this CallbackSettings.
        Trigger callback on compress.

        :return: The compress of this CallbackSettings.
        :rtype: str
        """
        return self._compress

    @compress.setter
    def compress(self, compress):
        """
        Sets the compress of this CallbackSettings.
        Trigger callback on compress.

        :param compress: The compress of this CallbackSettings.
        :type: str
        """

        self._compress = compress

    @property
    def extract(self):
        """
        Gets the extract of this CallbackSettings.
        Trigger callback on extract.

        :return: The extract of this CallbackSettings.
        :rtype: str
        """
        return self._extract

    @extract.setter
    def extract(self, extract):
        """
        Sets the extract of this CallbackSettings.
        Trigger callback on extract.

        :param extract: The extract of this CallbackSettings.
        :type: str
        """

        self._extract = extract

    @property
    def share_folder(self):
        """
        Gets the share_folder of this CallbackSettings.
        Trigger callback on share folder create.

        :return: The share_folder of this CallbackSettings.
        :rtype: str
        """
        return self._share_folder

    @share_folder.setter
    def share_folder(self, share_folder):
        """
        Sets the share_folder of this CallbackSettings.
        Trigger callback on share folder create.

        :param share_folder: The share_folder of this CallbackSettings.
        :type: str
        """

        self._share_folder = share_folder

    @property
    def send_files(self):
        """
        Gets the send_files of this CallbackSettings.
        Trigger callback on send files.

        :return: The send_files of this CallbackSettings.
        :rtype: str
        """
        return self._send_files

    @send_files.setter
    def send_files(self, send_files):
        """
        Sets the send_files of this CallbackSettings.
        Trigger callback on send files.

        :param send_files: The send_files of this CallbackSettings.
        :type: str
        """

        self._send_files = send_files

    @property
    def receive_files(self):
        """
        Gets the receive_files of this CallbackSettings.
        Trigger callback on receive folder create.

        :return: The receive_files of this CallbackSettings.
        :rtype: str
        """
        return self._receive_files

    @receive_files.setter
    def receive_files(self, receive_files):
        """
        Sets the receive_files of this CallbackSettings.
        Trigger callback on receive folder create.

        :param receive_files: The receive_files of this CallbackSettings.
        :type: str
        """

        self._receive_files = receive_files

    @property
    def update_share(self):
        """
        Gets the update_share of this CallbackSettings.
        Trigger callback on share folder update.

        :return: The update_share of this CallbackSettings.
        :rtype: str
        """
        return self._update_share

    @update_share.setter
    def update_share(self, update_share):
        """
        Sets the update_share of this CallbackSettings.
        Trigger callback on share folder update.

        :param update_share: The update_share of this CallbackSettings.
        :type: str
        """

        self._update_share = update_share

    @property
    def update_receive(self):
        """
        Gets the update_receive of this CallbackSettings.
        Trigger callback on receive folder update.

        :return: The update_receive of this CallbackSettings.
        :rtype: str
        """
        return self._update_receive

    @update_receive.setter
    def update_receive(self, update_receive):
        """
        Sets the update_receive of this CallbackSettings.
        Trigger callback on receive folder update.

        :param update_receive: The update_receive of this CallbackSettings.
        :type: str
        """

        self._update_receive = update_receive

    @property
    def delete_send(self):
        """
        Gets the delete_send of this CallbackSettings.
        Trigger callback on send files delete.

        :return: The delete_send of this CallbackSettings.
        :rtype: str
        """
        return self._delete_send

    @delete_send.setter
    def delete_send(self, delete_send):
        """
        Sets the delete_send of this CallbackSettings.
        Trigger callback on send files delete.

        :param delete_send: The delete_send of this CallbackSettings.
        :type: str
        """

        self._delete_send = delete_send

    @property
    def delete_receive(self):
        """
        Gets the delete_receive of this CallbackSettings.
        Trigger callback on receive folder delete.

        :return: The delete_receive of this CallbackSettings.
        :rtype: str
        """
        return self._delete_receive

    @delete_receive.setter
    def delete_receive(self, delete_receive):
        """
        Sets the delete_receive of this CallbackSettings.
        Trigger callback on receive folder delete.

        :param delete_receive: The delete_receive of this CallbackSettings.
        :type: str
        """

        self._delete_receive = delete_receive

    @property
    def delete_share(self):
        """
        Gets the delete_share of this CallbackSettings.
        Trigger callback on share folder delete.

        :return: The delete_share of this CallbackSettings.
        :rtype: str
        """
        return self._delete_share

    @delete_share.setter
    def delete_share(self, delete_share):
        """
        Sets the delete_share of this CallbackSettings.
        Trigger callback on share folder delete.

        :param delete_share: The delete_share of this CallbackSettings.
        :type: str
        """

        self._delete_share = delete_share

    @property
    def create_notification(self):
        """
        Gets the create_notification of this CallbackSettings.
        Trigger callback on notification create.

        :return: The create_notification of this CallbackSettings.
        :rtype: str
        """
        return self._create_notification

    @create_notification.setter
    def create_notification(self, create_notification):
        """
        Sets the create_notification of this CallbackSettings.
        Trigger callback on notification create.

        :param create_notification: The create_notification of this CallbackSettings.
        :type: str
        """

        self._create_notification = create_notification

    @property
    def update_notification(self):
        """
        Gets the update_notification of this CallbackSettings.
        Trigger callback on notification update.

        :return: The update_notification of this CallbackSettings.
        :rtype: str
        """
        return self._update_notification

    @update_notification.setter
    def update_notification(self, update_notification):
        """
        Sets the update_notification of this CallbackSettings.
        Trigger callback on notification update.

        :param update_notification: The update_notification of this CallbackSettings.
        :type: str
        """

        self._update_notification = update_notification

    @property
    def delete_notification(self):
        """
        Gets the delete_notification of this CallbackSettings.
        Trigger callback on notification delete.

        :return: The delete_notification of this CallbackSettings.
        :rtype: str
        """
        return self._delete_notification

    @delete_notification.setter
    def delete_notification(self, delete_notification):
        """
        Sets the delete_notification of this CallbackSettings.
        Trigger callback on notification delete.

        :param delete_notification: The delete_notification of this CallbackSettings.
        :type: str
        """

        self._delete_notification = delete_notification

    @property
    def create_user(self):
        """
        Gets the create_user of this CallbackSettings.
        Trigger callback on user create.

        :return: The create_user of this CallbackSettings.
        :rtype: str
        """
        return self._create_user

    @create_user.setter
    def create_user(self, create_user):
        """
        Sets the create_user of this CallbackSettings.
        Trigger callback on user create.

        :param create_user: The create_user of this CallbackSettings.
        :type: str
        """

        self._create_user = create_user

    @property
    def update_user(self):
        """
        Gets the update_user of this CallbackSettings.
        Trigger callback on user update.

        :return: The update_user of this CallbackSettings.
        :rtype: str
        """
        return self._update_user

    @update_user.setter
    def update_user(self, update_user):
        """
        Sets the update_user of this CallbackSettings.
        Trigger callback on user update.

        :param update_user: The update_user of this CallbackSettings.
        :type: str
        """

        self._update_user = update_user

    @property
    def delete_user(self):
        """
        Gets the delete_user of this CallbackSettings.
        Trigger callback on user delete.

        :return: The delete_user of this CallbackSettings.
        :rtype: str
        """
        return self._delete_user

    @delete_user.setter
    def delete_user(self, delete_user):
        """
        Sets the delete_user of this CallbackSettings.
        Trigger callback on user delete.

        :param delete_user: The delete_user of this CallbackSettings.
        :type: str
        """

        self._delete_user = delete_user

    @property
    def user_connect(self):
        """
        Gets the user_connect of this CallbackSettings.
        Trigger callback on user connect.

        :return: The user_connect of this CallbackSettings.
        :rtype: str
        """
        return self._user_connect

    @user_connect.setter
    def user_connect(self, user_connect):
        """
        Sets the user_connect of this CallbackSettings.
        Trigger callback on user connect.

        :param user_connect: The user_connect of this CallbackSettings.
        :type: str
        """

        self._user_connect = user_connect

    @property
    def user_disconnect(self):
        """
        Gets the user_disconnect of this CallbackSettings.
        Trigger callback on user disconnect.

        :return: The user_disconnect of this CallbackSettings.
        :rtype: str
        """
        return self._user_disconnect

    @user_disconnect.setter
    def user_disconnect(self, user_disconnect):
        """
        Sets the user_disconnect of this CallbackSettings.
        Trigger callback on user disconnect.

        :param user_disconnect: The user_disconnect of this CallbackSettings.
        :type: str
        """

        self._user_disconnect = user_disconnect

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
        if not isinstance(other, CallbackSettings):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
