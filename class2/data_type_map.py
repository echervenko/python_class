person1 = {
    "firstname": "elena",
    "lastname": "chervenko",
    "address": "7300 n harlem"
}
# print(person1)
# print(id(person1))
# print(type(person1))
# print(dir([person1]))

print(person1.values())
print(person1.keys())
print("This person's first name is", person1.get("firstname"))
print("This person's last name is", person1.get("lastname"))
print("This person's address is", person1.get("address"))