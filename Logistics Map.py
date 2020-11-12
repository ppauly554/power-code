import matplotlib.pyplot as plt

# Xn+1 = l * Xn(1-Xn)
# Zn + 1 refers to a recursion of the same formula but with Xn being the return
# l is a rate of growth
# Xn is population density

# /* CHANGEABLE

const_Xn = .5

# */

lam = 0  # the rising x value; short for lambda
Xn = const_Xn  # Is a constant to grab from

cords = []  # the coordinates to plot

# /* OPTIONAL
temp = lam  # temp is used later
# */

growth = lambda: lam * Xn * (1 - Xn)  # a function that runs the formula and outputs Xn

while lam <= 4:  # values won't register passed 4

    for i in range(30):  # 30 points on each x value allows shape to be visible

        Xn = growth()  # this is the Xn+1 part of the formula where the answer is put back into the formula; recursion

        if not 0 <= Xn <= 1:  # makes sure values are within percentage range if not it jumps out of for loop
            break
        else:
            cords.append((lam, Xn))  # adds the coordinate to the cords list

    lam = round(lam + .05, 2)  # increase x value, and rounds it up for readability

    Xn = const_Xn  # resets Xn for next lam

    # /* OPTIONAL
    if lam != temp:  # this reads out the number and skips repeats
        print(lam)
    temp = lam
    # */

print("list size:", len(cords))

plt.title('logistics map')
plt.scatter([x[0] * 1000 for x in cords], [y[1] * 1000 for y in cords])
plt.show()
