print("----Select an option from the menu to find the required ----")
print("1.Range")
print("2.coefficient of range")
print("3.mean")
print("4.mode")
print("5.median\n")


def Range():
    num = list(map(int, input("Enter data to find range=").split(",")))
    ans = max(num) - min(num)
    print("Range is=", ans)


def C_R():
    num = list(map(int, input("Enter data to find coefficient of range=").split(",")))
    r = max(num) - min(num)
    ans = (r) / (max(num) + min(num))
    print("Coefficient of range is=", ans)


def mean():
    print("1.for grouped data")
    print("2.ungrouped data")
    n = int(input("Enter your choice="))
    # match n:
    #     case 1:
    #         # grouped()
    #     case 2:
    #         ungrouped()


# def grouped():


def ungrouped():
    num = list(map(int, input("Enter data to find mean of ungrouped data=").split(",")))
    mean = sum(num) / len(num)
    print("Mean is=", mean)


def median():
    print("1.for grouped data")
    print("2.ungrouped data")
    n = int(input("Enter your choice="))
    # match n:
    #     case 1:
    #         grouped()
    #     case 2:
    #         ungrouped()


def ungrouped():
    num = list(map(int, input("Enter data separated by comma: ").split(",")))
    num.sort()
    n = len(num)
    if n % 2 == 0:
        m1 = num[n // 2 - 1]
        m2 = num[n // 2]
        median = (m1 + m2) / 2
    else:
        median = num[n // 2]
    print("Median is =", median)


choice = int(input("Enter your choice="))
match choice:
    case 1:
        Range()
    case 2:
        C_R()
    case 3:
        mean()
    # case 4:
    #     mode()
    case 5:
        median()
