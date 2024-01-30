#include "main.h"
/**
 * _strncpy - unctions that copies a string
 * @dest: an argument that points to position of a destination string
 * @src: an argument that points to position of a source string
 * @n: the number of character to copy
 * Return: dest
 */
char *_strncpy(char *dest, char *src, int n)
{
	int k;

	k = 0;
	while (k < n && src[k] != '\0')
	{
		dest[k] = src[k];
		k++;
	}
	while (k < n)
	{
		dest[k] = '\0';
		k++;
	}
	return (dest);
}

