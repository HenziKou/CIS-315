/*
Henzi Kou
CIS 315: Intermediate Algorithms
Christopher Wilson
Assignment 6

28 May 2019
*/

#include <iostream>
#include <stdlib.h>
#include <string>
#define INF 1000000

using namespace std;

typedef struct knapsackList
{
	int min_cal;
	int item;
} knapsackList;

typedef struct itemsList
{
	int cost;
	int calories;
	string name;
} itemsList;


/* Initialize global variables */
static int N = 0;					// Number of items
static int W = 0;					// Target amount
static itemsList *items = NULL;		// List of food items
static knapsackList *knap = NULL;	// Knapsack list
static int *itemCount = NULL;		// Item count


/* Initialize array */
void initialize()
{
	for (int i = 0; i <= W; i++)
	{
		// Set all parameter values to -1
		knap[i].min_cal = -1;
		knap[i].item = -1;
	}

	for (int j = 0; j <= N; j++)
		// Set selected menu items to none
		itemCount[j] = 0;

	return;
}

/* Helper function to update the item count */
void updateCount()
{
	int w = W;

	if (knap[w].item == -1)
	{
		cout << "Update item count has failed!" << endl;
		exit(EXIT_FAILURE);
	}

	while (w > 0)
	{
		itemCount[knap[w].item]++;
		w -= items[knap[w].item].cost;
	}

	return;
}
	
/* Memoized implementation. Using example pseudo-code provided in pdf. */
int mCal(int w)
{
	int cur_val = 0;
	int min_item = 0;

	if (w < 0)
		return INF;
	if (w == 0)
		return 0;
	if (knap[w].min_cal != -1)
		return knap[w].min_cal;

	int min_val = INF;

	for (int i = 0; i < N; i++)
	{
		cur_val = mCal(w - items[i].cost) + items[i].calories;

		if ((cur_val < min_val) && (cur_val >= 0))
		{
			min_val = cur_val;
			min_item = i;
		}
	}

	knap[w].min_cal = min_val;
	knap[w].item = min_item;

	return min_val;
}

/* Iterative Implementation */
int mCalIterative(int w)
{
	// Initialize variables
	int min_val = INF;
	int min_item = -1;
	int cur_item = -1;
	int cur_val = -1;
	knap[0].min_cal = 0;

	for (int i = 1; i <= W; i++)
	{
		for (int j = 1; j <= N; j++)
		{
			// 
			if (i - items[j].cost < 0)
				cur_val = -1;
			else if (knap[i - items[j].cost].min_cal < 0)
				cur_item = -1;
			else {
				cur_val = items[j].calories + knap[i - items[j].cost].min_cal;
				cur_item = j;
			}

			if ((cur_val < min_val) && (cur_val > 0))
			{
				min_val = cur_val;
				min_item = cur_item;
			}

			cur_val = -1;
			cur_item = -1;
		} // End of inner for loop

		if (min_val == INF)
			knap[i].min_cal = -1;
		else
			knap[i].min_cal = min_val;

		knap[i].item = min_item;
		min_val = INF;
		min_item = -1;
	} // End of outer for loop

	return knap[W].min_cal;
}

/* Caller function for memoized method algorithm */
void memoized()
{
	int min_cal = INF;
	min_cal = mCal(W);

	cout << "Memoized implementation: " << endl;

	if (min_cal < INF)
	{
		cout << '\t' << "Possible to spend exactly: " << W << endl;
		cout << '\t' << "Minimum calories: " << min_cal << endl;

		updateCount();

		for (int i = 1; i <= N; i++)
		{
			if (itemCount[i] > 0)
				cout << '\t' << items[i].name << " " << itemCount[i] << endl;
		}
	}

	else
		cout << "Not possible to spend exactly: " << W << endl;

	return;
}

/* Caller function for iterative method algorithm */
void iterative()
{
	int min_cal = INF;
	min_cal = mCalIterative(W);

	cout << "Iterative implementation: " << endl;

	if ((min_cal < INF) && (min_cal != -1))
	{
		cout << '\t' << "Possible to spend exactly: " << W << endl;
		cout << '\t' << "Minimum calories: " << min_cal << endl;

		updateCount();

		for (int i = 1; i <= N; i++)
		{
			if (itemCount[i] > 0)
				cout << '\t' << items[i].name << " " << itemCount[i] << endl;
		}
	}

	else
		cout << "Not possible to spend exactly: " << W << endl;

	return;
}


/* Main driver funtion uses STANDARD INPUT */
int main()
{
	// Pass in first two lines to respective variables
	cin >> N >> W;

	// Initialize variables, pointers and functions
	items = new itemsList[N + 1];
	itemCount = new int[N + 1];
	knap = new knapsackList[W + 1];
	initialize();

	// Read subsequent lines and assign variables to respective values
	for (int i = 0; i < N; i++)
		cin >> items[i].cost >> items[i].calories >> items[i].name;

	cout << endl;

	// Call functions to perform algorithm implementations
	iterative();
	initialize();

	cout << endl;

	memoized();

	delete[] items;
	delete[] itemCount;
	delete[] knap;
}



