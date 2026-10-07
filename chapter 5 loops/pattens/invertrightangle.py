n = 5

# Outer loop controls the rows
for i in range(n + 1):

    # Inner loop controls the columns
    for j in range(n + 1):

        # Print '*' when the column index is greater than the row index
        if j > i:
            print("* row " + str(i), end="")

        # Otherwise print a space
        else:
            print(" ", end="")

    # Move to the next line after each row
    print()