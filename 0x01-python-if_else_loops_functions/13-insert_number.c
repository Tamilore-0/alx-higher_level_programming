#include "lists.h"
#include <stdlib.h>

/**
* insert_node - Function that inserts a node
* @head: A pointer to a pointer to the head of the list
* @number: The value of the new node to be inserted
* Return: listint_t
*/
listint_t *insert_node(listint_t **head, int number)
{
	listint_t *current = *head;
	listint_t *node, *temp = NULL;

	node = malloc(sizeof(listint_t));
	if (node == NULL)
	{
		return (NULL);
	}
	node->n = number;
	node->next = NULL;

	if (*head == NULL || number < (*head)->n)
	{
		node->next = *head;
		*head = node;
		return (node);
	}

	while (current->next != NULL && current->next->n < number)
	{
		current = current->next;
	}

	temp = current->next;
	current->next = node;
	node->next = temp;

	return (node);
}
