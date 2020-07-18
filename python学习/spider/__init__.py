import random
import re

file = open('User-Agent.txt', 'r')
lines = file.read().split(',\n')

# print(lines[36])
# print(len(lines))
# print(random.randint(0, 37))

n = re.search(r'\d+', '/aa/12344.html')
print(n)

