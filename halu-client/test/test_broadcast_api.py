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
from swagger_client.apis.broadcast_api import BroadcastApi


class TestBroadcastApi(unittest.TestCase):
    """ BroadcastApi unit test stubs """

    def setUp(self):
        self.api = swagger_client.apis.broadcast_api.BroadcastApi()

    def tearDown(self):
        pass

    def test_modify_color_broadcast(self):
        """
        Test case for modify_color_broadcast

        Plays color
        """
        pass

    def test_turn_off_broadcast(self):
        """
        Test case for turn_off_broadcast

        Plays turnOff
        """
        pass

    def test_turn_on_broadcast(self):
        """
        Test case for turn_on_broadcast

        Plays turnOn
        """
        pass


if __name__ == '__main__':
    unittest.main()
