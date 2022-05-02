from base import db
from marshmallow_sqlalchemy import SQLAlchemyAutoSchema, auto_field

class Forest(db.Model):
   id = db.Column('forest_id', db.Integer, primary_key = True)
   name = db.Column(db.String(100))
   forestType = db.Column(db.String(50))
   imgUrl = db.Column(db.String(500)) 
   description = db.Column(db.String(1000))
   
   def __init__(self, name, forestType, imgUrl, description):
        self.name = name
        self.forestType = forestType
        self.imgUrl = imgUrl
        self.description = description

def create_forest(new_name, new_imgUrl, new_forestType, new_description):
    new_forest = Forest(new_name, new_forestType, new_imgUrl, new_description)
    db.session.add(new_forest)
    db.session.commit()
    return new_forest

class ForestSchema(SQLAlchemyAutoSchema):
    class Meta:
        model = Forest

forest_schema = ForestSchema()
forests_schema = ForestSchema(many=True)

def init():
    print("Creating database tables...")
    db.create_all()
    forest_count = Forest.query.count()
    if(forest_count == 0):
        from seed import seed
        seed()
    print("Done!")
