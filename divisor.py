def divisor(a,b):
    if a > b:
        a, b = b, a
    for i in reversed(range(1,a+1)):
        if (b%i ==0) and (a%i == 0):
            return i

def multiple(a, b):
    if a < b:
        a, b = b, a
    for i in range(1,b+1):
        if (a * i) % b == 0:
            return a * i

def main():
    while True:
        a = input('enter a:')
        b = input('enter b:')
        div = divisor(int(a),int(b))
        mul = multiple(int(a),int(b))
        print("最大公约数是:%d\n最小公倍数是:%d" % (div, mul))

if __name__ == "__main__":
    main()
