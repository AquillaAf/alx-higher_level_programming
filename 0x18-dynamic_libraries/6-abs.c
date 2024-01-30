#include "main.h"
/**
 * _abs - prints the absolute value of an integer
 * @c: absolute value of an integer
 * Return: c and 0
 *
 */

int _abs(int c)
{
	if (c < 0)
	{
		int av;

		av = c * -1;
		return (av);
	}
		return (c);
}
