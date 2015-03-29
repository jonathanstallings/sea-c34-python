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
    if donation <= 0:
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
    message = u"Some text with {donor} {donation}" \
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


donors = {}
# Add some donor history here.


if __name__ == '__main__':

    while True:
        main_prompt = raw_input(
            u"[1] Send a Thank You\n [2] Create a Report\n[Q]uit]\n)".lower()
        )

        if main_prompt == u"q":
            break

        elif main_prompt == u"1":
            while True:
                donor = raw_input(u"Type the name of the donor:\n[C]ancel") \
                    .lower()
                if donor == u"c":
                    break
                else:
                    while True:
                        donation = raw_input(
                            u"How much did {donor} donate?".format(donor=donor)
                        )
                        if validate_donation(donation):
                            break

            add_donation(donor, donation)

            print(thank_you_message(donor, donation))
            break

        elif main_prompt == u"2":
            show_report()
