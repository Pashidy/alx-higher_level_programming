/* listint.h */
#ifndef LISTINT_H
#define LISTINT_H

/* Structure for a singly linked list */
struct listint_s
{
	int data;
	struct listint_s *next;
};

typedef struct listint_s listint_t;

/* Function to check if a singly linked list has a cycle */
int check_cycle(listint_t *list);

#endif /* LISTINT_H */

