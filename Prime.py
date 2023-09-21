import time
print("\n")
print("               ---You are allowed to enter only the correct numbers---")
print("\n")
print("\n")
print("            ---You - are - allowed - to - enter - a - number - 9 - times---")
print("\n")

for i in range(1, 10):
    import time
    start = time.time()

    def Is_Prime(n):

        avval = True

        for i in range(2, n):

            if n % i == 0:

                avval = False

                break

        return avval

    print("\n")

    print('            ---------------------------------')
    
    print("\n")

    add = int(input("            range add ra vared konid : "))
    print("\n")
    print('            ---------------------------------')

    sum = 0

    last_Prime_Number = 0

    for i in range(1, add+1):

        # print("\n")

        # print(f"            Is The Number ({i}) prime ? {Is_Prime(i)}")

        # print("\n")

        # print('            ---------------------------------')

        if Is_Prime(i):

            print("\n")

            print(f"            prime {i}")

            last_Prime_Number = i

            sum += 1

            print("\n")

            print('            ---------------------------------')

    end = time.time()
    time = end - start
    print("\n")

    print(f"We Had {sum} Prime Numbers and time {time}")

    print(f" last_Prame_Number : {last_Prime_Number}")
    print("\n")



import time
print("game over😒🤣😂🤣😁😁😁")
print("\n")

print('            ---------------------------------')
time.sleep(30)
