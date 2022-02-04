import json


person = '{ "name":"Amol", "email":"amol@gmail.com","age":22}'
i = json.loads(person)
print(i["name"] + " " + i["email"] + " ", i["age"])