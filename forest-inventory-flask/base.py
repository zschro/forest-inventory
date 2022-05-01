from flask import Flask

api = Flask(__name__)

@api.route('/forests')
def forest():
    response_body = {"forests": [{
        "name": "Amazon Rain Forest",
        "type" :"conservation"
    },
    {
        "name": "Sahara Desert",
        "type" :"reforestation"
    },
    {
        "name": "Al Baydha",
        "type" :"afforestation"
    }
    ]}

    return response_body