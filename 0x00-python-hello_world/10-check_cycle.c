#include "lists.h"

/**
 * check_cycle - check if linked list is cycle.
 * @list: linked list.
 * Return: 0 if there is no cycle, 1 if there is a cycle.
 */
int check_cycle(listint_t *list)
{
	listint_t *head = list, *current = list->next;

	if (list == NULL || list->next == NULL)
	{
		return (0);
	}

	while (current)
	{
		if (current == head)
		{
			return (1);
		}
		current = current->next;
	}

	return (0);
}
