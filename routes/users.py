from flask import make_response, Blueprint, request
from DAL.users import *
from utils.file_uploads_utils import save_uploaded_file
users = Blueprint('users', __name__, url_prefix='/users')


# GET
# validate cookie
@users.route('/<user_id>')
def get_user(user_id):
    return get_user_data(user_id)


# PUT
# validate cookie
@users.route('/<user_id>', methods=['PUT'])
def update_user(user_id):

    user_profile_img = User.objects(id=user_id).first()['profileImg']
    if 'profileImg' in request.files:
        user_profile_img = save_uploaded_file(request.files['profileImg'])

    updated_user_data = {
        **request.values.to_dict(),
        "profileImg": user_profile_img
    }

    return update_user_data(updated_user_data)


# validate cookie
@users.route('/password/<user_id>', methods=['PUT'])
def update_password(user_id):
    return update_user_password(request.json)


# POST
@users.route('', methods=['POST'])
def add_user():
    return add_new_user(request.json)


@users.route('/login', methods=['POST'])
def login_user():
    result = login(request.json)
    del result['password']
    if isinstance(result, dict):
        res = make_response(result, 200)
        # res.set_cookie('fsCookie', str(result['id'])) # doesn't work - will create in client for now
        return res
    return result


