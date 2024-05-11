class time():
    def test(s):
        sec = int((input("Enter Time In Second = ")))
        h = int(sec/3600)
        sec = sec%3600
        m = int(sec/60)
        s = int(sec%60)
        print("HH=MM=SS",h,":",m,":",s)
obj = time()
obj.test()

# class second():
#     def test(s):
#         n=(input("Input Second = "))
#         sec=m/60
#         h=(sec/3600)
#         m=(sec-(3600*h))/60
#         s=(sec-(3600*h)-m*60)
#         print("h:",h ,"m:",m,"s",s)
# obj = second()
# obj.test()



# class seecond():
#     def time(s):
#         n=int(input("Inpur Seconds = "))
#         hour = s//3600
#         sec = s%60
        
#         s=s%3600
#         minute = s//60
#         print(":",":",hour,minute,sec)
# obj = seecond()
# obj.time()