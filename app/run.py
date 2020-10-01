from hydob_microservice import app,db
from hydrob_microservice.formulations.models import formulations

if __name__ == "__main__":
    app.run(host='0.0.0.0', debug=True)
