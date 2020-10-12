def f(x):
    return (25 - 3*x)/2


for i in range(20):
    if 0 <= f(i) < 20 and f(i).is_integer():
        print('a ={} and b = {}'.format(i, int(f(i))))
