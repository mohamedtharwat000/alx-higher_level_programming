#include "lists.h"

/**
 * check_cycle - check if linked list is cycle.
 * @list: linked list.
 * Return: 0 if there is no cycle, 1 if there is a cycle.
 */
int check_cycle(listint_t *list)
{
	listint_t *current_node = list, *next_node = list;

	while (current_node && next_node)
	{
		current_node = current_node->next;
		next_node = next_node->next->next;
		if (current_node == next_node)
		{
			return (1);
		}
	}

	return (0);
}
