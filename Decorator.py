# def sum(number,func):
#     total=0
#     for num in range(1,number+1):
#         total+=func(num)
#     return total
# def square(x):
#     return x*x

# print(sum(5,square))
# # ==============================================================
# from random import choice


# def greet(person):
#     def get_mood():
#         msg = choice(("hello there  ", "go away  ", "goodbye  "))
#         return msg

#     result = get_mood() + person
#     return result


# print(greet("armin"))
# # ==============================================================
# from random import choice
#
#
# def greet(person):
#     def get_mood():
#         msg = choice(("hello there  ", "go away  ", "goodbye  "))
#         Res = msg + person
#         return Res
#
#     return get_mood
#
#
# res = greet("armin")
# print(res())
# # ==============================================================
# def my_Decorator(func):
#     def say_bye():
#         print('bye guys')
#         func()

#     return say_bye


# def say_hello():
#     print('hello guys')


# sayhello = my_Decorator(say_hello)
# sayhello()
# # ==============================================================
# def my_Decorator(func):
#     def say_bye():
#         print('bye guys')
#         func()

#     return say_bye


# @my_Decorator
# def say_hello():
#     print('hello guys')


# say_hello()

# # ==============================================================
# def my_Decorator(func):
#     def say_bye(*args, **Kwargs):
#         print(f'this is working for me ')
#         func(*args, **Kwargs)

#     return say_bye


# @my_Decorator
# def say_hello(Name):
#     print(f'hello {Name}')


# @my_Decorator
# def say_my_name(name, family):
#     print(f"{name}  {family}")


# say_hello("armin")
# say_my_name("armin", "abdi")

# # ==============================================================
# def my_Decorator(func):
#     def wrapper(*args, **Kwargs):
#         print(args)
#         print(Kwargs)
#         func(*args, **Kwargs)

#     return wrapper


# @my_Decorator
# def say_hello(name, family):
#     print(f'hello {name}  {family}')


# say_hello('armin', 'abdi')
# # ==============================================================
# from functools import wraps


# def my_Decorator(func):
#     @wraps(func)
#     def wrapper(*args, **Kwargs):
#         print(f"function name is {func.__name__}")
#         return func(*args, **Kwargs)

#     return wrapper


# @my_Decorator
# def say_hello(name, family):
#     print(f'hello {name}  {family}')


# print(say_hello.__name__)
# print(say_hello.__doc__)
# help(say_hello)

# # ==============================================================
# from functools import wraps


# def show_Decrator(is_show):
#     def inner_Decrator(func):
#         @wraps(func)
#         def wrapper():
#             if is_show:
#                 func()
#             else:
#                 print("you dont have permission ")

#         return wrapper
#     return inner_Decrator


# @show_Decrator(True)
# def go_to_admin_page():
#     print("this is admin page")


# go_to_admin_page()

# # ==============================================================
# from functools import wraps


# def check_string_lengt(charactercount):
#     def inner_Decrator(func):
#         @wraps(func)
#         def wrapper(name):
#             if len(name) > charactercount:
#                 print("an error occured")
#             else:
#                 func(name)
#             return func
#         return wrapper
#     return inner_Decrator


# @check_string_lengt(10)
# def show_name(name):
#     print(name)


# show_name("armirfghyrtfn")

# # ==============================================================
# from time import time

# start_time = time()
# sum(num for num in range(20000000))
# end_time = time()

# print(end_time - start_time)

# # ==============================================================
# from time import time
#
#
# def speed_test_Decrator(func):
#     def wrapper(*args, **kwargs):
#         start_time = time()
#         result = func(*args, **kwargs)
#         end_time = time()
#         print(f"Time Elapsed : {end_time - start_time}")
#
#         return result
#
#     return wrapper
#
#
# @speed_test_Decrator
# def sum_nums_gen():
#     return sum(x for x in range(70000000))
#
#
# @speed_test_Decrator
# def sum_nums_list():
#     return sum([x for x in range(70000000)])
#
#
# sum_nums_gen()
# sum_nums_list()
# help(sum_nums_gen)

# # ==============================================================

