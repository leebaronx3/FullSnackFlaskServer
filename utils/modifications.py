import json

def convert_arr_elements_to_json(obj):
    result = []
    for element in obj.objects():
        result.append(element.to_json())
    return json.dumps(result)
