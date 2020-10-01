from stage import app, bcrypt , hashing
from flask import request, jsonify, Blueprint
from flask_marshmallow import Marshmallow
from stage.formulations.models import esmtable
from datetime import datetime
from flask_cors import CORS,cross_origin
import re ,random
import requests
from ..decorators import require_appkey


# Init bluebripnt
hydro = Blueprint('hydro', __name__)

# Init marshmallow
ma = Marshmallow(hydro)


# TestClass schema
class HydropSchema(ma.Schema):
    class Meta:
        # Fields to expose
        fields = ('designation')


# Init schema
hydrop_schema = HydropSchema()
hydrops_schema = HydropSchema(many=True)


@formulations.route('/formulations', methods=['GET'])
@require_appkey
@cross_origin()
def getformulations():
    all_formulations = formulations.query.all()
    result = formulations_schema.dump(all_formulations)
    return jsonify(result.data)






# Get Single fomulations by name
@formulations.route('/formulations/NAME', methods=['GET'])
@require_appkey
@cross_origin()
def getformulationNAME():
    NAME= request.json['NAME']
    # Fetch formulation
    formulations = formulations.query.filter_by(NAME=NAME).first()
   
    return formulations_schema.jsonify(formulations)



# add a formulation
@formulations.route("/formulations/addformulations", methods=['POST'])
@require_appkey
@cross_origin()
def addformulations():
    NAME = request.json['NAME']
    

   
# Update a formulation
@formulations.route('/formulations/update', methods=['PUT'])
@require_appkey
@cross_origin()
def updateformulations():
    id=request.json['id']
    # Fetch formulation
   formulations = formulations.query.filter_by(id=id).first()
    if not formulations:
        return jsonify({'msg': 'Notfound!',
                        'isUpdated': False
                        })

    NAME = request.json['NAME']
    N = request.json['N']
    P = request.json['P']
    K = request.json['K']
    MG = request.json['MG']
    CA=request.json['CA']
    S=request.json['S']
    B=request.json['B']
    FE=request.json['FE']
    ZN=request.json['ZN']
    CU=request.json['CU']
    MO=request.json['MO']
    MN=request.json['MN']
    UNITS=request.json['UNITS']
    
   formulations.NAME=NAME
   formulations.N=N 
   formulations.P=P 
   formulations.K=K 
   formulations.MG=MG 
   formulations.CA=CA
   formulations.S=S
    formulations.B=B
    formulations.FE=FE
    formulations.ZN=ZN
    formulations.CU=CU
    formulations.MO=MO
    formulations.MN=MN
     formulations.UNITS=UNITS
    formulations.save()

    return jsonify({'msg': 'formulation successfully updated!',
                    'isUpdated': True})

# Delete a formiulation

@formulations.route('/formulations/delete', methods=['DELETE'])
@require_appkey
@cross_origin()
def deleteformulations():
    NAME=request.json['NAME']
    # Fetch formul
    formul = formulations.query.filter_by(NAME=NAME).first()
    if not formul:
        return jsonify({'msg': 'Not found!',
                        'isDeleted': False})
    response = requests.delete("http://localhost:5003/deleteByNAME", json={"NAME":NAME},
                                    headers={"x-api-key":"ChEdLiZiEdKhOuLoUdYaSsInEsAiF"})
   formul.remove()
    return jsonify({'msg': 'formulation successfully deleted!',
                    'isDeleted': True,
                    })





