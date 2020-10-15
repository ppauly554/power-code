length = input("length?")
triangle = [[0,1,0]]

for chunk in range(length):
    triangle.append([0])
    for piece in range(1, len(triangle[chunk])):
        triangle[chunk + 1].append(triangle[chunk][piece - 1] + triangle[chunk][piece])
    triangle[chunk + 1].append(0)

for part, space in enumerate(length - 1, -1, -1):
    print(" "*space, triangle[part])
