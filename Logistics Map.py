#Xn + 1 = r * Xn(1 - Xn)
#Xn + 1 refers to a recursion of the same formula but with Xn being the return
#r is a constant rate of growth
#Xn is a percentage of maximum population from 0 to 1

growth = lambda r, x: r*x(1-x)

top = 10 # the amount of trials

rate = 5
Xn = .5

for iter in range(top):
	result = growth(rate, Xn)
	if Xn > result:
		print("grow:", result)
	else:
		print("shrink:", result)
	Xn = result
