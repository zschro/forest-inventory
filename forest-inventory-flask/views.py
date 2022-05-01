from models import Forest, create_forest, forests_schema
from base import api
from flask import jsonify, make_response

@api.route('/forests')
def forests():
    all_forests = Forest.query.all()
    result = forests_schema.dump(all_forests)
    return make_response(jsonify(result), 200)

print(__name__)