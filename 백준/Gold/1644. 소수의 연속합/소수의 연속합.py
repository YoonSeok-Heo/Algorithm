import sys

input = sys.stdin.readline

def prime_list(n):
	sieve = [True] * (n + 1)
	
	m = int(n ** 0.5)
	
	for i in range(2, m + 2):
		if sieve[i] == True:
			for j in range(i + i, n + 1, i):
				sieve[j] = False
				
	return [i for i in range(2, n + 1) if sieve[i] == True]
	
n = int(input().strip())

if n == 1:
	print(0)
	exit()
	
lst = prime_list(n)
l, r, answer, sum = 0, 0, 0, lst[0]

while l < len(lst) and r < len(lst):
	if sum == n:
		answer += 1
		sum -= lst[l]
		l += 1
	elif sum < n:
		if r == len(lst) - 1:
			break
		r += 1
		sum += lst[r]
	elif sum > n:
		sum -= lst[l]
		l += 1

print(answer)