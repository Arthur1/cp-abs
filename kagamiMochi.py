# AtCoderBeginnersSelection
# ABC085B - Kagami Mochi

n = int(input())
d = []

for i in range(n):
	d.append(int(input()))

d_unique = list(set(d))

print(str(len(d_unique)))