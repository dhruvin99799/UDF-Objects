class criket():
    def Match(s):
        player = dict()
        n=int(input("Enter Number Of Player= "))
        for i in range(n):
            name=(input("Enter Player Name = "))
            runs=[]
            n1=int(input("Enter Mathes Of Player= "))
            for i in range(n1):
                run = int(input("Enter Runs = "))
                runs.append(run)
            player[name] = runs
            t_runs=sum(runs)
            print("Total Runs = ",t_runs)
            avrage=t_runs/n1
            print("Player Avrage For Each Match = ",avrage)
            print("MinMum Runs Of All Matches = ",min(runs))
            print("Maximum Runs Of All Matches = ",max(runs))
        
obj = criket()
obj.Match()


