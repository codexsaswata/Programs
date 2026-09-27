def star_pattern(n):
    for i in range(1, n + 1):
        for j in range(i):
            print("*", end="")
        print()
n = int(input("Enter number of rows: "))
star_pattern(n)