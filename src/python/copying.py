import copy

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

# per1 = Person('Auth', 27)
# # shallow copy
# per2 = copy.copy(per1);
# per2.age = 28
# print(per1.age, per2.age)

class Team:
    def __init__(self, teacher, student):
        self.teacher = teacher
        self.student = student

per1 = Person('Auth', 27)
per2 = Person('Acct', 37)
team = Team(per1, per2)
team1 = copy.deepcopy(team)
team.teacher.age = 30

print(team.teacher.age, team1.teacher.age)
