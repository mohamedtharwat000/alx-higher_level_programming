#include "lists.h"

/**
 * check_cycle - check if linked list is cycle.
 * @list: linked list.
 * Return: 0 if there is no cycle, 1 if there is a cycle.
 */
int check_cycle(listint_t *list)
{
	listint_t *current = list, *head = list;

	while (current && current->next)
	{
		current = current->next;
		if (current == head)
		{
			return (1);
		}
	}
	return (0);
}