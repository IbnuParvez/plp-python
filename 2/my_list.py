#step 1
my_list = []

#step 2
my_list.append(10)
my_list.append(20)
my_list.append(30)
my_list.append(40)

#step 3
#syntax is first index then the element u wanna insert
my_list.insert(1,15)

#step 4
my_list.extend([50, 60, 70])

#step 5
#pop method removes last item
my_list.pop()

#step 6
my_list.sort()

#step 7
indexed = my_list.index(30)

print("The value of index of value of 30 is: " ,indexed)