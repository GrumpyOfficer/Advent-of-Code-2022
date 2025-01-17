from aocd import get_data

USE_TEST_INPUT = False
if USE_TEST_INPUT: input = open("2024/Day 2/tinput.txt", 'r').read().strip()
else: input = get_data(day=2, year=2024)
endValue = 0

reports = [list(map(int, x.split())) for x in input.split('\n')]

for report in reports:
    isDecreasing = report[0] - report[1] > 0
    safes = 0
    for i in range(len(report[:-1])):
        difference = report[i] - report[i+1]
        if (difference > 0) == isDecreasing and abs(difference) in range(1,4): #if safe
            safes += 1
        else: break
    if safes == len(report)-1:
        endValue += 1

print(endValue)
