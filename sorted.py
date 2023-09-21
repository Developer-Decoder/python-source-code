# numbers = [1, 5, 8, 4, 6, 2]
# print(numbers)
# numbers.sort()
# print(numbers)
# # ===============================================================
# numbers = [1, 5, 8, 4, 6, 2]
# result = sorted(numbers)
# print(numbers)
# print(result)
# # ===============================================================
# numbers = [1, 5, 8, 4, 6, 2]
# result = sorted(numbers, reverse=True)
# print(numbers)
# print(result)
# # ===============================================================
users = [
    {"name": "armin", "family": "abdi", "age": 19},
    {"name": "omar", "family": "fatahi", "age": 15},
    {"name": "matin", "family": "moradi", "age": 14}
]
print(sorted(users, key=lambda user: user["name"]))
# # ===============================================================
