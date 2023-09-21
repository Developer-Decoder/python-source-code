"""
user:{
    Attr->مشخصات
    functnalites->رفتار ها
    -----------------------------------------------------
    hellp(int)
    dir->نوع نوشتار داده های oop
    id-> آیدی مورد نظر
    -----------------------------------------------------
    Encapsulation->خصوصیات و رفتار های یک آیتم
    app section->ساختار پیچیده را نمایش نده
    -----------------------------------------------------
}
"""


# class User:
#     pass
#
#
# print(type(5))
#
#
# # ================================================================
# class User:
#     pass


# number_1 = list()
# number_2= User()
# print(type(number_2))
# print(__name__)
# # ================================================================
# help(len)
#
#
# # ================================================================
# class User:
#     user_name = "armin"
#     user_family = "abdi"
#     User_age = 19


# me = User()
# print(me.user_name)

#
# # ================================================================
# class User:
#     user_name = "armin"
#     user_family = "abdi"
#     User_age = 19
#
#     def show_full_name(self):
#         return self.user_name + " " + self.user_family
#
#
# me = User()
# print(me.show_full_name())
#
#
# # ================================================================
# class User:
#     User_name = "armin"
#     User_family = "abdi"
#     User_age = "19"

#     def show_full_name(self):
#         return self.User_name + " " + self.User_family + " " + self.User_age


# me = User()
# print(me.show_full_name())
#
#
# # ================================================================
# class car:
#     def __init__(self, User_name, User_number_of_doors, User_color):
#         self.User_name = User_name
#         self.User_number_of_doors = User_number_of_doors
#         self.User_color = User_color
#
#
# benz = car("sls", 2, "red")
# print(benz.User_color)
#
#
# # ================================================================
# class car:
#     def __init__(self, User_name, User_number_of_doors, User_color):
#         self.User_name = User_name
#         self.User_number_of_doors = User_number_of_doors
#         self.User_color = User_color

#     def show_car_full_Info(self):
#         return f"car name is : {self.User_name} car number of doors : {self.User_number_of_doors} car color is : {self.User_color}"


# benz = car("sls", 2, "red")
# print(benz.show_car_full_Info())
# # ================================================================
# _name
# __name->name
# mengling
# __name__

#
# class User:
#     def __init__(self, User_name):
#         self.User_name = User_name
#         self.User_password = "1946"
#         self.__massage = "I Love python"
#
#
# class person:
#     def __init__(self):
#         self.__massage = "test massage"
#     def login(self,gotpassword):
#         if self.password==gotpassword:
#             print("login User")
#         else:
#             print("you are not logged in")
#
#
# me = User("armin")
# print(dir(me))
# you = person()
# print(you._person__massage)
# print(me._User__massage)
#
#
# print(dir(me))
# # ================================================================
# class calculator:
#     def sum(self, a, b):
#         print(f"{a}+{b} = {a + b}")
#
#     def subtraction(self, a, b):
#         print(f"{a}-{b} = {a - b}")
#
#     def multiplication(self, a, b):
#         print(f"{a} * {b} = {a * b}")
#
#     def exponent(self, a, b):
#         print(f"{a} ** {b} = {a ** b}")
#
#     def division(self, a, b):
#         print(f"{a} / {b} = {a / b}")
#
#
# mycalc = calculator()
# mycalc.sum(20, 5)
# mycalc.subtraction(20, 5)
# mycalc.multiplication(20, 5)
# mycalc.exponent(20, 5)
# mycalc.division(20, 5)

