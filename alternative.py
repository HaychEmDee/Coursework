capitals_string = "This is a string."
result = ""

# First, I want to make each letter alternate between upper and lower case.

for i in range(len(capitals_string)):
    if i % 2 == 0:
        result = result + capitals_string[i].upper()
    else:
        result = result + capitals_string[i].lower()
print(result)

# Now, I want to make each word alternate case.

split_string = capitals_string.split()
print(split_string)

alternating_string = ""

for i in range(len(split_string)):
    if i % 2 == 0:
        alternating_string += " " + split_string[i].upper()
    else:
       alternating_string += " " + split_string[i].lower()

print(alternating_string.strip())