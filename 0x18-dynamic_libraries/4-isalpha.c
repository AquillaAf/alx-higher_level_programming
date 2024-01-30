#include "main.h"
/**
 * _isalpha - chech for alphabet character
 * @c: is a letter either lower case or upper case
 *
 * Return: 1 if its a letter and 0 othewise
 */

int _isalpha(int c)
{

	if ((c >= 65 && c <= 90) || (c >= 97 && c <= 122))
	{
		return (1);
	}
	else
	{
		return (0);
	}

}
