from DAL.notifications import *
from DAL.projects import get_did_user_like_project, remove_like, add_new_like
from flask import request, Blueprint
events = Blueprint('events', __name__, url_prefix='/events')


# NOTIFICATIONS
# GET , PUT
# validate cookie
@events.route('/notifications/<user_id>', methods=['GET', 'PUT'])
def get_update_notification(user_id):
    if request.method == 'GET':
        return get_users_new_notifications(user_id)
    elif request.method == 'PUT':
        return update_notifications_as_read(user_id)


# POST
# validate cookie
@events.route('/notifications', methods=['POST'])
def add_notification():
    return add_new_notifications(request.json)


# LIKES
# GET & DELETE
# validate cookie
@events.route('/likes/<user_id>/<project_id>', methods=['GET', 'DELETE'])
def get_or_remove_like(user_id, project_id):
    if request.method == 'GET':
        return get_did_user_like_project(user_id, project_id)
    else:
        return remove_like(user_id, project_id)


# POST
# validate cookie
@events.route('/likes', methods=['POST'])
def add_like():
    return add_new_like(request.json)
