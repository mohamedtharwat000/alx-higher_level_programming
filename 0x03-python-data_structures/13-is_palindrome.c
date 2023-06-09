#include "lists.h"

/**
 * is_palindrome - function checks if a singly linked list is a palindrome.
 * @head: pointer to linked list head node
 *
 * Return: 0 if it is not a palindrome, 1 if it is a palindrome
 *
 * An empty list is considered a palindrome
 */
int is_palindrome(listint_t **head)
{
	listint_t *current = *head;
	long unsigned int i = 0, num_of_nodes = 0;
	int *list_cmp = NULL;

	if (head == NULL)
	{
		return (0);
	}

	if (*head == NULL)
	{
		return (1);
	}

	while (current)
	{
		list_cmp = realloc(list_cmp, (num_of_nodes + 1) * sizeof(int));
		list_cmp[num_of_nodes] = current->n;
		current = current->next;
		num_of_nodes++;
	}

	while (i <= num_of_nodes / 2)
	{
		if (list_cmp[i] != list_cmp[num_of_nodes - 1 - i])
		{
			free(list_cmp);
			return (0);
		}
		i++;
	}

	free(list_cmp);
	return (1);
}
