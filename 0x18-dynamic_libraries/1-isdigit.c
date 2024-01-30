#include "main.h"
/**
 * _isdigit - to check if a character is a digit
 * @c: the character to be checked
 *
 * Return: 1 if its a digit otherwise 0
 */
int _isdigit(int c)
{
	if (c >= 48 && c <= 57)
	{
		return (1);
	}
	else
	{
		return (0);
	}
}

