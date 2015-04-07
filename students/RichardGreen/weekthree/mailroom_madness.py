# From Sys import exit
from send_a_thankyou import send_a_thankyou

'''It should have a data structure that holds a list of your donors and
a history of the amounts they have donated. This structure should be populated
at first with at least five donors, with between 1 and 3 donations each'''


donor_info = {"Doug Peters": 150,"Gene Simmons": 1000, "Julie Andrews": 500,"Guy Ritchie": 0, "Paul Allen": 0, "Paul Allen": 5000, "Paul Allen": 500,"Doug Peters": 100, "Doug Peters": 250, "Gene Simmons": 1000,"Gene Simmons": 1000,}

def menu():
    print"Welcome to Mailroom Madness Menu:"
    print "Please enter a suggestion below:"
    print("Enter     0. Menu")
    print("Enter 1 to send a thank you letter")
    print ("Enter 2 to create a report")
    # print ("Enter 3 to exit")
    access = int(input("Make a selection from the above list: "))
    return access #

access = menu() #

if access == 1:
    # if suggestion == 1:

    print("Print a Thank you letter")
    print("Type 'list': to see a list of current donors")
    print("Type 'new' to enter the full name of the donor and donation amount")
    print("Type 'update' add an additional donation to an existing member")

    option = raw_input()

    send_a_thankyou(option)
    # send_a_thankyou()

if access == 2:

        print "createareport"
    # # create_a_report()


else:

    menu()
    #     loop = 0

    # print "Thankyou for using Mailroom Madness!"

# Function 1


# def send_a_thankyou(option):

#     # option = raw_input()

#     if option == 'list':

#         print donor_info.keys()

# # If the name is not in the key and the user entered a name add it to the donor
# # info along with donation amount

#     if option == 'new':

#         if donor_info.has_key(name) and len(name) > 0:
#             print "This is not a new donor . try again "
#             menu()
#     print "Enter new donors name:"
#     name = raw_input()
#     print "Enter donation amount:"
#     donation_amount = raw_input()
#     donor_info[name] = donation_amount
#     # donor_info.{donor_info.name: donation_amount})

# elif option == 'update':
# # If the user wants to add another donation from someone already in the system
# #if not donor_info.has_key(name) and len(name) > 0: print "This donor is not in the system try again" break

# print "Enter donation amount:"
# donation_amount = raw_input()

# #Add donation amount to Donor_info dictionary
# if donation_amount.isdigit():
# donor_info.update({name: donation_amount})
# else:
# print " the value you entered is not a number. try again"
# break

# print "Dear %name, Thank you so much for the donation of $ %donation_amount, We really appreciate. This will provide necessary funds to our core operations. This donation should be tax deductable. Please consult an account specialist for further information.
# Sincerely
# Rich Green"
# break
#Return to menu
