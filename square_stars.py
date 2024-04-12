# This program reads a positive integer n entered by the user and prints a square of n * n asterisks on the console.
# There are spaces between asterisks.

n = int(input())
char = "*"
space = " "
rows = (char+space) * n
for columns in range(n):
    print(rows.rstrip())