# AtCoderBeginnersSelection
# ABC088B - Card Game for Two

n = int(input())
a = list(map(int, input().split()))

alice = 0
bob = 0

for i in range(n):
	a_max = max(a)
	if i % 2 == 0:
		alice += a_max
	else:
		bob += a_max
	a.remove(a_max)

print(str(alice - bob))