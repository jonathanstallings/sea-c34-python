def list_donors():
    """Print the current donor list"""
    for donor in donors:
        print donor


def validate_donation(donation):
    """Check if given donation is a valid number."""
    try:
        float(donation)
    except ValueError:
        return False
    else:
        if float(donation) <= 0:
            print(u"Amounts must be greater than $0\n")
            return False
        else:
            return True


def add_donation(donor, donation):
    """
    Add the new donation to the stored donors data.

    If the donor exists, update recored; otherwise, add new donor info.
    """
    if donor in donors:
        donors[donor] += donation
    else:
        donors[donor] = donation


def thank_you_message(donor, donation):
    """Compose message to donor thanking them for the donation"""
    message = u"Some text with {donor} {donation}." \
        .format(donor=donor, donation=donation)
    return message


def show_report():
    """Extract data from donor records and sort by total historical donations."""
    sorted_donors = []

    for donor in donors:
        total = sum(donors[donor])
        number = len(donors[donor])
        average = total / number
        sorted_donors.append(donor, total, number, average)
    sorted_donors.sort(key=lambda x: x[1], reverse=True)

    print headers_for_report
    for i in sorted_donors:
        print formatted_tabular_data(donor, total, number, average)
    print new_line


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
                        print donor
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
