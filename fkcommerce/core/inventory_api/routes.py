from apifairy import response

from . import inventory_category_api_blueprint
from ..models import Category
from ..schema import CategorySchema

category_schema = CategorySchema(many=True)


@inventory_category_api_blueprint.route('/category', methods=['GET'])
@response(category_schema)
def category():
    return Category.query.all()
