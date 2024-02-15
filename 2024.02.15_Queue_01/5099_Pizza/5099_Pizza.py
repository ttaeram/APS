from collections import deque
import sys
sys.stdin = open('5099_input.txt')

T = int(input())

for t in range(1, T + 1):
    N, M = map(int, input())
    cheese = list(map(int, input().split()))

