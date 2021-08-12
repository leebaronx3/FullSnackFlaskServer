from mongoengine import Document, StringField, IntField, BooleanField, DateTimeField, ObjectIdField, ReferenceField
import datetime
from .users import User
from .projects import Project


class Notification(Document):
    notificationText = StringField(required=True)
    actedUserId = ReferenceField(User, required=True)
    notifiedUserId = ReferenceField(User, required=True)
    projectId = ReferenceField(Project, required=True)
    isRead = BooleanField(default=False)
    timestamp = DateTimeField(default=datetime.datetime.utcnow)

    def to_json(self):
        return {
            "id": str(self.id),
            "acted_user": {"username": self.actedUserId.username},
            "acted_user_id": str(self.actedUserId.id),
            "is_read": self.isRead,
            "notified_user_id": str(self.notifiedUserId.id),
            "project": {"id": str(self.projectId.id)},
            "project_id": str(self.projectId.id),
            "timestamp": str(self.timestamp),
            "type": {"text": self.notificationText},

        }


