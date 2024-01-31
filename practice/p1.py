import sys

sys.stdin = open('input.txt')

# 33
# => 홀수면 1, 짝수면 0
N = int(input())

result = 1 if N % 2 else 0
print(f'{result}')

arr2 = [list(map(int, input().split())) for _ in range(N)]  # [표현식, 표현식, list(map(int, input()))]