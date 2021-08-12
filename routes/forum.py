from DAL.forum import *
from flask import Blueprint, request
forum = Blueprint('forum', __name__, url_prefix='/forum')

# GET
@forum.route('/<project_id>')
def get_threads_of_project(project_id):
    return get_projects_threads_comments(project_id)


# POST
# validate cookie
@forum.route('/thread', methods=['POST'])
def add_thread():
    return add_new_thread(request.json)

# validate cookie
@forum.route('/comment', methods=['POST'])
def add_comment():
    return add_new_comment(request.json)
