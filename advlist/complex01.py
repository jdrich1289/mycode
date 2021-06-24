#!/usr/bin/env python3

# create a list called list1
list1 = ["cisco_nxos", "arista_eos", "cisco_ios"]
# display list1
print(list1)
# display list1[1] 
print(list1[1])
# new list 
list2 = ["juniper"]
# extend list1 by list2
list1.extend(list2)
# display list1
print(list1)
# create list3 
list3 = ["10.1.0.1", "10.2.0.1", "10.3.0.1"]
# use append list1 by list3
list1.append(list3)
# display new complex list1
print(list1)
# display the list of ip addr
print(list1[4])
# display the first item in the list - first ip addr
print(list1[4][0])
