# with open("poem.txt","r") as f:
#     a=f.read()
#     if("khanna" in a):
#         print("yes the word twinkle is present\n")
#     else:
#         print("the word is not present\n")
# print(a)
# f=open("poem.txt","r")
# data=f.read()
# if "twinkle" in data:
#     print("yes the word twinkle is present")
# else:
#     print("sorry")
# f.close()
# def fun(n):
#     return n
# b=int(input("enter the number\n"))
# data=fun(b)
# with open("score.txt","r") as f:
#     a=f.read()
# if a=='':
#      with open("score.txt","w") as f:
#         f.write(str(data))
         
# elif int(a)<data:
#     with open("score.txt","w") as f:
#         f.write(str(data))


# for i in range(2,21):
#     with open(f"Multiplication of {i}.txt","w") as f:
#         for j in range(1,11):
#             f.write(f"{i} X {j} = {i*j}\n")


# with open("censored.txt") as f:
#     content=f.read()
# if "donkey" or "monkey" in f:
#     content=content.replace("donkey"or"monkey","######")
#     content=content.replace("monkey","$$$$$$")
# with open("censored.txt","w") as f:
#     f.write(content)

# content=True
# i=1
# with open("censored.txt","r") as f:
#     while content:
#      content=f.readline()
#      if "python" in content.lower():
        
#         print(f"yes the python is present in {i}")
#         print(content)
#      i+=1


# with open("censored.txt") as f:
#     content=f.read()
#     with open("this.txt","w") as a:
#         a.write(content)

with open("this.txt","r") as f:
    content=f.read()
    print (content)
    with open("this.txt","w") as f:
        f.write("")