def fibonacci(n):
    a = 1
    b = 1
    if n <= 0:
        print("Podaj liczbe dodatnia")
        exit()
    elif n == 1:
        return a
    else:
        for i in range(2, n):
            c = a + b
            a = b
            b = c
        return b
 
x=int(input("Podaj liczbe ciagu: "))
print(x, "Wyraz ciagu fiboniacciego to: ",fibonacci(x))