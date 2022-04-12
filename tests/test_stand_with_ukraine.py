import unittest
import sys
import os
import json
from flask import Flask
sys.path.append(os.path.join(os.path.dirname(__file__), ".."))
sys.path.append(os.path.join(os.path.dirname(__file__), "..", "elonmusk"))

from tests.mock_dialogflow_utils import *

from elonmusk.main import cloud_function

class TestStandWithUkraine(unittest.TestCase):

    def test_ukraine(self):
        """Test that question about Ukraine has Ukraine in answer"""
        app = Flask(__name__)

        with app.app_context():
            ukraine_request = get_test_request("ukraine_invasion")
            response = cloud_function(ukraine_request)
            result = json.loads(response.get_data(as_text=True))

            self.assertTrue(
                "Ukraine" in result["fulfillmentMessages"][0]["text"]["text"][0]
            )
        
    
    def test_zelensky(self):
        """Test that question about Zelensky has Zelensky in answer"""
        app = Flask(__name__)

        with app.app_context():
            zelensky_request = get_test_request("talk_to_zelensky")

            response = cloud_function(zelensky_request)
            result = json.loads(response.get_data(as_text=True))

            self.assertTrue(
                "Zelensky" in result["fulfillmentMessages"][0]["text"]["text"][0]
            )
    
    def test_kyiv(self):
        """Test that question about Kyiv has Kyiv in answer"""
        app = Flask(__name__)

        with app.app_context():
            kyiv_request = get_test_request("kyiv")

            response = cloud_function(kyiv_request)
            result = json.loads(response.get_data(as_text=True))

            self.assertTrue(
                "Kyiv" in result["fulfillmentMessages"][0]["text"]["text"][0]
            )

if __name__ == "__main__":
    unittest.main()