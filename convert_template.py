def convert(fahr):
    return (fahr - 32)*(5/9)

def main():
    while True:
        fahr = input('enter fahrenheit:')
        cent = convert(int(fahr))
        print('%s 华氏度等于 %.2f 摄氏度' % (fahr,cent))

if __name__ == "__main__":
    main()
