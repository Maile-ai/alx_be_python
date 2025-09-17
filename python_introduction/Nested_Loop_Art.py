rows =5
i =0

while i < rows:
#spaces before stars
    j = 0
    while j < rows - i -1:
        print(" " , end="")
        j +=1
    k = 0
    while k < 2 * i + 1:
        print("*", end="")
        k += 1

    # move to next line
    print()
    i += 1