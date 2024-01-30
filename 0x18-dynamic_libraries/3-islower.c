#include "main.h"
/**
 * _islower - Entry point
 * @c: 'check for lowercase letter'
 * Return: 1 for upercase letter and 0 for any other
 */

int _islower(int c)
{

	if (c >= 97 && c <= 122)
	{
		return (1);
	}
	else
	{
		return (0);
	}

}
