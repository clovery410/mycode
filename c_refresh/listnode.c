#include <stdio.h>
#include <stdlib.h>
#define N 5

struct ListHead {
  struct ListNode* next;
};

struct ListNode {
  int val;
  struct ListNode* next;
};

struct ListHead* create_list (int n);
void print_list (struct ListHead* head);
void delete_node (struct ListHead* head, int value);
void insert_node (struct ListHead* head, int value, int new_node);
void reverse_list (struct ListHead* head, int num);
struct ListNode* reverse_list2 (struct ListHead* head, int num);
struct ListNode* reverse_list_recursive2 (struct ListHead* head);
struct ListHead* reverse_list_recursive (struct ListHead* head);
void switch_list (struct ListHead* head);

int main (void){
  struct ListHead* head_node = create_list(N);
  print_list(head_node);
  /* reverse_list(head_node, N); */
  /* print_list(head_node); */
  switch_list(head_node);
  print_list(head_node);
  reverse_list2(head_node, N);
  print_list(head_node);
  /* delete_node(head_node, 50); */
  /* print_list(head_node); */
  
  /* insert_node(head_node, 0, 101); */
  /* print_list(head_node); */
  
  return 0;
}

struct ListHead* create_list (int n) {
  int i;
  struct ListHead* head;
  struct ListNode* tail;
  struct ListNode* first_node;

  head = (struct ListHead*)malloc(sizeof(struct ListHead));
  if (n <= 0)
    head->next = NULL;
  else {
    first_node = (struct ListNode*)malloc(sizeof(struct ListNode));
    first_node->val = 1;
    first_node->next = NULL;
    head->next = first_node;
    tail = first_node;
  }
  
  for (i = 1; i < n; ++i) {
    struct ListNode *newnode = (struct ListNode*)malloc(sizeof(struct ListNode));
    newnode->val = i + 1;
    newnode->next = NULL;
    tail->next = newnode;
    tail = newnode;
  }

  return head;
}

void delete_node (struct ListHead* head, int value) {
  struct ListNode* pre_node;
  struct ListNode* current_node = head->next;

  if (value == 1)
    head->next = current_node->next;

  else {
    while (current_node->val != value) {
      pre_node = current_node;
      current_node = current_node->next;
    }
    pre_node->next = current_node->next;
  }

  free(current_node);
}

void insert_node (struct ListHead* head, int value, int new_value) {
  struct ListNode* newnode = (struct ListNode*)malloc(sizeof(struct ListNode));
  struct ListNode* list;
  struct ListNode* temp_node;
  newnode->val = new_value;
  list = head->next;

  if (value <= 0) {
    head->next = newnode;
    newnode->next = list;
  }
  
  else {
    while (list->val != value)
      list = list->next;
    temp_node = list->next;
    list->next = newnode;
    newnode->next = temp_node;
  }
}

void print_list (struct ListHead* head) {
  struct ListNode* list = head->next;
  
  while (list != NULL) {
    printf("%d ", list->val);
    list = list->next;
  }
  printf("\n");
}

void reverse_list (struct ListHead* head, int num) {
  struct ListNode* first_node;
  struct ListNode* current_node;
  struct ListNode* pre_node;
  struct ListNode* next_node;

  if (num <= 1)
    return;

  first_node = head->next;
  pre_node = head->next;
  current_node = pre_node->next;
  next_node = current_node->next;
  
  while (next_node != NULL) {
    current_node->next = pre_node;
    pre_node = current_node;
    current_node = next_node;
    next_node = next_node->next;
  }

  current_node->next = pre_node;
  head->next = current_node;
  first_node->next = NULL;
}

struct ListHead* reverse_list_recursive (struct ListHead* head) {
  if (head->next == NULL) {
    return head;
  }

  struct ListNode* first_node = head->next;
  head->next = first_node->next;
  head = reverse_list_recursive(head);

  struct ListNode* tail = head->next;
  if (tail == NULL) {
    head->next = first_node;
  } else {
    while (tail->next != NULL) {
      tail = tail->next;
    }
    tail->next = first_node;
  }

  first_node->next = NULL;
  return head;
}

struct ListNode* reverse_list_recursive2(struct ListHead* head) {
  if (head->next == NULL) {
    return NULL;
  }

  struct ListNode* first_node = head->next;
  head->next = first_node->next;
  struct ListNode *tail = reverse_list_recursive2(head);
  if (tail == NULL) {
    head->next = first_node;
  } else {
    tail->next = first_node;
  }
  first_node->next = NULL;

  return first_node;
}

struct ListNode* reverse_list2 (struct ListHead* head, int num) {
  struct ListNode* first_node;

  if (num <= 1)
    return head->next;

  first_node = head->next;
  head->next = first_node->next;
  //print_list(head);
  (reverse_list2(head, num - 1))->next = first_node;
  first_node->next = NULL;
  //print_list(head);

  return first_node;
}

void switch_list (struct ListHead* head) {
  if (head->next == NULL || head->next->next == NULL)
    return;
  
  struct ListNode* pre_node;
  struct ListNode* first_node = head->next;
  struct ListNode* second_node = first_node->next;

  head->next = second_node;
  first_node->next = second_node->next;
  second_node->next = first_node;

  while (first_node->next != NULL) {
    pre_node = first_node;
    first_node = first_node->next;
    second_node = first_node->next;
    if (second_node == NULL)
      return;
    else {
      pre_node->next = second_node;
      first_node->next = second_node->next;
      second_node->next = first_node;
    }
  }
}

  
