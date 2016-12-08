#! /usr/bin/env python
# Perform various bit shifts within a matrix

class Matrix:
    """ A matrix, or nested arrays of equal length """
    rows = 0
    cols = 0

    # Build up a matrix of values:
    def __init__(self, x, y, val):
        self.matrix = []
        self.rows = y
        self.cols = x
        for i in range(y):
            self.matrix.append([val]*x)

    # Turn on all cells in an x*y rectangle from (0,0):
    def rect(self, cols, rows):
        for row in range(rows):
            for col in range(cols):
                self.matrix[row][col] = 1

    # Shift cells right by some amount, in row r (with wrapping):
    def shift_row(self, r, amount):
        self.matrix[r] = self.matrix[r][-amount:] + self.matrix[r][:-amount]

    # Shift cells down by some amount, in column c (with wrapping):
    def shift_col(self, c, amount):
        # Extract column values:
        column = [self.matrix[r][c] for r in range(len(self.matrix))]
        # Perform wrapped shift in place:
        column = column[-amount:] + column[:-amount]
        # Rewrite to matrix:
        for row in range(len(self.matrix)):
            self.matrix[row][c] = column[row]

    # Count the number of times a specific value appears in the matrix:
    def count_values(self, val):
        count = 0
        for r in range(self.rows):
            for c in range(self.cols):
                if self.matrix[r][c] == val:
                    count = count + 1
        return count

    # Print nicely:
    def printme(self):
        for row in self.matrix:
            print row


# Process input:
n = Matrix(50,6,0)
with open('day08_input.txt') as fp:
    for line in fp:
        # Parse line to figure out which function to apply:
        if line[:4] == "rect":
            values = line.split()[1].split("x")
            n.rect(int(values[0]),int(values[1]))

        elif line[:6] == "rotate":
            words = line.split()
            x = words[2].split("=")[-1]
            amount = words[-1]

            if line[7:10] == "row":
                n.shift_row(int(x), int(amount))

            elif line[7:10] == "col":
                n.shift_col(int(x), int(amount))

n.printme()
print n.count_values(1)
