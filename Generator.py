## Generator
# def count_up_to(max):
#     count=1
#     while count<max:
#         yield count
#         count+=1
# counter=count_up_to(10)
# print(next(counter))
# print(next(counter))
# print(next(counter))
# print(next(counter))
# # # ================================================================
# def fib_list(max):
#     nums = []
#     a, b = 0, 1
#     while len(nums) < max:
#         nums.append(b)
#         a, b = b, a + b
#     return nums
#
#
# print(fib_list(100))
# # # ================================================================
# def fib_generator(max):
#     a, b = 0, 1
#     count = 0
#     while count < max:
#         a, b = b, a + b
#         yield b
#         count += 1
#
#
# for num in fib_generator(10):
#     print(num)
# # # ================================================================
# def nums():
#     for num in range(10):
#         yield num
#
#
# me = nums()
# print(next(me))
# print(next(me))
# print(next(me))
# print(next(me))
# # # ================================================================
# print(sum([num for num in range(1000000000)]))
# # # ================================================================
# print(sum((num for num in range(100000000))))
# # # ================================================================
