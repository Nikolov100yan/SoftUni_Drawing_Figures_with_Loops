# This program reads a positive integer n entered by the user and prints a rectangle of n * n asterisks on the console.

n = int(input())
char = "*"
rows = char * n
for columns in range(n):
    print(rows)
