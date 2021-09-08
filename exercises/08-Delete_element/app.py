people = ['juan','ana','michelle','daniella','stefany','lucy','barak']

#Your code go here:
def deletePerson(person_name, arr):
    new_people = []
    for name in arr:
        if name != person_name:
            new_people.append(name)
    return new_people
print(deletePerson("daniella", people))
print(deletePerson("juan", people))
print(deletePerson("emilio", people))