import re

lines = [x.strip() for x in open('input.txt')]
valid = ['byr','iyr','eyr','hgt','hcl','ecl','pid']

def validate_pass(passport: str):
    {
        byr: re.match(r"byr:([12][90][2-9]\d)",passport).group(1),
        iyr: re.match(r"iyr:(20[12]\d)",passport).group(1),
        eyr: re.match(r"eyr:(20[23]\d)",passport).group(1),
        hgt: re.match(r"hgt:(\d{3})(?=cm)|(\d{2})(?=in)",passport).group(1),
        hcl: re.match(r"hcl:(\w+)",passport).group(1),
        ecl: re.match(r"ecl:(amb|blu|brn|gry|grn|hzl|oth)",passport),

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