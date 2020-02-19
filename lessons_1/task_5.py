# #выручка есть
earnings = 5000
lose = 3000
profit = ((earnings) - (lose))
#print ("profit is", profit)

rentability = earnings / profit
print(rentability)
employers = input("How many employers in company? ")
salary = profit / int(employers)
print(f"{salary:.1f}$")

#выручки нет
earnings = 5000
lose = 6000
profit = ((earnings) - (lose))
#print ("profit is", profit)

rentability = earnings / profit
print(rentability)
# employers = input("How many employers in company? ")
# salary = profit / int(employers)
# print(f"{salary:.1f}$")


#Доход=расходам
earnings = 5000
lose = 5000
profit = ((earnings) - (lose))
print ("profit is", profit)
