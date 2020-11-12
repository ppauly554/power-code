from random import uniform as rand

#Xn + 1 = r * Xn(1 - Xn)
#Xn + 1 refers to a recursion of the same formula but with Xn being the return
#r is a constant rate of growth
#Xn is a percentage of maximum population from 0 to 1

growth = lambda r, x: r*x*(1-x)


# /* changable variables
top = 50 # the amount of trials

rate = round(rand(0, 10), 2)
Xn = round(rand(0, 1), 2)
# */

print('Rate:',rate)
print('Max:', Xn)

for iter in range(top):
	result = growth(rate, Xn)
	if Xn < result:
		print("grow:", result)
	else:
		print("shrink:", result)
	Xn = result
