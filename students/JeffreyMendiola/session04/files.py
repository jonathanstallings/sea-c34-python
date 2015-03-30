# File Reading and Writing (2 questions)

# Question 1
import io


def read_a_file():
    """
    How do I read a file?
    Result:
        The file is printed.
    """
    examine_file = io.open('file_name.txt', encoding='utf-8')
    file_data = examine_file()
    examine_file.close()
    print(file_data)


read_a_file()


# Question 2


def raise_exception(user_input):
    """
    How do I read a particular line?
    Result:
        Line is printed.
    """
    examine_file = open("file_name.txt", encoding='utf-8')
    print("File name: %s" % examine_file)

    read_line = examine_file.readline(user_input)
    print "Read Line: %s" % (read_line)

    examine_file.close()

desired_line = int(raw_input("What line do you want to read? "))
raise_exception(desired_line)
