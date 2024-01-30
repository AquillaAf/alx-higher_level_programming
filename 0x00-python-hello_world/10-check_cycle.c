#include "lists.h"
#include <stdio.h>
/**
 * check_cycle - check a linked list if its in cycle
 * @list: a pointer to the linked list
 *
 * Return: 1 if its a cycle and 0 if not
 */
int check_cycle(listint_t *list)
{
	listint_t *traverse;

	if (list == NULL)
	{
		printf("1 node in list");
		return (-1);
	}
	traverse = list;
	while (traverse->next != NULL)
	{
		if (traverse->next == list)
		{
			return (1);
		}
	}
	return(0);
}
