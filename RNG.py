import random;
from typing import List

random.seed()

#TODO: add some form of type checking for the entire file (plus error handling)

def generateNumbers(diceSides, numberOfRolls):
    nums = []

    for roll in range(numberOfRolls):
        nums.append(random.randint(1, diceSides))
    
    return nums

def calcTotalRoll(nums: List[int]) -> int:
    total = int(0)

    for num in nums:
        total = total + num

    return total



if __name__ == "__main__":
    #Execute early tests here
    ans = int(0)
    testDice = [4,6,8,10,12,20,100]
    
    for dice in testDice:
        ans = generateNumbers(dice, 3)
        print(ans)
        ans = calcTotalRoll(ans)
        print(ans)
