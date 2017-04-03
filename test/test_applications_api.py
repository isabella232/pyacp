# coding: utf-8

"""
    Platform Operations Rest API

    The Platform Operations REST API can be leveraged to customize the Platform Operator experience of managing infrastructure and applications for the Apprenda Platform. This allows some of the functionality of the Platform's System Operations Center (SOC) to be accomplished through a variety of means such as custom-built UX or command-line interfaces.   For more information about the abilities of Platform Operators, see our documentation on the [SOC](/current/SOC).   ##Authentication   Before making a request, you must be authenticated. Learn how to [get authenticated](/restapi/platformops/v1/authentication).   ##Making a Request   ###Prerequisites   * Installed Platform of version 6.5.1 or later (Note that most endpoints are only available in verison 6.7.0 and later)    * Authentication token   * If SOC authorization is enabled on your Platform, you must be assigned as an active Platform Operator   ###Request URL   All requests must use **https**.   The URL for every request you make is the Cloud URI of your Platform followed by \"/soc\" and the path structure of the endpoint. For example, if your Cloud URI is apps.apprenda.harp and you want to get the Add-ons for your Platform, the request URI will be **apps.apprenda.harp/soc/api/v1/addons**.   For more information, see our documentation on [using API resources](/restapi/platformops/v1/using-resources) and [finding your Cloud URI](/current/clouduri).   ###Request Headers   Your authenication token must be passed in the header of all requests using the key **ApprendaSessionToken** (not case sensitive).  

    OpenAPI spec version: v1

    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

from __future__ import absolute_import

import os
import sys
import unittest

import pyacp
from pyacp.rest import ApiException
from pyacp.apis.applications_api import ApplicationsApi
from pyacp.apprenda_ops_client import ApprendaOpsClient


class TestApplicationsApi(unittest.TestCase):
    """ ApplicationsApi unit test stubs """

    def setUp(self):
        self.api = pyacp.apis.applications_api.ApplicationsApi()

    def tearDown(self):
        pass

    def test_api_v1_applications_app_alias_versions_get(self):
        """
        Test case for api_v1_applications_app_alias_versions_get

        Get an application
        """

        try:
            self.client = ApprendaOpsClient('https://apps.se-sandbox.apprendalabs.com', 'elustgarten@apprenda.com',
                                            '@ppr3nd@')
            response = self.client.getApplications('developer')
            print(response)
        except ConnectionError as error:
            print(error)
        except Exception as ex:
            print(ex)

    def test_api_v1_applications_app_alias_versions_version_alias_get(self):
        """
        Test case for api_v1_applications_app_alias_versions_version_alias_get

        Get an application version
        """
        pass

    def test_apps_search_new(self):
        """
        Test case for apps_search_new

        Get all applications
        """
        pass

    def test_get_app_by_alias(self):
        """
        Test case for get_app_by_alias

        Get application
        """
        try:
            self.client = ApprendaOpsClient('https://apps.se-sandbox.apprendalabs.com', 'elustgarten@apprenda.com',
                                            '@ppr3nd@')
            response = self.client.getApplications()
            print(response)
        except ConnectionError as error:
            print(error)
        except Exception as ex:
            print(ex)


if __name__ == '__main__':
    unittest.main()
