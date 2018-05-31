# AtCoderBeginnersSelection
# ABC083B - Some Sums

n, a, b = map(int, input().split())

ans = 0

for i in range(1, n + 1):
	s = sum(map(int, list(str(i))))
	if s >= a and s <= b:
		ans += i

print(str(ans))