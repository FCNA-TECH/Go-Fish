# Designed by Ferdinand
# Created on 25/01/2022 and was finished on 13/02/2022

import random
import time
from random import randint
from time import sleep

def Authenticating(player):
    with open('Authorised_Players.txt', 'r') as player_vault:
        name = player_vault.read().splitlines()  
        if player.upper() in name:                    
            return "let them through"
        else:
            return "IMPOSTER"

def Registration(player):
    with open('Authorised_Players.txt', 'a') as player_vault:   
        player_vault.write("\n" + player.upper())
    with open('Authorised_Players.txt', 'r') as player_vault:
        name = player_vault.read().splitlines()
        if player.upper() in name:                                    
            return "success"
        else:
            return "failure"

def champion(player,score):
    try:
        with open("Leaderboard.txt", "x") as champfile:    
            champfile.write(player + ":" + str(score))
        time.sleep(1)
    except:
        with open("Leaderboard.txt", "a") as champfile:
            champfile.write("\n" + player + ":" + str(score))
        time.sleep(1)

def random_dice_engine():
    dice_roll = random.randint(1,6)     
    return dice_roll

overallWinnerString = """
********* GAME WINNER **********
   The winner of this game is:
            {User}
    with {Score} total points! 
********************************
"""

roundWinnerString = """
**************************************
     The winner of this round is:
       {User} with a score of                 
        {Score}, congratulations!
**************************************
"""

ascii_text = "║ ═ ╔ ╗ ╝ ╚ "

menu =  """
╔═════════════════════════════════════════════════════════════╗
║                                                             ║
║                          Go-Fish!                           ║
║                                                             ║
║     1. Start Game...................(Who will Win?)   <     ║  
║     2. Leaderboard...............(Local not Global)         ║
║     3. New User.................(username specific)         ║
║     4. Settings...............(configure the setup)         ║
║                                                             ║
║                                                             ║
║                       Created in 2022                       ║
╚═════════════════════════════════════════════════════════════╝     
"""

rules = """
• The points rolled on each player’s dice are added to their score.
• If the total is an even number, an additional 10 points are added to their score.
• If the total is an odd number, 5 points are subtracted from their score.
• If they roll a double, they get to roll one extra die and get the number of points rolled added to their score.
• The score of a player cannot go below 0 at any point.
• The person with the highest score at the end of the rounds wins. (default number of rounds is 5)
• If both players have the same score at the end of the 5 rounds, they each roll 1 die and whoever gets the highest score wins (this repeats until someone wins).
"""

autoconfig = """
slowdown:1
rounds:5
plus points:10
minus points:5
co-author:
the numbers can be altered to your hearts content but please do not change the order the words
"""


global slowdown
global rounds
global pluspoints
global minuspoints
global coauthor

global nameregistering     
nameregistering = False

global lauchgame         
launchgame = False

try:
    with open("Configuration.txt", "x") as checkconfigfile:    
        checkconfigfile.write(autoconfig)
    with open("Configuration.txt", "r") as checkconfigfile:
        setup = checkconfigfile.read().splitlines()
        almost_slowdown = setup[1]
        slowdown = almost_slowdown.lstrip("slowdown:")   
        slowdown = int(slowdown)

            
        almost_rounds = setup[2]
        rounds = almost_rounds.lstrip("rounds:")   
        rounds = int(rounds)
       

        almost_pluspoints = setup[3]
        pluspoints = almost_pluspoints.lstrip("plus points:")   
        pluspoints = int(pluspoints)


        almost_minuspoints = setup[4]
        minuspoints = almost_minuspoints.lstrip("minus points:")   
        minuspoints = int(minuspoints)

        almost_coauthor = setup[5]                                
        coauthor = almost_coauthor.lstrip("co-author:")
    time.sleep(1)
