import io
import sys

_INPUT = """\
6
31 87
101 65
3 3
"""

sys.stdin = io.StringIO(_INPUT)
case_no=int(input())
for __ in range(case_no):
  A,D=map(int,input().split())
  if A<=D: print((A+1)*D)
  else: print(A*(D+1))