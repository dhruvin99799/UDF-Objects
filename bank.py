class bank():
    def account(s):
        ac=int(input("Enter Account Number = "))
        ps=int(input("Enter Your Password = "))
        balance=int(input("Enter your Current Balance = "))
        cpass=int(input("Enter your Confirm Password = "))

        if(ps == cpass):
            print("1 - Saving Account")
            print("2 - Currant Account")
            print("3 - New Account")
            print("4 - Bank Inquiry")
            print("5 - Exit")

            t=int(input("Enter Your Account Type = "))
            if(t<=3):
                print("Enter Your Password = ",ps)
                if(ps==cpass):
                    print("Welcome")
                    print("\n")
                    print("1 = Deposit Ammount")
                    print("2 = Widraw Ammount")
                    print("3 = Display Your Current Balance")
                    print("4 = Exit")
                    ch=(input("Enter Your Type = "))
                    while ch!=4:
                        if(ch==1):
                            d=int(input("Enter Deposite Amount = "))
                            balance = balance + d
                        elif(ch==2):
                            w=int(input("Enter Widraw Ammount = "))
                            balance = balance - w
                        elif(ch==3):
                            print("Your Current Ammount = ",balance)
                        elif(ch==4):
                            print("Press Any One Key For Exit")
                        else:
                            print("Your Choice Is Wrong.")
                            print("Press Any One Key For Exit -->")
                else:
                    print("Your Password Is Wrong.")
            else:
                print("YOUR ACCOUNT HAS BEEN NOT FOUND...!")
        else:
            print("YOUR PASSWORD IS WRONG....!")
obj=bank()
obj.account()
        
	    
# class bank():
#     def acount(s):
#         print("1.Saving Account")
#         print("2.Currant Account")
#         print("3.New Account")
#         print("4.Bank Inquiry")
#         print("5.Exit")
#         choice=int(input("Enter Your Choice = "))
#         if(choice==1):
#             ac=int(input("Enter Account Number = "))
#             ps=int(input("Enter Your Password = "))
#             balance=int(input("Enter your Current Balance = "))
#             cpass=int(input("Enter your Confirm Password = "))
#         elif(choice==2):
#             ac=int(input("Enter Account Number = "))
#             ps=int(input("Enter Your Password = "))
#             balance=int(input("Enter your Current Balance = "))
#             cpass=int(input("Enter your Confirm Password = "))
#         elif(choice==3):
#             ac=int(input("Enter Account Number = "))
#             ps=int(input("Enter Your Password = "))
#             balance=int(input("Enter your Current Balance = "))
#             cpass=int(input("Enter your Confirm Password = "))
#         elif(choice==4):
#             print(ac,ps,balance,cpass)
#         else:
#             print("Exit")


# class bank():
#     def information(s):
#         ac=int(input("Enter Your Account number = "))
#         a=int(input("Enter Your Password = "))
#         n=int(input("Enter Blance = "))
#         b=int(input("Enter your Confirm Password = "))
#         if(a==b):
#             print("1.Saving Account")
#             print("2.Currant Account")
#             t=int(input("Enter Your Account Type = "))
#             if(t<=3):
#                 c=int(input("Enter Your Password = "))
#                 if(a==c):
#                     print("Welcome")
#                     for i in range(ch!=4):   
#                         print("1 = Deposit Amount")
#                         print("2 = Widraw Amount")	   
#                         print("3 = Display Balance")
#                         print("4 = Exit")
#                         ch=int(input("Enter Type = "))
#                         if(ch==1):
#                             d=int(input("Enter Deposite Amount = "))
#                             n = n+d
#                         elif(ch==2):
#                             w=int(input("Enter Widraw Amount = "))
#                             n=n-w
#                         elif(ch==3):
#                             print("Your Amount",n)
#                         elif(ch==4):
#                             print("Exit")
#                         else:
#                             print("Choice is Wrong.")
#                 else:
#                     print("Password Is Wrong.")
#         else:
#             print("Account Has Been Not Found.")

# obj = bank()
# obj.information()
            
            

# # # obj = bank()
# # # obj.acount()


