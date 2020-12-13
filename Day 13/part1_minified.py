t,i=open("input.txt").readlines()
d={x:x-(int(t)%x)for x in(int(x)for x in i.split(',')if x!='x')}
m=min(d,key=d.get)
print(m*d[m])