#
# # ================================================================
# class User:
#     def __init__(self, got_Name, got_Family, got_age):
#         self.Users_Name = got_Name
#         self.Users_Family = got_Family
#         self.Users_age = got_age
#
#     def show_Full_Name(self):
#         return f"{self.Users_Name} {self.Users_Family}"
#
#     def show_Age_status(self):
#         return "adult" if self.Users_age > 18 else "not adult"
#
#
# me = User("armin", "abdi", 19)
# print(me.show_Full_Name())
# print(me.show_Age_status())
#
#
# # ================================================================
# class User:
#     active_count = 0
#
#     def __init__(self, got_Name, got_Family):
#         self.Users_Name = got_Name
#         self.Users_Family = got_Family
#         User.active_count += 1
#         print(f"{self.Users_Name} logged in")
#
#
# print(f"activ User : {User.active_count}")
# armin = User("armin", "abdi")
# sara = User("sara", "moradi")
# print(f"activ User : {User.active_count}")
#
#
# # ================================================================
# class User:
#     active_count = 0
#     allowed_User = ["armin", "sara", "ali"]
#     loggedInUser = []

#     def __init__(self, got_Name, got_Family):
#         if got_Name not in User.allowed_User:
#             raise ValueError(f"{got_Name}can not loggin")
#         self.Users_Name = got_Name
#         self.Users_Family = got_Family
#         User.active_count += 1
#         User.loggedInUser.append(got_Name)
#         print(f"{self.Users_Name} logged in")

#     def loggout(self):
#         print(f"{self.Users_Name} has logged out")
#         User.active_count -= 1
#         User.loggedInUser.remove(self.Users_Name)


# print(f"activ User : {User.active_count}")
# print(f"loggedInUser : {User.loggedInUser}")
# armin = User("armin", "abdi")
# print(f"loggedInUser : {User.loggedInUser}")
# sara = User("sara", "moradi")
# print(f"loggedInUser : {User.loggedInUser}")
# sara.loggout()
# print(f"activ User : {User.active_count}")
# print(id(sara))

# # ================================================================
# class User:
#     def __init__(self, got_Name, got_Family):
#         self.Users_Name = got_Name
#         self.Users_Family = got_Family
#
#     def __repr__(self):
#         return f"{self.Users_Name}  {self.Users_Family}"
#
#
# me = User("Armin", "Abdi")
# print(me)
#
#
# # ================================================================
# class User:
#     classAttribute = "test value"
#
#     def __init__(self, got_Name, got_Family, got_age):
#         self.Users_Name = got_Name
#         self.Users_Family = got_Family
#         self.User_Age = got_age
#
#     def show_full_name(self):
#         return f"{self.Users_Name} {self.Users_Family}"
#
#     @classmethod
#     def showclassAttribute(cls):
#         return User.classAttribute
#
#
# class Person(User):
#     pass
#
#
# armin = User("armin", "abdi", 19)
# sara = Person("sara", "moradi", 24)
# print(armin.Users_Name)
# print(Person.showclassAttribute())
# print(sara.show_full_name())
# print(Person.showclassAttribute())
# print(sara.Users_Name)
#
#
# # ================================================================
# class User:
#     def __init__(self, got_Name, got_Family, got_age):
#         self.Users_Name = got_Name
#         self.Users_Family = got_Family
#         if got_age >= 0:
#             self.User_age = got_age
#         else:
#             self.User_age = 0


# me = User("armin", "abi", -15)
# print(me.User_age)
# #
#
# # ================================================================
# class User:
#     def __init__(self, got_Name, got_Family, got_age):
#         self.Users_Name = got_Name
#         self.Users_Family = got_Family
#         if got_age >= 0:
#             self._age = got_age
#         else:
#             self._age = 0

#     def get_age(self):
#         return self._age

#     def set_age(self, age_value):
#         if age_value >= 0:
#             self._age = age_value
#         else:
#             raise ValueError(" age can not be hegative")


# me = User("Armin", "Abdi", 25)
# me.set_age(-10)
# print(me.get_age())


# # ================================================================
# class User:
#     def __init__(self, got_Name, got_Family, got_age):
#         self.Users_Name = got_Name
#         self.Users_Family = got_Family
#         if got_age >= 0:
#             self._age = got_age
#         else:
#             self._age = 0

