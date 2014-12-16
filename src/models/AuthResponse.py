#!/usr/bin/env python
"""
Copyright 2014 ExaVault, Inc.

NOTE: This file was generated automatically. Do not modify by hand.
"""

class AuthResponse:

    def __init__(self):
        self.swaggerTypes = {
            'success': 'int',
            'error': 'Error',
            'results': 'Auth'

        }            

        self.success = None # int
        self.error = None # Error
        self.results = None # Auth
        
        def __repr__(self):
            return '<Auth success:%s error:%s :%s results:%s>' % (
                self.success, self.error, self.results
            )
