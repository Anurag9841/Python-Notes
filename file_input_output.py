#open()---> this is built in function it takes two parameter filename and mode
a=open("sample.txt","r")
data=a.read(50)
print(data)
a.close()