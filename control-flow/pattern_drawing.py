#3. Drawing Patterns with Nested Loops

#Prompt User for Pattern Size
count = 0
pattern_size = int(input("Enter the size of the pattern: "))

#Draw the Pattern
while count != pattern_size:
    for i in range (1,5):
        print("*", end="")
    count += 1
    print("")

