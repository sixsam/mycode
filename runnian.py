import sys 

def judge_runnian(year):
    if year%400 == 0:
        return "%s是闰年" % year
    elif (year%4 == 0) and (year%100 != 0):
        return "%s是闰年" % year
    else:
        return "%s不是闰年" % year


def main():
    year = sys.argv[1]
    judge = judge_runnian(int(year))
    print(judge)


if __name__ == "__main__":
    main()
