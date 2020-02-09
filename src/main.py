import os
import utility,init

def printGameOptions(carrom):

    counter = 1

    for option in carrom.getGameOptions():
        print("{0}. {1}\n".format(counter,option) )
        counter+=1 

def playGame(carrom):
    
    message = "Choose an option from below\n"

    while True:

        for player in range(len(carrom.players)):

            while True:

                print( "{0}: {1}".format(carrom.players[player].name,message) )
                printGameOptions(carrom)

                try:

                    option = int(input())

                except KeyboardInterrupt:
                    exit("Exiting......")
                
                except EOFError:
                     exit("Exiting......")
                
                except:
                    print("Please enter a valid input \n")
                    continue

                if( option == 1 ):
                    if( not carrom.strike(player) ):
                        print("No more black coins available on board\n")
                        continue
                    break
                elif( option == 2 ):
                    if( not carrom.multiStrike(player) ):
                        print("Less than 2 black coins available on board\n")
                        continue
                    break
                elif( option == 3 ):
                    if ( not carrom.redStrike(player) ):
                        print("No more red coins available on board\n")
                        continue
                    break
                elif(option == 4 ):
                    carrom.strikerStrike(player)
                    break
                elif( option == 5 ):
                    coin_type = input("Which coin is defuncted? red or black?\n").lower()
                    if(coin_type == "red" or coin_type == "black"):
                        if( not carrom.defunct(player,coin_type) ):
                            print("No {0} coins available".format(coin_type))
                            continue
                        break
                    else:
                        print("Coin type should be red or black\n")
                        continue
                elif( option == 6 ):
                    carrom.noneStrike(player)
                    break
            
            status,winner = utility.checkResult(carrom)
            if( status ):
                if(winner ==  None ):
                    print("All coins exhausted !! Game Drawn !!")
                else:
                    print( "{0} won the game\n".format(winner) )

                return

if __name__ == "__main__":

    os.environ["PYTHONPATH"] = os.getcwd()
    carrom = init.initializeGame()
    playGame(carrom)