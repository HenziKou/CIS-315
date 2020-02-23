"""
Henzi Kou
CIS 315: Intermediate Algorithms
Christopher Wilson
Assignment 2

21 April 2019
"""

import sys

class Graph:
	def __init__(self, n):
		self.v = n	# Set of vertices
		self.graph = {}

		for i in range(1, n + 1):
			# Initialize graph
			self.graph[i] = {}

	def addEdge(self, v1, v2):
		"""Add an edge to the graph with weight of 1."""
		self.graph[v1][v2] = 1

		return

	def shortestPath(self):
		"""Finds the shortest path from node 1 to node n, in an unweighted
		directed acyclic graph. Overall run time is Theta(V + E)."""
		visited = []
		table = {}
		x = float('inf')

		# Topologically sort the graph into a table holding values of distance and occurrence.
		# Set distance for all vertices besides the source, to infinity.
		for i in range(1, self.v + 1):
			table[i] = [x, 0]

		# Initialize the distance to the source node to 0
		# Set minimum number of shortest paths to 1
		table[1][0] = 0
		table[1][1] = 1
		visited.append(1)

		for u in range(1, self.v + 1):
			# For each vertex u, taken in topologically sorted order
			for v, w in self.graph[u].items():
				# Grab adjacent vertex v and the weight of edge(u,v)
				if (v not in visited):
					visited.append(v)
				
				# Perform relaxation step on edge (u,v)
				if (table[v][0] > table[u][0] + w):
					table[v][1] = 0
					table[v][0] = table[u][0] + w
					table[v][1] += table[u][1]

				# If two paths of the same length, then add to the total number
				elif (table[u][0] + w == table[v][0]):
					table[v][1] += table[u][1]

		return table

	def longestPath(self):
		"""Finds the longest path from node 1 to node n, in an unweighted
		directed acyclic graph. Overall run time is Theta(V + E)."""
		visited = []
		table = {}

		# Topologically sort the graph into a table holding values of distance and occurrence.
		# Set distance for all vertices to 0.
		for i in range(1, self.v + 1):
			table[i] = [0, 0]

		# Set minimum number of longest paths to 1
		table[1][1] = 1
		visited.append(1)

		for u in range(1, self.v + 1):
			# For each vertex u, taken in topologically sorted order
			for v, w in self.graph[u].items():
				# Grab adjacent vertex v and the weight of edge(u,v)
				if (v not in visited):
					visited.append(v)

				# Perform relaxation step on edge (u,v)
				if (table[u][0] + w > table[v][0]):
					table[v][1] = 0
					table[v][0] = table[u][0] + w
					table[v][1] += table[u][1]

				# If multiple paths of the same length, then add to the total number
				elif (table[u][0] + w == table[v][0]):
					table[v][1] += table[u][1]

		return table


def main():
	# Read file from standard input
	try:
		f = sys.stdin
	except:	
		print("ERROR: No input file declared.")
		sys.exit(1)

	# Store first line as value for N nodes
	n = int(f.readline().strip())

	# Store second line as value for M edges
	m = int(f.readline().strip())

	# Initialize graph
	g = Graph(n)

	# Read subsequent lines
	for i in range(m):
		data = f.readline().strip().split()
		u = int(data[0])
		v = int(data[1])

		# Add edge from node i to node j
		g.addEdge(u, v)

	# Find shortest path and the number of distinct ones of the same length
	table_sp = g.shortestPath()

	# Find longest path and the number of distinct ones of the same length
	table_lp = g.longestPath()

	# Print shortest path results
	print("Shortest path: {}".format(table_sp[n][0]))
	print("Number of short paths: {}".format(table_sp[n][1]))

	# Print longest path results
	print("Longest path: {}".format(table_lp[n][0]))
	print("Number of long paths: {}".format(table_lp[n][1]))

	return



if __name__ == "__main__":
	main()

