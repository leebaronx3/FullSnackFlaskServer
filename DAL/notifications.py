import json
from models.notifications import Notification
from models.users import User
from models.projects import Project
from .staticData import NotificationType


# GET
def get_users_new_notifications(user_id):
    users_notifications = Notification.objects(notifiedUserId=user_id, isRead=False)
    result = []
    for notification in users_notifications:
        result.append(notification.to_json())

    return json.dumps(result)


# PUT
def update_notifications_as_read(user_id):
    users_notifications = Notification.objects(notifiedUserId=user_id, isRead=False)
    for notification in users_notifications:
        notification['isRead'] = True
        notification.save()

    return 200


# POST
def add_new_notifications(notification_data):
    notification = Notification(
        notificationText=NotificationType.objects(id=notification_data['type_id']).first()['text'],
        actedUserId=User.objects(id=notification_data['acted_user_id']).first(),
        notifiedUserId=User.objects(id=notification_data['notified_user_id']).first(),
        projectId=Project.objects(id=notification_data['project_id']).first()
    )
    notification.save()
    return notification.to_json()
