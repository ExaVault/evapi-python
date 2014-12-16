evapi-python
============

evapi-python is an API client written in Python for connecting to the
ExaVault API. The ExaVault API is a REST-like API providing operations
for file and user management, and supports both ``POST`` and ``GET``
requests.

To get started using ExaVault's API, you first must have an ExaVault
account and obtain an API key. For more information, please refer to
our [Developer page](https://www.exavault.com/developer) or contact
support@exavault.com for details.

## Prerequisites ##

evapi-python makes use of the [requests]
(https://github.com/kennethreitz/requests) library. Please ensure that
this library is installed before proceeding to use evapi-python.

**Note:** Some users have reported issues authenticating over SSL with
Python versions <= 2.7.2 (see [this
issue](https://github.com/kennethreitz/requests/issues/1847)). This
problem appears to be due to Python's SSL library automatically
choosing SSLv2/3 during SSL handshake, which will result in failure as
ExaVault has disabled both of these protocols due to the POODLE
exploit. As of this writing, testing the evapi-python client using
Python 2.7.8 does not reproduce this issue.

## Usage ##

TODO