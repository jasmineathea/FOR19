from capp import db
from capp.models import User, Transport

db.create_all()

user1 = User(username = 'Bjørk', email = 'bjørk@demo.com', password = 'regn')
db.session.add(user1)

user2 = User(username = 'Fjell', email = 'fjell@demo.com', password = 'regn')
db.session.add(user2)
db.session.commit()

transport1 = Transport(kms=10, transport='car', fuel='diesel', co2=1, ch4=0.5, total= 1.5,  user_id=user1.id)
transport2 = Transport(kms=15,  transport='bike', fuel='none', co2=0, ch4=0, total= 0, user_id=user1.id)
transport3 = Transport(kms=25,  transport='plane', fuel='diesel', co2=3, ch4=1, total= 4, user_id=user1.id)
transport4 = Transport(kms=12,  transport='bus', fuel='petrol', co2=1, ch4=1, total= 2, user_id=user1.id)

db.session.add(transport1) 
db.session.add(transport2) 
db.session.add(transport3) 
db.session.add(transport4)

transport5 = Transport(kms=5, transport='motorbike', fuel='diesel', co2=0.7, ch4=0.6, total= 1.3, user_id=user2.id)
transport6 = Transport(kms=7, transport='ferry', fuel='diesel', co2=0.8, ch4=0.2, total= 1,  user_id=user2.id)
transport7 = Transport(kms=15, transport='walk', fuel='none', co2=0, ch4=0, total= 0, user_id=user2.id)
transport8 = Transport(kms=19, transport='bike', fuel='none', co2=0, ch4=0, total= 0,  user_id=user2.id)

db.session.add(transport5) 
db.session.add(transport6) 
db.session.add(transport7) 
db.session.add(transport8) 

db.session.commit()

# Some basic queries
user1 = User.query.get(1)
user2 = User.query.get(2)
transport1 = Transport.query.first()
transport1.user_id
transport1.author
transport1.author.username

# Erase tables and rows
# db.drop_all()
