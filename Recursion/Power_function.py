
def Pow(x, n): # calculates x^n
    if n == 0 : return 1 
    if x == 0 or x == 1 or n == 1 : return x

    return x * Pow(x,n-1)

print(Pow(4,3))

    