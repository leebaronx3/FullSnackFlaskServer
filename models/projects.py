from mongoengine import Document, StringField, DateTimeField, BooleanField, ListField, URLField, ReferenceField, EmbeddedDocument, ObjectIdField, EmbeddedDocumentListField, IntField
from bson.objectid import ObjectId
import datetime
import os
from .users import User
from .staticData import DifficultyLevel, RequiredTech


class Picture(EmbeddedDocument):
    id = ObjectIdField(required=True, default=lambda: ObjectId())
    pic_src = StringField(required=True)

    def to_json(self):
        return {
            'id': str(self.id),
            "pic_src": self.pic_src,
            # "name": self.name
        }


class Project(Document):
    userId = ReferenceField(User, required=True)
    name = StringField(required=True)
    difficultyLevel = ReferenceField(DifficultyLevel, required=True)
    requiredTechs = ListField(ReferenceField(RequiredTech), required=True)
    pictures = EmbeddedDocumentListField(Picture)
    description = StringField()
    assetsSrc = StringField()
    githubUrl = StringField()
    likesCounter = IntField(default=0)
    likedUsers = ListField()
    timestamp = DateTimeField(default=datetime.datetime.utcnow)
    isVisible = BooleanField(default=True)

    # meta = {'indexes': [
    #     {'fields': ['$name'],
    #      'default_language': 'english',
    #      }
    # ]}

    def to_json(self):
        return {
            'id': str(self.id),
            "user": {'id': str(self.userId.id), 'username': self.userId.username},
            "name": self.name,
            "difficulty_level": {'id': str(self.difficultyLevel.id), 'name': str(self.difficultyLevel.name)},
            "project_required_tech_id": self.convert_objs_arr_for_json(self.requiredTechs, ['id', 'name']),
            "projects_pictures": self.convert_objs_arr_for_json(self.pictures, ['id', 'pic_src']),
            "description": self.description,
            "assets_src": is_assets_src(self.assetsSrc),
            "github_url": self.githubUrl,
            "liked_project_id": self.likedUsers,
            "likesCounter": self.likesCounter, # required for sorting
            "timestamp": str(self.timestamp),
            "isVisible": self.isVisible,
        }

# transfer to utils
    def convert_objs_arr_for_json(self, arr, keys):
        result = []
        for obj in arr:
            result.append({k: str(obj[k]) for k in keys})
        return result


def is_assets_src(assets_src):
    if assets_src is not None:
        return assets_src.replace(os.sep, '/')

    return assets_src
