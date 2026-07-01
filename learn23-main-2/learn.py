#
# Python - learning - a place to start
#
import pandas as pd
# note: install pandas and openpyxl packages

def concatenate_strings(string1, string2, string3, string4, string5):
    """Concatenates five strings"""
    return string1 + string2 + string3 + string4 + string5


def main():
    # Get user input
    string1 = input("Enter the first string: ")
    string2 = input("Enter the second string: ")
    string3 = input("Enter the third string: ")
    string4 = input("Enter the fourth string: ")
    string5 = input("Enter the fifth string: ")

    # Concatenate the strings
    result = concatenate_strings(string1, string2, string3, string4, string5)

    # Print the result
    print("The concatenated string is:", result)

#
# example of 'list comprehension' - making a new list from an old list
#
def do_list1():
    print("Running do_list1()...\n")
    # here is list
    list1 = ['dog','cat','squirrel']
    print(f"original list1:\n{list1}\n")

    # here is an example of using a for loop to make a new list
    list2 = [] # empty list
    for animal in list1:
        list2.append("hello, " + animal + "!")
    print(f"new list2:\n{list2}\n")

    # notice that list2 is derived from list1
    # this pattern is often needed
    # there's another way to do it... see do_list2()

def do_list2():
    print("Running do_list2()...\n")
    # here is an example of using 'list comprehension'
    list1 = ['dog','cat','squirrel']
    print(f"original list1:\n{list1}\n")

    list2 = ["hello, " + animal + "!" for animal in list1]
    # ^ this may not seem like a big deal right now
    # but notice how compact this statement is
    # the output is identical
    print(f"new list2:\n{list2}\n")

def do_list3():
    print("Running do_list3()...\n")

    df = pd.read_excel("doctor schedule-southwest.xlsx")
    df = df.query("Doctor == 'Deshpande' and Service == 'Hospital'")
    print(f"df query:\n", df, "\n")

    print("All weeks:\n",[f"Week_{week}" for week in df.Week],"\n")
    print("All Mondays:\n",[week for week in df.Mon],"\n")

def main():
    do_list1()
    do_list2()
    do_list3()

# Call the main function
if __name__ == '__main__':
    main()
