# print(test)
# # ================================================================
# None = 1
# # ================================================================
# raise IndexError
# # ================================================================
# raise IndexError("you have Entered invalid value")
# # ================================================================
# raise IndexError("throw indax error")
# # ================================================================
# raise IndexError("invalid value")
#
#
# # ================================================================
# def colorize(text, color):
#     if type(text) is not str:
#         raise TypeError("text must be a string")
#     else:
#         print(f"printed {text} in {color}")
#
#
# colorize(8, "red")
#
#
# # ================================================================
def colorize(text, color):
    colors = ("red", "green", "blue")
    if type(text) is not str:
        raise TypeError("text must be a string")
    elif color not in colors:
        raise ValueError(f"{color} is not in colors")
    else:
        print(f"printed {text} in {color}")


colorize("hallo", "yellow")
# # ================================================================
