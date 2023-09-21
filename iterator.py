# iterable
# iterator
# iterate
#
# numbers = [1, 2, 3, 4, 5, 6]
# for num in numbers:
#     print(num)
# # ==========================================
#
# next()
# iter()
# iterable = > iter() = > iterator
#
# # ==========================================
# numbers = [1, 2, 3, 4, 5, 6]
# iternums = iter(numbers)
# print(next(iternums))
# print(next(iternums))
# print(next(iternums))
# print(next(iternums))
# print(next(iternums))
# print(next(iternums))
# # ==========================================
# name = "Armin"
# iterName = iter(name)
# print(next(iterName))
# print(next(iterName))
# print(next(iterName))
# print(next(iterName))
# print(next(iterName))
# # ==========================================
def my_for(iterable,func):
    iterator = iter(iterable)
    while True:
        try:
            num = next(iterator)
        except StopIteration:
            break
        else:
            func(num)


numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]


def square(num):
    print(num ** 2)


my_for(numbers,square)
