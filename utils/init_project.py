# from models.staticData import *
# from models.users import *
# from models.projects import *
# from models.forum import *
# from models.notifications import *
#
#
# # Static Data
# def set_notifs_types():
#     notification_types = [{'name': 'project thread', 'text': 'posted a new thread on your project'},
#                          {'name': 'project like', 'text': 'liked your project'},
#                          {'name': 'project comment', 'text': 'commented on a thread in your project'},
#                          {'name': 'thread comment', 'text': 'commented on your thread'}]
#     notifs_types_instances = [NotificationType(**data) for data in notification_types]
#     NotificationType.objects.insert(notifs_types_instances, load_bulk=False)
#
#
# def set_required_techs():
#     required_techs = [
#         {"name": "HTML"},
#         {"name": "CSS"},
#         {"name": "JavaScript"},
#         {"name": "Python"},
#         {"name": "C#"},
#         {"name": "ASP.NET"},
#         {"name": "C++"},
#         {"name": "C"},
#         {"name": "React"},
#         {"name": "Node.js"},
#         {"name": "Express.js"},
#         {"name": "MySQL"},
#         {"name": "MongoDB"},
#         {"name": "Vue.js"},
#         {"name": "Flask"},
#         {"name": "Angular"},
#         {"name": "Sequelize"},
#     ]
#     required_techs_instances = [RequiredTech(**data) for data in required_techs]
#     RequiredTech.objects.insert(required_techs_instances, load_bulk=False)
#
#
# def set_difficulty_levels():
#     difficulty_levels = [
#         {"name": "Easy"},
#         {"name": "Medium"},
#         {"name": "Hard"},
#     ]
#     difficulty_levels_instances = [DifficultyLevel(**data) for data in difficulty_levels]
#     DifficultyLevel.objects.insert(difficulty_levels_instances, load_bulk=False)
#
# def set_genders():
#     genders = [
#         {"name": "Female"},
#         {"name": "Male"},
#         {"name": "Other"},
#     ]
#     genders_instances = [Gender(**data) for data in genders]
#     Gender.objects.insert(genders_instances, load_bulk=False)
#
#
# def set_occupations():
#     occupations = [
#         {"name": "Student"},
#         {"name": "Junior Developer"},
#         {"name": "Senior Developer"},
#         {"name": "Other"},
#     ]
#     occupations_instances = [Occupation(**data) for data in occupations]
#     Occupation.objects.insert(occupations_instances, load_bulk=False)
#
# def set_first_user():
#     user = User(username="xmba",
#                 email="xmbaron@gmail.com",
#                 password="Lb123456",
#                 birthdate= "1994-03-26",
#                 gender="Female",
#                 isActive="true"
#                 )
#
#     user.save()
#
# def set_first_project():
#     leebaronx3 = User.objects(id='6107f146d02522d4bbd1b19d').first()
#     hardLvl = DifficultyLevel.objects(name='Medium').first()
#     react = RequiredTech.objects(name__in=['React'])
#
#     print(leebaronx3, hardLvl, react)
#     project = Project(userId=leebaronx3,
#                       name='Dashboard',
#                       difficultyLevel=hardLvl,
#                       requiredTechs=react,
#                       pictures=[{'picSrc': 'files//img.png'}],
#                       description='in this project you can create a dashboard',
#                       githubUrl='http://leeba.github.com',
#                       )
#     project.save()
#
# def set_first_thread_comment():
#     leebaronx3 = User.objects(id='6107f146d02522d4bbd1b19d').first()
#     recipes = Project.objects().first()
#     thread = Thread(projectId=recipes,
#                     userId=leebaronx3,
#                     topic='Hello it\'s me')
#     thread.save()
#     comment = Comment(userId=leebaronx3, text='lala')
#     thread.comments.append(comment)
#     thread.save()
#
#
# def set_first_notification():
#     set_first_user()
#     leebaronx3 = User.objects(id='6107f146d02522d4bbd1b19d').first()
#     mai = User.objects(username='xmba').first()
#     notif = Notification(notificationText='liked your project',
#                          actedUserId=mai,
#                          notifiedUserId=leebaronx3,
#                          projectId=Project.objects.first()
#                          )
#     notif.save()