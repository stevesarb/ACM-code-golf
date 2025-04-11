y,m,d=map(int,input().split("-"))
if m in (1,2):y-=1;m+=12
K,J=y%100,y//100
l=['Saturday','Sunday','Monday','Tuesday','Wednesday','Thursday','Friday']
print(l[(d+13*(m+1)//5+K+K//4+J//4+5*J)%7])