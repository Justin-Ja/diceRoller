import random;
from typing import List

random.seed()

#TODO: overhaul into a class

def generateNumbers(diceSides: int, numberOfRolls: int) -> List[int]:
    nums = []

    try:
        if diceSides <= 0:
            raise ValueError("diceSides must be a positive integer")
        
        #Use underscore to indicate that loop var is unused/not needed
        for _ in range(numberOfRolls):
            nums.append(random.randint(1, diceSides))

    except ValueError as e:
        print(f"ERROR: {e}")
        nums = None
    
    return nums

def calcTotalRoll(nums: List[int]) -> int:
    total = int(0)

    for num in nums:
        total = total + num

    return total


if __name__ == "__main__":
    #Execute tests here

    ans = int(0)
    test = int(0)
    testDice = [4,6,8,10,12,20,100]
    failDice = -2

    for dice in testDice:
        ans = generateNumbers(dice, 3)
        print(ans)
        ans = calcTotalRoll(ans)
        print(ans)
    
    test = generateNumbers(failDice, 3)
    print(test)
