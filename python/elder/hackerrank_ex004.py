# Task
# Given an integer, , perform the following conditional actions:
#
# If  is odd, print Weird
# If  is even and in the inclusive range of  to , print Not Weird
# If  is even and in the inclusive range of  to , print Weird
# If  is even and greater than , print Not Weird
# Input Format
#
# A single line containing a positive integer, .
#
# Constraints
#
# Output Format
#
# Print Weird if the number is weird. Otherwise, print Not Weird.
# Sample Input 0
# 3
# Sample Output 0
# Weird

n = int(input())
if n % 2 != 0 or 5 < n < 21:
    print("Weird")
else:
    print("Not Weird")
