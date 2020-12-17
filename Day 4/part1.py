lines = [x.strip() for x in open('input.txt')]
valid = ['byr','iyr','eyr','hgt','hcl','ecl','pid']
valid_passes = 0
current = ''
for line in lines:
    if line == '':
        if all(x in current for x in valid):
            valid_passes += 1
        current = ''
    else:
        current += ' ' + line
print(valid_passes)