def list_donors():
    """Print the current donor list"""
    for donor in donors:
        print donor


def validate_donation(donation):
    """Check if given donation is a valid number."""
    if not is_number(donation)
        return False
    elif donation <= 0:
        print(more_than_zero)
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
    message = u"Some text with {donor} {donation}"
    return message


def show_report():
    """Extract data from donor records and sort by total historical donations."""
    sorted_donors = []
    total = sum_of_donations(donor)
    number = number_of_donations(donor)
    average = total / number

    for donor in donors:
        sorted_donors.append(donor, total, number, average)
    sorted_donors.sort(sort_parameters)

    print headers_for_report
    for i in sorted_donors:
        print formatted_tabular_data(donor, total, number, average)
    print new_line


donors = {}
# Add some donor history here.


if __name__ == '__main__':

    while True:
        main_prompt = get_input(prompt_thank_you_or_report_or_quit)

        if main_prompt == quit
            break

        elif main_prompt == thank_you
            while True:
                donor = get_input(prompt_donor_or_cancel)
                if donor == cancel:
                    break
                else:
                    while True:
                        donation = get_input(prompt)
                        if validate_donation(donation)
                            break

            add_donation(donor, donation)

            print(thank_you_message(donor, donation))
            break

        elif main_prompt == report
            show_report()
