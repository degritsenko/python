a=int(input("первый день пробежки в км "))
b=int(input("цель в км "))
day = 1
while a < b:
    a = a * 1.1
    day = day + 1
print ("наш атлет достиг цели на", day, "день")
