import functools;import math;g=lambda a,b,x,y:g(a,b+a*(max(-1,y-b-1)//a+1),x,y+x*(max(-1,b-y-1)//x+1))if b!=y else(math.lcm(a,x),b);print(functools.reduce(lambda n,m:g(*n,*m),((int(x),-i)for i,x in enumerate(open("input.txt").readlines()[1].split(','))if x!='x'),(1,0))[1])
