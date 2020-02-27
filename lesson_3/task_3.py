def two(a, b, c):
   list = [a, b, c]
   small = min(list)
   list.remove(small)
   print(sum(list))
two(4,9,10)