# AtCoderBeginnersSelection
# ABC085C - Otoshidama

def search(n, y):
	ykc_max = min(y // 10000, n)
	for i in reversed(range(ykc_max + 1)):
		y_left = y - 10000 * i
		n_left = n - i
		hgc_max = min(y_left // 5000, n_left)
		for j in reversed(range(hgc_max + 1)):
			y_left2 = y_left - 5000 * j
			n_left2 = n_left - j
			if y_left2 == 1000 * n_left2:
				return [str(i), str(j), str(n_left2)]
	return ['-1', '-1', '-1']

n, y = map(int, input().split())

answer = search(n, y)
print(' '.join(answer))

