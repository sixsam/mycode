import sys 

def dollar_to_cent(dollar):
    cent_25 = dollar // 25
    balance = dollar % 25
    if balance != 0:
        cent_10 = balance // 10
        balance %= 10
        if balance != 0:
            cent_5 = balance // 5
            balance %= 5
            if balance != 0:
                return cent_25,cent_10,cent_5,balance
            else:
                return cent_25,cent_10,cent_5,0
        else:
            return cent_25,cent_10,0,0
    else:
        return cent_25,0,0,0
def main():
    fdollar = float(sys.argv[1])
    dollar_int = int(fdollar*100)
    cents = dollar_to_cent(dollar_int)
    print("%.2f dollar equl %d(x25_cent),%d(x10_cent),%d(x5_cent),%d(x1_cent)" % (fdollar,cents[0],cents[1],cents[2],cents[3]))



if __name__ == "__main__":
    main()
