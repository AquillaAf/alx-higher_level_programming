#include "main.h"

/**
 * _strspn - function that gets the length of a prefix substring.
 * @s: points to the string to be checked
 * @accept: consist of all the string to be checked for
 *
 * Return: b
 */
unsigned int _strspn(char *s, char *accept)
{
	int j;
	int i;
	int b = 0;

	for (j = 0; s[j] != '\0'; j++)
	{

		for (i = 0; accept[i] != '\0'; i++)

			if (s[j] == accept[i])
			{
				b++;
				break;
			}
			else if (accept[i + 1] == '\0')
			{
				return (b);
			}
	}
	return (0);
}
