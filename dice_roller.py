import random
dice_rolls =2
dice_sum=0
for i in range(0,dice_rolls):
    roller=random.randint(1,6)
    dice_sum+=roller
    print('You rolled a',roller)
print('You have rolled a total of',dice_sum)
def main():
  roller =random.randint(1,6)
  print('You rolled a',roller)
  

if __name__== "__main__":
  main()