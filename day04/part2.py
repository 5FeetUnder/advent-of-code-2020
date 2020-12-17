import re

lines = [x.strip() for x in open('input.txt')]
valid = ['byr','iyr','eyr','hgt','hcl','ecl','pid']

def validate_pass(passport: str):
    {
        'byr': re.match(r"byr:([12][90][2-9]\d)\s{1}",passport),
        'iyr': re.match(r"iyr:(20[12]\d)\s{1}",passport),
        'eyr': re.match(r"eyr:(20[23]\d)\s{1}",passport),
        'hgt': re.match(r"hgt:(\d{3})(?=cm)|(\d{2})(?=in)\s{1}",passport),
        'hcl': re.match(r"hcl:#([0-9a-f])\s{1}",passport),
        'ecl': re.match(r"ecl:(amb|blu|brn|gry|grn|hzl|oth)\s{1}",passport),
        'pid': re.match(r"hcl:#([0-9a-f])\s{1}",passport)
    }

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