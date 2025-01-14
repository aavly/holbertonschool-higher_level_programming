#!/usr/bin/python3
def uppercase(str):
	for a in str:
		if ord(a) < 123 and ord(a) > 96:
			a = ord(a) - 32
			print(chr(a), end="")
		else:
				print(a, end="")
	print("")

uppercase("best")
uppercase("Best School 98 Battery street")
