# This program adds all the numbers the user types in together, until they type -1, at which point it prints out the average.

def average(lst):
        return sum(lst) / len(lst)

user_number = int(input("Please type a whole number."))
number_list = [ ]
number_list.append(user_number)

while user_number != -1:
        user_number = int(input("Now type another whole number. Type -1 to finish."))
        number_list.append(user_number)
        print(number_list) # This is for debugging purposes, to check if the list is updating correctly.
        if user_number == -1:
                number_list.pop()
                break
# An "else" statement isn't necessary in this code.

list_average = average(number_list)
print("The average of all your numbers is " + str(list_average) + ".")
