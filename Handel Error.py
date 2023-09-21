# try:
#     print(myName)
# except:
#     print("an Error occured")
#
#
# # ===============================================================
# def get(num, key):
#     return num[key]


# person = {
#     "name": "Armin",
#     "family": "Abdi"
# }
# print(get(person, "age"))
#
#
# # ===============================================================
# def get(num, key):
#     try:
#         return num[key]
#     except:
#         return None


# person = {
#     "name": "Armin",
#     "family": "Abdi"
# }
# print(get(person, "age"))
#
#
# # ===============================================================
# def get(num, key):
#     try:
#         return num[key]
#     except KeyError:
#         return "No key found"
#     except IndexError:
#         return "IndexError"
#
#
# person = {
#     "name": "Armin",
#     "family": "Abdi"
# }
# print(get(person, "age"))
# # ===============================================================
# try:
#     num = int(input("Please Enter a Number : "))
# except:
#     print('thats not a number')
# # ===============================================================
# try:
#     num = int(input("Plese Enter a Number : "))
# except:
#     print('thats not a number')
# else:
#     print("this is else section")
# # ===============================================================
# try:
#     num = int(input("Plese Enter a Number : "))
# except:
#     print('thats not a number')
# else:
#     print("this is else section")
# finally:
#     print("this is finally section")
#
#
# # ===============================================================
# def divide(first, second):
#     try:
#         return first / second
#     except ZeroDivisionError:
#         return "ZeroDivisionError"


# print(divide(1, 0))
#
#
# # ===============================================================
def divide(first, second):
    try:
        return first / second
    except ZeroDivisionError:
        return "ZeroDivisionError"
    except TypeError as error:
        print(error)
        return "first and second must be number"


print(divide(1, "armin"))
