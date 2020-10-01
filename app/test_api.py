import json
import unittest
from hydrob_microservice.formulations.routes import formulations
from hydrob_microservice import app


app.register_blueprint(formulations)

app.testing = True
app_context = app.app_context()


class TestApi(unittest.TestCase):

    #test add formulations
    def testAddformulations(self):
        data = dict(NAME='Strawberry',N ="       80.00000000",
            P="       45.00000000",
            K="      100.00000000",
            MG="       50.00000000",
            CA="      200.00000000",
            S="      180.00000000",
            B="        0.50000000",
            FE="        3.00000000",
            ZN="        0.50000000",
            CU="        0.05000000",
            MO="        0.05000000",
            MN="        0.50000000",
            UNITS="ppm")

        with app.app_context():
            self.formulations = app.test_client()

            response = self.formulations.post('/addformulations', data=json.dumps(data), content_type='application/json')

    #test delete formul
    def testDeleteformulations(self):
        data = dict(list_id=1, enabled=True)
        with app.app_context():
            self.formulations = app.test_client()
            response = self.formulations.delete('/formulations/delete/<string:NAME>', data=json.dumps(data),
                                              content_type='application/json')

            self.assertEqual(response.status_code, 200)




    # test get formul by NAME

    def testGetformulationsByNAME(self):
        data = dict(NAME='Lettuce General (Howard Resh)', enabled=True)
        with app.app_context():
            self.formulations = app.test_client()
            response = self.formulations.get('/formulations/findByNAME/<string:NAME>', data=json.dumps(data), content_type='application/json')
            self.assertEqual(response.status_code, 200)


    


if __name__ == "__main__":
    unittest.main()
