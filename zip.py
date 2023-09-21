# numbers_1 = [1, 2, 3]
# numbers_2 = [4, 5, 6]
# print(zip(numbers_1, numbers_2))
# # ================================================================
# numbers_1 = [1, 2, 3]
# numbers_2 = [4, 5, 6]
# print(list(zip(numbers_1, numbers_2)))
# # ================================================================
# numbers_1 = [1, 2, 3]
# numbers_2 = [4, 5, 6]
# print(dict(zip(numbers_1, numbers_2)))
# # ================================================================
# numbers = [(1, 4), (2, 5), (3, 6)]
# print(list(zip(*numbers)))
# # ================================================================
# students = ["Armin", "Omar", "matin"]
# midterm = [15, 16, 17]
# final = [16, 17, 18]
# print([pair for pair in zip(midterm, final)])
# # ================================================================
# students = ["Armin", "Omar", "matin"]
# midterm = [15, 16, 17]
# final = [16, 17, 18]
# print({t[0]: max(t[1], t[2]) for t in zip(students, midterm, final)})
# # ================================================================
# students = ["Armin", "Omar", "matin"]
# midterm = [15, 16, 17]
# final = [16, 17, 18]
# print({(f"name: {t[0]},midterm: {t[1]} ,final: {t[2]}") for t in zip(students, midterm, final)})
# # ================================================================
# students = ["Armin", "Omar", "matin"]
# midterm = [16, 17, 18]
# final = [17, 18, 19]
# final_Grades = zip(
#     students,
#     map(
#         lambda piar: max(piar),
#         zip(midterm, final)
#     )
# )
# print(dict(final_Grades))
# # ================================================================
# students = ["Armin", "Omar", "matin"]
# midterm = [15, 16, 17]
# final = [16, 17, 18]
# final_Grades = zip(
#     students,
#     map(
#         lambda piar: (piar[0] + piar[1]) / 2,
#         zip(midterm, final)
#     )
# )
# print(dict(final_Grades))
# # ================================================================
# midterm = [15, 16, 17]
# final = [16, 17, 18]
# final_Grades = map(
#     lambda piar: (piar[0] + piar[1]) / 2,
#     zip(midterm, final)
# )

# print(list(final_Grades))
# # ================================================================
