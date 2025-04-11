Y,M,D=map(int,input().split('-'));t=(0,3,2,5,0,3,5,1,4,6,2,4);y=Y-(M<3);w=(y+y//4-y//100+y//400+t[M-1]+D)%7;print("Monday Tuesday Wednesday Thursday Friday Saturday Sunday".split()[(w+6)%7])
