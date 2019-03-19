def calc(expr):
    exprl = expr.split(' ')
    try:
        exprl_0 = int(exprl[0])
    except ValueError:
        exprl_0 = float(exprl[0])
    except:
        return "type error"

    try:
        exprl_2 = int(exprl[2])
    except ValueError:
        exprl_2 = float(exprl[2])
    except:
        return "type error"

    if exprl[1] == '+':
        return exprl_0 + exprl_2

    if exprl[1] == '-':
        return exprl_0 - exprl_2

    if exprl[1] == '*':
        return exprl_0 * exprl_2

    if exprl[1] == '/':
        return exprl_0 / exprl_2

    if exprl[1] == '%':
        return exprl_0 % exprl_2

    if exprl[1] == '**':
        return exprl_0 ** exprl_2

def main():
    while True:
        expr = input("please enter an expression:")
        result = calc(expr)
        print(result)


if __name__ == "__main__":
    main()
