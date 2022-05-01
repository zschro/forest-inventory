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

def create_forest(new_name, new_forestType, new_imgUrl, new_description):
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
        print("Creating sample forests...")
        create_forest("Amazon rainforest", "Conservation", "https://upload.wikimedia.org/wikipedia/commons/thumb/e/ef/Amazonia.jpg/272px-Amazonia.jpg", "The Amazon rainforest, alternatively, the Amazon jungle or Amazonia, is a moist broadleaf tropical rainforest in the Amazon biome that covers most of the Amazon basin of South America. This basin encompasses 7,000,000 km2 (2,700,000 sq mi), of which 5,500,000 km2 (2,100,000 sq mi) are covered by the rainforest.")
        create_forest("Sahara desert", "Afforestation", "https://upload.wikimedia.org/wikipedia/commons/thumb/a/a0/Algeria_Sahara_Desert_Photo_From_Drone_5.jpg/220px-Algeria_Sahara_Desert_Photo_From_Drone_5.jpg", "The desert comprises much of North Africa, excluding the fertile region on the Mediterranean Sea coast, the Atlas Mountains of the Maghreb, and the Nile Valley in Egypt and the Sudan. It stretches from the Red Sea in the east and the Mediterranean in the north to the Atlantic Ocean in the west, where the landscape gradually changes from desert to coastal plains. To the south, it is bounded by the Sahel, a belt of semi-arid tropical savanna around the Niger River valley and the Sudan Region of Sub-Saharan Africa. The Sahara can be divided into several regions, including the western Sahara, the central Ahaggar Mountains, the Tibesti Mountains, the Aïr Mountains, the Ténéré desert, and the Libyan Desert.")
    print("Done!")

if __name__ == "__main__":
    init()