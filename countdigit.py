def count_digits(n):
    count = 0
    if n == 0:
        return 1
    if n < 0:
        n = -n
    while n > 0:
        n = n // 10
        count = count + 1
    return count
n = int(input("Enter a number: "))
print("Number of digits:", count_digits(n))