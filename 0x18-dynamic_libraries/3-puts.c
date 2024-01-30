int _putchar(char c);
#include "main.h"
/**
 *  _puts - function to print string
 *  @str: statment to print string
 *
 */
void _puts(char *str)
{
	int j = 0;

	while (str[j])
	{
		_putchar(str[j]);
		j++;
	}
	_putchar('\n');

}
