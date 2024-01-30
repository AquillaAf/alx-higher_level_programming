#include "main.h"
/**
 * *_strcat - function that concatenates two strings
 * @dest: argument that points to the first string that the function expect
 * @src: argument that points to the second string that the function expect
 *
 * Return: always *dest
 */

char *_strcat(char *dest, char *src)
{

	int p = 0;
	int l = 0;

	while (dest[l])
	{
		l++;
	}
	while (src[p] != '\0')
	{
		dest[l + p] = src[p];
		p++;
	}
	dest[l + p] = '\0';
	return (dest);
}
