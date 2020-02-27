def fun (a, b):
    try:
        c = a / b
        return c
    except ZeroDivisionError:
        return "b is not be 0"
    except ValueError:
        print("HOW I CAN PRINT THIS?!")
print(fun (int(input("enter a = ")), int(input("enter b = "))))
