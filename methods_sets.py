#methods of empty sets 

# b=set()
# print(type(b))
# #--> 1st method is to add elemrnt on empty set

# b.add(4)
# b.add(5)
# b.add(6)
# b.add(7)
# b.add(4)
# print(b)

# c={45,6,66}
# c.add(34)
# c.add(42)
# c.add(65)
# c.add((1,2,3,4))#-->can add tuple in sets bcz it is hashable
# c.add([1,2,3,4])#-->can not add list in sets bcz it is unhashable as its element can be changes
# c.add({1:4,5:"hello"})#-->can not add dict in sets bcz it is unhashable like list
# c.add((1,2,3,4,5))
# c.add("hello")
# print(c)
# print(len(c))

#-->methods to remve element of set

# c.remove((1,2,3,4,5))#-->remove elements from sets
# print(c)
#--->question arise ?? if we remove elements that is not present in the sets...for exmaple i want to remove 100 from set which is not present in set..lets see the output
# c.remove(100)#--> this throws key error in sets
# print(c)

# print(c.pop())#--> removes random aribitary elements from sets and return set

# print(c.clear())#-->empty sets

#uninon and intersection with empty sets
c=set()
print(c.union({1,2,3}))
print(c.intersection({45}))

#union and intersection with non empty sets

c={"hello",1,2,4}
print(c)
print(c.union({"hi",3,4}))
print(c.intersection({"hello",2}))