
# Idea for dealer phone return policy
# Dealer can return 2% of their total phone purchased. Allowance accumulates as dealer purchase phones or
# subtracts as dealers uses them

# SR dealers have 2% return rate and AR dealers have 1% return rate



class dealerSR(object):
    def __init__(self):
        self.phonepurchased = 0
        self.allowance = 0

    def buyphone(self,phone):
        self.phonepurchased += phone
        self.allowance += phone * .02
        print "Currently, you have %s" % (int(self.allowance))
    def useallowance(self):
        loop = True
        while loop == True:
            if int(self.allowance) < 1:
                print "You don't have enough allowance"
                break
            print "Currently, you have %s" % (int(self.allowance))
            x = int(raw_input("How many returns?: "))
            if x > int(self.allowance):
                print "You don't have enough allowance"
            self.allowance -= x
            print int(self.allowance)
            y = raw_input("Done?Y/N: ")
            if y == 'y':
                loop = False


class dealerAR(dealerSR):

    def buyphone(self,phone):
        self.phonepurchased += phone
        self.allowance += phone * .01
        print "Currently, you have %s" % (int(self.allowance))