except:
    with open("Configuration.txt", "r") as checkconfigfile:
        setup = checkconfigfile.read().splitlines()
        almost_slowdown = setup[1]
        slowdown = almost_slowdown.lstrip("slowdown:")   
        slowdown = int(slowdown)

            
        almost_rounds = setup[2]
        rounds = almost_rounds.lstrip("rounds:")   
        rounds = int(rounds)
       

        almost_pluspoints = setup[3]
        pluspoints = almost_pluspoints.lstrip("plus points:")   
        pluspoints = int(pluspoints)


        almost_minuspoints = setup[4]
        minuspoints = almost_minuspoints.lstrip("minus points:")   
        minuspoints = int(minuspoints)

        almost_coauthor = setup[5]                                
        coauthor = almost_coauthor.lstrip("co-author:")
    time.sleep(1)

time.sleep(slowdown+1)
print("")
print("")
print("Welcome to Go-Fish! -(dice game) by Ferdinand " + coauthor)
print("")
time.sleep(random.randint(slowdown+2,slowdown+4))
print("The rules are simple: ")
time.sleep(slowdown)
print(rules)
print("")
time.sleep(slowdown+2)
print("let the games begin...")
time.sleep(random.randint(slowdown+1,slowdown+2))



try:
    with open("Authorised_Players.txt", "x") as checkfile:    
        checkfile.write("Ferdinand was here ;) ")
    time.sleep(1)
except:
    with open("Authorised_Players.txt", "a") as checkfile:
        checkfile.write("\n" + "Ferdinand was here ;) ")
    time.sleep(1)


