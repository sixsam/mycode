import sys 

def judge_leap_year(year):
    if year%400 == 0:
        return "%s is leap year" % year
    elif (year%4 == 0) and (year%100 != 0):
        return "%s is leap year" % year
    else:
        return "%s is not leap year" % year


def main():
    year = sys.argv[1]
    judge = judge_leap_year(int(year))
    print(judge)


if __name__ == "__main__":
    main()
