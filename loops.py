# i=0
# while i<5 :
#     print(i)
#     i=i+1
#wap to print the elements of list
# li=["cats","dogs","mouse","lion","cheeta"]
# i=0
# while i<len(li):
#     print(li[i])
#     i=i+1

#for loop
# li=["banana","mango","apple","strawberry"]
# for items in li:
#     print(items)

# range function in python 
# range(Start,stop,stepsize)note:though step size is not used with range
# below function starts from 0 and ends at 7
# for i in range(8):
#     print(i)

#below function starts from 1 and ends at 10
# for i in range(4,11):
#     print(i)

# range with start stop and stepsize

# for i in range(2,11,2):
#     print(i)

# else in for loop

# for a in range(1,10,3):
#     print(a)
# else:
#     print("you are out of for loop")--->else loop runs in sucessful iteration of for loop

#break in for loop
# for i in range(1,10):
#     print("this is\t",i)
#     if i==5:
#         break
# else:
#     print("this is executed after sucessful iteration of loops")

# continue statement in for loop

for i in range(1,10):
    if i==5:
        continue
    print(i)