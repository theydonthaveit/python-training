import sys

from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine

Base = declarative_base()


class Restaurant(Base):
	__tablename__ = 'restaurant'

	id = Column(Integer, primary_key=True)
	name = Column(String(80), nullable=False)


class MenuItem(Base):
	__tablename__ = 'menu_item'

	id = Column(Integer, primary_key=True)
	course = Column(String(250))
	description = Column(String(250))
	price = Column(String(8))
	restaurant_id = Column(Integer, ForeignKey('restaurant.id'))
	restaurant = relationship(Restaurant)

	@property
	def serialize(self):
		return {
			'course': self.course,
			'description': self.description,
			'id': self.id,
			'price': self.price,
		}


engine = create_engine('postgresql://localhost:5434/restaurants')
Base.metadata.create_all(engine)