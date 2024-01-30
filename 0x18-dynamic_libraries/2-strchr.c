#include "main.h"

/**
 * _strchr -  locates a character in a string.
 * @s: string to be checked
 * @c: character to be found
 *
 * Return: s
 * if c isnt found - NULL
 */
char *_strchr(char *s, char c)
{
	int p;

	for (p = 0; s[p] >= '\0'; p++)
	{
		if (s[p] == c)
		{
			return (s + p);
		}
	}
	return ('\0');
}
