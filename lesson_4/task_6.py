"""6. Реализовать два небольших скрипта:
а) бесконечный итератор, генерирующий целые числа, начиная с указанного,
б) бесконечный итератор, повторяющий элементы некоторого списка, определенного заранее.
Подсказка: использовать функцию count() и cycle() модуля itertools."""
from itertools import count
for x in count():
    if x == 10:
        break
    print(x)

#тут не смог придумать, как сделать break по условию
from itertools import cycle

for y in cycle([1, 2]):
    if count(cycle()) > 2:
        break
    print(y)

