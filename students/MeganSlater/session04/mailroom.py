donors = {}


def safe_input(x):
    try:
        return raw_input(x)
    except (EOFError, KeyboardInterrupt):
        thankyous()


def thankyous():
    """ask user whether to send thank you or create report.  Take action based
    on input
    """
    try:
        userprompt = raw_input("Choose Send a Thank You or Create a Report. ")
        userprompt = userprompt.lower()
        if userprompt == "send a thank you":
            send_thank_you()
        elif userprompt == "create a report":
            create_a_report()
        # unexpected input from user
        else:
            print("I'm sorry, I don't understand.  Try again. ")
            thankyous()

    # let the user quit out of the function entirely
    except (EOFError, TypeError, AttributeError, KeyboardInterrupt):
        pass


def send_thank_you():
        donorname = "list"
        while donorname == "list":
            donorname = safe_input("What is the donor's full name? \n"
                                   "Type list to see list of "
                                   "current donors ")
            if donorname == "list":
                print donors.keys()

        amount = "amount"
        while amount.isalpha() == True:
            amount = safe_input("How much did they donate? ")
        # Unknown name added to dict.  Add amount for any donor.
        if donorname in donors.keys():
            donors[donorname] = donors[donorname] + [float(amount)]
        else:
            donors[donorname] = [float(amount)]

        """Once an amount has been added the user will receive a print
        out of an email for every donor and return to the beginning.
        """
        print("""
Dear %s, \n
Thank you for donating $%.2f to the Spanish Inquisition. Our chief weapon
is surprise!  Surprise and fear... fear and surprise... Our TWO weapons are
fear and surprise... and ruthless efficiency!  Our THREE weapons are fear and
surprise and ruthless efficiency.  And we could not do it without your
support!\n
With suprise, fear, ruthless efficiency and an almost fanatical devotion
to the Pope,
The Spanish Inquisition
            """ % (donorname, donors[donorname][-1]))
        thankyous()


def create_a_report():
        totaldonated = []
        # add up the total donations for each donor and put it in a list
        for name in donors.iterkeys():
            totaldonated.append(reduce(lambda x, y: x+y, donors[name]))
        # sort that list highest to lowest
        totaldonated = sorted(totaldonated, reverse=True)
        # create report list with biggest donor listed first
        report = ['Name: %s'
                  '\tTotal: $%.2f '
                  '\tDonations: %d'
                  '\tAvg Donation: $ %.2f'
                  % (name, total, len(donors[name]),
                     total/len(donors[name]))
                  for total in totaldonated
                  for name, donation in donors.iteritems()
                  if total == reduce(lambda x, y: x+y, donors[name])]
        for line_item in report:
            print(line_item)
        thankyous()

thankyous()

