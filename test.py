import re

line = ".......738...*....222......................706.......*..825.............474%...........*...........*.405.........779..............542...405."
pattern = re.compile(r'\d+')

matches = [match.group() for match in pattern.finditer(line)]
print(matches)