import sys
import re

sys.stdin = open("input.txt")

N = sys.stdin.readline()
numbers = list(map(int, re.findall(r'\d+', sys.stdin.readline())))

print(sum(numbers))
