fibonacci=[]
a = 0
b = 1
while True:
    if b>4000000:
        break
    c = a + b
    a = b
    b = c
    if b%2==0:
        fibonacci.append(b)
    else:
        continue
suma = sum(fibonacci)
print("Wyrazy ciagu fibonacciego: ",fibonacci)
print("Suma wyrazow ciagu: ", suma)