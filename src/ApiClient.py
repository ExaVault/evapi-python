#!/usr/bin/env python
"""
ApiClient

Generic ApiClient contains a callAPI method for sending API requests
to the API server.
"""

import sys
import os
import re
import urllib
import httplib
import json
import datetime

from models import *
from requests import Request, Session  # EV NOTE - use requests instead of urllib2

class ApiClient:
    """Generic API client for Swagger client library builds"""

    def __init__(self, apiKey=None, apiServer=None):
        if apiKey == None:
            raise Exception('You must pass an apiKey when instantiating the '
                            'APIClient')
        self.apiKey = apiKey
        self.apiServer = apiServer
        self.cookie = None

    # EV NOTE: we need to seralize this data as x-www-form-urlencoded
    # data (minus the URL encoding, since this is sent via the POST
    # body)
    def __serializeAsFormData (self, dict):

        formData = "";

        for key in dict :
            value = dict[key]
            if type(value) is list :
                for item in value :
                    formData += (key + "[]=" + str(item) + "&")
            else :
                formData += (key + "=" + str(value) + "&")

        return formData[:-1]    

    def callAPI(self, resourcePath, method, queryParams, postData, headerParams=None):

        url = self.apiServer + resourcePath

        # set the headers
        headers = {}
        if headerParams:
            for param, value in headerParams.iteritems():
                headers[param] = value

        headers['api_key'] = self.apiKey

        data = None

        if method in ['GET']:
            pass
        elif method in ['POST', 'PUT', 'DELETE']:
            if postData:
                """ EV NOTE: POST requests are specified differently for our API
                headers['Content-type'] = 'application/json'
                data = self.sanitizeForSerialization(postData)
                data = json.dumps(data)
                """
                headers['Content-Type'] = 'application/x-www-form-urlencoded'
                data = self.__serializeAsFormData(postData)
        else:
            raise Exception('Method ' + method + ' is not recognized.')

        # create and prepare the request
        session = Session()
        request = Request(method, url = url, data = data, headers = headers)

        prepared = session.prepare_request(request)

        # send the request
        response = session.send(prepared)

        if 'Set-Cookie' in response.headers:
            self.cookie = response.headers['Set-Cookie']

        try:
            data = json.loads(response.content)
        except ValueError:
            data = None

        return data

    def toPathValue(self, obj):
        """Convert a string or object to a path-friendly value
        Args:
            obj -- object or string value
        Returns:
            string -- quoted value
        """
        if type(obj) == list:
            return urllib.quote(','.join(obj))
        else:
            return urllib.quote(str(obj))

    def sanitizeForSerialization(self, obj):
        """Dump an object into JSON for POSTing."""

        if type(obj) == type(None):
            return None
        elif type(obj) in [str, int, long, float, bool]:
            return obj
        elif type(obj) == list:
            return [self.sanitizeForSerialization(subObj) for subObj in obj]
        elif type(obj) == datetime.datetime:
            return obj.isoformat()
        else:
            if type(obj) == dict:
                objDict = obj
            else:
                objDict = obj.__dict__
            return {key: self.sanitizeForSerialization(val)
                    for (key, val) in objDict.iteritems()
                    if key != 'swaggerTypes'}

        if type(postData) == list:
            # Could be a list of objects
            if type(postData[0]) in safeToDump:
                data = json.dumps(postData)
            else:
                data = json.dumps([datum.__dict__ for datum in postData])
        elif type(postData) not in safeToDump:
            data = json.dumps(postData.__dict__)

    def deserialize(self, obj, objClass):        
        
        """Derialize a JSON string into an object.

        Args:
            obj -- string or object to be deserialized
            objClass -- class literal for deserialzied object, or string
                of class name
        Returns:
            object -- deserialized object"""

        # Have to accept objClass as string or actual type. Type could
        # be a native Python type, or one of the model classes.

        if type(objClass) == str:
            if 'list[' in objClass:
                match = re.match('list\[(.*)\]', objClass)
                subClass = match.group(1)
                return [self.deserialize(subObj, subClass) for subObj in obj]

            # EV NOTE: add 'unicode' as valid type for Python -
            # unicode and ascii encoded 'str' type are different
            if (objClass in ['int', 'float', 'long', 'dict', 'list', 'str', 'bool', 'datetime', 'unicode']):
                objClass = eval(objClass)
            else:  # not a native type, must be model class
                objClass = eval(objClass + '.' + objClass)

        # EV NOTE: add 'unicode' as valid type
        if objClass in [int, long, float, dict, list, str, bool, unicode]:
            return objClass(obj)
        elif objClass == datetime:
            # Server will always return a time stamp in UTC, but with
            # trailing +0000 indicating no offset from UTC. So don't process
            # last 5 characters.
            return datetime.datetime.strptime(obj[:-5],
                                              "%Y-%m-%dT%H:%M:%S.%f")

        instance = objClass()

        for attr, attrType in instance.swaggerTypes.iteritems():
            if obj is not None and attr in obj and type(obj) in [list, dict]:
                value = obj[attr]
                if attrType in ['str', 'int', 'long', 'float', 'bool']:
                    attrType = eval(attrType)
                    try:
                        value = attrType(value)
                    except UnicodeEncodeError:
                        value = unicode(value)
                    except TypeError:
                        value = value
                    setattr(instance, attr, value)
                    
                elif (attrType == 'datetime'):
                    setattr(instance, attr, datetime.datetime.strptime(value[:-5],
                                              "%Y-%m-%dT%H:%M:%S.%f"))
                elif 'list[' in attrType:
                    match = re.match('list\[(.*)\]', attrType)
                    subClass = match.group(1)
                    subValues = []
                    if not value:
                        setattr(instance, attr, None)
                    else:
                        for subValue in value:

                            # EV NOTE - This is a hack, but no way
                            # around it. 'str' is an ascii encoded
                            # string, while 'unicode' is for unicode
                            # strings. Since our API resource
                            # specifies the paths parameter as a
                            # string (other languages don't have a
                            # 'unicode' type), we need to force the
                            # class type here so that the
                            # deserialization process won't break

                            if attr == 'paths':
                                subClass = unicode

                            subValues.append(self.deserialize(subValue,
                                                              subClass))
                            
                    setattr(instance, attr, subValues)
                else:
                    setattr(instance, attr, self.deserialize(value,
                                                             attrType)) # EV NOTE - this was 'objClass' (bug)

        return instance

