#include "main.h"

/**
 * _memcpy - unction that copies memory area.
 * @dest: destination memory area
 * @src: source memory area
 * @n: number of block to be assigned
 *
 * Return: dest
 */
char *_memcpy(char *dest, char *src, unsigned int n)
{
	unsigned int p;

	for (p = 0; p < n; p++)
	{
		dest[p] = src[p];
	}
	return (dest);
}
