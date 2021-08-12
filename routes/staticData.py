from DAL.staticData import *
from flask import Blueprint
staticData = Blueprint('staticData', __name__, url_prefix='/staticdata')


@staticData.route('/requiredtechs')
def get_techs():
    return get_required_techs()


@staticData.route('/difficultylevels')
def get_diff_levels():
    return get_difficulty_levels()


@staticData.route('/notificationstypes')
def get_notifs_types():
    return get_notifications_types()


@staticData.route('/gender')
def get_genders():
    return get_gender()


@staticData.route('/occupations')
def get_occupations_list():
    return get_occupations()
