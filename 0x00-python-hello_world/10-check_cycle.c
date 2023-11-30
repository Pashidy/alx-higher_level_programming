#include <stdio.h>
#include <stdlib.h>
#include <listint.h>

/**
 * check_cycle - Checks if a singly linked list has a cycle
 * @list: Pointer to the head of the linked list
 *
 * Return: 0 if there is no cycle, 1 if there is a cycle
 */
int check_cycle(listint_t *list)
{
	if (list == NULL || list->next == NULL)
		return (0);

	listint_t *slow = list;
	listint_t *fast = list->next;

	while (fast != NULL && fast->next != NULL)
	{
		if (slow == fast)
			return (1);
		slow = slow->next;
		fast = fast->next->next;
	}

	return (0);
}

/**
 * main - Entry point
 *
 * Return: Always 0 (Success)
 */
int main(void)
{
	listint_t *head = (listint_t *)malloc(sizeof(listint_t));
	head->data = 1;
	head->next = (listint_t *)malloc(sizeof(listint_t));
	head->next->data = 2;
	head->next->next = (listint_t *)malloc(sizeof(listint_t));
	head->next->next->data = 3;
	head->next->next->next = head;

	int hasCycle = check_cycle(head);
	if (hasCycle)
		printf("The linked list has a cycle.\n");
	else
		printf("The linked list does not have a cycle.\n");

	free(head->next->next);
	free(head->next);
	free(head);

	return (0);
}

