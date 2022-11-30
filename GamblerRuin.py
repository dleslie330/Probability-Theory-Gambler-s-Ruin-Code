import math
import random

# Used to play games where the house has the probability to win indicated by the keys
prime = {(1/2) : 2, (2/3) : 3, (3/5) : 10, (6/11) : 11, (5/8): 16}

def driver():
    fairRuin = []
    
    # plays 100000 fair games, and records how many rounds it takes for the player to become ruined in each game
    # note the player is not ruined every game. Num Games player is not ruined = 100000 - len(fairRuin)
    for i in range(0, 100001):
        temp = game(50, 1000, (1/2))
        if (temp[0]):
            fairRuin.append(temp[1])

    print(len(fairRuin))

    # calculates the average number of rounds it takes the player to be ruined in a fair game with a starting wealth of 50 against 1000
    fairRuinAppAv = average(fairRuin)
    print()
    print(fairRuinAppAv)

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