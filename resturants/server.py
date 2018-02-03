from flask import Flask
app = Flask(__name__)

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from database_setup import Base, Restaurant, MenuItem

engine = create_engine('postgresql://localhost:5434/resturants')
Base.metadata.create_all(engine)

DBsession = sessionmaker(bind=engine)
session = DBsession()

@app.route('/')
@app.route('/hello')
def HelloWorld():
    restaurant = session.query(Restaurant).first()
    items = session.query(MenuItem).filter_by(restaurant_id = restaurant.id)

    output = ''
    for i in items:
        output += i.course
        output += '</br>'

    return output

if __name__ == '__main__':
    app.debug=True
    app.run(host='0.0.0.0', port=6060)