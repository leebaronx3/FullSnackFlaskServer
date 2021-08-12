from utils.modifications import convert_arr_elements_to_json
from models.staticData import *

def get_required_techs():
    return convert_arr_elements_to_json(RequiredTech)


def get_difficulty_levels():
    return convert_arr_elements_to_json(DifficultyLevel)


def get_notifications_types():
    return convert_arr_elements_to_json(NotificationType)



def get_gender():
    return convert_arr_elements_to_json(Gender)



def get_occupations():
    return convert_arr_elements_to_json(Occupation)

