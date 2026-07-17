import random as rd

i = 0
while True:
    x = rd.randint(1, 10)
    y = rd.randint(1, 10)
    print("Solve The Addition and Built up Your Score🙂:", x, "+", y)
    z = x + y
    c = int(input("Addition is:"))
    if c == z:
        i = i + 1
        print("True😀")
    elif c != z:
        print("False🤨")
        print("Go To The Nursary Again..🙁")
        break
    # else:
    #     print("End Game")
print("\nYour Score is ❤️  :", i)
