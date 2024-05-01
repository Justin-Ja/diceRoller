import random;
from typing import List

class RandomNumberGenerator:

    def __init__(self):
        random.seed()

    #Generates a list of numbers size numberOfRolls within a bounded range, from 1 to diceSides
    def generateNumbers(self, diceSides: int, numberOfRolls: int) -> List[int]:
        nums = []

        try:
            if diceSides <= 0:
                raise ValueError("diceSides must be a positive integer")
            
            for _ in range(numberOfRolls):
                nums.append(random.randint(1, diceSides))

        except ValueError as e:
            print(f"ERROR: {e}")
            nums = None
        
        return nums

    #Sums all values in a list
    def calcTotalRoll(self, nums: List[int]) -> int:
        total = int(0)

        for num in nums:
            total = total + num

        return total


if __name__ == "__main__":
    #Execute tests here
    print("Running tests...\n")
    RNG = RandomNumberGenerator()

    ans = int(0)
    test = int(0)
    testDice = [4,6,8,10,12,20,100]
    failDice = -2

    for dice in testDice:
        ans = RNG.generateNumbers(dice, 3)
        print(ans)
        ans = RNG.calcTotalRoll(ans)
        print(ans)
    
    test = RNG.generateNumbers(failDice, 3)
    print(test)
