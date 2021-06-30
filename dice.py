import random
import time
winner = 0

diceone = 0
dicetwo = 0

while winner != 12:
    diceone = random.randint(5, 6)
    dicetwo = random.randint(5, 6)
    totalroll = dicetwo + diceone
    print(totalroll)
    time.sleep(1)
    if totalroll == 12:
        print("You win.")
        winner = 12