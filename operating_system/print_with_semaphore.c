#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>
#include <sys/ipc.h>
#include <sys/sem.h>
#include <semaphore.h>
#include <sys/types.h>
#include <sys/mman.h>
#include <sys/stat.h>
#include <fcntl.h>
#include <errno.h>
#include <pthread.h>

char buf_1, buf_2;
sem_t *empty_1, *empty_2, *full_1, *full_2, *done_3;
int finished = 0;

void print_semaphore(sem_t *sem) {
  int val;
  printf("Getting semaphore value\n");
  sem_getvalue(sem, &val);
  fprintf(stderr, "Semaphor value: %d", val);
}

void *a_to_b(void){
  finished = 0;
  for (int i = 0; i < 26; ++i) {
    sem_wait(done_3);
    sem_wait(empty_1);
    buf_1 = 'a' + i;
    if (i == 26 - 1) {
      finished = 1;
    }

    sem_post(full_1);
  }

  sem_wait(done_3);

  pthread_exit(0);
}

void *b_to_c(void){
  while (1) {
    if (finished) {
      break;
    }
    sem_wait(full_1);
    sem_wait(empty_2);
    buf_2 = buf_1;
    /*  fprintf(stderr, "put buf_1 to buf_2\n");*/
    sem_post(empty_1);
    sem_post(full_2);
  }
  pthread_exit(0);
}

void *print_c(void){
  while (1) {
    if (finished) {
      break;
    }
    sem_wait(full_2);
    /*  fprintf(stderr, "print buf_2\n");*/
    printf("%c\n", buf_2);
    sem_post(empty_2);
    sem_post(done_3);
  }
  pthread_exit(0);
}

int main(int argc, char *argv[]) {
  int s;
  pthread_t thread_a;
  pthread_t thread_b;
  pthread_t thread_c;

  sem_unlink("empty_1");
  sem_unlink("empty_2");
  sem_unlink("full_1");
  sem_unlink("full_2");
  sem_unlink("done_3");


  empty_1 = sem_open("empty_1", O_CREAT, 0600, 1);
  empty_2 = sem_open("empty_2", O_CREAT, 0600, 1);
  done_3 = sem_open("done_3", O_CREAT, 0600, 1);
  full_1 = sem_open("full_1", O_CREAT, 0600, 0);
  full_2 = sem_open("full_2", O_CREAT, 0600, 0);

  s = pthread_create(&thread_a, NULL, a_to_b, NULL);
  if (s != 0){
    printf("pthread_create returnen error code %d\n", s);
    exit(EXIT_FAILURE);
  }
  s = pthread_create(&thread_b, NULL, b_to_c, NULL);
  if (s != 0){
    printf("pthread_create returnen error code %d\n", s);
    exit(EXIT_FAILURE);
  }

  s = pthread_create(&thread_c, NULL, print_c, NULL);
  if (s != 0){
    printf("pthread_create returnen error code %d\n", s);
    exit(EXIT_FAILURE);
  }

  pthread_join(thread_a, NULL);
  pthread_join(thread_b, NULL);
  pthread_join(thread_c, NULL);


  return 0;
}

