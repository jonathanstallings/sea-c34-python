from __future__ import print_function


def list_donors():
    """Print the current donor list"""
    for donor in donors:
        print(donor)


def validate_donation(donation):
    """Check if given donation is a valid number."""
    try:
        float(donation)
    except ValueError:
        return False
    else:
        float(donation)
        if donation <= 0:
            print(u"Amounts must be greater than $0\n")
            return False
        else:
            return donation


def add_donation(donor, donation):
    """
    Add the new donation to the stored donors data.

    If the donor exists, update recored; otherwise, add new donor info.
    """
    if donor in donors:
        donors[donor] += donation
    else:
        donors[donor] = [donation]


def thank_you_message(donor, donation):
    """Compose message to donor thanking them for the donation"""
    message = u"Some text with {donor} {donation}." \
        .format(donor=donor, donation=donation)
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


donors = {
    "Abigail Simmons": [50.00, 75.00, 25.00],
    "Bruce Thompson": [20.00, 200.00],
    "Chase Riley": [45.00, 10.00, 10.00, 20.00],
    "Darlene Staley": [2000.00],
    "Edgar Mason": [1500.00, 400.00]
}


if __name__ == '__main__':

    while True:
        main_prompt = raw_input(
            u"\n[1] Send a Thank You\n[2] Create a Report\n[Q]uit\n\n>"
        )

        if main_prompt.lower() == u"q":
            break

        elif main_prompt == u"1":
            while True:
                donor = raw_input(
                    u"\nType the name of the donor:\n[C]ancel\n\n>"
                )
                if donor == u"list":
                    for donor in donors.keys():
                        print(donor)
                elif donor.lower() == u"c":
                    break
                else:
                    while True:
                        donation = raw_input(
                            u"\nHow much did {donor} donate?\n\n>"
                            .format(donor=donor)
                        )
                        if validate_donation(donation):
                            break

                    add_donation(donor, donation)

                    print(thank_you_message(donor, donation))
                    break

        elif main_prompt == u"2":
            show_report()
