class circle():
    def cal(s):
        r=float(input("Enter Redius Of Circle = "))
        area=3.14*r*r
        print("Area Of Circle Is : ",area)

    def squre(a):
        sq=float(input("Enter Redius Of Squre = "))
        cal1=pow(sq,2)
        print("Ans = ",cal1)
        
        
obj=circle()
obj.cal()
obj.squre()