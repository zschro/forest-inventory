from flask import Flask

api = Flask(__name__)

@api.route('/forests')
def forest():
    response_body = {"forests": [{
        "name": "Amazon Rain Forest",
        "type" :"conservation",
        "imgUrl" :"https://upload.wikimedia.org/wikipedia/commons/thumb/e/ef/Amazonia.jpg/272px-Amazonia.jpg"
    },
    {
        "name": "Sahara Desert",
        "type" :"reforestation",
        "imgUrl" :"https://upload.wikimedia.org/wikipedia/commons/thumb/a/a0/Algeria_Sahara_Desert_Photo_From_Drone_5.jpg/220px-Algeria_Sahara_Desert_Photo_From_Drone_5.jpg"
    },
    {
        "name": "Rand Wood, Lincolnshire, England",
        "type" :"afforestation",
        "imgUrl" :"https://upload.wikimedia.org/wikipedia/commons/thumb/b/bb/New_afforestation_looking_into_Rand_Wood_-_geograph.org.uk_-_329908.jpg/280px-New_afforestation_looking_into_Rand_Wood_-_geograph.org.uk_-_329908.jpg"
    }
    ]}

    return response_body