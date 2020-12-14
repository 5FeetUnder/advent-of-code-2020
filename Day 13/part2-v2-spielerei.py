t,s=0,1;w=lambda t,s,o,b:w(t+s,s,o,b)if(t+o)%b else 0
for o,b in ((i,int(b))for i,b in enumerate(open("input.txt").readlines()[1].split(','))if b!='x'):t,s=w(t,s,o,b),s*b;print(t)