stu=dict()
def res():
    n=int(input("Student Number = "))
    for i in range(n):
        name=(input("Enter Students Name = "))
        marks=[]
        for i in range(5):
            mark = int(input("Enter Marks = "))
            marks.append(mark)
        stu[name] = marks
        s_mark=sum(marks)
        print("Total = ",s_mark)
        per=s_mark/5
        print("Per",per)
        print("Min = ",min(marks))
        print("Max = ",max(marks))
        if(per>90):
            print("Grade = A1")
        elif(per>80):
            print("Grade = A2")
        elif(per>70):
            print("Grade = B")
        elif(per>60):
            print("Grade = C")
        elif(per>50):
            print("Grade = D")
        else:
            print("Grade = E1")

        if(per>35):
            print("Result = PASS")
        else:
            print("Result = FAIL")

        
print(res())
print("Students Is = ",stu)