# daydream.pyで解けたが、dreraseeeraseaerasem->YESはおかしいので修正版(未完成)

# AtCoderBeginnersSelection
# ABC049C - 白昼夢 / Daydream

def cut(s):
	length = len(s)
	if length == 0:
		return 'YES'
	elif s[length - 5:] == 'dream':
		return cut(s[:length - 5])
	elif s[length - 7:] == 'dreamer':
		return cut(s[:length - 7])
	elif s[length - 5:] == 'erase':
		return cut(s[:length - 4])
	elif s[length - 6:] == 'eraser':
		return cut(s[:length - 6])
	else:
		return 'NO'

s = input()

print(cut(s))