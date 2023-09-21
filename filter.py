# mynumbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]
# print(list(filter(lambda num: num % 2 == 0, mynumbers)))
# # ==============================================================
# print("-----------------------------")
# mynumbers = [{"num": "ARMIN", "item": [1]}, {"name": "OMAR", "item": []}]
# print(len(mynumbers))
# print(list(filter(lambda num: len(num["item"]) == 0, mynumbers)))
# # ==============================================================
# print("-----------------------------")
# mynumbers = [{"num": "ARMIN", "item": [1]}, {"name": "OMAR", "item": []}]
# print(list(filter(lambda num: num["item"], mynumbers)))
# # ==============================================================
# print("-----------------------------")
# mynumbers = [{"num": "ARMIN", "item": [1]}, {"name": "OMAR", "item": []}]
# print(list(filter(lambda num: not num["item"], mynumbers)))
# # ==============================================================
# print("-----------------------------")
mynumbers = [{"num": "ARMIN", "item": [1]}, {"name": "OMAR", "item": []}]
print(list(map(lambda num: num["name"], filter(lambda num: not num["item"], mynumbers))))
# # ==============================================================
# print("-----------------------------")
