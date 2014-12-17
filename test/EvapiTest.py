"""
Copyright 2014, ExaVault, Inc.

EvapiTest.py

This file contains unit tests for testing the the swagger
generated API client

@author Dylan Gleason, support -at- exavault -dot- com

"""

# load the src path containing API library
import sys
sys.path.insert(0, '../src')

# load API client and unittest libraries
import V1Api
import ApiClient
import unittest
import traceback

class EvapiTest(unittest.TestCase):

    # NOTE: the below variables are needed for successful completion
    # of tests. Be sure to populate each with your actual account
    # information, where relevant

    USERNAME      = 'yourusername'                      # replace with our username
    PASSWORD      = 'yourpassword'                      # replace with your password
    API_KEY       = 'yourappname-XXXXXXXXXXXXXXXXXXXX'  # replace with your API key
    API_SERVER    = 'https://api.exavault.com'
    ROOT_DIR      = '/'
    FOLDER        = 'unit-tests'
    SUBFOLDER     = 'subfolder'
    TEST_USER     = 'unit-tests'
    TEST_EMAIL    = 'youremail@yourdomain.com'          # replace with your email address
    PREVIEW       = '/path/to/preview_file.jpg'         # replace with actual file path
    RENAME_FOLDER = 'test-rename-folder'
    DOWNLOAD_FILE = '/path/of/file/to/download'         # replace with actual file path
    TIMEZONE      = 'America/Los_Angeles'
    USER_TYPE     = 'user'
    PERMISSIONS   = '"upload":true,"download":true'     # NOTE: server not decoding, fix

    ### setUp and tearDown methods ###

    def setUp(self):
        """Initialize the API client"""
        self.api = V1Api.V1Api( ApiClient.ApiClient(self.API_KEY, self.API_SERVER) )

    def tearDown(self):
        """Logout the current user if an access token was set"""
        if hasattr(self, 'accessToken'):
            self.api.logoutUser(self.accessToken)

    ### Test Cases ###

    def testAuthenticateUser(self):
        """Test authenticating a user"""

        # attempt to authenticate the user
        apiError = False
        try:
            response = self.__authenticateUser()
            results = response.results
        except Exception as e:
            print 'Error on authenticateUser: ', e
            apiError = True

        # test all assertions
        self.assertFalse(apiError)
        self.assertIsNotNone(response)
        self.assertEquals(results.username, self.USERNAME)
        self.assertIsNotNone(self.accessToken)
        self.assertIsNotNone(results.clientIp)

    def testCheckFileExists(self):
        """Test to see if file exists"""

        # authenticate and check if file exists
        apiError = False
        try:
            self.__authenticateUser()
            response = self.api.checkFilesExist(self.accessToken, self.ROOT_DIR)
        except Exception as e:
            print 'Error on checkFileExists: ', e
            apiError = True

        # test all assertions
        self.assertFalse(apiError)
        self.assertIsNotNone(response)

    def testCopyResources(self):
        """Test copying a resource from one location to another"""

        # authenticate and copy resource
        apiError = False
        try:
            self.__authenticateUser()

            # create two folders, both in the root directory
            folder1 = self.api.createFolder(self.accessToken, self.FOLDER, self.ROOT_DIR)
            folder2 = self.api.createFolder(self.accessToken, self.SUBFOLDER, self.ROOT_DIR)

            if (not folder1.success) or (not folder2.success):
                raise Exception('One or more test folders could not be created')

            # copy the subfolder to the folder
            response = self.api.copyResources(self.accessToken, [self.SUBFOLDER], self.FOLDER)
            self.__checkResponseStatus(response)
            firstResult = response.results[0]

            # setup expected values
            folder = self.ROOT_DIR + self.FOLDER
            subFolder = self.ROOT_DIR + self.SUBFOLDER
            copiedFolder = folder + subFolder

            # cleanup directories we just created
            self.api.deleteResources(self.accessToken, folder)
            self.api.deleteResources(self.accessToken, subFolder)

        except Exception as e:
            print 'Error on copyResources: ', e
            apiError = True

        # test all assertions
        self.assertFalse(apiError)
        self.assertIsNotNone(firstResult)
        self.assertEquals(subFolder, firstResult.file)
        self.assertEquals(copiedFolder, firstResult.destination)

    def testCreateFolder(self):
        """Test creating a folder on the remote host"""

        # authenticate and create a folder
        apiError = False
        try:
            self.__authenticateUser()
            response = self.api.createFolder(self.accessToken, self.FOLDER, self.ROOT_DIR)
        except Exception as e:
            print 'Error on createFolder: ', e
            apiError = True

        # test all assertions
        self.assertFalse(apiError)
        self.assertIsNotNone(response)
        self.assertEquals(1, response.success)

    def testCreateUser(self):
        """Test creating a new subaccount user"""

        # authenticate and create the user
        apiError = False
        try:
            self.__authenticateUser()
            response = self.__createUser()
        except Exception as e:
            print 'Error on createUser: ', e
            apiError = True

        # test all assertions
        self.assertFalse(apiError)
        self.assertIsNotNone(response)
        self.assertEquals(1, response.success)

        # delete the user
        self.__deleteUser()

    def testDeleteResources(self):
        """Test deleting a file at a specified path"""

        apiError = False
        try:
            # authenticate the user first
            self.__authenticateUser()

            # create a test folder, then attempt to delete it
            self.api.createFolder(self.accessToken, self.FOLDER, self.ROOT_DIR)
            response = self.api.deleteResources(self.accessToken, self.ROOT_DIR + self.FOLDER)
            firstResult = response.results[0]

        except Exception as e:
            print 'Error on deleteResources: ', e
            apiError = True

        # test all assertions
        self.assertFalse(apiError)
        self.assertIsNotNone(response)
        self.assertIsNotNone(firstResult)
        self.assertEquals(self.ROOT_DIR + self.FOLDER, firstResult.file)

    def testDeleteUser(self):
        """Test deleting a specified subaccount user"""

        # create then delete the test user
        apiError = False
        try:
            self.__authenticateUser()
            self.__createUser()
            response = self.__deleteUser()
        except Exception as e:
            print 'Error on deleteUser: ', e
            apiError = True

        # test all assertions
        self.assertFalse(apiError)
        self.assertIsNotNone(response)
        self.assertEquals(1, response.success)

    def testGetAccount(self):
        """Test getting the account for the currently logged in user"""

        apiError = False
        try:
            self.__authenticateUser()
            response = self.api.getAccount(self.accessToken)
        except Exception as e:
            print 'Error on getAccount: ', e
            apiError = True

        self.assertFalse(apiError)
        self.assertIsNotNone(response)
        self.assertEquals(self.USERNAME, response.results.username)

    def testGetCurrentUser(self):
        """Test getting the currently logged in user"""

        # authenticate and get the current user
        apiError = False
        try:
            self.__authenticateUser()
            response = self.api.getCurrentUser(self.accessToken)
            results = response.results
        except Exception as e:
            print 'Error on getCurrentUser: ', e
            apiError = True

        # test all assertions
        self.assertFalse(apiError)
        self.assertIsNotNone(results)
        self.assertEquals(self.USERNAME, results.username)
        self.assertEquals(self.USERNAME, results.nickname)
        self.assertEquals('master', results.role)

    def testGetDownloadFileUrl(self):
        """Test getting a URL for the specified file to download"""

        # authenticate the user and get the download file URL
        apiError = False
        try:
            self.__authenticateUser()
            response = self.api.getDownloadFileUrl(self.accessToken, self.DOWNLOAD_FILE)
            results = response.results
        except Exception as e:
            print 'Error on getDownloadFileUrl: ', e
            apiError = True

        # test all assertions
        self.assertFalse(apiError)
        self.assertIsNotNone(response)
        self.assertIsNotNone(results)
        self.assertTrue(results.url)

    def testGetFileActivityLogs(self):
        """Test retrieving the file activity logs for the given account"""

        # authenticate and get the file activity logs for the account
        apiError = False
        try:
            self.__authenticateUser()
            response = self.api.getFileActivityLogs(self.accessToken, **{'offset':0})
        except Exception as e:
            print 'Error on getFileActivityLogs: ', e
            apiError = True

        # test all assertions
        self.assertFalse(apiError)
        self.assertIsNotNone(response)
        self.assertTrue(response.success)
        self.assertIsInstance(response.results, list)

    def testGetFolders(self):
        """Test retrieving folders for a specified root path"""

        # authenticate and get the folders at the root path
        apiError = False
        try:
            self.__authenticateUser()
            response = self.api.getFolders(self.accessToken, self.ROOT_DIR)
            firstResult = response.results[0]
        except Exception as e:
            print 'Error on getFolders: ', e
            apiError = True

        # test all assertions
        self.assertIsNotNone(response)
        self.assertTrue(response.success)
        self.assertIsNotNone(firstResult)
        self.assertIsInstance(response.results, list)

    def testGetResourceList(self):
        """Test retrieving all resources for a specified root path"""

        # authenticate user and get the resource list
        apiError = False
        try:
            self.__authenticateUser()
            response = self.api.getResourceList(
                self.accessToken, self.ROOT_DIR, 'sort_files_type', 'asc', 1, 25
                )
            results = response.results
        except Exception as e:
            print 'Error on getResourcesList: ', e
            apiError = True

        # test all assertions
        self.assertFalse(apiError)
        self.assertIsNotNone(response)
        self.assertIsNotNone(results)
        self.assertIsInstance(results.resources, list)

    def testGetResourceProperties(self):
        """Test retrieving all resource properties for a specified root path"""

        # authenticate user and get the resource properties
        apiError = False
        try:
            self.__authenticateUser()
            response = self.api.getResourceProperties(self.accessToken, [self.ROOT_DIR])
        except Exception as e:
            print 'Error on getResourceProperties: ', e
            apiError = True

        # test all assertions
        self.assertFalse(apiError)
        self.assertIsNotNone(response)
        self.assertIsInstance(response.results, list)

    def testGetUser(self):
        """Test retrieving a specified subaccount user"""

        # authenticate user and get the specified user
        apiError = False
        try:
            self.__authenticateUser()
            response = self.api.getUser(self.accessToken, self.USERNAME)
        except Exception as e:
            print 'Error on getUser: ', e
            apiError = True

        # test assertions
        self.assertFalse(apiError)
        self.assertIsNotNone(response)
        self.assertIsNotNone(response.results)

    def testGetUsers(self):
        """Test getting all users for the current account"""

        # authenticate user and get the users associated with this
        # account
        apiError = False
        try:
            self.__authenticateUser()
            response = self.api.getUsers(self.accessToken, "sort_users_username", "asc")
        except Exception as e:
            print 'Error on getUsers: ', e
            apiError = True

        # test assertions
        self.assertFalse(apiError)
        self.assertIsNotNone(response)
        self.assertIsNotNone(response.results[0])

    def testMoveResources(self):
        """Test moving the specified resource to another path"""

        # authenticate the user and move test resource from one
        # location to another
        apiError = False
        try:
            self.__authenticateUser()

            # create bunch of test folders
            folder1 = self.api.createFolder(self.accessToken, self.FOLDER, self.ROOT_DIR)
            folder2 = self.api.createFolder(self.accessToken, self.SUBFOLDER, self.ROOT_DIR)

            if (not folder1.success) or (not folder2.success):
                raise Exception('One or more test folders could not be created')

            # make the call to moveResources
            response = self.api.moveResources(self.accessToken, [self.SUBFOLDER], self.FOLDER)
            self.__checkResponseStatus(response)
            firstResult = response.results[0]

            # setup the expected values
            folder      = self.ROOT_DIR + self.FOLDER
            subFolder   = self.ROOT_DIR + self.SUBFOLDER
            movedFolder = folder + subFolder

            # cleanup test folders
            self.api.deleteResources(self.accessToken, folder)
            self.api.deleteResources(self.accessToken, movedFolder)

        except Exception as e:
            print 'Error on moveResources: ', e
            apiError = True

        # test assertions
        self.assertFalse(apiError)
        self.assertIsNotNone(firstResult)
        self.assertEquals(subFolder, firstResult.file)

    def testPreviewFile(self):
        """Test retrieving a preview image for a previewable file"""

        # authenticate the user and retrieve the preview image
        apiError = False
        try:
            self.__authenticateUser()
            response = self.api.previewFile(self.accessToken, self.PREVIEW, "small")
            results = response.results
        except Exception as e:
            print 'Error on previewFile: ', e
            apiError = True

        # test assertions
        self.assertFalse(apiError)
        self.assertIsNotNone(response)
        self.assertIsNotNone(results)

    def testRenameResource(self):
        """Test renaming a file or folder"""

        # authenticate and rename the test resource
        apiError = False
        try:
            self.__authenticateUser()

            # create the test folder
            response = self.api.createFolder(self.accessToken, self.RENAME_FOLDER, self.ROOT_DIR)
            self.__checkResponseStatus(response)

            # rename the folder
            originalFolder = self.ROOT_DIR + self.RENAME_FOLDER
            newFolderName  = self.RENAME_FOLDER + "-CHANGED"
            response = self.api.renameResource(self.accessToken, originalFolder, newFolderName)
            self.__checkResponseStatus(response)

            # delete test folder
            self.api.deleteResources(self.accessToken, newFolderName)

        except Exception as e:
            print 'Error on renameResource: ', e
            apiError = True

        # test assertions
        self.assertFalse(apiError)
        self.assertIsNotNone(response)
        self.assertEquals(1, response.success)

    def testUpdateUser(self):
        """Test updating the settings for a user"""

        # authenticate, create a temp user and update its details
        apiError = False
        try:
            self.__authenticateUser()

            # create a temporary user
            response = self.__createUser()
            self.__checkResponseStatus(response)

            # make call to update the user's username
            response = self.api.getUser(self.accessToken, self.TEST_USER)
            userId   = response.results.id
            response = self.api.updateUser(self.accessToken, userId, self.TEST_USER + "-CHANGED")
            self.__checkResponseStatus(response)

            # delete the user
            self.api.deleteUser(self.accessToken, self.TEST_USER + "-CHANGED")

        except Exception as e:
            print 'Error on updateUser: ', e
            apiError = True

        # test assertions
        self.assertFalse(apiError)
        self.assertIsNotNone(response)
        self.assertEquals(1, response.success)

    def testUserAvailable(self):
        """Test to verify that a given username is available"""

        # authenticate and test if the given username is available
        apiError = False
        try:
            self.__authenticateUser()
            response = self.api.userAvailable(self.accessToken, self.USERNAME)
            results = response.results
        except Exception as e:
            print 'Error on userAvailable: ', e
            apiError = True

        # test assertions
        self.assertFalse(apiError)
        self.assertIsNotNone(response)
        self.assertIsNotNone(results)
        self.assertFalse(results.available)

    ### Private Methods ###

    def __authenticateUser(self):
        """Authenticates the test user"""
        response = self.api.authenticateUser(self.USERNAME, self.PASSWORD)
        if response.success:
            self.accessToken = response.results.accessToken
            return response
        else:
            raise Exception(response.error.message)

    def __createUser(self):
        """Creates a test user"""
        return self.api.createUser(
            self.accessToken,
            self.TEST_USER,
            self.ROOT_DIR,
            self.TEST_EMAIL,
            self.PASSWORD,
            self.USER_TYPE,
            self.PERMISSIONS,
            self.TIMEZONE            
            )

    def __deleteUser(self):
        """Deletes a test user"""
        return self.api.deleteUser(self.accessToken, self.TEST_USER)

    def __checkResponseStatus(self, response):
        """Checks for a valid API response"""
        if not response.success:
            raise Exception(response.error.message)        

# Execute the unit tests        
if __name__ == '__main__':
    unittest.main()

