donor_info = {"Doug Peters": [150.0],
              "Gene Simmons": [1000.50, 150],
              "Julie Andrews": [500.90],
              "Guy Ritchie": [0, 25]}


def send_a_thankyou():
    print "Enter full name(or type list for a list of donors:"
    name = raw_input()

    if name == 'list':
        print donor_info.keys()
        # I had this function call recrusively to
        # return so the user to restart with donor name
        send_a_thankyou()
        return

    print "Enter donation amount:"
    donation_amount = raw_input()

    try:
        donation_amount == float(donation_amount)

    except TypeError:
        print " the value you entered is not a number. try again"
        send_a_thankyou()
        return

    if name in donor_info:
        donor_info[name].append(float(donation_amount))
    else:
        donor_info[name] = [float(donation_amount)]

      # '\n\n{}'

    thanks = (
        'Dear {} , Thank you so much for the donation of $ {} , We '
        'really appreciate it. This will provide necessary funds to our core '
        'operations. This donation should be tax deductable. Please consult an'
        ' account specialist for further information. Sincerely - Rich Green')

    thanks_formatted = thanks.format(name, donation_amount)


    print thanks_formatted

def create_a_report():

    # describe dictionaries
    sum_of_donations = {}
    avg_of_donations = {}

    for name, donations in donor_info.iteritems():
        try:

            sum_of_donations[name] = sum(donations)

            avg_of_donations[name] = sum(donations) / len(donations)

        except TypeError:
            pass

    print sum_of_donations
    print avg_of_donations



send_a_thankyou()

create_a_report()
