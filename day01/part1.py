items = [int(x.strip()) for x in open("input.txt")]

done = False

for n in items:
    for m in items:
        if n + m == 2020 and n != m:
            print(n * m)
            done = True
            break
    if done:
        break