while True: 
    print("")
    print(menu)
    options = input("please select from the menu above: ")

    if options == "1":
        attemptplayer1 = 0
        attemptplayer2 = 0
        while True:
            print("")
            if attemptplayer1 == 4:
                time.sleep(slowdown)
                print("please go to section 3 on the menu to register as a new user ")
                time.sleep(slowdown+2)
                nameregistering = True
                break
            player1 = str(input("Player 1 enter your username: "))
            time.sleep(slowdown)
            print("Initiating verification... ")
            lock = Authenticating(player1)  
            if lock == "let them through":
                time.sleep(random.randint(slowdown,slowdown+2))
                print("Authentication succesful ")
                time.sleep(slowdown)
                break
            elif lock == "IMPOSTER":
                time.sleep(random.randint(slowdown,slowdown+2))
                print("Authentication failed")
                time.sleep(slowdown)
                attemptplayer1 += 1

        while True:
            print("")
            if attemptplayer2 == 4:
                time.sleep(slowdown)
                print("please go to section 3 on the menu to register as a new user ")
                time.sleep(slowdown+2)
                nameregistering = True
                break
            if attemptplayer1 == 4:
                break
            player2 = str(input("Player 2 enter your username: "))
            time.sleep(slowdown)
            print("Initiating verification... ")
            lock = Authenticating(player2)
            if lock == "let them through":
                time.sleep(random.randint(slowdown,slowdown+2))
                print("Authentication succesful ")
                time.sleep(slowdown)
                break
            elif lock == "IMPOSTER":
                time.sleep(random.randint(slowdown,slowdown+2))
                print("Authentication failed")
                time.sleep(slowdown)
                attemptplayer2 += 1            


        roundnumber = 0
        player1_score = 10
        player2_score = 10
        player1_duplicate = ["this string is just a filler"]
        player2_duplicate = ["this string is just a filler"]
        tiebreaker = False
        launchgame = False
        while True:
            if nameregistering == True:  
                nameregistering = False     
                break
            
            if launchgame == False:
                print("")
                print("launching game...")
                print("")
                print("")
                time.sleep(random.randint(slowdown,slowdown+2))
                launchgame = True       

            if player1_score <= 0:
                time.sleep(slowdown+2)
                print("")
                print("GAME OVER!")
                time.sleep(slowdown)
                print("[" + player1 + "] has lost the game as their score has reached 0 ")
                time.sleep(slowdown+3)
                print("")
                playerlost = "player1"
                print(overallWinnerString.format(User = player2, Score = player2_score))
                champion(player2,player2_score)
                time.sleep(slowdown)
                break

            if player2_score <= 0:
                time.sleep(slowdown+2)
                print("")
                print("GAME OVER!")
                time.sleep(slowdown)
                print("[" + player2 + "] has lost the game as their score has reached 0 ")
                time.sleep(slowdown+3)
                print("")
                playerlost = "player2"
                print(overallWinnerString.format(User = player1, Score = player1_score))
                champion(player1,player1_score)
                time.sleep(slowdown)
                break
                

            if roundnumber == rounds and tiebreaker == False:
                if player1_score > player2_score:
                    print("")
                    time.sleep(slowdown)
                    print("Max number of rounds " +"(" + str(rounds) + ")" + " has been reached")
                    time.sleep(slowdown+3)
                    print(overallWinnerString.format(User = player1, Score = player1_score))
                    champion(player1,player1_score)
                    time.sleep(slowdown)
                    break
                elif player2_score > player1_score:
                    print("")
                    time.sleep(slowdown+3)
                    print(overallWinnerString.format(User = player2, Score = player2_score))
                    champion(player2,player2_score)
                    time.sleep(slowdown)
                    break
                else:
                    print("")
                    time.sleep(slowdown+3)
                    print("TIEBREAKER!")
                    tiebreaker = True
                    
                                                    
            roundnumber = roundnumber + 1

            input("[" + player1 + "] Roll the dice... (press ↩ to continue) ")
            player1roll = random_dice_engine()
            print("[" + player1 + "] You rolled: "+ str(player1roll))
            print("")

            input("[" + player2 + "] Roll the dice... (press ↩ to continue) ")
            player2roll = random_dice_engine()
            print("[" + player2 + "] You rolled: "+ str(player2roll))
            print("")

            if player1roll == player1_duplicate[-1]: 
                print("[" + player1 + "] You have rolled a double! ")
                time.sleep(slowdown)
                player1rollextra = random_dice_engine()
                print("[" + player1 + "] Your extra roll is: "+ str(player1rollextra))    
                print("")
                player1_score += (player1roll + player1rollextra)
            else:
                player1_duplicate.append(player1roll)                   
                if player1roll %2 == 0:
                    player1_score += 10
                else:
                    player1_score -= 5


            if player2roll == player2_duplicate[-1]: 
                print("[" + player2 + "] You have rolled a double! ")
                time.sleep(slowdown)
                player2rollextra = random_dice_engine()
                print("[" + player2 + "] Your extra roll is: "+ str(player2rollextra))   
                print("")
                player2_score += (player2roll + player2rollextra)
            else:
                player2_duplicate.append(player2roll)                    
                if player2roll %2 == 0:
                    player2_score += 10
                else:
                    player2_score -= 5


            time.sleep(1)
            if player1_score > player2_score:
                print(roundWinnerString.format(User = player1, Score = player1_score))
            elif player2_score > player1_score:
                print(roundWinnerString.format(User = player2, Score = player2_score))
            else:
                print("")
                time.sleep(slowdown+1)
                print("Its a draw!")
                time.sleep(slowdown)
                print("who will win...")
                print("")



    if options == "2":
        try:
            with open("Leaderboard.txt", "x") as champfile:
                champfile.write("test" + ":" + "123456789")
                print("")
                time.sleep(slowdown)
                print("leaderboard was created")
            time.sleep(1)
        except:
            with open("Leaderboard.txt", "r") as champfile:    
                leaderboard = champfile.read().splitlines()
                time.sleep(slowdown)
                print("")
                print("")
                for f in leaderboard:
                    print(f)
            time.sleep(slowdown+2)

            
    if options == "3":
        while True:
            Attemptregistration = 1
            print("")
            player = str(input("Please enter the name you want to store: "))
            check = Registration(player)
            if check == "success":
                time.sleep(random.randint(slowdown,slowdown+2))
                print("Registration succesful ")
                time.sleep(slowdown+1)
                print("Welcome to the game "+ player)
                time.sleep(slowdown)
                break
            elif check == "failure":
                time.sleep(random.randint(slowdown,slowdown+2))
                print("Registration failed ")
                time.sleep(slowdown)
                print("Attempt number - " + str(Attemptregistration))
                Attemptregistration += 1

                
    if options == "4":
        print("")
        print("")
        time.sleep(slowdown+3)
        print("please go to the 'configuration.txt' file saved in the same folder as this program to access the settings")
        time.sleep(slowdown+3)      


# Designed by Ferdinand
