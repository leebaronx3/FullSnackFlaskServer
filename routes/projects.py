from DAL.projects import *
from flask import request, Blueprint
from utils.file_uploads_utils import save_uploaded_file

projects = Blueprint('projects', __name__, url_prefix='/projects')


# GET
@projects.route('/explore')
def get_projects():
    return get_projects_cards_data(request.args.to_dict())


# validate cookie
@projects.route('/dashboard')
def get_users_projects():
    return get_projects_cards_data(request.args.to_dict())


@projects.route('/<project_id>', methods=['GET'])
def get_project(project_id):
    return get_project_data(project_id)


# PUT
# validate cookie
@projects.route('', methods=['PUT'])
def update_project():
    assets_location = ''
    if 'assetsSrc' in request.values.to_dict():
        assets_location = request.values.to_dict()['assetsSrc']
    elif request.files and 'assetsSrc' in request.files:
        assets_location = save_uploaded_file(request.files['assetsSrc'])

    new_pictures_files = request.files.getlist('pictures')
    new_pictures = []
    for picture in new_pictures_files:
        file_location = save_uploaded_file(picture)
        new_pictures.append(file_location)

    project_updated_data = {**request.values.to_dict(), 'assetsSrc': assets_location, 'new_pictures': new_pictures}
    return update_project_data(project_updated_data)


# validate cookie
@projects.route('/<project_id>/<user_id>/remove', methods=['PUT'])
def hide_project_from_user(project_id, user_id):
    res = hide_project(project_id, user_id)

    if not res['isVisible']:
        return (True, 200)
    else:
        return (False, 500)


# validate cookie
@projects.route('/remove/picture/<picture_id>', methods=['DELETE'])
def delete_picture(picture_id):
    return remove_picture(picture_id)


# POST
# validate cookie
@projects.route('', methods=['POST'])
def add_project():
    # pictures
    pictures_files = request.files.getlist('pictures')
    pictures = []
    for picture in pictures_files:
        file_location = save_uploaded_file(picture)
        pictures.append(file_location)
    # assetsSrc
    assets_location = ''
    if 'assetsSrc' in request.files:
        assets_location = save_uploaded_file(request.files['assetsSrc'])
    project_data = {**request.values.to_dict(), 'assetsSrc': assets_location, 'pictures': pictures}
    return add_new_project(project_data)

