# AtCoderBeginnersSelection
# ABC049C - 白昼夢 / Daydream

s = input()
replaced = s.replace('eraser', '').replace('erase', '').replace('dreamer', '').replace('dream', '')

if (replaced == ''):
	print('YES')
else:
	print('NO')