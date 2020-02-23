/*
Henzi Kou
Assignment 0
CIS 315
Chris Wilson

5 April 2019
*/

#include <stdio.h>
#include <stdlib.h>
#include <string.h>

int main(int argc, char *argv[])
{
    // Initialize variables
    FILE *f_in, *f_out;
    int value, num;
    char c;

    // Argument count must have 2 values
    if (argc != 2)
    {
	printf("Usage: %s <file1>\n", argv[0]);
	exit(EXIT_FAILURE);
    }

    // Open input file
    f_in = fopen(argv[1], "r");

    if (!f_in)
    {
	perror("Error: File open failed!\n");
	exit(EXIT_FAILURE);
    }

    // Store first line as number of arguments
    fscanf(f_in, "%d", &value);
    printf("First line = %d\n", value);

    // Read subsequent lines and perform operations
/*
    while ((c = fgetc(f_in)) != EOF)
    {
	fscanf(f_in, "%d", &num);
	printf("%d", num);

    }
*/

    for (int i = 0; i < value; i++)
    {
	fseek(f_in, i, SEEK_SET);
	num = ftell(f_in);
	printf("%d\n", num);
    }

    fclose(f_in);

    return 0;
}
