# This program reads an integer n entered by the user and prints a triangle of dollars.

n = int(input())
for columns in range(n):
    print(("$ " * (columns + 1)).rstrip())