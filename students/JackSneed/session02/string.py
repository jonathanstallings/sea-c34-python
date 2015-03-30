def grandmas_email():
    """Sometimes my grandmother writes me e-mails in all
    CAPS. Can I write a function to change that?
    """

    what_grandma_wrote = u"I HOPE YOU ARE HAVING A NICE DAY, LOVE!!!"
    what_grandma_wrote = what_grandma_wrote[0] + what_grandma_wrote[1:-3].swapcase() + "!!!"

    print(what_grandma_wrote)

grandmas_email()




def diguise_me():
    """Can I write a function to diguise a message?"""


    message = u"The car key is next to the house key under the plant"
    message = message[:52].lower()
    message = message[::-1]
    new_message = ''.join(message.split(' '))

    print(new_message)

diguise_me()




def change_the_name(name, sequence_of_day):
    """How would I format a greeting in a welcome program?"""

    welcome =  u"Hello, {}. Have a good {}!".format(name, sequence_of_day)
    print(welcome)

change_the_name("Jack","evening")
