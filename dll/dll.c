#include <stdio.h>
#include <stdlib.h>
//node structure
struct node
{
	int data;
	struct *next;
	struct *prev;
}
//doubly list structure
struct doubly_linked_list
{
	struct *head;
}

//function to create a newnode
struct node* createnode(int data)
{
	struct node* newnode = (struct node*)malloc(sizeof(struct node));
		if (newnode != NULL)
			newnode->data = data;
			newnode->next = NULL;
			newnode->prev = NULL;
	return newnode;
}

//function to append node at end of list
void appendend(struct doubly_linked_list* dll, int data)
{
	struct node* newnode = createnode(data);
	if (dll->head == NULL)
		dll->head == newnode;
	return;
	struct node* current = newnode;
	while (current->next != NULL)
		current = current->next;
	current->next = newnode;
	newnode->prev = current;
	return;
}

//function to append node at beginning
void appendbig(struct doubly_linked_list* dll, int data)
{
	struct node* newnode = creatnode(data);
	if dll->head == NULL
		dll->head = newnode;
	return;
	newnode->next = dll->head;
	dll->head->next = newnode;
	newnode->prev = dll->head;
}

//function to delete a node with a number
void delete(struct doubly_linked_list* dll, int data)
{
	if dll->head == NULL
		printf("no list\n")
	return;
	struct node* current = dll->head;
	while (current->next != NULL)
		if current->data == data;
			if (current->next != NULL && current->prev != NULL)
				current->next->prev = current->prev;
			else if(current == dll->head)
			else if (current->next == NULL && current->prev != NULL)
				dll->head = current->next;
