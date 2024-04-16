from capp.carbon_interface.api import CarbonAPI
from flask import render_template, Blueprint, request, redirect, url_for, flash
from capp.models import Transport
from capp import carbon_calc, db
from datetime import timedelta, datetime
from flask_login import login_required, current_user
from capp.carbon_calc.forms import BusForm, CarForm, PlaneForm, FerryForm, MotorbikeForm, BicycleForm, WalkForm
import json

api = CarbonAPI()


carbon_interface = Blueprint('carbon_interface',__name__)

#API
@carbon_interface.route('/carbon_interface/cars')
def allV():
    return api.allVehicleMakes()

@carbon_interface.route('/carbon_interface/models/<id>')
def getMakes(id):
    return api.getVehicleMake(id)