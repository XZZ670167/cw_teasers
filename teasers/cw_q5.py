def cw_q5():
    customers = {}
    customers['1001'] = ["James Loh", 98778521, "18, Abc Road"]
    customers['1002'] = ["Amy Tan", 87556012, "1, Xyz Road"]

    for c in customers:
        s = str(customers[c])
        print("{:s} corresponds to {:s}".format(c, s[1:len(s) - 1]))


if __name__ == "__main__":
    cw_q5()
