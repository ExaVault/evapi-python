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

from models import *
from var_dump import var_dump

class EvapiTest(unittest.TestCase):

    # NOTE: the below variables are needed for successful completion
    # of tests. Be sure to populate each with your actual account
    # information, where relevant

    USERNAME      = 'yourusername'
    PASSWORD      = 'yourpassword'
    API_KEY       = 'yourapp-XXXXXXXXXXXXXXXXXXXX'
    API_SERVER    = 'https://api.exavault.com'
    ROOT_DIR      = '/'
    FOLDER        = 'unit-tests'
    SUBFOLDER     = 'subfolder'
    TEST_USER     = 'unit-tests'
    TEST_EMAIL    = 'youremail@yourdomain.com'
    PREVIEW       = '/test-files/preview/images.jpg'
    RENAME_FOLDER = 'test-rename-folder'
    DOWNLOAD_FILE = '/test-files/file-tree.txt'
    UPLOAD_FILE   = 'test-filename.txt'
    TIMEZONE      = 'America/Los_Angeles'
    USER_TYPE     = 'user'
    PERMISSIONS   = 'upload,download,modify,delete'

    api = None
    accessToken = None

    ### Setup and teardown methods ###

    @classmethod
    def setUpClass(cls):
        cls.api = V1Api.V1Api( ApiClient.ApiClient(cls.API_KEY, cls.API_SERVER) )

    @classmethod
    def tearDownClass(cls):
        if cls.accessToken is not None:
            cls.api.logoutUser(cls.accessToken)

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
        return self.api.createUser(self.accessToken, self.TEST_USER, self.ROOT_DIR, self.TEST_EMAIL, self.PASSWORD, self.USER_TYPE, self.PERMISSIONS, self.TIMEZONE)

    def __deleteUser(self):
        """Deletes a test user"""
        return self.api.deleteUser(self.accessToken, self.TEST_USER)

    def __checkResponseStatus(self, response):
        """Checks for a valid API response"""
        if not response.success:
            raise Exception(response.error.message)

    def __runResponseAssertions(self, response, apiError):
        """Run the standard response assertions"""
        self.assertFalse(apiError)
        self.assertIsNotNone(response)
        self.assertEquals(response.success, 1)

    def __runErrorAssertions(self, error):
        """Run the standard error assertions"""
        self.assertIsNotNone(error)
        self.assertEqual(error.__class__.__name__, "Error")
        self.assertIsNone(error.code)
        self.assertIsNone(error.message)

    def __runUserAssertions(self, user):
        self.assertIsNotNone(user)
        self.assertEquals(user.__class__.__name__, "User")
        self.assertIsInstance(user.id, int)
        self.assertIsInstance(user.gid, int)
        self.assertIsInstance(user.owningAccountId, int)
        self.assertIsInstance(user.role, str)
        self.assertIsInstance(user.email, str)
        self.assertIsInstance(user.status, int)
        self.assertIsInstance(user.username, str)
        self.assertIsInstance(user.nickname, str)
        self.assertIsInstance(user.accessTimestamp, str)
        self.assertIsInstance(user.homeDir, str)
        self.assertIsInstance(user.share, bool)
        self.assertIsInstance(user.upload, bool)
        self.assertIsInstance(user.changePassword, bool)
        self.assertIsInstance(user.download, bool)
        self.assertIsInstance(user.modify, bool)
        self.assertIsInstance(user.notification, bool)
        self.assertIsInstance(user.list, bool)
        self.assertIsInstance(user.delete, bool)
        self.assertIsInstance(user.expiration, str)
        self.assertIsInstance(user.timeZone, str)
        self.assertIsInstance(user.created, str)
        self.assertIsInstance(user.modified, str)

    def __runResourcePropertyAssertions(self, resourceProp):
        self.assertIsNotNone(resourceProp)
        self.assertEquals(resourceProp.__class__.__name__, "ResourceProperty")
        self.assertIsInstance(resourceProp.parent, str)
        self.assertIsInstance(resourceProp.type, str)
        self.assertIsInstance(resourceProp.shares, list)
        self.assertIsInstance(resourceProp.uploadDate, str)
        self.assertIsInstance(resourceProp.createdBy, str)
        self.assertIsInstance(resourceProp.path, str)
        self.assertIsInstance(resourceProp.size, int)
        self.assertIsInstance(resourceProp.previewable, bool)
        self.assertIsInstance(resourceProp.fileCount, int)
        self.assertIsInstance(resourceProp.name, str)

    ### Test Cases ###

    def testAuthenticateUser(self):                
        """Test authenticating a user"""

        # attempt to authenticate the user
        apiError = False
        try:
            response = self.__authenticateUser()
            results = response.results
        except Exception as e:
            apiError = True

        # run assertions
        self.__runResponseAssertions(response, apiError)
        self.__runErrorAssertions(response.error)
        self.assertEqual(response.__class__.__name__, "AuthResponse")

        results = response.results;
        self.assertIsNotNone(results)
        self.assertEquals(results.__class__.__name__, "Auth")
        self.assertEquals(results.username, self.USERNAME)
        self.assertIsNotNone(results.accessToken)
        self.assertIsNotNone(results.clientIp)
        self.assertIsInstance(results.accessToken, str)
        self.assertIsInstance(results.clientIp, str)

    def testCheckFilesExist(self):
        """Test to see if file exists"""

        # authenticate and check if file exists
        apiError = False
        try:
            self.__authenticateUser()
            response = self.api.checkFilesExist(self.accessToken, [self.ROOT_DIR])
        except Exception as e:
            apiError = True

        # run assertions
        self.__runResponseAssertions(response, apiError)
        self.__runErrorAssertions(response.error)
        self.assertEqual(response.__class__.__name__, "ExistingResourcesResponse")

        results = response.results;
        self.assertIsNotNone(results)
        self.assertIsInstance(results, list)
        self.assertGreater(len(results), 0)

        firstResult = response.results[0];
        self.assertIsNotNone(firstResult)
        self.assertEquals(firstResult.__class__.__name__, "ExistingResource")
        self.assertTrue(firstResult.exists)

        resource = firstResult.resource;
        self.assertIsNotNone(resource)
        self.assertEquals(resource.__class__.__name__, "ResourceProperty")

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

            # setup expected values
            copiedFolder = self.FOLDER + "/" + self.SUBFOLDER

            # cleanup directories we just created
            self.api.deleteResources(self.accessToken, [self.FOLDER, self.SUBFOLDER])

        except Exception as e:
            apiError = True

        # run assertions
        self.__runResponseAssertions(response, apiError)
        self.__runErrorAssertions(response.error)
        self.assertEqual(response.__class__.__name__, "ModifiedResourcesResponse")

        firstResult = response.results[0]
        self.assertIsNotNone(firstResult)
        self.assertEqual(firstResult.__class__.__name__, "ModifiedResource")
        self.assertEquals(firstResult.success, 1)
        self.assertGreater(firstResult.size, 0)
        self.assertEquals(self.ROOT_DIR + self.SUBFOLDER, firstResult.file)
        self.assertEquals(self.ROOT_DIR + copiedFolder, firstResult.destination)

    def testCreateFolder(self):
        """Test creating a folder on the remote host"""

        # authenticate and create a folder
        apiError = False
        try:
            self.__authenticateUser()
            response = self.api.createFolder(self.accessToken, self.FOLDER, self.ROOT_DIR)
        except Exception as e:
            apiError = True

        # run assertions
        self.__runResponseAssertions(response, apiError)
        self.__runErrorAssertions(response.error)
        self.assertEqual(response.__class__.__name__, "Response")        

        results = response.results
        self.assertIsNotNone(results)
        self.assertIsInstance(results, list)
        self.assertEquals(len(results), 0)

        # cleanup
        self.api.deleteResources(self.accessToken, self.FOLDER)

    def testCreateUser(self):
        """Test creating a new subaccount user"""

        # authenticate and create the user
        apiError = False
        try:
            self.__authenticateUser()
            response = self.__createUser()
        except Exception as e:
            apiError = True

        # run assertions
        self.__runResponseAssertions(response, apiError)        
        self.__runErrorAssertions(response.error)
        self.assertEqual(response.__class__.__name__, "Response")

        results = response.results
        self.assertIsNotNone(results)
        self.assertIsInstance(results, list)
        self.assertEquals(len(results), 0)

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
            response = self.api.deleteResources(self.accessToken, [self.FOLDER])

        except Exception as e:
            apiError = True

        # test all assertions
        self.__runResponseAssertions(response, apiError)
        self.__runErrorAssertions(response.error)
        self.assertEqual(response.__class__.__name__, "DeletedResourcesResponse")

        firstResult = response.results[0]
        self.assertIsNotNone(firstResult)
        self.assertEqual(firstResult.__class__.__name__, "DeletedResource")

        self.assertIsInstance(firstResult.success, int)
        self.assertIsInstance(firstResult.size, int)
        self.assertIsInstance(firstResult.file, str)

        self.assertEquals(firstResult.success, 1)
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
            apiError = True

        # test all assertions
        self.__runResponseAssertions(response, apiError)
        self.__runErrorAssertions(response.error)
        self.assertEqual(response.__class__.__name__, "Response")

        results = response.results
        self.assertIsNotNone(results)
        self.assertIsInstance(results, list)
        self.assertEquals(len(results), 0)

    def testGetAccount(self):
        """Test getting the account for the currently logged in user"""

        apiError = False
        try:
            self.__authenticateUser()
            response = self.api.getAccount(self.accessToken)
        except Exception as e:
            apiError = True

        # run assertions
        self.__runResponseAssertions(response, apiError)
        self.__runErrorAssertions(response.error)
        self.assertEqual(response.__class__.__name__, "AccountResponse")

        results = response.results
        self.assertIsNotNone(results)
        self.assertEquals(results.__class__.__name__, "Account")

        self.assertIsInstance(results.id, int)
        self.assertIsInstance(results.clientId, int)        
        self.assertIsInstance(results.userCount, int)
        self.assertIsInstance(results.redirect, str)
        self.assertIsInstance(results.bandwidthQuotaUsed, long)
        self.assertIsInstance(results.bandwidthQuotaLimit, long)
        self.assertIsInstance(results.diskQuotaUsed, long)
        self.assertIsInstance(results.diskQuotaLimit, long)
        self.assertIsInstance(results.showReferralLinks, bool)
        self.assertIsInstance(results.customDomain, bool)
        self.assertIsInstance(results.secureOnly, bool)
        self.assertIsInstance(results.username, str)
        self.assertIsInstance(results.status, int)
        self.assertIsInstance(results.maxUsers, int)
        self.assertIsInstance(results.planCode, str)
        self.assertIsInstance(results.appliedTrial, str)
        self.assertIsInstance(results.externalDomains, str)
        self.assertIsInstance(results.branding, bool)
        self.assertIsInstance(results.freeTrial, bool)
        self.assertIsInstance(results.quotaNoticeEnabled, int)
        self.assertIsInstance(results.quotaNoticeThreshold, int)
        self.assertIsInstance(results.complexPasswords, bool)
        self.assertIsInstance(results.created, str)        
        self.assertIsInstance(results.modified, str)

        self.assertEquals(self.USERNAME, results.username)

        masterAccount = results.masterAccount
        self.__runUserAssertions(masterAccount)

    def testGetCurrentUser(self):
        """Test getting the currently logged in user"""

        # authenticate and get the current user
        apiError = False
        try:
            self.__authenticateUser()
            response = self.api.getCurrentUser(self.accessToken)            
        except Exception as e:
            apiError = True

        # run assertions
        self.__runResponseAssertions(response, apiError)
        self.__runErrorAssertions(response.error)
        self.assertEqual(response.__class__.__name__, "UserResponse")

        results = response.results
        self.__runUserAssertions(results)

    def testGetDownloadFileUrl(self):
        """Test getting a URL for the specified file to download"""

        # authenticate the user and get the download file URL
        apiError = False
        try:
            self.__authenticateUser()
            response = self.api.getDownloadFileUrl(self.accessToken, self.DOWNLOAD_FILE)
        except Exception as e:
            apiError = True

        # test all assertions
        self.__runResponseAssertions(response, apiError)
        self.__runErrorAssertions(response.error)
        self.assertEqual(response.__class__.__name__, "UrlResponse")

        results = response.results
        self.assertIsInstance(results.url, str)        

    def testGetFileActivityLogs(self):
        """Test retrieving the file activity logs for the given account"""

        # authenticate and get the file activity logs for the account
        apiError = False
        try:
            self.__authenticateUser()
            response = self.api.getFileActivityLogs(self.accessToken, **{'offset':0})
        except Exception as e:
            apiError = True

        # test all assertions
        self.__runResponseAssertions(response, apiError)
        self.__runErrorAssertions(response.error)
        self.assertEqual(response.__class__.__name__, "LogResponse")

        results = response.results
        self.assertIsInstance(results, list)

        for log in results:
            self.assertIsInstance(log.fileName, str)
            self.assertIsInstance(log.fileSource, str)
            self.assertIsInstance(log.operation, str)
            self.assertIsInstance(log.duration, str)
            self.assertIsInstance(log.id, int)
            self.assertIsInstance(log.created, str)
            self.assertIsInstance(log.username, str)
            self.assertIsInstance(log.sessionId, str)
            self.assertIsInstance(log.ipAddress, str)
            self.assertIsInstance(log.protocol, str)
            self.assertIsInstance(log.status, str)

    def testGetFolders(self):
        """Test retrieving folders for a specified root path"""

        # authenticate and get the folders at the root path
        apiError = False
        try:
            self.__authenticateUser()
            response = self.api.getFolders(self.accessToken, self.ROOT_DIR)
        except Exception as e:
            apiError = True

        # test all assertions
        self.__runResponseAssertions(response, apiError)
        self.__runErrorAssertions(response.error)
        self.assertEqual(response.__class__.__name__, "ResourcePropertiesResponse")

        firstResult = response.results[0]
        self.__runResourcePropertyAssertions(firstResult)

    def testGetResourceList(self):
        """Test retrieving all resources for a specified root path"""

        # authenticate user and get the resource list
        apiError = False
        try:
            self.__authenticateUser()
            response = self.api.getResourceList(self.accessToken, self.ROOT_DIR, 'sort_files_type', 'asc', 1, 25)
        except Exception as e:
            apiError = True

        # test all assertions
        self.__runResponseAssertions(response, apiError)
        self.__runErrorAssertions(response.error)
        self.assertEqual(response.__class__.__name__, "ResourceResponse")

        results = response.results
        self.assertIsNotNone(results)
        self.assertEquals(results.__class__.__name__, "Resource")
        self.assertIsInstance(results.totalFiles, int)
        self.assertIsInstance(results.resources, list)

        for resource in results.resources:
            self.__runResourcePropertyAssertions(resource)

    def testGetResourceProperties(self):
        """Test retrieving all resource properties for a specified root path"""

        # authenticate user and get the resource properties
        apiError = False
        try:
            self.__authenticateUser()
            response = self.api.getResourceProperties(self.accessToken, [self.ROOT_DIR])
        except Exception as e:
            apiError = True

        # run assertions
        self.__runResponseAssertions(response, apiError)
        self.__runErrorAssertions(response.error)
        self.assertEqual(response.__class__.__name__, "ResourcePropertiesResponse")

        results = response.results
        self.assertIsInstance(results, list)

        for resourceProperty in results:
            self.__runResourcePropertyAssertions(resourceProperty)

    def testGetUploadFileUrl(self):
        """Test getting a URL for the specified file to upload"""

        # authenticate the user and get the upload file URL
        apiError = False
        try:
            self.__authenticateUser()
            response = self.api.getUploadFileUrl(self.accessToken, 1024, self.ROOT_DIR + self.UPLOAD_FILE)
        except Exception as e:
            apiError = True

        # test all assertions
        self.__runResponseAssertions(response, apiError)
        self.__runErrorAssertions(response.error)
        self.assertEqual(response.__class__.__name__, "UrlResponse")

        results = response.results
        self.assertIsInstance(results.url, str)

    def testGetUser(self):
        """Test retrieving a specified subaccount user"""

        # authenticate user and get the specified user
        apiError = False
        try:
            self.__authenticateUser()
            response = self.api.getUser(self.accessToken, self.USERNAME)
        except Exception as e:
            apiError = True

        # run assertions
        self.__runResponseAssertions(response, apiError)
        self.__runErrorAssertions(response.error)
        self.assertEqual(response.__class__.__name__, "UserResponse")

        results = response.results
        self.__runUserAssertions(results)

    def testGetUsers(self):
        """Test getting all users for the current account"""

        # authenticate user and get the users associated with this
        # account
        apiError = False
        try:
            self.__authenticateUser()
            response = self.api.getUsers(self.accessToken, "sort_users_username", "asc")
        except Exception as e:
            apiError = True

        # run assertions
        self.__runResponseAssertions(response, apiError)
        self.__runErrorAssertions(response.error)
        self.assertEqual(response.__class__.__name__, "UsersResponse")

        results = response.results
        self.assertIsInstance(results, list)

        for user in results:
            self.__runUserAssertions(user)

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

            # setup the expected values
            movedFolder = self.FOLDER + "/" + self.SUBFOLDER

            # cleanup test folder
            self.api.deleteResources(self.accessToken, [self.FOLDER, movedFolder])

        except Exception as e:
            apiError = True

        # test assertions
        self.assertFalse(apiError)

        firstResult = response.results[0]
        self.assertIsNotNone(firstResult)
        self.assertEquals(self.ROOT_DIR + self.SUBFOLDER, firstResult.file)

    def testPreviewFile(self):
        """Test retrieving a preview image for a previewable file"""

        # authenticate the user and retrieve the preview image
        apiError = False
        try:
            self.__authenticateUser()
            response = self.api.previewFile(self.accessToken, self.PREVIEW, "small")
            
        except Exception as e:
            apiError = True

        # run assertions
        self.__runResponseAssertions(response, apiError)
        self.__runErrorAssertions(response.error)
        self.assertEqual(response.__class__.__name__, "PreviewFileResponse")

        results = response.results
        self.assertIsNotNone(results)
        self.assertIsInstance(results.size, int)
        self.assertIsInstance(results.image, str)
        self.assertIsInstance(results.imageId, str)

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
            apiError = True

        # run assertions
        self.__runResponseAssertions(response, apiError)
        self.__runErrorAssertions(response.error)
        self.assertEqual(response.__class__.__name__, "Response")

        results = response.results
        self.assertIsNotNone(results)
        self.assertIsInstance(results, list)
        self.assertEquals(len(results), 0)

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
            username = self.TEST_USER + "-CHANGED"
            response = self.api.updateUser(self.accessToken, userId, **{'username':username})
            self.__checkResponseStatus(response)

            # delete the user
            self.api.deleteUser(self.accessToken, self.TEST_USER + "-CHANGED")

        except Exception as e:
            apiError = True

        # run assertions
        self.__runResponseAssertions(response, apiError)        
        self.__runErrorAssertions(response.error)
        self.assertEqual(response.__class__.__name__, "Response")
            
        results = response.results
        self.assertIsNotNone(results)
        self.assertIsInstance(results, list)
        self.assertEquals(len(results), 0)

    def testUserAvailable(self):
        """Test to verify that a given username is available"""

        # authenticate and test if the given username is available
        apiError = False
        try:
            self.__authenticateUser()
            response = self.api.userAvailable(self.accessToken, self.TEST_USER)
            results = response.results
        except Exception as e:
            apiError = True

        # test assertions
        self.__runResponseAssertions(response, apiError)
        self.__runErrorAssertions(response.error)
        self.assertEqual(response.__class__.__name__, "AvailableUserResponse")

        results = response.results
        self.assertIsNotNone(results)
        self.assertIsInstance(results.available, bool)
        self.assertTrue(results.available)        

# Execute the unit tests        
if __name__ == '__main__':
    unittest.main()
