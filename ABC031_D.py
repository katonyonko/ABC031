import io
import sys

_INPUT = """\
6
6 4
356 migoro
461 yoroi
2 ni
12 ini
3 4
21 aaa
12 aaa
123 aaaaaa
13 aaaa
2 3
12211 abcaaaaabcabc
2121 aaabcaaabc
222221 aaaaaaaaaaabc
2 1
12 abcab
"""

sys.stdin = io.StringIO(_INPUT)
case_no=int(input())
for __ in range(case_no):
  from itertools import product
  K,N=map(int,input().split())
  goro=[list(input().split()) for _ in range(N)]
  for k in product(*[list(range(3)) for _ in range(K)]):
    fl=1
    ans=['']*K
    for i in range(N):
      v,w=goro[i]
      if len(w)!=sum([k[int(v[j])-1]+1 for j in range(len(v))]): fl=0
      now=0
      for j in range(len(v)):
        if ans[int(v[j])-1]=='': ans[int(v[j])-1]=w[now:now+k[int(v[j])-1]+1]
        elif ans[int(v[j])-1]!=w[now:now+k[int(v[j])-1]+1]: fl=0
        now+=k[int(v[j])-1]+1
    if fl==1:
      break
  print(*ans,sep='\n')