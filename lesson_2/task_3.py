#через списки (хотя списки тут условно, могли быть и кортежи, например, да?) т.е. коряво как-то сделал
month = int(input("Enter the month: "))
if month in [ 12, 1, 2 ]:
	print("winter")
elif month in [3, 4, 5]:
    print("spring")
elif month in [6, 7, 8]:
    print("summer")
elif month in [9, 10, 11]:
    print("autumn")

#через словари. ужасно примитивно, хотел в словари засунуть range, но не вышло. и не понял почему только с ковычками {} работает
month = int(input("Enter the month: "))
dict = {12: "winter", 1: "winter", 2: "winter", 3: "spring", 4: "spring", 5: "spring" , 6: "summer", 7: "summer", 8: "summer", 9: "autumn", 10: "autumn", 11: "autumn"}
print(dict.get(month))


