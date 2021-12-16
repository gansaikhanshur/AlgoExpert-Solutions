"""
Method 1:
    Brute Force
"""

def getNthFib(n):
	fib_seq = [0]

	if n == 1:
		return 0
	
    for i in range(0, n):
        if i == 0 or i == 1:
            fib_seq.append(1)
        else:
            fib_seq.append((fib_seq[i] + fib_seq[i - 1]))

    fib_seq = fib_seq[:-1]
    return fib_seq[n - 2] + fib_seq[n - 3]

"""
Method 2:
    A bit smarter way
"""

def getNthFib(n):
	if n == 1:
		return 0
	elif n == 2:
		return 1
	else:
		return getNthFib(n - 1) + getNthFib(n - 2)
