#include "main.h"

/**
 * _strpbrk - searches a string for any of a set of bytes.
 * @s: pointer to bytes of strings s
 * @accept: pointer to the string ti be checkguided
 *
 * Return: pointer s if it matches accept
 * NULL if it doesnt
 */
char *_strpbrk(char *s, char *accept)
{
	int i;
	int j;

	for (i = 0; s[i] != '\0'; i++)

		for (j = 0; accept[j] != '\0'; j++)

			if (accept[j] == s[i])
			{
				return (s + i);
			}
	return ('\0');
}
