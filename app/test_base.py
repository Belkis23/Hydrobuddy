import unittest

from flask_mongoalchemy import MongoAlchemy

from hydrob_microservice import db


class BaseTestCase(MongoAlchemy):

    def setUp(self):
        self.db_name = 'Hydrob_DB'
        self.app.config['MONGODBALCHEMY_DATABASE'] = self.db_name
        self.app.config['MONGOALCHEMY_CONNECTION_STRING'] = 'mongodb://db:27017'
        self.app.config['TESTING'] = True

        db = MongoAlchemy(self.app)

        self.db = db

    def tearDown(self):
        db.session.remove()
        db.drop_all()



if __name__ == '__main__':
    unittest.main()
