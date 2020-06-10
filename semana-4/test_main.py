from main import create_token, verify_signature, SALT


class TestChallenge4:
    TOKEN = b'eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJsYW5ndWFnZSI6IlB5dGhvbiJ9.sM_VQuKZe_VTlqfS3FlAm8XLFhgvQQLk2kkRTpiXq7M'

    PAYLOAD = {"language": "Python"}

    def test_create_token(self):
        assert create_token(data=self.PAYLOAD, secret=SALT) == self.TOKEN

    def test_verify_signature(self):
        assert verify_signature(token=self.TOKEN) == self.PAYLOAD

    def test_verify_error_signature(self):
        assert verify_signature(token=self.TOKEN) == {"error": 2}
