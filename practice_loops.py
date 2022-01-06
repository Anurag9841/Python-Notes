# problem no 1

# a=int(input("enter the number whose multiplication table u want\n"))
# print("\n")
# for i in range(1,11):
#     print(f"{a} X {i}={a*i}")

# problem no 2

# li=["anurag","anuska","aka","bhattu","chattu","khattu"]
# for i in li:
#     if i.startswith("a"):
#         print("hello\t"+i)

#problem no 3

# b=int(input("enter the number whose multiplication table u want\n"))
# i=1
# while i<=10:
#     print(f"{b} X {i} = {b*i}")
#     i=i+1

# problem no 4

# a=int(input("enter the number to check whether it is prime or not\n"))
# prime=True
# for i in range(2,a):
#     if (a%i==0):
#         prime=False
#         break
# if prime==True:
#     print("the number is prime")
# else:
#     print("the number is not prime")

#problem no 5

# n=int(input("enter the number\n"))
# sum=0
# i=1
# while i<=n:
#     sum=sum+i
#     i=i+1
# print(f"the sum of number is {sum}")

#problem no 6

# n=int(input("enter the number\n"))
# i=1
# fact=1
# while i<=n:
#     fact=fact*i
#     i=i+1
# print(f"the factorial of the given number is {fact}")


# n=int(input("enter the number \n"))
# prime=False
# for i in range(2,n):
#     if(n%i==0):
#         prime=True
#         break
# if prime==False:
#     print("the number is prime")
# else:
#     print("the number is not prime")
l=int(input("enter the length of square : "))
for i in range(l):
    for j in range(l):
        if(i== 0 or i== l - 1 or j== 0 or j== l - 1):
            print("*",end = ' ')
        else:
            print(" ",end = ' ')
    print()
        

# n=int(input("enter the number"))
# for i in range(0,3):
#     print(" "*(n-i-1),end="")
#     print("*"*(2*i+1),end="")
#     print(" "*(n-i+1))

