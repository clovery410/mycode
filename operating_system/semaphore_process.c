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

char *buf_1, *buf_2;
sem_t *empty_1, *empty_2, *full_1, *full_2, *done_3;
int finished = 0;
/* for debug 
void print_semaphore(sem_t *sem) {
  int val;
  printf("Getting semaphore value\n");
  sem_getvalue(sem, &val);
  fprintf(stderr, "Semaphor value: %d", val);
}
*/

/* Following implemented with each iteration copying one character */
void process_a(){
  FILE* fp;
  size_t read_len;
  fp = fopen("test.txt", "r");
  finished = 0;
  while (1) {
    sem_wait(done_3);
    sem_wait(empty_1);
    read_len = fread(buf_1, 1, 1, fp);
    if (read_len != 1) {
      finished = 1;
      sem_post(full_1);
      break;
    }
    sem_post(full_1);
  }
  sem_wait(done_3);
}

void process_b() {
  while (1) {
    if (finished) {
      break;
    }
    sem_wait(full_1);
    sem_wait(empty_2);
    *buf_2 = *buf_1;
    sem_post(empty_1);
    sem_post(full_2);
  }
}

void process_c() {
  while (1) {
    if (finished) {
      break;
    }
    sem_wait(full_2);
    fprintf(stderr, "%c", *buf_2);
    sem_post(empty_2);
    sem_post(done_3);
  }
}

int main(int argc, char *argv[]) {
  /* On OS X, need to clear semaphore first for named semaphore 
    see http://stackoverflow.com/questions/8063613/c-macs-os-x-semaphore-h-trouble-with-sem-open-and-sem-wait
  */
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

  buf_1 = mmap(NULL, sizeof(char), PROT_READ | PROT_WRITE,  MAP_SHARED | MAP_ANONYMOUS, -1, 0);
  buf_2 = mmap(NULL, sizeof(char), PROT_READ | PROT_WRITE,  MAP_SHARED | MAP_ANONYMOUS, -1, 0);

  if (fork() == 0) {
    process_a();
    return 0;
  }

  if (fork() == 0) {
    process_b();
    return 0;
  }

  if (fork() == 0) {
    process_c();
    return 0;
  }

  waitpid(-1, NULL, 0);

  return 0;
}

