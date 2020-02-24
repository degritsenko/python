#не получилось сделать, что бы 3 была последняя :(
list = [7, 5, 3, 3, 2]

while True:
    n = int(input("enter number:"))
    list.append(float(n))
    break

list.sort()
list = list[::-1]
print(list)
