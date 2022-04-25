import io
import sys

_INPUT = """\
6
6
1 -3 3 9 1 6
3
5 5 5
8
-1 10 -1 2 -1 10 -1 0
"""

sys.stdin = io.StringIO(_INPUT)
case_no=int(input())
for __ in range(case_no):
  N=int(input())
  A=list(map(int,input().split()))
  ans=-(10**10)
  for i in range(N):
    a=-(10**10)
    ai=0
    for j in range(N):
      if i==j: continue
      if j<i: tmp=sum([A[j+2*k+1] for k in range((i-j+1)//2)])
      else: tmp=sum([A[i+2*k+1] for k in range((j-i+1)//2)])
      if tmp>a:
        a=tmp
        ai=j
    if ai<i: tmp2=sum([A[ai+2*k] for k in range((i-ai+2)//2)])
    else: tmp2=sum([A[i+2*k] for k in range((ai-i+2)//2)])
    ans=max(ans,tmp2)
  print(ans)