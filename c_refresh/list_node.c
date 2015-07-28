#include <stdio.h>
#include <stdlib.h>
#define N 10

struct list_node{
  int val;
  struct list_node *next;
};

struct list_node* populate_list(int num);
struct list_node* re_populate_list(struct list_node *head_node, int num);
void print_list(struct list_node *list);

struct list_node* populate_list(int num) {
  struct list_node *head;
  struct list_node *last_node;
  int i;

  for (i = 1; i <= num; ++i) {
    struct list_node* new_node = (struct list_node*)malloc(sizeof(struct list_node));
    //(*new_node).val = i;
    new_node->val = i;
    //    new_node->next = NULL;

    if (i == 1) {
      head = new_node;
      last_node = new_node;
    }
    else {
      last_node->next = new_node;
      last_node = new_node;
    }
  }
  last_node->next = NULL;

  return head;
}

int main(void)
{
  //  struct list_node list = malloc(N * (sizeof(int) + sizeof(int *)));
  struct list_node *head = (struct list_node*)malloc(sizeof(struct list_node));;
  head -> next = NULL;
  //struct list_node *list = populate_list(N);
  struct list_node *list2 = re_populate_list(head, N);
   
  print_list(list2);

  return 0;
}

void print_list(struct list_node* list)
{
  while (list != NULL)
    {
      printf("%d\n", list->val);
      list = list->next;
    }
}

struct list_node* re_populate_list (struct list_node *head_node, int num)
{
  struct list_node *new_node = (struct list_node*)malloc(sizeof(struct list_node));

  if (num <= 0)
    return head_node ;
  
  new_node->val = num;
  new_node -> next = head_node;
  re_populate_list(new_node, num - 1);
}
/*
list_node * populate_list(int num)
{
  if (num == 0)
    return &list;

  struct list_node list = malloc(sizeof(int) + sizeof(list_node *));
  if (num == N)
    list.val = 1;
  else
    list.val += 1;
  list.(*next) = populate_list(num - 1);
  
}
*/
