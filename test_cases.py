
import unittest
from app import create_app
from db import db
from config_database import FULL_URL_DB

class TestWebApp(unittest.TestCase):
    def setUp(self):
        self.app = create_app()
        self.appctx = self.app.app_context()
        self.appctx.push()
        db.create_all()
        self.client = self.app.test_client()

    def tearDown(self):
        db.drop_all()
        self.appctx.pop()
        self.app = None
        self.appctx = None
        self.client = None

    # def test_app(self):
    #     assert self.app is not None
    #     assert current_app == self.app

    # test status 200 in /jokes/
    def test_get_jokes(self):
        response = self.client.get("/math", follow_redirects=True)
        self.assertEqual(response.status_code,200)

if __name__ == '__main__':
    print(FULL_URL_DB)
    unittest.main()