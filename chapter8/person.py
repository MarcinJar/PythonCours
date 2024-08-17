import os

os.system("clear")

def build_person(first_name: str, last_name: str, age: int=None):
    person = {'first':first_name,'last':last_name}
    if age:
        person['age'] = age
    return person

musician = build_person('jimi', 'hendrix')
print(musician)

musician = build_person('jimi', 'hendrix', 48)
print(musician)