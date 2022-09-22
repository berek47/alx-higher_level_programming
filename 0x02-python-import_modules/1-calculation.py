#!/usr/bin/python3
if __name__ == '__main__':
    from calculator_1 import add, sub, mul, div

    a = 10
    b = 5
    Add = add(a, b)
    Sub = sub(a, b)
    Mul = mul(a, b)
    Div = div(a, b)

    print('{} + {} = {}'.format(a, b, Add))
    print('{} - {} = {}'.format(a, b, Sub))
    print('{} * {} = {}'.format(a, b, Mul))
    print('{} / {} = {}'.format(a, b, Div))
