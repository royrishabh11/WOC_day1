player1=int(input("runs scored: "))
player2=int(input("runs scored: "))
player3=int(input("runs scored: "))

strike_rate_1=player1*100/60 
strike_rate_2=player2*100/60 
strike_rate_3=player3*100/60 

print("strike rate of player1:",strike_rate_1)
print("strike rate of player2:",strike_rate_2)
print("strike rate of player3:",strike_rate_3)

print("runs by player1 if more than 60 balls faced:",player1*2)
print("runs by player2 if more than 60 balls faced:",player2*2)
print("runs by player3 if more than 60 balls faced:",player3*2)

print("maximum no. of sixes by player1: ", player1//6)
print("maximum no. of sixes by player2: ", player2//6)
print("maximum no. of sixes by player3: ", player3//6)