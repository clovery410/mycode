#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <limits.h>
#define PRIME 31
#define SIZE 2000000
#define LEN 1000000

struct entry_s {
  long key;
  int value;
  struct entry_s *next;
};
  
long hash_fun(long key, long max) {
  long result = ((key % max) * (key % max + PRIME)) % max;
  if (result < 0)
    return -result;
  else
    return result;
}

struct hashtable_s {
  long max;
  long number_of_elements;
  struct entry_s **elements;
};

/*Create a new hashtable */
struct hashtable_s *ht_create(long size) {
  struct hashtable_s *hashtable = NULL;
  long i;

  if (size < 1) return NULL;

  if ((hashtable = malloc(sizeof(struct hashtable_s))) == NULL) {
    return NULL;
  }

  if ((hashtable->elements = malloc(sizeof(struct entry_s) * size)) == NULL) {
    return NULL;
  }

  for (i = 0; i < size; i++) {
    hashtable->elements[i] = NULL;
  }

  hashtable->number_of_elements = 0;
  hashtable->max = size;
  return hashtable;
}

struct hashtable_s* read_into_hash(const char* file_name, int *array, struct hashtable_s* hash_table) {
  FILE *fp;
  char *line = NULL;
  size_t len = 0;
  ssize_t read;
  long hash;
  struct entry_s *entry;
  int i = 0;

  fp = fopen(file_name, "r");
  if (fp == NULL)
    exit(EXIT_FAILURE);

  //read from file
  while ((read = getline(&line, &len, fp)) != -1) {
    long x;
    sscanf(line, "%ld\n", &x);
    //printf("Original x: %lld\n", x);
    array[i++] = x;
    struct entry_s* data = (struct entry_s*)malloc(sizeof(struct entry_s));
    data->key = x;
    //printf("%lld\n", data->key);
    data->value = 1;
    data->next = NULL;

    if (hash_table->number_of_elements >= hash_table->max) {
      printf("FULL\n");
      break;
    }
    hash = hash_fun(data->key, hash_table->max);
    //printf("Hash value: %lld\n", hash);
    if (hash_table->elements[hash] == NULL)
      hash_table->elements[hash] = data;
    else {
      entry = hash_table->elements[hash];
      while (entry->next != NULL && entry->key != data->key)
	entry = entry->next;
      if (entry->key == data->key)
	entry->value++;
      else
	entry->next = data;
    }
    hash_table->number_of_elements++;
  }
  fclose(fp);
  if (line)
    free(line);

  return hash_table;
}
    
/* Insert */
/*
int hash_insert(struct entry_s *data, struct hashtable_s *hash_table) {
  int try, hash;
  if (hash_table->number_of_elements >= hash_table->max) {
    return 0;
  }
  for (try = 0; true; try++) {
    hash = hash_fun(data->key, try, hash_table->max);
    if (hash_table->elements[hash] == 0) {
      hash_table->elements[hash] = data;
      hash_table->number_of_elements++;
      return 1;
    }
  }
  return 0;
  } */

/* Check whether data in hashtable */
int hash_count(long key, struct hashtable_s* hash_table) {
  long hash;
  int count = 0;
  struct entry_s* entry;
  hash = hash_fun(key, hash_table->max);
  entry = hash_table->elements[hash];
  while (entry != NULL) {
    if (entry->key == key) {
      count = count + entry->value;
      break;
    }
    entry = entry->next;
  }
  return count;
}

int hash_search(int *array, struct hashtable_s *hash_table) {
  int sum, i, count;
  long y;
  count = 0;
  
  for (sum = -10000; sum <= 10000; sum++) {
    printf("Current sum: %d\n", sum);
    for (i = 0; i < LEN; i++) {
      //printf("Current x: %d\n", array[i]);
      y = sum - array[i];
      //printf("Current y: %ld\n", y);
      if (array[i] == y) {
	if (hash_count(y, hash_table) > 1) {
	  count++;
	  printf("x: %d, y: %ld, sum: %d, count: %d\n", array[i], y, sum, count);
	  break;
	}
      }
      else if (hash_count(y, hash_table) > 0) {  
	count++;
	printf("%d\n", count);
	break;
      }
    }
  }
  return count;
}

int main(void) {
  int num;
  int array[LEN] = {0};
  struct hashtable_s *hashtable = ht_create(SIZE);
  hashtable = read_into_hash("algo1-programming_prob-2sum.txt", array, hashtable);
  //hashtable = read_into_hash("test.txt", array, hashtable);
  for (int i = 0; i < LEN; i++)
    printf("%d\n", array[i]);
  num = hash_search(array, hashtable);

  printf("There are %d number of target value t in the interval.\n", num);

  return 0;
}
  
  

