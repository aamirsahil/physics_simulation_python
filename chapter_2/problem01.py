# root findng
def func1(x):
    y = x**2
    return y
def NewtRaph(x, func, dfunc, N=100, error=0.001):
    error = 0.01
    N = 100
    for i in range(N):
        x = x - func(x)/dfunc(x, func, h=0.001)
        if abs(func(x)) < error:
            break
    return x,i
def bisection(a,b,func, N=100, error=0.001):
    if func(a)*func(b) >= 0:
        return "Choose a different initial guess", None
    for i in range(N):
        x = (a+b)/2
        if func(x)*func(a) < 0:
            b = x
        else:
            a = x
        if abs(func(x)) < error:
            break
    return x, i
def main():
    func = func1
    a = -2
    b = 40
    x,i = bisection(a=a, b=b, func=func, N=100, error=0.001)
    print(x)
    if i !=None:
        print(f"f({x}) = {func(x)}")
        print(f"Found in {i} iterations")
if __name__ == "__main__":
    main()