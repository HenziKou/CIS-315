"""
Henzi Kou
CIS 315: Intermediate Algorithms
Christopher Wison
25 May 2019

Assignment 6

Optimized for Python 2.7.15
"""

import sys
from collections import defaultdict

class Knapsack():

	def __init__(self, n, w):
		self.n = n						# Number of items
		self.w = w						# Target value
		self.itemCount = []				# Item count array
		self.items = defaultdict(list)	# Dictionary of all items and their respective values
		self.table = {}					# Return table

		for i in range(n + 1):
			# Initialize items dictionary and item count array
			self.items[i] = {}
			self.itemCount.append(0)


	def initTable(self):
		"""Initialize the return dictionary"""
		for i in range(self.w + 1):
			self.table[i] = [-1, -1]	# [min calories, number of item]

		return None

	def addItems(self, index, cost, calories, name):
		"""Initialize dictionary of all items and their respective values"""
		self.items[index][0] = cost
		self.items[index][1] = calories
		self.items[index][2] = name

		return None

	def updateItemCount(self):
		"""Updates the itemCount array"""
		# Create a temporary variable
		w = self.w

		if (self.table[w][1] == -1):
			print("Update item count failed.")
			sys.exit(1)

		while (w > 0):
			self.itemCount[self.table[w][1]] += 1	# Increment item count
			w -= self.items[self.table[w][1]][0]	# Decrement target value

		return None

	def mCal_Memoized(self, w):
		"""Memoized implementation"""
		# Initialize variables
		cur_val = 0
		min_item = 0
		min_val = float('INF')

		if (w < 0):
			return float('INF')
		if (w == 0):
			return 0
		if (self.table[w][0] != -1):
			return self.table[w][0]

		for i in range(0, self.n):
			# Recursive call 
			cur_val = self.mCal_Memoized(w - self.items[i][0]) + self.items[i][1]

			if (cur_val < min_val and cur_val >= 0):
				# Update new minimum value and the item amount
				min_val = cur_val
				min_item = i

		# Store item's minimum calories and amount
		self.table[w][0] = min_val
		self.table[w][1] = min_item

		return min_val

	def runMemoized(self):
		"""Call mCal_Memoized function"""
		# Store return value
		min_cal = self.mCal_Memoized(self.w)

		print("Memoized:")

		if (min_cal < float('INF')):
			# Minimum calories is found
			print("    Possible to spend exactly: {}".format(self.w))
			print("    Minimum calories: {}".format(min_cal))

			self.updateItemCount()

			for i in range(1, self.n):
				# Print items if they are added to knapsack
				if (self.itemCount[i] > 0):
					print("    {} {}".format(self.items[i][2], self.itemCount[i]))

		else:
			print("Not possible to spend exactly: {}".format(self.w))

		return None

	# TODO: NOT IMPLEMENTED CORRECTLY; IGNORE!
	def mCal_Iterative(self):
		"""Iterative implementation"""
		# Initialize variables
		min_val = float('INF')
		cur_val = -1
		min_item = -1
		cur_item = -1
		self.table[0][0] = 0

		for i in range(1, self.w + 1):
			for j in range(1, self.n + 1):
				# Loop through each element and perform calculations
				if (i - self.items[j][0] < 0):
					cur_val = -1
				elif (self.table[i - self.items[j][0]][0] < 0):
					cur_item = -1
				else:
					cur_val = self.items[j][1] + self.table[i - self.items[j][0]][0]
					cur_item = j

				if (cur_val < min_val and cur_val >= 0):
					# Update new minimum value and the item amount
					min_val = cur_val
					min_item = cur_item

				# Reset current value and the current item
				cur_val = -1
				cur_item = -1

			if (min_val == float('INF')):
				self.table[i][0] = -1
			else:
				self.table[i][0] = min_val

			self.table[i][1] = min_item
			min_val = float('INF')
			min_item = -1

		return self.table[self.w][0]
	# TODO: NOT IMPLEMENTED CORRECTLY; IGNORE!

	def runIterative(self):
		"""Call mCal_Iterative function"""
		min_cal = self.mCal_Iterative()

		print("Iterative:")

		if (min_cal < float('INF')):
			print("    Possible to spend exactly: {}".format(self.w))
			print("    Minimum calories: {}".format(min_cal))

			self.updateItemCount()

			for i in range(1, self.n):
				# Print items if they are added to knapsack
				if (self.itemCount[i] > 0):
					print("    {} {}".format(self.items[i][2], self.itemCount[i]))

		else:
			print("Not possible to spend exactly: {}".format(self.w))

		return None


def main():
	# Read from standard input
	try:
		f = sys.stdin
	except:
		print("ERROR: No input file declared!")
		sys.exit(1)

	# Store first line as number of items
	n = int(f.readline().strip())

	# Store second line as target value
	w = int(f.readline().strip())

	# Set maximum recursion depth
	sys.setrecursionlimit(w)

	# Initialize knapsack algorithm
	k = Knapsack(n, w)

	# Read subsequent lines
	for i in range(n):
		data = f.readline().strip().split()
		cost = int(data[0])
		calories = int(data[1])
		name = data[2]

		# Add values to respective variable names
		k.addItems(i, cost, calories, name)

	print("")

	# Initialize table
	k.initTable()

	# Implement memoized algorithm
	k.runMemoized()

	# Implement iterative algorithm
	#k.runIterative()

	print("")

	return None


if __name__ == "__main__":
	main()


