def find_squared_rooted(a):
    EPSILON = 0.001
    x0 =a
    while True:
        x1= x0- (x0**2 - a)/(2*x0)
        if abs(x1-x0) < EPSILON:
            break
        x0=x1
    return x1
print(find_squared_rooted(2))
print(find_squared_rooted(3))