#     def get_age(self):
#         return self._age

#     def set_age(self, age_value):
#         if age_value >= 0:
#             self._age = age_value
#         else:
#             raise ValueError(" age can not be hegative")

#     @property
#     def age(self):
#         return self._age

 
# me = User("Armin", "Abdi", 23)
# print(me.age)
#
#
# # ================================================================
# class User:
#     def __init__(self, got_Name, got_Family, got_age):
#         self.Users_Name = got_Name
#         self.Users_Family = got_Family
#         if got_age >= 0:
#             self._age = got_age
#         else:
#             self._age = 0
#
#     @property
#     def age(self):
#         return self._age
#
#     @age.setter
#     def age(self, value):
#         if value >= 0:
#             self._age = value
#         else:
#             raise ValueError(" age can not be hegative")
#
#
# me = User("armin", "abdi", 23)
# me.age = 40
# print(me.age)
#
#
# # ================================================================
# class User:
#     def __init__(self, got_Name, got_Family):
#         self.Users_Name = got_Name
#         self.Users_Family = got_Family

#     @property
#     def fullname(self):
#         return f"{self.Users_Name}  {self.Users_Family}"


# class Person(User):
#     def __init__(self, got_Name, got_Family, Email):
#         super().__init__(got_Name, got_Family)
#         self.Person_Email = Email


# Armin = Person("Armin", "Abdi", "arminabdi2018@gmail.com")
# print(Armin.fullname)


# # ================================================================
class Person:
    def __init__(self, name):
        self.name = name

    def seyHello(self):
        return f'Hello {self.name}'


class User:
    def __init__(self, name):
        self.name = name

    def seyHello(self):
        return f'Hello {self.name}'


class Admin(Person, User):
    def __init__(self, name):
        super().__init__(name)


Person_1 = Admin("Armin")
print(Person_1.name)
print(isinstance(Person_1, Admin))
print(isinstance(Person_1, User))
print(isinstance(Person_1,Person))
#
#
# # ================================================================
# class Person:
#     def __init__(self, name):
#         print("person init")
#         self.name = name
#
#     def seyHello(self):
#         return f'Hello {self.name}'
#
#
# class User:
#     def __init__(self, name):
#         print("User init")
#         self.name = name
#
#     def seyHello(self):
#         return f'Hello {self.name}'
#
#     def saybye(self):
#         return f"goodbye {self.name}"
#
#
# class Admin(Person, User):
#     def __init__(self, name):
#         print("Admin init")
#         super().__init__(name)
#
#
# Person_1 = Admin("Armin")
# print(Person_1.name)
# print(Person_1.saybye())
#
#
# # ================================================================
# class Person:
#     def __init__(self, name):
#         print("person init")
#         self.name = name
#
#     def seyHello(self):
#         return f'Hello {self.name}'
#
#
# class User:
#     def __init__(self, name):
#         print("User init")
#         self.name = name
#
#     def seyHello(self):
#         return f'Hello {self.name}'
#
#     def saybye(self):
#         return f"goodbye {self.name}"
#
#
# class Admin(Person, User):
#     def __init__(self, name):
#         print("Admin init")
#         super().__init__(name)
#
#
# print(Admin.__mro__)
# print(Admin.mro())
# help(Admin)
#
#
# # ================================================================
# class a:
#     def sayhello(self):
#         print("hello python in a")
#
#
# class b(a):
#     def sayhello(self):
#         print("hello python in b")
#
#
# class c(a):
#     def sayhello(self):
#         print("hello python in c")
#
#
# class d(b, c):
#     pass
#
#     def sayhello(self):
#         print("hello python in d")
#
#
# item = d()
# item.sayhello()
# # ================================================================
# polymorphism
# poly->multyi
# morph->form
#
#
#
# class DOG:
#     def makeSound(self):
#         return f'DOG make Sound '
#
#
# class CAT:
#     def makeSound(self):
#         return f'CAT make Sound '
#
#
# dog = DOG()
# cat = CAT()
# print(dog.makeSound())
# print(cat.makeSound())

