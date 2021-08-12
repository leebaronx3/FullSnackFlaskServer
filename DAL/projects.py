import json
from models.projects import Project, Picture
from models.users import User
from models.staticData import DifficultyLevel, RequiredTech
from utils.modifications import convert_arr_elements_to_json


# //GET
def get_projects_cards_data(filter_data):
    query = {
        'isVisible': True
    }
    if 'search' in filter_data and not filter_data['search'] == '':
        query['name__contains'] = filter_data['search']

    if 'reqtechs' in filter_data and (filter_data['reqtechs'] != ''):
        query['requiredTechs__all'] = filter_data['reqtechs'].split(',')

    if 'difflvls' in filter_data and (filter_data['difflvls'] != ''):
        query['difficultyLevel__in'] = filter_data['difflvls'].split(',')

    if filter_data['assets'] == '0':
        query['assetsSrc'] = ""
    elif filter_data['assets'] == '1':
        query['assetsSrc__ne'] = ""

    if 'userId' in filter_data:
        query['userId'] = filter_data['userId']

    projects_offset = (int(filter_data.get('currentpage', 1)) - 1) * int((filter_data.get('amount', 20)))
    projects_limit = int(filter_data.get('amount', 20))

    chosen_order = 'likesCounter'
    if filter_data['sortby'] == 'timestamp':
        chosen_order = 'timestamp'
    projects_card_data = Project.objects(**query)\
        .exclude('githubUrl', 'description')\
        .skip(projects_offset)\
        .limit(projects_limit)\
        .order_by('-'+chosen_order)

    result = []
    for project in projects_card_data:
        result.append(project.to_json())
    return json.dumps(result)


def get_project_data(project_id):
    project = Project.objects(id=project_id).first()
    return project.to_json()


def update_project_data(updated_data):
    new_pictures = [Picture(pic_src=src) for src in updated_data['new_pictures']]
    required_techs = [RequiredTech.objects(id=tech_id).first() for tech_id in updated_data['requiredTechnologies'].split(',')]

    project = Project.objects(id=updated_data['id']).first()
    old_pictures = project['pictures']

    pictures = old_pictures + new_pictures
    project.update(name=updated_data['name'],
                   difficultyLevel=DifficultyLevel.objects(id=updated_data['difficultyLevel']).first(),
                   requiredTechs=required_techs,
                   pictures=pictures,
                   description=updated_data['description'],
                   assetsSrc=updated_data['assetsSrc'],
                   githubUrl=updated_data['githubLink'],
                   )

    project.save()
    return project.to_json()


def hide_project(project_id, user_id):
    project = Project.objects(id=project_id).first()
    project.update(isVisible=False)
    project.save()
    return project.reload().to_json()


def add_new_project(project_data):
    pictures = [Picture(pic_src=src) for src in project_data['pictures']]
    required_techs = [RequiredTech.objects(id=tech_id).first() for tech_id in
                      project_data['requiredTechnologies'].split(',')]

    project = Project(userId=project_data['userId'],
                      name=project_data['name'],
                      difficultyLevel=DifficultyLevel.objects(id=project_data['difficultyLevel']).first(),
                      requiredTechs=required_techs,
                      pictures=pictures,
                      description=project_data['description'],
                      assetsSrc=project_data['assetsSrc'],
                      githubUrl=project_data['githubLink'],
                      )

    project.save()
    return project.to_json()


def remove_picture(picture_id):
    project = Project.objects.filter(pictures__match={"id": picture_id}).first()
    pics_array = project['pictures']

    for i in range(len(pics_array)):
        if str(pics_array[i].id) == picture_id:
            pics_array.remove(pics_array[i])
            break

    project.save()
    return project.to_json()


# Projects Likes
# GET
def get_did_user_like_project(user_id, project_id):
    users_liked = Project.objects(id=project_id).first()['likedUsers']
    return json.dumps(user_id in users_liked)


# POST
def add_new_like(like_data):
    project = Project.objects(id=like_data['projectId']).first()
    project.likesCounter += 1
    likes_array = project.likedUsers
    likes_array.append(like_data['userId'])
    project.save()
    return project.to_json()


# DELETE
def remove_like(user_id, project_id):
    project = Project.objects(id=project_id).first()
    project.likesCounter -= 1
    likes_array = project.likedUsers
    likes_array.remove(user_id)
    project.save()
    return project.to_json()

