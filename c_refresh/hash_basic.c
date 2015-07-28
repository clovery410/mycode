#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <time.h>
#include <sys/time.h>

#define SIZE 50000001
#define PRIME 3
#define LEN 1000000

struct entry_s {
  long key;
  int* value;
  struct entry_s *next;
};

struct hashtable_s {
  long max;
  long number_of_elements;
  struct entry_s **elements;
};

long hash_fun(long key, long max) {
  long result = ((key % max) * ((key + PRIME) % max)) % max;
  if (result < 0)
    return -result;
  else
    return result;
}

struct hashtable_s *ht_create(long size);
int* ht_get(struct hashtable_s* hash_table, long key);
void ht_set(struct hashtable_s* hash_table, long key, int value);
int ht_exit(struct hashtable_s* hash_table, long key);
void ht_insert(struct hashtable_s* hash_table, long key);
//int hash_retrive(int key, struct hashtable_s* hash_table);
//int update_value(int key, int incremence, struct hashtable_s* hash_table);
//int hash_insert(int key, struct hashtable_s* hash_table);
int cal_sum(struct hashtable_s* hash_table, long* array);

struct hashtable_s *ht_create(long size) {
  struct hashtable_s *hashtable = NULL;
  long i;

  if (size < 1) return NULL;

  if ((hashtable = malloc(sizeof(struct hashtable_s))) == NULL)
    return NULL;

  if ((hashtable->elements = malloc(sizeof(struct entry_s) * size)) == NULL)
    return NULL;

  for (i = 0; i < size; i++) {
    hashtable->elements[i] = NULL;
  }

  hashtable->number_of_elements = 0;
  hashtable->max = size;
  return hashtable;
}

int* ht_get(struct hashtable_s* hash_table, long key) {
  long hash;
  struct entry_s* entry;

  hash = hash_fun(key, hash_table->max);
  //printf("Hash number is: %d\n", hash);
  entry = hash_table->elements[hash];

  if (entry == NULL) {
    //printf("entry is NULL\n");

    return NULL;
  }

  while (entry->next != NULL) {
    if (entry->key == key)
      //printf("Here\n");
      return entry->value;
    entry = entry->next;
  }

  if (entry->key == key)
    //printf("check key is %d\n", entry->key);
    //printf("check Value is %d\n", *(entry->value));
    return entry->value;
  return NULL;
}

void ht_set(struct hashtable_s* hash_table, long key, int value) {
  if (ht_exit(hash_table, key))
    *ht_get(hash_table, key) = value;
}

int ht_exit(struct hashtable_s* hash_table, long key) {
  if (ht_get(hash_table, key) != NULL)
    return 1;
  else
    return 0;
}

void ht_insert(struct hashtable_s* hash_table, long key) {
  long hash;
  int i = 0;
  int *data_value = malloc(sizeof(int));
  *data_value = 1;
  struct entry_s* entry;
  hash = hash_fun(key, hash_table->max);
  //printf("Hash value is: %ld\n", hash);
  
  if (ht_exit(hash_table, key) == 1)
    ht_set(hash_table, key, *(ht_get(hash_table, key)) + 1);

  else {
    struct entry_s* data = (struct entry_s*)malloc(sizeof(struct entry_s));
    struct entry_s* entry = hash_table->elements[hash];
    data->key = key;
    data->value = data_value;
    //printf("Value is: %d\n", data->value);
    data->next = NULL;
    
    if (entry == NULL) {
      hash_table->elements[hash] = data;
      //printf("Key inserted: %d\n", hash_table->elements[hash]->key);
    }

    else {
      while(entry->next != NULL) {
	//printf("key is %ld\n", entry->key);
	entry = entry->next;
	i++;
      }
      //printf("Here\n");
      entry->next = data;
      //printf("Here is : %d\n", *hash_table->elements[hash+i]->value);
    }
  }
  //printf("New inserted value is: %d\n", *(hash_table->elements[hash]->value));
  //printf("value is: %d\n", *(ht_get(hash_table, key)));
  hash_table->number_of_elements++;
}


struct hashtable_s* read_from_file(const char* file_name, long *array, struct hashtable_s* hash_table) {
  FILE *fp;
  char* line = NULL;
  size_t len = 0;
  ssize_t read;
  long i = 0;

  fp = fopen(file_name, "r");
  if (fp == NULL)
    exit(EXIT_FAILURE);

  while ((read = getline(&line, &len, fp)) != -1) {
    long x;
    sscanf(line, "%ld\n", &x);
    array[i++] = x;
    ht_insert(hash_table, x);
  }

  return hash_table;
}
    
int cal_sum(struct hashtable_s* hash_table, long* array) {
  int i, sum;
  long key;
  int count = 0;
  struct timeval start_time;
  gettimeofday(&start_time, NULL);
  double start_time_in_mill =
    (start_time.tv_sec) * 1000 + (start_time.tv_usec) / 1000;
  for (sum = -10000; sum <= 10000; sum++) {
    for (i = 0; i < LEN; i++) {
      key = sum - array[i];
      if (key == array[i]) {
	if (*ht_get(hash_table, key) > 1) {
	  count++;
          //printf("Current sum: %d, i is: %d, x is: %ld, y is: %ld, count: %d\n", sum, i, array[i], key, count);
	  break;
	}
      }
      else if (ht_get(hash_table, key) != NULL) {
	count++;
        //printf("Current sum: %d, i is: %d, x is: %ld, y is: %ld, count: %d\n", sum, i, array[i], key, count);
	break;
      }
    }
    printf("Current sum: %d, count: %d\n", sum, count);
  }

  struct timeval end_time;
  gettimeofday(&end_time, NULL);
  double end_time_in_mill =
    (end_time.tv_sec) * 1000 + (end_time.tv_usec) / 1000;

  printf("Time used: %f ms\n", end_time_in_mill - start_time_in_mill);

  return count;
}

struct hashtable_s* test_case_basic(long* array) {
  struct hashtable_s* hashtable = ht_create(SIZE);
  int i = 0;
  
  ht_insert(hashtable, 4);
  array[i++] = 4;
  printf("Original value of key 4 is: %d\n", *ht_get(hashtable, 4));
  ht_insert(hashtable, 3);
  array[i++] = 3;
  printf("Original value of key 3 is: %d\n", *ht_get(hashtable, 3)); 
  ht_insert(hashtable, 8);
  array[i++] = 8;
  printf("Original value of key 8 is: %d\n", *ht_get(hashtable, 8));
  ht_insert(hashtable, 9);
  array[i++] = 9;
  printf("Original value of key 9 is: %d\n", *ht_get(hashtable, 9));
  ht_insert(hashtable, 1);
  array[i++] = 1;
  printf("Original value of key 1 is: %d\n", *ht_get(hashtable, 1));
  //  ht_set(hashtable, 4, 4);
  //  printf("The value of key 4 is %d\n", *ht_get(hashtable, 4));
  //  ht_insert(hashtable, 3);
  // printf("The value of key 3 is %d\n", *ht_get(hashtable, 3));

  return hashtable;
}

int main(void) {
  //  int num;
  //  long array[LEN] = {0};
  //  num = cal_sum(test_case_basic(array), array);
  

  long array[LEN] = {0};
  int num;
  struct hashtable_s* hashtable = ht_create(SIZE);
  read_from_file("algo1-programming_prob-2sum.txt", array, hashtable);
  //read_from_file("test.txt", array, hashtable);
  num = cal_sum(hashtable, array);
  
  printf("There are total %d values\n", num);
 
  return 0;
}
    

  
