def fac():
    i=int(input("Enter Number = "))
    fact=1
    while(i>0):
        fact=fact*i
        i=i-1
    print("Factorial = ",fact)
print(fac())