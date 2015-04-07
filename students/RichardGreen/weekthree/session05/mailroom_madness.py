#!/usr/bin/env python
# Import the modules needed to run the script.
import sys
import os
import time
# Main definition - constants
menu_actions = {}
# ======================
#     MAILROOM MADNESS
# =======================
# It should have a data structure that holds a list of your donors and
# a history of the amounts they have donated. This structure should be
# populated at first with at least five donors, with between 1 and 3 donations
# each

donor_info = {"Doug Peters": [150.0],
              "Gene Simmons": [1000.50, 150],
              "Julie Andrews": [500.90],
              "Guy Ritchie": [0, 25]}

# Main menu


def main_menu():
    os.system('clear')

    print "Welcome,\n"
    print "Please choose the menu you want to start:"
    print "1. Send a Thank you"
    print "2. Create a Report"
    print "\n0. Quit"
    choice = raw_input(" >>  ")
    exec_menu(choice)

    return

# Execute menu


def exec_menu(choice):
    os.system('clear')
    ch = choice.lower()
    if ch == '':
        menu_actions['main_menu']()
    else:
        try:
            menu_actions[ch]()
        except KeyError:
            print "Not a valid selection, please try again.\n"
            menu_actions['main_menu']()
    return


def send_a_thankyou():

    print "Welcome to Send a Thank you\n"
    print "Enter full name(or type list for a list of donors:"
    print "9. Back"
    print "0. Quit"

    name = raw_input()

    if name == 'list':
        print donor_info.keys()
        # I had this function call recrusively to
        # return so the user to restart with donor name
        send_a_thankyou()
        return

    if name == '9':
        print "Going Back"
        # I had this function call recrusively to
        # return so the user to restart with donor name
        send_a_thankyou()
        return

    if name == '0':
        print "Returning to Main Menu"
        # I had this function call recrusively to
        # return so the user to restart with donor name
        main_menu()
        return

    print "Enter donation amount:"
    donation_amount = raw_input()

    if len(donation_amount) == 0:
        print "Please enter a donation amount"
        send_a_thankyou()
        return

    try:
        donation_amount == float(donation_amount)

    except TypeError:
        print "The value you entered is not a number. try again"
        send_a_thankyou()
        return

    if name in donor_info:
        donor_info[name].append(float(donation_amount))
    else:
        donor_info[name] = [float(donation_amount)]

    thanks = (
        'Dear {} , Thank you so much for the donation of $ {} , We '
        'really appreciate it. This will provide necessary funds to our core '
        'operations. This donation should be tax deductable. Please consult an'
        ' account specialist for further information. Sincerely - Rich Green')

    thanks_formatted = thanks.format(name, donation_amount)

    print thanks_formatted
    time.sleep(6)    # pause for  6 seconds
    print("Returning to Main Menu")
    # return to main menu
    main_menu()
    return


def write_to_a_file(s, y):
    '''function definition: This function will take a string and write it to a
    file. It will also take raw input from the user. Arguments: a string,
    and y a file to write to'''

    try:
        f = open(y, 'w')
        f.write(s)
        f.close()
    except IOError:
        print "couldn't open file, please check to see if it exists"
    f.close()


# Create a Report
def create_a_report():
    print "Hello Welcome to Create a Report !\n"

    # describe dictionaries
    sum_of_donations = {}
    avg_of_donations = {}
    num_of_donations = {}

    for name, donations in donor_info.iteritems():
        try:

            sum_of_donations[name] = sum(donations)

            avg_of_donations[name] = sum(donations) / len(donations)

            num_of_donations[name] = len(donations)

        except TypeError:
            pass
    # Create a Report Table
    # Include Donor Name, total donated, number of donations
    # and average donation amount
    # Let me create a list to write my formatted report to so
    # I can send it to a file
    s = ''

    report_table = {"Donors Names": donor_info.keys(),
                    "Totals": sum_of_donations.values(),
                    "Number": num_of_donations.values(),
                    "Average": avg_of_donations.values()}

    for row in zip(*([k] + map(str, v) for k, v in report_table.items())):
        print "\t".join(row)

        s += str('\t'.join(row) + '\n')

    print("               ")
    print("Writing to File....")
    time.sleep(10)    # pause for  10 seconds
    write_to_a_file(s, 'donor_report.txt')
    print("Returning to Main Menu")
    # return to main menu
    main_menu()


def back():
    menu_actions['main_menu']()

# Exit program


def exit():
    sys.exit()

# =======================
#    MENUS DEFINITIONS
# =======================

# Menu definition
menu_actions = {
    'main_menu': main_menu,
    '1': send_a_thankyou,
    '2': create_a_report,
    '9': back,
    '0': exit,
}

# =======================
#      MAIN PROGRAM
# =======================

# Main Program
if __name__ == "__main__":
    # Launch main menu
    main_menu()
