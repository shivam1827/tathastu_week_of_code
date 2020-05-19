Player1_Runs=int(input("Enter the runs of player1 in 60 balls: "))
Player2_Runs=int(input("Enter the runs of player2 in 60 balls: "))
Player3_Runs=int(input("Enter the runs of player3 in 60 balls: "))
Strike_Rate1=Player1_Runs*100/60
Strike_Rate2=Player2_Runs*100/60
Strike_Rate3=Player3_Runs*100/60
print("Strike_Rate of player1: ",Strike_Rate1)
print("Strike_Rate of player2: ",Strike_Rate2)
print("Strike_Rate of player3: ",Strike_Rate3)
print("Player 1 runs if he play more 60 balls: ",Player1_Runs*2)
print("Player 2 runs if he play more 60 balls: ",Player2_Runs*2)
print("Player 3 runs if he play more 60 balls: ",Player3_Runs*2)
print("Maximum Number of Six Player1 could Hit: ",Player1_Runs//6)
print("Maximum Number of Six Player2 could Hit: ",Player2_Runs//6)
print("Maximum Number of Six Player3 could Hit: ",Player3_Runs//6)
