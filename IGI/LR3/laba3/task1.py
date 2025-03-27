import math

def calculate(x, eps, max_n = 500):
    if abs(x) >= 1:
        return None, None, None, None
    
    math_f = math.log(1 - x)
    n = 1
    sum_f = 0.0
    term = - x

    for n in range(1, max_n):
        sum_f += term
        n += 1
        term = - (x ** n) / n

        if abs(sum_f - math_f) <= eps:
            break

        if n > 500:
            return None, None, None, None

    return x, n, sum_f, math_f

def user_input():
    while True:
        try:
            x = float(input("Введите значение x (|x| < 1): "))
            if abs(x) >= 1:
                print("Ошибка: |x| должно быть меньше 1. Попробуйте снова.")
                continue
            
            eps = float(input("Введите точность вычислений (например, 1e-6): "))
            if eps <= 0:
                print("Ошибка: точность должна быть положительным числом. Попробуйте снова.")
                continue
            
            return x, eps
        except ValueError:
            print("Ошибка: введите числовое значение. Попробуйте снова.")

x, eps = user_input()
x_val, n_val, f_x, math_f_x = calculate(x, eps)

if x_val is not None:
    print("\nРезультат вычисления: ")
    print("| x       | n  | F(x)       | Math F(x)  | eps     |")
    print(f"|{x_val:.6f}|{n_val:2}|{f_x:.6f}|{math_f_x:.6f}|{eps}|")
else:
    print("Ошибка выполнения условия")