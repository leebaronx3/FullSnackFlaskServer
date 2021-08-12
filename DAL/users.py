import json
from models.users import User
from .staticData import Gender, Occupation
import bcrypt


# GET
def get_user_data(user_id):
    user = User.objects(id=user_id).first()
    return user.to_json()


# PUT
def update_user_data(updated_data):
    user = User.objects(id=updated_data['userId']).first()
    del updated_data['userId']

    if 'gender' in updated_data:
        updated_data['gender'] = Gender.objects(id=updated_data['gender']).first()

    if 'occupation' in updated_data:
        updated_data['occupation'] = Occupation.objects(id=updated_data['occupation']).first()

    if 'birthdate' in updated_data and updated_data['birthdate'] == 'None':
        del updated_data['birthdate']

    user.update(**updated_data)
    return json.dumps(user.to_json())


def update_user_password(updated_password_data):
    user = User.objects(id=updated_password_data['userId']).first()

    old_password = updated_password_data['oldPassword']
    new_password = updated_password_data['newPassword']

    if bcrypt.checkpw(old_password.encode('utf-8'), user.password.encode('utf-8')):
        hashed_new_password = bcrypt.hashpw(new_password.encode('utf-8'), bcrypt.gensalt())
        user.update(password=hashed_new_password.decode('utf-8'))
        user.save()
        return {"changed": True}, 200
    return {"changed": False}, 401


# POST
def login(login_data):
    username = login_data['username']
    password = login_data['password']

    user = User.objects(username=username).first()
    if not user:
        return 'User not found', 404

    if bcrypt.checkpw(password.encode('utf-8'), user.password.encode('utf-8')):
        return user.to_json()
    return 'Wrong password', 403


def add_new_user(user_data):
    user_data['password'] = bcrypt.hashpw(user_data['password'].encode('utf-8'), bcrypt.gensalt()).decode('utf-8')
    user = User(**user_data)
    user.save()
    return user.to_json()


