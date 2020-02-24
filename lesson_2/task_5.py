#не получилось сделать, что бы 3 была последняя :(
list = [7, 5, 3, 3, 2]

while True:
    n = int(input("enter number:"))
    list.append(n)
    break

list.sort()
list.reverse()
print(list)

