"""
Henzi Kou
Assignment 0
CIS 315
Chris Wilson

5 April 2019
"""

import sys

def main():
	# Read from standard input
	try:
		f_in = sys.stdin
	except:
		print("No input file declared.")
		sys.exit(1)

	# Store value of first line as number of arguments
	n = int(f_in.readline().strip())

	for i in range(n):
		# Take respective integers and perform addition and multiplication
		data = f_in.readline().strip().split()
		num1 = int(data[0])
		num2 = int(data[1])

		print("{} {}".format(num1 + num2, num1 * num2))


if __name__ == "__main__":
	main()
       
