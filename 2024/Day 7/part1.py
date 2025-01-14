import time
from aocd import get_data

USE_TEST_INPUT = False
if USE_TEST_INPUT: input = open("2024/Day 7/tinput.txt", 'r').read().strip()
else: input = get_data(day=7, year=2024)
endValue = 0

start = time.time()

equations = [x.split(':') for x in input.split('\n')]
equations = [[int(x[0]), x[1].split()] for x in equations]

for eqation in equations:
    result = eqation[0]
    nums = list(map(int, eqation[1]))
    
    maxOptions = pow(2, len(nums)-1)
    for i in range(0, maxOptions):
        eqationResult = nums[0]
        for j in range(len(nums)-1):
            if i >> j & 1: eqationResult += nums[j+1]
            else: eqationResult *= nums[j+1]
        if eqationResult == result:
            endValue += result
            break

end = time.time()
print(end - start)

print(endValue)