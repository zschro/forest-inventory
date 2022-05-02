from models import Forest, create_forest, forests_schema
from base import api
from flask import jsonify, make_response, request

ROWS_PER_PAGE = 9

@api.route('/forests')
def forests():
    page = request.args.get('page', 1, type=int)
    paged_forests = Forest.query.paginate(page=page, per_page=ROWS_PER_PAGE)
    result = forests_schema.dump(paged_forests.items)
    pagedResult = {"forests": result, "totalPages": paged_forests.pages, "currentPage": paged_forests.page}
    return make_response(pagedResult, 200)
