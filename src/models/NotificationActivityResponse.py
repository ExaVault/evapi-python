#!/usr/bin/env python
"""
Copyright 2014 ExaVault, Inc.

NOTE: This file was generated automatically. Do not modify by hand.
"""

class NotificationActivityResponse:

    def __init__(self):
        self.swaggerTypes = {
            'success': 'int',
            'error': 'Error',
            'results': 'list[NotificationMessage]'

        }


        self.success = None # int
        self.error = None # Error
        self.results = None # list[NotificationMessage]
        
