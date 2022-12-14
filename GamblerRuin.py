import math
import random

# Used to play games where the house has the probability to win indicated by the keys
prime = {(1/2) : 2, (3/5) : 10, (6/11) : 11}

def driver():
    # Ruin= []
    
    # # plays 100000 fair games, and records how many rounds it takes for the player to become ruined in each game
    # # note the player is not ruined every game. Num Games player is not ruined = 100000 - len(Ruin)
    # for i in range(0, 100000):
    #     temp = game(50, 1000, (1/2))
    #     if (temp[0]):
    #         Ruin.append(temp[1])

    # proboutcome = len(Ruin) / 100000
    # expected = 1 - (50 / 1050)

    # # calculates the average number of rounds it takes the player to be ruined in a fair game with a starting wealth of 50 against 1000
    # RuinAppAv = average(Ruin)
    # print()
    # print("Average rounds to be ruined (fair -  50 / 1000): ", RuinAppAv)
    # print("\nsimulated: ", proboutcome, "\nexpected: ", expected)

    # Ruin= []
    
    # # plays 100000 fair games, and records how many rounds it takes for the player to become ruined in each game
    # # note the player is not ruined every game. Num Games player is not ruined = 100000 - len(Ruin)
    # for i in range(0, 100000):
    #     temp = game(20, 10000, (1/2))
    #     if (temp[0]):
    #         Ruin.append(temp[1])

    # proboutcome = len(Ruin) / 100000
    # expected = 1 - (20 / 10020)

    # # calculates the average number of rounds it takes the player to be ruined in a fair game with a starting wealth of 50 against 1000
    # RuinAppAv = average(Ruin)
    # print()
    # print("Average rounds to be ruined (fair - 20/10000): ", RuinAppAv)
    # print("\nsimulated: ", proboutcome, "\nexpected: ", expected)

    # Ruin= []
    
    # # plays 100000 fair games, and records how many rounds it takes for the player to become ruined in each game
    # # note the player is not ruined every game. Num Games player is not ruined = 100000 - len(Ruin)
    # for i in range(0, 100000):
    #     temp = game(500, 1000, (1/2))
    #     if (temp[0]):
    #         Ruin.append(temp[1])

    # proboutcome = len(Ruin) / 100000
    # expected = 1 - (500 / 1500)

    # # calculates the average number of rounds it takes the player to be ruined in a fair game with a starting wealth of 50 against 1000
    # RuinAppAv = average(Ruin)
    # print()
    # print("Average rounds to be ruined (fair - 500/1000): ", RuinAppAv)
    # print("\nsimulated: ", proboutcome, "\nexpected: ", expected)

    # Ruin= []
    
    # # plays 100000 unfair games, and records how many rounds it takes for the player to become ruined in each game
    # # note the player is not ruined every game. Num Games player is not ruined = 100000 - len(Ruin)
    # for i in range(0, 100000):
    #     temp = game(50, 1000, (3/5))
    #     if (temp[0]):
    #         Ruin.append(temp[1])

    # proboutcome = len(Ruin) / 100000
    # expected = 1 - (((1 - pow((3/5)/(2/5), 50))) / (1 - pow((3/5)/(2/5), 1050)))

    # # calculates the average number of rounds it takes the player to be ruined in a fair game with a starting wealth of 50 against 1000
    # RuinAppAv = average(Ruin)
    # print()
    # print("Average rounds to be ruined (3/5 - 50/1000): ", RuinAppAv)
    # print("\nsimulated: ", proboutcome, "\nexpected: ", expected)

    # Ruin= []

    # # plays 100000 unfair games, and records how many rounds it takes for the player to become ruined in each game
    # # note the player is not ruined every game. Num Games player is not ruined = 100000 - len(Ruin)
    # for i in range(0, 100000):
    #     temp = game(500, 1000, (3/5))
    #     if (temp[0]):
    #         Ruin.append(temp[1])

    # proboutcome = len(Ruin) / 100000
    # expected = 1 - (((1 - pow((3/5)/(2/5), 500))) / (1 - pow((3/5)/(2/5), 1500)))

    # # calculates the average number of rounds it takes the player to be ruined in a fair game with a starting wealth of 50 against 1000
    # RuinAppAv = average(Ruin)
    # print()
    # print("Average rounds to be ruined (3/5 - 500/1000): ", RuinAppAv)
    # print("\nsimulated: ", proboutcome, "\nexpected: ", expected)

    # Ruin= []
    
    # # plays 100000 unfair games, and records how many rounds it takes for the player to become ruined in each game
    # # note the player is not ruined every game. Num Games player is not ruined = 100000 - len(Ruin)
    # for i in range(0, 100000):
    #     temp = game(50, 1000, (6/11))
    #     if (temp[0]):
    #         Ruin.append(temp[1])

    # proboutcome = len(Ruin) / 100000
    # expected = 1 - (((1 - pow((6/11)/(5/11), 50))) / (1 - pow((6/11)/(5/11), 1050)))

    # # calculates the average number of rounds it takes the player to be ruined in a fair game with a starting wealth of 50 against 1000
    # RuinAppAv = average(Ruin)
    # print()
    # print("Average rounds to be ruined (6/11 - 50/1000): ", RuinAppAv)
    # print("\nsimulated: ", proboutcome, "\nexpected: ", expected)

    # Ruin= []
    
    # # plays 100000 unfair games, and records how many rounds it takes for the player to become ruined in each game
    # # note the player is not ruined every game. Num Games player is not ruined = 100000 - len(Ruin)
    # for i in range(0, 100000):
    #     temp = game(500, 1000, (6/11))
    #     if (temp[0]):
    #         Ruin.append(temp[1])

    # proboutcome = len(Ruin) / 100000
    # expected = 1 - (((1 - pow((6/11)/(5/11), 500))) / (1 - pow((6/11)/(5/11), 1500)))

    # # calculates the average number of rounds it takes the player to be ruined in a fair game with a starting wealth of 50 against 1000
    # RuinAppAv = average(Ruin)
    # print()
    # print("Average rounds to be ruined (6/11 - 500/1000): ", RuinAppAv)
    # print("\nsimulated: ", proboutcome, "\nexpected: ", expected)

    Ruin= []
    
    # plays 100000 unfair games, and records how many rounds it takes for the player to become ruined in each game
    # note the player is not ruined every game. Num Games player is not ruined = 100000 - len(Ruin)
    for i in range(0, 100000):
        temp = game(950, 1000, (6/11))
        if (temp[0]):
            Ruin.append(temp[1])

    proboutcome = len(Ruin) / 100000
    expected = 1 - (((1 - pow((6/11)/(5/11), 950))) / (1 - pow((6/11)/(5/11), 1950)))

    # calculates the average number of rounds it takes the player to be ruined in a fair game with a starting wealth of 50 against 1000
    RuinAppAv = average(Ruin)
    print()
    print("Average rounds to be ruined (6/11 - 950/1000): ", RuinAppAv)
    print("\nsimulated: ", proboutcome, "\nexpected: ", expected)

    return None

# This method is what plays each game of coin flip
def game(pw, cw, p):
    rng = prime[p]
    count = 0

    # each loop is one round and it returns weather or not the player was ruined and the number of rounds the game took
    while (pw > 0 and cw > 0):
        if (flipcoin(rng) == 0):
            pw = pw + 5
            cw = cw - 5
        else:
            pw = pw - 5
            cw = cw + 5
        count = count + 1

    return [(pw <= 0), count]

# Generates a random number from the range determined by the probility the house wins, checks if it is prime, and if it is prime, the player wins
def flipcoin(rng):
    if (isprime(random.randint(1, rng))):
        return 0

    return 1

# This method checks if a number is prime. Used in determining the winner of a round
def isprime(n):
    if (n == 1):
        return False
    for i in range(2, int(math.sqrt(n)) + 1):
        if (n % i == 0):
            return False
    return True

# this calculates the average number of rounds it takes to ruin a player in a real random application
def average(arr):
    return int(sum(arr) / len(arr))

# This simply runs the code
driver()