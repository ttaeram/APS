import sys
sys.stdin = open('4880_input.txt')

T = int(input())

# def RPS(arr, N):


for t in range(1, T + 1):
    N = int(input())
    arr = list(map(int, input().split()))