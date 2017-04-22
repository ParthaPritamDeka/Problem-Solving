


import json

# fix this function, so it adds the given name
# and salary pair to salaries_json, and return it
def add_employee(salaries_json, name, salary):
    salaries = json.loads(salaries_json)
    salaries[name] = salary

    return json.dumps(salaries)

# test code
#salaries = '{"Foo": "gsdjh", "Bar": "partha", "Quux": {"QuuxId": 1234,"QuuxName": "Sam"}}'
salaries = open('C:\Python27\New_sample.json', 'r').read()

salary_json = json.dumps(salaries)
#print salary_json
print salaries
    
#new_salaries = add_employee(salaries, "Me", 800)
#decoded_salaries = json.loads(salaries)
#print decoded_salaries["guid"]
#print decoded_salaries["index"]
#print decoded_salaries["favoriteFruit"]
#print decoded_salaries
#print new_salaries
