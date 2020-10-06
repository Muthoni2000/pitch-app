from app import app
import unittest
from app.models import User

@@ -8,4 +7,16 @@ def setUp(self):
        self.new_user = User(password = 'bread')

    def test_password_setter(self):
        self.assertTrue(self.new_user.pass_secure is None) 
        self.assertTrue(self.new_user.pass_secure is None)


    def test_no_access_password(self):
        with self.assertRaises(AttributeError):
            self.new_user.password

    def test_password_verification(self):
        self.assertTrue(self.new_user.verify_password('bread'))


if __name__ == '__main__':
    unittest.main() 
