input = open('input.txt').readline().split(',')

numbers = {int(n):(i,-1) for i,n in enumerate(input)}

if 0 not in numbers:
    numbers[0] = (-1,-1)
turn = len(input)
last = int(input[-1])
while turn < 30000000:
    if numbers[last][1] == -1:
        last = 0
        numbers[0] = (turn, numbers[0][0])
    else:
        last = numbers[last][0] - numbers[last][1]
        numbers[last] = (turn,numbers[last][0]) if last in numbers else (turn,-1)
    turn += 1

print(last)