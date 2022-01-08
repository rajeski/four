
# Virtual coin toss program (randomly tell the user "Heads" or "Tails")
# Note, the first letter needs to be capitalized, e.g. Heads, not heads.

# Use the random module 
import random

# Keep this code 
test_seed = int(input("Create a seed number: "))
random.seed(test_seed)

# Write your code
randomSide = random.randint(0, 1)
if randomSide == 1:
    print("Heads")
else:
    print("Tails")