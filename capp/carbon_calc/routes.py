from flask import render_template, Blueprint

carbon_calc=Blueprint('carbon_calc',__name__)

@carbon_calc.route('/carbon_calc')
def carbon_calc_home():
    return render_template('carbon_calc/carbon_calc.html', title='carbon_calc')
