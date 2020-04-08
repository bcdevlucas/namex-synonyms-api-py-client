# coding: utf-8

"""
    Synonyms API

    Retrieves the sets of synonyms for a given word.  # noqa: E501

    OpenAPI spec version: 1.0.0
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from __future__ import absolute_import

import unittest

import swagger_client
from swagger_client.api.name_processing_api import NameProcessingApi  # noqa: E501
from swagger_client.rest import ApiException


class TestNameProcessingApi(unittest.TestCase):
    """NameProcessingApi unit test stubs"""

    def setUp(self):
        self.api = swagger_client.api.name_processing_api.NameProcessingApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_get_word_classification(self):
        """Test case for get_word_classification

        """
        pass


if __name__ == '__main__':
    unittest.main()
