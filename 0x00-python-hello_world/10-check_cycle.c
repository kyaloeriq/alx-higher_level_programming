#include <stdlib.h>
#include <stdio.h>
#include "lists.h"
/**
 * check_cycle - checks if a singly linked list has a cycle
 * @list: linked list head
 * Return: 0 if there is no cycle, 1 if there is
 */
int check_cycle(listint_t *list)
{
	listint_t *slw_ptr = list;
	listint_t *fst_ptr = list;

	while (slw_ptr != NULL && fst_ptr != NULL && fst_ptr->next != NULL)
	{
		slw_ptr = slw_ptr->next;
		fst_ptr = fst_ptr->next->next;
		if (slw_ptr == fst_ptr)
		{
			return (1);/*Cycle detected*/
		}
	}
	return (0);/*No cycle found*/
}
