hrs = input("Enter Hours:")
h = float(hrs)
rate = float(input("pay: "))
if h <= 40:
    print(h * rate)
else:
    print(40 * rate + (h - 40) * rate * 1.5)
