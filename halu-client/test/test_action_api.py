# coding: utf-8

"""
    Halu API

    This should be a basic guide for the new Halu API. It will be updated as soon as I add new messages (or i'll try). The IP address to communicate with the master lamp is 10.0.0.1 by default.

    OpenAPI spec version: 1.0.0
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from __future__ import absolute_import

import os
import sys
import unittest

import swagger_client
from swagger_client.rest import ApiException
from swagger_client.apis.action_api import ActionApi


class TestActionApi(unittest.TestCase):
    """ ActionApi unit test stubs """

    def setUp(self):
        self.api = swagger_client.apis.action_api.ActionApi()

    def tearDown(self):
        pass

    def test_modify_effect(self):
        """
        Test case for modify_effect

        Stop effect
        """
        pass

    def test_use_ambiance(self):
        """
        Test case for use_ambiance

        Use Ambiance.
        """
        pass


if __name__ == '__main__':
    unittest.main()