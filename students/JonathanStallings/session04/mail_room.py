from __future__ import print_function

import json


def list_donors():
    """Print the current donor list, sorted by name (simply)."""
    sorted_donors = []
    for donor in donors:
        sorted_donors.append(donor)
    sorted_donors.sort()
    print("\n")
    for donor in sorted_donors:
        print(donor)


def is_invalid(donation):
    """Check if given donation is a valid number."""
    try:
        float(donation)
    except ValueError:
        print(u"Please enter a valid amount.\n")
        return True
    else:
        if float(donation) <= 0:
            print(u"Amounts must be greater than $0\n")
            return True
        else:
            return False


def add_donation(donor, donation):
    """
    Add the new donation to the stored donors json data file.

    If the donor exists, update recored; otherwise, add new donor info.
    """
    if donor in donors:
        donors[donor].append(donation)
    else:
        donors[donor] = [donation]
    with open('donors.json', 'w') as outfile:
        json.dump(donors, outfile)


def thank_you_message(donor, donation):
    """Compose message to donor thanking them for the donation"""
    message = (
        u"\n\nDear {},\n\nThank you for your generous donation of "
        "${:.2f}. The Seattle chapter of the Pythonic Poetry Foundation "
        "is made possible by the continued support of individuals like "
        "you. \n\nSemper Py,\nPeter Pythonista\n"
        .format(donor, donation)
    )
    return message


def show_report():
    """Display donor data sorted by total historical donations."""
    sorted_donors = []

    for donor in donors:
        total = sum(donors[donor])
        number = len(donors[donor])
        average = total / number
        sorted_donors.append([donor, total, number, average])
    sorted_donors.sort(key=lambda x: x[1], reverse=True)

    print(
        "{:22s} {:16s} {:20s} {:20s}\n".format(
            "Name", "Total Donations", "Number of Donations",
            "Average Donation"
        )
    )
    for i in sorted_donors:
        print(
            "{:22s} {:<16.2f} {:<20d} {:<20.2f}".format(
                i[0], i[1], i[2], i[3]
            )
        )
    print("\n\n")


if __name__ == '__main__':

    with open('donors.json') as data_file:
        donors = json.load(data_file)

    while True:
        main_prompt = raw_input(
            u"\n[1] Send a Thank You\n"
            "[2] Create a Report\n[Q]uit\n\n> "
        )

        if main_prompt.lower() == u"q":
            break

        elif main_prompt == u"1":
            while True:
                donor = raw_input(
                    u"\nType the full name of the donor:\n"
                    "[L]ist or [C]ancel\n\n> "
                )
                if donor.lower() == u"l":
                    list_donors()
                elif donor.lower() == u"c":
                    break
                else:
                    donation = raw_input(
                        u"\nHow much did {donor} donate?\n\n> "
                        .format(donor=donor)
                    )
                    while is_invalid(donation):
                        donation = raw_input(
                            u"\nHow much did {donor} donate?\n\n> "
                            .format(donor=donor)
                        )
                    donation = float(donation)
                    add_donation(donor, donation)

                    print(thank_you_message(donor, donation))
                    break

        elif main_prompt == u"2":
            show_report()
