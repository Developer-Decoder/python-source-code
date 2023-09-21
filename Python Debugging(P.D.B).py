# number_1 = int(input("please Enter a Number : "))
# number_2 = int(input("please Enter a Number : "))
# result = number_1 + number_2
# print(result)
# # # =====================================================
# import pdb
#
# pdb.set_trace()
# number_1 = int(input("please Enter a Number : "))
# number_2 = int(input("please Enter a Number : "))
# result = number_1 + number_2
# print(result)
#
#
# # common pdb commands
# # L->your commands list
# # N->next line
# # C->continue->finished debugging
# # p->print
# # # =====================================================
def abc(a, s, b, f):
    import pdb;pdb.set_trace()
    return a + s + b + f


num = abc(12, 13, 17, 18)
print(num)
