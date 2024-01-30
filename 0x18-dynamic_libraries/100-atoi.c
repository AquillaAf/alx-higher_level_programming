int putchar (int i);
#include "main.h"
#include <stdio.h>
/**
 * _atoi - function that converts a string to integer
 * @s: argument that points to the string to be converted to integer
 *
 * Return: always 0
 */
int _atoi(char *s)
{
	int i;
	int k;
	int j;


	for (i = 0; s[i] != '\0'; i++)
	{	
		if (s[i] == '-')
		{
			k = '-';
			putchar (k);
		}
		if (s[i] == '+')
		{
			j = '+';
			putchar (j);
		}

		if ((s[i] >= 48) && (s[i] <= 57))
		{
			putchar (s[i]);
		}
	}
	for (k = 0; s[i] != '\0'; k++)
	{
		return (k);
	}
	for (j = 0; s[i] != '\0'; j++)
	{
		return (j);
	}
	if (k <	j)
	{
		putchar ('-');
	}
	else
	{
		return (s[i]);
	}
	return (0);
}	
