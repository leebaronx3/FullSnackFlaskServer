from mongoengine import Document, StringField, DateField, BooleanField, EmailField, ReferenceField
from .staticData import Gender, Occupation


class User(Document):
    username = StringField(min_length=4, max_length=12,unique=True, required=True)
    email = EmailField(unique=True, required=True)
    password = StringField(required=True)
    birthdate = DateField(default=None)
    gender = ReferenceField(Gender, default=None)
    occupation = ReferenceField(Occupation, default=None)
    profileImg = StringField(default='files/0userplaceholder.png')
    isActive = BooleanField(default=True)


    def to_json(self):
        return {
            'id': str(self.id),
            "username": self.username,
            "email": self.email,
            "password": self.password,
            "birthdate": set_val_by_current_val(self, "birthdate"),
            "gender_id": set_val_by_current_val(self, "gender"),
            "occupation_id": set_val_by_current_val(self, "occupation"),
            "profile_img": self.profileImg,
            "is_active": self.isActive
        }



def set_val_by_current_val(user, prop):
    if user[prop] is None:
        return user[prop]
    elif prop != 'birthdate':
        return str(user[prop].id);
    return str(user[prop])

