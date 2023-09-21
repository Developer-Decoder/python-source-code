# mydictionary = {
#     "name": "item1",
#     "count": 3,
#     "price": 4500
# }
# print(mydictionary)
#
# mydictionary2 = dict(name="newdictionary")
# print(mydictionary2)
# # =====================================================
# print("-----------------------------")
# mydictionary = {
#     "name": "item1",
#     "count": 3,
#     "price": 4500
# }
# print(mydictionary["name"])
# # =====================================================
# print("-----------------------------")
# mydictionary = {
#     "name": "item1",
#     "count": 3,
#     "price": 4500
# }
# print(mydictionary.values())
# print(mydictionary.keys())
# for value in mydictionary.values():
#     print(value)
# # =====================================================
# print("-----------------------------")
# numbers = {
#     "name": "item1",
#     "count": 3,
#     "price": 4500
# }
# for key in numbers.keys():
#     print(numbers[key])
# # =====================================================
# print("-----------------------------")
# num = {
#     "name": "item1",
#     "count": 3,
#     "price": 4500
# }
# for item in num.items():
#     print(item)
# # =====================================================
# print("-----------------------------")
# num = {
#     "name": "item1",
#     "count": 3,
#     "price": 4500
# }
# print("item1" in num.values())
# # =====================================================
# print("-----------------------------")
# numbers = {
#     "name": "item1",
#     "count": 3,
#     "price": 4500
# }
# if "name" in numbers:
#     print(numbers["name"])
# else:
#     print("there is NO name key  in numbers")
# # =====================================================
# print("-----------------------------")
# item = {
#     "name": "item",
#     "count": 5,
#     "price": 4500
# }
# print(item)
# item.clear()
# print(item)
# # =====================================================
# print("-----------------------------")
# mynumbers = {
#     "name": "item",
#     "count": 5,
#     "price": 7
# }
# copy = mynumbers.copy()
# print(mynumbers, copy, mynumbers == copy, mynumbers is copy)
# # =====================================================
# print("-----------------------------")
# newnum = {"name": "unknown", "family": "unknown"}
# newnum2 = {}.fromkeys(["num"], "unknown")
# print(newnum2)
# # =====================================================
# print("-----------------------------")
# mynum = {"name": "item", "count": 5, "price": 7}
# print(mynum.get("name"))
# # =====================================================
# print("-----------------------------")
# mynum = {"name": "item", "count": 5, "price": 7}
# print(mynum.get("num"))
# # =====================================================
# print("-----------------------------")
# mynum = {"name": "item1", "count": 5, "price": 7}
# mynum.pop("name")
# print(mynum)
# # =====================================================
# print("-----------------------------")
# mynum = {"name": "item1", "count": 5, "price": 7}
# mynum.popitem()
# print(mynum)
# # =====================================================
# print("-----------------------------")
# mynum = {"name": "item", "count": 5, "price": 7}
# second = {"age": 50}
# second.update(mynum)
# print(second)
# # =====================================================
# print("-----------------------------")
# mynum = {"name": "item", "count": 5, "price": 7}
# second = {"age": 50}
# second.update(mynum)
# second["name"] = "SARA"
# print(second)
# # =====================================================
# print("-----------------------------")
# numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]
# doublenumbers = [num * 2 for num in numbers]
# print(doublenumbers)
# # =====================================================
# print("-----------------------------")
# num = dict(name=1, m=2, k=3)
# print(num)
# # =====================================================
# print("-----------------------------")
# num = dict(name=1, m=2, k=3)
# numbers = {key: value ** 2 for key, value in num.items()}
# print(numbers)
# # =====================================================
# print("-----------------------------")
# item = {num: num for num in [1, 2, 3, 4, 5, 6, 7]}
# print(item)
# # =====================================================
# print("-----------------------------")
numbers = {num: ("even" if num % 2 == 0 else "odd") for num in [1, 2, 3, 4]}
print(numbers)
# # =====================================================
# print("-----------------------------")
