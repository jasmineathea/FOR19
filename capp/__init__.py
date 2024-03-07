from flask import Flask

application = Flask(__name__)

# secret key
application.config['SECRET_KEY'] = '3oueqkfdfas8ruewqndr8ewrewrouewrere44554'

from capp.home.routes import home
from capp.methodology.routes import methodology
from capp.carbon_calc.routes import carbon_calc
from capp.users.routes import users

application.register_blueprint(home)
application.register_blueprint(methodology)
application.register_blueprint(carbon_calc)
application.register_blueprint(users)
