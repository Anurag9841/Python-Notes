#Methods of sets
#ADD method
s=set()
s.add(2)
s.add(5)
s.add(8)
s.add(10)
s.add(15)
print(s)
#s.add([2,5,6,7,8])-->can not add list in set bcz elements of list can be changed that is mutable
s.add((5,6,7,0))#-->can add tuple in set bca tuble is immutable
# s.add({4:5,"anurag":"good boi"})-->can not add dictionary in set bcz dictionary is unhashable type
print(s)
#len method
# print(len(s))
# #remove method
# s.remove(5)#-->removes 5 from set s
# #s.remove(11)-->throws an error since 11 is not present in set
# print(s)
#-->pop method
# print(s.pop())#--->removes random element from set and retur it
# print(s)
#intersection method
b={5,8,10,24,56}
print(s.intersection(b))
#union method
print(s.union(b))