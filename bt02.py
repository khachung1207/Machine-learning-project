import random

count = 0

while True:
    a = random.randint(1, 20)
    b = random.randint(1, 20)
    count += 1
    if a + b == 40:
        print(f"Tìm được: a = {a}, b = {b} sau {count} lần thử")
        break
