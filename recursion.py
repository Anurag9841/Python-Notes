def fact_rec(n):
    if n==0 or n==1:
        return 1
    else:
        return n*fact_rec(n-1)
p=fact_rec(7)
print("The factorial of number is",p)