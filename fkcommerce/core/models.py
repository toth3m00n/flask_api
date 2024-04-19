import uuid

from sqlalchemy import Integer
from sqlalchemy.dialects.postgresql import UUID

from . import database as db


class Category(db.Model):
    __tablename__ = 'category'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), unique=True, nullable=False)
    slug = db.Column(db.String(200), unique=True, nullable=False)
    is_active = db.Column(db.Boolean, default=True)
    parent_id = db.Column(db.Integer, db.ForeignKey('category'))

    def __repr__(self):
        return f'<Category {self.name}>'


class Product(db.Model):
    __tablename__ = 'product'

    id = db.Column(db.Integer, primary_key=True)
    pid = db.Column(
                    UUID(as_uuid=True),
                    unique=True, nullable=False,
                    server_default=db.text('uuid_generate_v4()')
                    )
    name = db.Column(db.String(200), unique=True, nullable=False)
    slug = db.Column(db.String(255), unique=True, nullable=False)
    description = db.Column(db.Text, )
    is_digital = db.Column(db.Boolean, default=False)
    created_at = db.Column(db.DateTime, server_default=db.text("CURRENT_TIMESTAMP"))
    updated_at = db.Column(db.DateTime, server_default=db.text("CURRENT_TIMESTAMP"), onupdate=db.func.now())
    is_active = db.Column(db.Boolean, default=True)
    stock_status = db.Column(db.String(100), default='OUT_OF_STOCK') # order, backorder and ect

    category_id = db.Column(db.Integer, db.ForeignKey('category.id'))
    seasonal_event = db.Column(db.Integer, db.ForeignKey('seasonal_event.id'), nullable=True)
    
    def __repr__(self):
        return f'<Product {self.name}>'


class ProductLine(db.Model):
    __tablename__ = 'product_line'

    id = db.Column(db.Integer, primary_key=True)
    price = db.Column(db.DECIMAL(5, 2), nullable=False)
    sku = db.Column(UUID(as_uuid=True), default=uuid.uuid4)
    stock_qty = db.Column(Integer, default=0)
    is_active = db.Column(db.Boolean, default=True)
    order = db.Column(db.Integer)
    weight = db.Column(db.Float)
    created_at = db.Column(db.DateTime, server_default=db.text("CURRENT_TIMESTAMP"))
    product_id = db.Column(db.Integer, db.ForeignKey('product.id'))
    
    def __repr__(self):
        return f'<ProductLine {self.id}>'


class ProductImage(db.Model):
    __tablename__ = 'product_image'

    id = db.Column(db.Integer, primary_key=True)
    alternative_text = db.Column(db.String(200))
    url = db.Column(db.String(200))
    order = db.Column(db.Integer)
    product_line_id = db.Column(db.Integer, db.ForeignKey('product_line.id'))
    
    def __repr__(self):
        return f'<ProductImage {self.id}>'
    
    
class SeasonalEvent(db.Model):
    __tablename__ = 'seasonal_event'

    id = db.Column(db.Integer, primary_key=True)
    start_date = db.Column(db.DateTime)
    end_date = db.Column(db.DateTime)
    name = db.Column(db.String(100), unique=True)
    
    def __repr__(self):
        return f'<Name: {self.id}>'