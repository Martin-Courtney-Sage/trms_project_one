# UNIT TESTING

import unittest
from exceptions.resource_not_found import ResourceNotFound
from exceptions.funds_not_available import FundsNotAvailable


class TestExceptions(unittest.TestCase):

    def test_resource(self):
        print("First Test")
        try:
            raise ResourceNotFound
        except:
            print("handled it")
        print("Complete")

    def test_funds(self):
        print("Second Test")
        try:
            raise FundsNotAvailable
        except:
            print("handled it")
        print("Complete")
