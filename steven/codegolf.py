d=input()
y=int(d[:4])-1583
m=int(d[5:7]) - 1
dy=int(d[8:])
numLeapYrs = y % 4
days = ["Saturday", "Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday"]
choice = y % 7
choice = (choice + numLeapYrs) % 7
choice = (choice + dy) % 7

monthLengths = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
for i in range(m):
	choice = (choice + monthLengths[i]) % 7

print(days[choice])