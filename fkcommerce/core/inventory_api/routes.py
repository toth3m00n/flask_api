from apifairy import response, body

from . import inventory_category_api_blueprint
from core import database
from ..models import Category
from ..schema import CategoryInsertSchema, CategoryResponseSchema

category_schema_response = CategoryResponseSchema(many=True)
category_schema_insert = CategoryInsertSchema()
# category_schema_insert = CategoryInsertSchema()


@inventory_category_api_blueprint.route('/category', methods=['GET'])
@response(category_schema_response)
def category():
    return Category.query.all()


@inventory_category_api_blueprint.route('/category', methods=['POST'])
@body(category_schema_insert)
@response(category_schema_insert)
def category_insert(kwargs):
    new_category = Category(**kwargs)
    database.session.add(new_category)
    database.session.commit()
    return new_category
