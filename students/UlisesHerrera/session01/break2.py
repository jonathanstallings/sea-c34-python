def show_name_error():
    print(i_do_not_exist)


def show_type_error():
    error = 5 + "I can't be added to 5"


def show_syntax_error():
    eval("text = 'hmm did I forget something?")


def show_attribute_error():
    print("This is how you make a string uppercase, right?".UPPER())


if __name__ == "__main__":
    while True:
        errorType = raw_input("\n\nType a letter to see the error:\n"
                              "(N)ameError\n(T)ypeError\n(S)yntaxError\n(A)ttributeError:\n\n")

        errorType = errorType.upper()

        if errorType == "N":
            show_name_error()

        elif errorType == "T":
            show_type_error()
        
        elif errorType == "S":
            show_syntax_error()
        
        elif errorType == "A":
            show_attribute_error()