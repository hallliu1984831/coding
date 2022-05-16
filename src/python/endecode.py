import json
from json import JSONEncoder
# dict_1 = {'name': 'aaa', 'age': 38, 'work': True}
# json_1 = json.dumps(dict_1)
# print(json_1)

def encode_dict(o):
    if isinstance(o, People):
        return {'name': o.name, 'age': o.age, 'work': o.work}

class people_encode(JSONEncoder):
    def default(self, o):
        if isinstance(o, People):
            return {'name': o.name, 'age': o.age, 'work': o.work, o.__class__.__name__: True}

class People:
    def __init__(self, name, age, work):
        self.name = name
        self.age = age
        self.work = work

people = People('aaa', 38, True)
peoJson = json.dumps(people, default=encode_dict)
peoJson1 = json.dumps(people, cls=people_encode)
print(peoJson, peoJson1)

new_people = json.loads(peoJson)
print(new_people)

def people_decode(dct):
    if People.__name__ in dct:
        return People(name= dct['name'], age= dct['age'], work= dct['work'])
    return dct
new_people1 = json.loads(peoJson1, object_hook=people_decode)
print(new_people1.name)
