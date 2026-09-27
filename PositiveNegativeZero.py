def PositiveNegative(n):
    if(n>0):
        return 'Positive'
    elif(n<0):
        return 'negative'
    else: return 'zero'
n = int(input("Enter a number: "))
print(PositiveNegative(n))