#include "lists.h"

/**
 * check_cycle - check if linked list is cycle.
 * @list: linked list.
 * Return: 0 if there is no cycle, 1 if there is a cycle.
 */
int check_cycle(listint_t *list)
{
	listint_t *head = list, *next = list->next;

	while (head && next)
	{
		if (next == head)
		{
			return (1);
		}
		next = next->next;
	}

	return (0);
}
