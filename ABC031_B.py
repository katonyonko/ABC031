import io
import sys

_INPUT = """\
6
300 400
3
240
350
480
50 80
5
10000
50
81
80
0
"""

sys.stdin = io.StringIO(_INPUT)
case_no=int(input())
for __ in range(case_no):
  L,H=map(int,input().split())
  N=int(input())
  A=[int(input()) for _ in range(N)]
  for i in range(N):
    if A[i]<L: print(L-A[i])
    elif A[i]<=H: print(0)
    else: print(-1)