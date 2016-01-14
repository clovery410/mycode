#include <stdio.h>
#include <stdlib.h>

struct ListHead {
  struct ListNode* next;
};

struct ListNode {
  int val;
  struct ListNode* next;
};

struct ListHead* createEmptyList(void) {
  struct ListHead* head;
  head = (struct ListHead*)malloc(sizeof(struct ListHead));
  head->next = NULL;
  return head;
}

void addNode(struct ListHead* head, int key) {
  struct ListNode* newnode = (struct ListNode*)malloc(sizeof(struct ListNode));
  struct ListNode* list;
  newnode->val = key;
  newnode->next = NULL;
  list = head->next;

  if (list == NULL)
    head->next = newnode;

  else {
    while (list->next != NULL)
      list = list->next;
    list->next = newnode;
  }
}

struct ListNode* addTwoNumbers(struct ListNode* l1, struct ListNode* l2) {
  struct ListHead* lst = createEmptyList();
  int key, carryon;
  carryon = 0;

  while (l1 != NULL) {
    if (l2 != NULL) {
      key = (l1->val + l2->val + carryon) % 10;
      carryon = (l1->val + l2->val + carryon) / 10;;
      l2 = l2->next;
    }
    else {
      key = (l1->val + carryon) % 10;
      carryon = (l1->val + carryon) / 10;
    }
    addNode(lst, key);
    l1 = l1->next;
  }

  while (l2 != NULL) {
    key = (l2->val + carryon) % 10;
    carryon = (l2->val + carryon) / 10;
    addNode(lst, key);
    l2 = l2->next;
  }
    
  if (carryon != 0)
    addNode(lst, carryon);
  return lst->next;
}

void printList(struct ListNode* list) {
  if (list == NULL)
    printf("Empty Linked List\n");
  else {
    while (list->next != NULL) {
      printf("%d -> ", list->val);
      list = list->next;
    }
    printf("%d\n", list->val);
  }
}
  
int main(void) {
  struct ListHead* head1 = createEmptyList();
  struct ListHead* head2 = createEmptyList();
  addNode(head1, 9);
  addNode(head1, 8);
  //addNode(head1, 3);
  addNode(head2, 1);
  //addNode(head2, 6);
  //addNode(head2, 4);

  printList(head1->next);
  printList(head2->next);
  struct ListNode* lst1;
  struct ListNode* lst2;
  struct ListNode* result;
  lst1 = head1->next;
  lst2 = head2->next;

  result = addTwoNumbers(lst1, lst2);
  printList(result);

  return 0;
}
