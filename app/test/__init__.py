import unittest

from app import create_app, db

class BaseTestClass(unittest.TestCase):
    def setUp(self):
        self.app = create_app(settings_module="config.testing")
        self.client = self.app.test_client()

        # Create a context for application:
        with self.app.app_context():
            # Create tables from database:
            db.create_all()

    def tearDown(self):
        with self.app.app_context():
            # Delete all tables from database:
            db.session.remove()
            db.drop_all()