number = int(input("Enter the size of the pattern:"))
while number > 0:
    for i in range(number):
        for j in range(number + 1):
            print("*", end=" ")
        print()
    number -= 1
    print()
    if number > 0:
        number = int(input("Enter the size of the pattern:"))   
    else:
        break