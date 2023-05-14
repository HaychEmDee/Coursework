# This program prints out an additional asterisk each time, until it reaches five.

counter = 1

for asterisk in range(1, 6):
    print("*" * counter)
    counter += 1
    if counter == 1:
        break
