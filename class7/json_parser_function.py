# importing existing json module
import json


# reading json file from current directory
with open("data.json", "r") as data_file:
    data = json.load(data_file)

#get class value from json object
print(data["class"])

#get school value from json pbject
print(data["school"])

#get location value from json object
print(data["location"])

#get instructors value from json object
print(data["instructors"])

#get 1binstructors value from json object
print(data["instructors"][0]["instructor1"]["name"])
instructor1_name = data["instructors"][0]["instructor1"]["name"]
instructor1_lastname = data["instructors"][0]["instructor1"]["lastname"]

#for i in data["instructors"]:
#   print(i)

#write instructor 1 information to a file
with open("instrucstor1_data", "a") as target_file:
    target_file.write(instructor1_name + " " + instructor1_lastname)

    target_file.close()
