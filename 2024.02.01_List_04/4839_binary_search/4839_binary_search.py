import sys
sys.stdin = open('4839_input.txt')

T = int(input())

def binarysearch(a, N, key):
    start = 0
    end = N -1
    cnt = 0
    while start <= end:
        middle = (start + end) // 2
        cnt += 1
        if a[middle] == key:
            return cnt
        elif a[middle] > key:
            end = middle - 1
        else:
            start = middle + 1
    return False

for t in range(1, T + 1):
    total, A_search, B_search = map(int, input().split())

    book = []
    page = 0
    for p in range(1, total + 1):
        page += 1
        book.append(page)

    A_score = binarysearch(book, total, A_search)
    B_score = binarysearch(book, total, B_search)

    if A_score < B_score:
        print(f'#{t} A')
    elif A_score == B_score:
        print(f'#{t} 0')
    elif A_score > B_score:
        print(f'#{t} B')