# # # ================================================================
# class Animal:
#     def makeSound(self):
#         raise NotImplementedError
#
#
# class DOG(Animal):
#     def makeSound(self):
#         return "DOG is making Sound"
#
#
# class CAT(Animal):
#     def makeSound(self):
#         return "CAT is making Sound"
# class Wirm(Animal):
#     def makeSound(self):
#         return "Worm does not  make any Sound"
#
#
#
# dog: DOG = DOG()
# cat = CAT()
# worm=Wirm()
# print(dog.makeSound())
# print(cat.makeSound())
# print(worm.makeSound())
# # # ================================================================
# class IUserService:
#     def getAllUsers(self): raise NotImplementedError
#
#     def getUserById(self): raise NotImplementedError
#
#     def createNewUser(self): raise NotImplementedError
#
#
# class UserserviceBysql(IUserService):
#     def getAllUsers(self):
#         print("get all ysers from sql server")
#
#
# class UserserviceByOracle(IUserService):
#     def getAllUsers(self):
#         print("get all ysers from sql server")
#
#
# userservicBysql = UserserviceBysql()
# userserviceByOracle = UserserviceByOracle()
# userservicBysql.getAllUsers()
# userserviceByOracle.getAllUsers()
# # # ================================================================
# class Persan:
#     def __init__(self, name, family, age, money):
#         self.name = name
#         self.family = family
#         self.age = age
#         self.money = money
#
#     def __repr__(self):
#         return f"{self.name} {self.family}"
#
#     def __len__(self):
#         return self.age
#
#     def __add__(self, other):
#         return self.money + other.money
#     def __mul__(self, other):
#         return self.money*other.money
#     def __truediv__(self, other):
#         return self.money / other.money
#
# person_1 = Persan("armin", "Abdi", 19, 50000)
# person_2 = Persan("matin", "moradi", 19, 50000)
# print(person_1)
# print(person_2)
# print(person_1 + person_2)
# print(person_1 * person_2)
# print(person_1 / person_2)
# # # ================================================================
# class Counter:
#     def __init__(self,start,end,step=1):
#         self.current=start
#         self.end=end
#         self.step=step
#     def __iter__(self):
#         return self
#     def __next__(self):
#         if self.current <= self.end:
#             Num = self.current
#             self.current += self.step
#             return Num
#         raise StopIteration
#
# myCounter=Counter(10,16)
#
# for num in myCounter:
#     print(num)
# # # ================================================================
# class User:
#     ActiveUser=[]
#     def __init__(self,name,family):
#         self.User_name=name
#         self.User_family=family
#         User_Dict={"name":name,"family":family}
#         User.ActiveUser.append(User_Dict)
# me=User("Armin","Abdi")
# print(User.ActiveUser)
# # # ================================================================
# class User:
#     ActiveUsers = []
#
#     def __init__(self, name, family):
#         self.name = name
#         self.family = family
#         User_Dict = {"name": name, "family": family}
#         User.ActiveUsers.append(User_Dict)
#         self.index = 0
#
#     def log_out(self):
#         print(f"{self.name} in logged out")
#         curent_User = list(filter(lambda num: num["name"] == self.name, User.ActiveUsers))[0]
#         print(curent_User)
#
#     def __iter__(self):
#         return self
#
#     def __next__(self):
#         if self.index<len(User.ActiveUsers):
#             numbers=User.ActiveUsers[self.index]
#             self.index+=1
#             return numbers
#         raise StopIteration
#
# me = User("Armin", "Abdi")
# you = User('armin', 'abdi')
# s=User("ali","aaa")
# print(User.ActiveUsers)
#
# for seed in me:
#     print(seed)
# # # ================================================================
# ## Generator
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
