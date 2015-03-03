from dshbrd import create_app
from dshbrd.database import db
from config import TestConfig
from dshbrd.auth.models import User
from faker import Factory

import unittest

fake = Factory.create()

admin_username = 'info'
admin_email = 'info@dshbrd.io'
admin_password = '123'


def make_db(num_users=5):
    db.drop_all()
    db.create_all()

    users = [
        User(
            admin_username,
            admin_email,
            admin_password,
            fake.ipv4(),
            active=True,
            is_admin=True
        )
    ]

    for _ in range(num_users):
        u = User(
            fake.userName(),
            fake.email(),
            fake.word() + fake.word(),
            fake.ipv4()
        )
        users.append(u)

    [db.session.add(x) for x in users]

    db.session.commit()


class ApiTestCase(unittest.TestCase):
    def setUp(self):
        app = create_app(TestConfig)
        db.app = app
        self.app = app.test_client()
        make_db()

    def tearDown(self):
        make_db()

    def login(self, username, password):
        return self.app.post('/login', data=dict(
            username=username,
            password=password
        ), follow_redirects=True)

    def register_user(self, username, email, password):
        return self.app.post('/register', data=dict(
            username=username,
            email=email,
            password=password,
            confirm=password,
            accept_tos=True
        ), follow_redirects=True)


if __name__ == '__main__':
    unittest.main()
