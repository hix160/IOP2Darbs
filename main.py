from sympy import symbols, diff
import sys

def is_number(num):
    try:
        float(num)
        return True
    except ValueError:
        return False

def optimize_variables(x1, x2, t=0.01, epsilon=0.015):
    a = 2
    b = 4
    c = 2
    d = 4

    x, y = symbols('x y', real=True)
    fun = x - a * y + b * x**2 + c * x * y + d * y**2
    der_fun_x = diff(fun, x)
    der_fun_y = diff(fun, y)

    grad = [der_fun_x.evalf(subs={x: x1, y: x2}), der_fun_y.evalf(subs={x: x1, y: x2})]

    iterations = 0
    while abs(grad[0]) > epsilon and abs(grad[1]) > epsilon:
        x1 -= t * grad[0]
        x2 -= t * grad[1]
        grad = [der_fun_x.evalf(subs={x: x1, y: x2}), der_fun_y.evalf(subs={x: x1, y: x2})]
        iterations += 1
        if iterations > 5000:
            print("Current configuration will not find the optimum values.")
            return

    return x1, x2, iterations

def main():
    if len(sys.argv) < 3:
        print("Usage: {} x1 x2 [t] [eps]".format(sys.argv[0]))
        print("All variables must be numbers.")
        return

    if not all(is_number(value) for value in sys.argv[1:]):
        print("Visiem jābūt cipariem")
        return

    x1 = float(sys.argv[1])
    x2 = float(sys.argv[2])

    t = float(sys.argv[3]) if len(sys.argv) > 3 else 0.01
    epsilon = float(sys.argv[4]) if len(sys.argv) > 4 else 0.015

    x1_opt, x2_opt, iterations = optimize_variables(x1, x2, t, epsilon)

    print("t =", t)
    print("Epsilon =", epsilon)
    print("X1 =", x1_opt)
    print("X2 =", x2_opt)
    print("Iterations = ", iterations)

if __name__ == "__main__":
    main()