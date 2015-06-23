#!/usr/bin/env python
"""
Copyright 2014 ExaVault, Inc.

NOTE: This file was generated automatically. Do not modify by hand.
"""

class Notification:

    def __init__(self):
        self.swaggerTypes = {
            'id': 'int',
            'userId': 'str',
            'type': 'str',
            'path': 'str',
            'name': 'str',
            'action': 'str',
            'usernames': 'list[str]',
            'recipients': 'list[Recipient]',
            'recipientEmails': 'list[str]',
            'sendEmail': 'str',
            'readableDescription': 'str',
            'readableDescriptionWithoutPath': 'str',
            'shareId': 'str',
            'created': 'str',
            'modified': 'str'

        }


        self.id = None # int
        self.userId = None # str
        self.type = None # str
        self.path = None # str
        self.name = None # str
        self.action = None # str
        self.usernames = None # list[str]
        self.recipients = None # list[Recipient]
        self.recipientEmails = None # list[str]
        self.sendEmail = None # str
        self.readableDescription = None # str
        self.readableDescriptionWithoutPath = None # str
        self.shareId = None # str
        self.created = None # str
        self.modified = None # str
        
