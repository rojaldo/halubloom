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
from swagger_client.apis.effect_api import EffectApi


class TestEffectApi(unittest.TestCase):
    """ EffectApi unit test stubs """

    def setUp(self):
        self.api = swagger_client.apis.effect_api.EffectApi()

    def tearDown(self):
        pass

    def test_play_effect(self):
        """
        Test case for play_effect

        Adds a new Effect to the database
        """
        pass

    def test_stop_effect(self):
        """
        Test case for stop_effect

        Stops an effect
        """
        pass


if __name__ == '__main__':
    unittest.main()
