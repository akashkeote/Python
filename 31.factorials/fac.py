def fac(n=4):
    if(n==0|n==1):return n;
    return n*fac(n-1);
print(fac())

def fac2(n):
    sum=1;
    for i in range(1,n+1):
        sum*=i;
    return sum;
print(fac2(5))
print(fac2(0))

import sys
print(sys.getrecursionlimit())
sys.setrecursionlimit(100000);
print(sys.getrecursionlimit())
import time 
time.sleep(20)