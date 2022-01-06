# def greatest(a,b,c):
#     if(a>b and a>c):
#         return a
#     elif(b>a and b>c):
#         return b
#     else:
#        return c

# # a=int(input("enter the number 1nd no\n"))
# # b=int(input("enter the number 2nd no\n"))
# # c=int(input("enter the number 3rd no\n"))
# p=greatest(10,12,34)
# print("the greatest number is ",p)

# def cel(c):
#     p=c*1.80+32
#     return p
# d=int(input("enter the temperature in celcius\n"))
# per=cel(d)
# print(f"the farhenite convresion of the given celcius is {per}F")


# def rec(n):
#     if n==0:
#         return 0
#     else:
#         return n+rec(n-1)
# num=int(input("enter the number\n"))
# pr=rec(num)
# print("the sum of number is = ",pr)


# def pattern(n):
#     for i in range(0,n):
#         print("*"*(n-i))
# pr=pattern(3)
# print(pr)


def remove(string,word):
    if(word in string):
        str=string.replace(word,"anurag")
        
        return str.strip()
    else:
        print("no word to strip and remove")

n=input("enter the string\n")
ptr=remove(n,"programmer")
print(ptr)
