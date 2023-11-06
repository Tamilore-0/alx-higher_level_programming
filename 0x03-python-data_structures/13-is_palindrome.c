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

	if (*head == NULL)
	{
		return (1);
	}

	while (current != NULL)
	{
		rev_num = reverseInteger(current->n);
		if (current->n != rev_num)
			return (0);
		current = current->next;
	}
	return (1);
}

/**
* reverseInteger - Entry point
* @num: Number to be reversed
* Return: reversed number
*/
int reverseInteger(int num)
{

	int reversed = 0;

	while (num != 0)
	{
		int remainder = num % 10;

		reversed = reversed * 10 + remainder;
		num /= 10;
	}

	return (reversed);
}
