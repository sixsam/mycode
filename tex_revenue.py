def tax_revenue(mone):
    return mone * 0.03

def main():
    while True:
        mone = input('please enter your money:')
        tax = tax_revenue(int(mone))
        print('税收额为%f' % tax)

if __name__ == "__main__":
    main()
