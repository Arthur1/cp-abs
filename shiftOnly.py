# AtCoderBeginnersSelection
# ABC081B - Shift only

n = int(input())
a = list(map(int, input().split()))
i = 0

while True:
	if 1 in list(map(lambda x: x % 2, a)):
		break
	a = list(map(lambda x: x // 2, a))
	i += 1

print(i)