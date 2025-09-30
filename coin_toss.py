# Name: Justin Coon
# Date: 09-29-2025
# Description: A simple coin flipper program

import random

print("===== Coin Flipper =====")

coin_flip = random.randint(1, 100)

if coin_flip >= 51:
    print("Tails")
    
else:
    print("Heads")
    