#is

# NUMBER1 = 10
# NUMBER2 = 10

# if NUMBER1 is NUMBER2:
#     print("they're equal")
#     else:
#         print("they're not equal")
# if NUMBER1 is not NUMBER2: 
#     print("they're not equal")
# else:
#     print("they're equal")

#in
# HIDDEN_FRUIT = "kiwi"

# FRUIT_LIST1 = ["apple", "pear", "banana"]
# print(type(FRUIT_LIST1))
# FRUIT_LIST2 = ("mango", "melon", "kiwi")
# FRUIT_LIST3 = {"peach", "apricot", "cherry"}

# if HIDDEN_FRUIT is in FRUIT_LIST1
#     print("hidden fruit is in list1")
# elif HIDDEN_FRUIT in FRUIT_LIST2:
#     print("hidden fruit is in list2")
# elif HIDDEN_FRUIT in FRUIT_LIST3:
#     print("hidden fruit is in list3")
# else:
#     print("hidden fruit is not found")


# try:
#     RESPONSE = int(input("when are you born: "))
# except:
#     print("did u provide digit? e.g. 1?")


# if RESPONSE >= 2000 and RESPONSE <= 2022:
#     print("you were born in 21st century")
# elif RESPONSE >= 1900 and RESPONSE <= 1999:
#     print("u were born in 20th century")
# elif RESPONSE == 1899 or RESPONSE <= 1800:
#     print("u should not be runnung this")
# else:
#         print("pls give me a number")


#
#[]
# COMMAND ]  --- move to the right
# COMMAND [ MOVE TOT HE LEFT]
    #test


# while True: 
#     try:
#         RESPONSE = int(input("when are you born: "))
#         if RESPONSE >= 2000 and RESPONSE <= 2022:
#             print("you were born in 21st century")
#         elif RESPONSE >= 1900 and RESPONSE <= 1999:
#             print("u were born in 20th century")
#         elif RESPONSE == 1899 or RESPONSE <= 1800:
#             print("u should not be runnung this")
#         else:
#             print("pls give me a number")
#         break
#     except:
#         print("ERROR: did u provide digit? e.g. 1?")

ANSWER = "no"
while ANSWER != "yes":
    ANSWER = input("are you crazy? ")
    if ANSWER == "yes":
        print("I knew that")
    