#include "main.h"

/**
 * _strstr - locates a substring
 * @haystack: string to be checked 
 * @needle: its checkguide
 *
 * Return: needle 
 * NULL if non found
 */
char *_strstr(char *haystack, char *needle)
{
	
	int i;
	int j;

	for (i = 0; needle[i] != '\0'; i++)

		for (j = 0; haystack[j] >= '\0'; j++)

			if ((haystack[j] == needle[i]) && ((haystack[j] + 1) != (needle[i] + 1))) 
			{
				return (needle);
			}
			else 
				continue;

	return ('\0');
}
