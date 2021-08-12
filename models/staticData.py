from mongoengine import Document, StringField


class NotificationType(Document):
    name = StringField()
    text = StringField()
    def to_json(self):
        return {
            "id": str(self.id),
            "name": self.name,
            "text": self.text
        }


class RequiredTech(Document):
    name = StringField()

    def to_json(self):
        return {
            "value": str(self.id),
            "label": self.name,
        }


class DifficultyLevel(Document):
    name = StringField()
    def to_json(self):
        return {
            "value": str(self.id),
            "label": self.name,
        }

class Gender(Document):
    name = StringField()
    def to_json(self):
        return {
            "id": str(self.id),
            "name": self.name,
        }


class Occupation(Document):
    name = StringField()
    def to_json(self):
        return {
            "id": str(self.id),
            "name": self.name,
        }

