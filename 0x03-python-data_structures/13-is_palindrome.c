#include "lists.h"

/**
 * is_palindrome - entry point
 * @head: a double pointer that points to a linked list
 * Return: 0 if it is not a palindrome, 1 if it is a palindrome
 */
int is_palindrome(listint_t **head)
{
	listint_s *current = *head;
	int rev_num;

	int remainder = 0;

	int num;

	if (*head == NULL)
	{
		return (1);
	}

	while (current != NULL)
	{
		rev_num = 0;
		num = current->n;
		while (num != 0)
		{
			remainder = num % 10;
			rev_num = rev_num * 10 + remainder;
			num /= 10;
		}
		if (current->n != rev_num)
			return (0);
		current = current->next;
	}
	return (1);
}
