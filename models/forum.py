from mongoengine import Document, EmbeddedDocument, StringField, DateTimeField, ReferenceField,\
    ObjectIdField, CASCADE, EmbeddedDocumentListField
from bson.objectid import ObjectId
import datetime
from .users import User
from .projects import Project


class Comment(EmbeddedDocument):
    id = ObjectIdField(default=lambda: ObjectId())
    userId = ReferenceField(User, required=True)
    text = StringField(required=True, min_length=1)
    timestamp = DateTimeField(default=datetime.datetime.utcnow)

    def to_json(self):
        return {
            "user": {'user_id': str(self.userId.id), 'username': self.userId.username, 'profile_img': self.userId.profileImg},
            "text": self.text,
            "timestamp": str(self.timestamp),
        }


class Thread(Document):
    projectId = ReferenceField(Project, required=True, reverse_delete_rule=CASCADE)
    userId = ReferenceField(User, required=True)
    topic = StringField(required=True, min_length=2, max_length=75)
    body = StringField(max_length=1000)
    timestamp = DateTimeField(default=datetime.datetime.utcnow)
    comments = EmbeddedDocumentListField(Comment)

    def to_json(self):
        return {
            "id": str(self.id),
            "user": {'id': str(self.userId.id), 'username': self.userId.username, 'profile_img': self.userId.profileImg},
            "project_id": str(self.projectId.id),
            "topic": self.topic,
            "body": self.body,
            "comments": self.comments,
            "timestamp": str(self.timestamp),
        }

