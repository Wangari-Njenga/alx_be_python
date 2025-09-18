#A while loop to draw a pattern of asterisks

size = int(input("Enter the size of the pattern: "))
i = 1
while i <= size:
    print('*' * i)
    i += 1
