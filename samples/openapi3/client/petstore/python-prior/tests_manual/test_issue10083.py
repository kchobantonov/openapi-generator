# coding: utf-8

"""
    OpenAPI Petstore

    This spec is mainly for testing Petstore server and contains fake endpoints, models. Please do not use this for any other purpose. Special characters: \" \\  # noqa: E501

    The version of the OpenAPI document: 1.0.0
    Generated by: https://openapi-generator.tech
"""


import sys
import unittest

import petstore_api
from petstore_api.model.dog import Dog
from petstore_api.model.legs import Legs


class TestSetAttrForComposedSchema(unittest.TestCase):
    """TestSetAttrForComposedSchema unit test"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testSetAttrForComposedSchema(self):
        """Test SetAttrForComposedSchema"""
        try:
            dog_instance = Dog(class_name="Dog", color="Black")
            dog_instance.breed = "bulldog"
            dog_instance.legs = Legs(legs="4")
        except petstore_api.exceptions.ApiTypeError:
            self.assertTrue(False)


if __name__ == '__main__':
    unittest.main()