

donor_info = {"Doug Peters": 150,"Gene Simmons": 1000, "Julie Andrews": 500,
"Guy Ritchie": 0, "Paul Allen": 0, "Paul Allen": 5000, "Paul Allen": 500,
"Doug Peters": 100, "Doug Peters": 250, "Gene Simmons": 1000,
"Gene Simmons": 1000,}


def print_thank_you(x, y):
    print type(x)
    print type(y)

    # print " Dear ' %s ', Thank you so much for the donation of $ ' %i ', We really appreciate. This will provide necessary funds to our core operations. This donation should be tax deductable. Please consult an account specialist for further information. Sincerely - Rich Green" % (x, y)
    print (x)
    print(y)
    # send_a_thankyou()


def send_a_thankyou(option):

    name = ''
    donation_amount = ''

    if option == 'list':
        print donor_info.keys()
    menu()

# If the name is not in the key and the user entered a name add it to the donor
# info along with donation amount

    if option == 'new':

        if donor_info.has_key(name) and len(name) > 0:
            print "This is not a new donor . try again and select update"
            send_a_thankyou()
        else:
            print "Enter new donors name:"
            name = raw_input()
            print "Enter donation amount:"
            donation_amount = float(raw_input())
            # float(donation_amount) = donation_amount
            donor_info[name] = donation_amount
            print " Your information has been recorded"
            # print type(donation_amount)
            print_thank_you(name, donation_amount)


    # donor_info.{donor_info.name: donation_amount})

    if option == 'update':
        print "Enter new donors name:"
        name = raw_input()
# If the user wants to add another donation from someone already in the system
    if not donor_info.has_key(name) and len(name) > 0:
        print "This donor is not in the system try again"
        # send_a_thankyou()

    if len(name) or len(donation_amount) == 0:
        print "Please enter a name and donation amount. Try again"
        # send_a_thankyou()
    else:
        print "Enter donation amount:"
        donation_amount = float(raw_input())

# Add donation amount to Donor_info dictionary
    if donation_amount.isdigit():
        insert_dict = {name: donation_amount}
        donor_info.update(insert_dict)
    else:
        print " the value you entered is not a number. try again"


# break

#String formatting u"My name is {first} {last}".format(**d)

#Also

# print "Dear %name, Thank you so much for the donation of $ %donation_amount, We really appreciate. This will provide necessary funds to our core operations. This donation should be tax deductable. Please consult an account specialist for further information.
# Sincerely
# Rich Green"
# break
#Return to menu

        send_a_thankyou(new)
