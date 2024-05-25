#else-suit

playerlist = ["rohit","shubhman","virat","iyer","dhoni"]
playername=input("enter name of player :")

for player in playerlist:
    
    if player == playername:
        print(playername,"present in list.")
        break 
else:                                                            # for-else
    print(playername,"is not present in the list.")
