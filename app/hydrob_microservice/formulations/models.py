from hydrob_microservice import db



class formulations(db.Document):
   NAME = db.StringField(max_length=200)
   N = db.StringField(max_length=200)
    P = db.StringField(max_length=200)
    K = db.StringField(max_length=200)
    MG = db.StringField(max_length=200)
    CA=db.StringField(max_length=200)
    S=db.StringField(max_length=200)
    B=db.StringField(max_length=200)
    FE=db.StringField(max_length=200)
    ZN=db.StringField(max_length=200)
    CU=db.StringField(max_length=200)
    MO=db.StringField(max_length=200)
    MN=db.StringField(max_length=200)
    UNITS=db.StringField(max_length=200)


    def __str__(self):
        return self.NAME + self.N + self.P + self.K  + self.MG + self.CA + self.S + self.B + self.FE + self.ZN + self.CU + self.MO + self.MN + self.UNITS 
