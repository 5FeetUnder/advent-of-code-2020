items = [int(x.strip()) for x in open("input.txt")]

done = False

for n in items:
    for m in items:
        for o in items:
            if n + m + o == 2020 and n != m and n != o and m != o:
                print(n * m * o)
                done = True
                break
        if done:
            break
    if done:
        break
