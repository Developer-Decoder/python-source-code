# item = ["ARMIN", "OMAR", "MATIN", "SARA"]
# num = item.index("OMAR")
# print(num)
# # ==============================================================
# print("-----------------------------")
# item = ["python", "kotlin", "ionic", "python",
#         "Jquery", "vue JS", "python", "vue JS"]
# num = item.index("python", 1, 7)
# print(num)
# # ==============================================================
# print("-----------------------------")
# item = ["python", "kotlin", "ionic", "python", "Jquery", "python"]
# num = item.count("python")
# print(num)
# # ==============================================================
# print("-----------------------------")
# item = ["python", "kotlin", "ionic", "Jquery"]
# print(item)
# item.reverse()
# print(item)
# # ===============================================================
# print("-----------------------------")
# item = [7, 98, 65, 45, 75, 89, 33, 2, 1, 6]
# print(item)
# item.sort()
# print(item)
# # ==============================================================
# print("-----------------------------")
# item = ["Python", "Kotlin", "Ionic"]
# num = " _ ".join(item)
# print(num)
# # ===============================================================
# print("-----------------------------")
# mynumbers = ["Python", "Kotlin", "Ionic"]
# print(mynumbers[1])
# # ===============================================================
# print("-----------------------------")
# mynumbers = ["python", "kotlin", "ionic", "python", "Jquery", "python"]
# print(mynumbers[5:1:-1])
# # ================================================================
# print("-----------------------------")
# mynumbers = ["python", "kotlin", "ionic", "python", "Jquery"]
# print(mynumbers[2:])
# # ================================================================
# print("-----------------------------")
# mynumbers = ["python", "kotlin", "ionic"]
# print(mynumbers[:])
# # ================================================================
# print("-----------------------------")
# numbers = [[1, 2, 3], [4, 5, 6]]
# for li in numbers:
#     for num in li:
#         print(num)
# # ===============================================================
# print("-----------------------------")
# number = [[1, 2, 3, 4], [5, 6, 7, 8]]
# print(number)
# copynumbers = [[l for l in li] for li in number]
# print(copynumbers)
# print(number == copynumbers)
# print(number is copynumbers)
# # ===============================================================
# print("-----------------------------")
# numbers = [[1, 2, 3], [4, 5, 6]]
# copylist = [[print(li) for li in numbers]]
# # ===============================================================
# print("-----------------------------")
# numbers = [[1, 2, 3], [4, 5, 6]]
# copylist = [[print(l) for l in num] for num in numbers]
# # ===============================================================
# print("-----------------------------")
# numbers = [[1, 2, 3], [4, 5, 6]]
# nestedlist = [[Newnum for Newnum in range(1, 4)] for num in range(1, 4)]
# print(nestedlist)
# # ===============================================================
# print("-----------------------------")
# numbers = [[1, 2, 3], [4, 5, 6]]
# nestedlist = [["X" if num % 2 == 0 else "O" for num in range(1, 4)] for num in range(1, 4)]
# print(nestedlist)
# # ===============================================================
# print("-----------------------------")
# item = range(1, 11)
# print(item)
# num = list(item)
# print(num)
# # ===============================================================
# print("-----------------------------")
# print(list(range(1, 11)))
# # ===============================================================
# print("-----------------------------")
# item = ("python", "kotlin", "ionic")
# num = list(item)
# print(num)
# # ===============================================================
# print("-----------------------------")
# item = [[1, 2, 3], [4, 5, 6]]
# num = item[0][1]
# print(num)
# # ===============================================================
# print("-----------------------------")
# mynumbers = ["python", "kotlin", "ionic", "python",
#              "Jquery", "vue JS", "python"]
# myname = mynumbers[0:6:1]
# print(myname)
# # ================================================================
# print("-----------------------------")
# mynumbers = ["python", "kotlin", "ionic", "python", "Jquery", "vue JS", "python"]
# print(mynumbers[2:])
# # ================================================================
# print("-----------------------------")
# mynumber = ["python", "kotlin", "ionic", "python", "Jquery", "vue JS", "python"]
# copy = mynumber[:]
# print(mynumber)
# print(copy)
# print(mynumber == copy)
# print(mynumber is copy)
# # ================================================================
# print("-----------------------------")
# mynumbers = [1, 2, 3]
# doublenumbers = []
# for num in mynumbers:
#     doublenumbers.append(num)
# print(mynumbers)
# print(doublenumbers)
# # ================================================================
# print("-----------------------------")
# number = "ARMIN"
# item = [num for num in number]
# print(item)
# # ================================================================
# print("-----------------------------")
# item = "armin"
# numbers = [num.upper() for num in item]
# print(numbers)
# # ================================================================
# print("-----------------------------")
# mynumbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]
# even = [num for num in mynumbers if num % 2 == 0]
# odd = [num for num in mynumbers if num % 2 != 0]
# print(even)
# print(odd)
# newlist = [num * 2 if num % 2 == 0 else num * 3 for num in mynumbers]
# print(newlist)
# # ================================================================
# print("-----------------------------")
# import random
#
# list_1 = [random.randint(-20, 20) for num in range(5)]
# print(list_1)
# max = 0
# for num in list_1:
#     if max < num:
#         max = num
# print(f"max : {max}   max index : {list_1.index(max)}")
# min = 0
# for num in list_1:
#     if min > num:
#         min = num
# print(f"min : {min}   min index : {list_1.index(min)}")
# # ================================================================
# print("-----------------------------")
