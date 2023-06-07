#include "lists.h"

/**
 * insert_node - Inserts a new node into a sorted linked list
 * @head: Pointer to the head of the linked list
 * @number: Value to be inserted into the new node
 *
 * Return: Pointer to the newly inserted node, or NULL on failure
 */
listint_t *insert_node(listint_t **head, int number)
{
	listint_t *current_node = *head, *new_node = NULL;

	new_node = malloc(sizeof(listint_t));
	if (!new_node)
	{
		return (NULL);
	}

	new_node->n = number;
	new_node->next = NULL;

	if (!current_node || current_node->n >= number)
	{
		new_node->next = current_node;
		*head = new_node;
		return (new_node);
	}

	while (current_node->next && current_node->next->n < number)
	{
		current_node = current_node->next;
	}

	new_node->next = current_node->next;
	current_node->next = new_node;

	return (new_node);
}
