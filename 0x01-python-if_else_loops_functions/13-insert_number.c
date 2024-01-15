#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include "lists.h"
/**
 * insert_node - inserts a number into a sorted singly linked list
 * @head: pointer to the head of the linked list
 * @number: pointer to an int
 * Return: address of the new node or NULL if it failed
 */
listint_t *insert_node(listint_t **head, int number)
{
	listint_t *current = *head;
	listint_t *prev = NULL;
	listint_t *new_node;

	if (head == NULL)
	{
		return (NULL);
	}
	new_node = malloc(sizeof(listint_t));
	if (new_node == NULL)
	{
		return (NULL);
	}
	new_node->number = number;
	new_node->next = NULL;

	while (current != NULL && current->number < number)
	{
		prev = current;
		current = current->next;
	}
	if (prev == NULL)
	{
		new_node->next = *head;
		*head = new_node;
	}
	else
	{
		prev->next = new_node;
		new_node->next = current;
	}
	return(new_node);
}
