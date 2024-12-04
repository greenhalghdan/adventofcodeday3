import re
from nis import match
from sys import flags

results = []
with open('sampledata.txt') as data:
    for row in data:
        x = re.findall(r"mul\([0-9]{1,3},[0-9]{1,3}\)",row)
        # print(x)
        for i in x:
            # b = i.str()
            b = i.strip('mul')
            c =  b.strip("'(")
            d = c.strip(")'")
            s = d.split(',')
            # print(type(s))
            # print(s[0])
            # print(s[1])
            results.append(int(s[0])*int(s[1]))
            # input()
print(f'The answer is {sum(results)}')

# not my code: but answer question 2 by first looking for the mul(x,y), do{} and don't()
# This is then added to a list
# I then go through the list in a for loop evaluating each object first checking if it is a do this turns multiplication on then if that not true it checks if its a don't and if that true it turns multiplication of and if thats not true i check if multiplication is on or off and if it is on a multiple what i have found


pattern = r"mul\(\d+,\d+\)|do\(\)|don't\(\)"
matches = re.findall(pattern,open("sampledata.txt").read())
res = 0
flag = True
for match in matches:
    if match == "do()":
        flag = True
    elif match == "don't()":
        flag= False
    else:
        if flag:
            x,y = map(int, match[4:-1].split(","))
            res += x * y
print(res)
