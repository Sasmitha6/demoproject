import json
import unittest
from miniproj.src import palindrome


class Testpalindrome(unittest.TestCase):
    def setUp(self):
        self.event = {"numbers": [3553,0]}
        self.num = 3553
        self.rev = 0

    def test_lambda_handler(self):
        result = palindrome.lambda_handler(self.event, '')
        data = json.loads(result["body"])
        print("data: ", data)
        expected_response = {"palindrome": palindrome.palindrom(3553, 0)}
        self.assertEqual(data, expected_response)

    def test_palindrome(self):
        result = palindrome.palindrom(self.num, self.rev)
        self.assertEqual(result, palindrome.palindrom(3553, 0))
