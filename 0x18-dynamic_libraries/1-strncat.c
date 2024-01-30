#include "main.h"
/**
 * *_strncat - function that points to two string and cancatenate.
 * @dest: points to destination of character position
 * @src: points to the source string
 * @n: the number of possible string to cancatenate
 *
 * Return: pointe to destination string
 */
char *_strncat(char *dest, char *src, int n)
{
	int p = 0;
	int j = 0;

	while (dest[j])
	{
		j++;
	}
	while (p < n && src[p] != '\0')
	{
		dest[j] = src[p];
		j++;
		p++;
	}
	dest[j] = '\0';
	return (dest);
}
