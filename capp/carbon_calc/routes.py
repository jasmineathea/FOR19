from flask import render_template, Blueprint
from capp.models import Transport
from flask_login import login_required

carbon_calc = Blueprint('carbon_calc',__name__)

@carbon_calc.route('/carbon_calc')
@login_required
def carbon_calc_home():
    return render_template('carbon_calc/carbon_calc.html', title = 'carbon_calc')
