our_list = []
for i in range(0, 5):
  number = int(input('enter a five numbers: '))
  our_list.append(number)
our_list[0], our_list[1], our_list[2], our_list[3] = our_list[1], our_list[0], our_list[3], our_list[2]
print(our_list)