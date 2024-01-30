#include "main.h"

/**
 * _memset - function that fills memory with a constant byte.
 * @s: parameter that points to the memory address of the memblock
 * @b: constant byte
 * @n: number of bytes to fill with a constant
 *
 * Return: s
 */
char *_memset(char *s, char b, unsigned int n)
{
	unsigned int p;

	for (p = 0; p < n; p++)
	{
		s[p] = b;
	}
	return (s);
}
