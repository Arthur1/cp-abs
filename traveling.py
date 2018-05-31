# AtCoderBeginnersSelection
# ABC086C - Traveling

n = int(input())
t_last, x_last, y_last = 0, 0, 0

for i in range(n):
	t, x, y = map(int, input().split())
	r = abs(x - x_last) + abs(y - y_last)
	if (r > (t - t_last) or (t - t_last) % 2 == r % 2):
		print('No')
		exit()
	t_last, x_last, y_last = t, x, y

print('Yes')