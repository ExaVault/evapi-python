#!/usr/bin/env python
"""
Copyright 2014 ExaVault, Inc.

NOTE: This file was generated automatically. Do not modify by hand.
"""

class Auth:

    def __init__(self):
        self.swaggerTypes = {
            'username': 'str',
            'accessToken': 'str',
            'mode': 'int',
            'clientIp': 'str'

        }

    def __repr__(self):
        return '<Auth username:%s accessToken:%s mode:%s clientIp:%s>' % (
            self.username, self.accessToken, self.mode, self.client
            )

        self.username = None # str
        self.accessToken = None # str
        self.mode = None # int
        self.clientIp = None # str


