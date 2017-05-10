#include <stdlib.h>
#include <sys/types.h>
#include <stdio.h>
#include <unistd.h>

int main(int argc, char *argv[])
{
  pid_t pid;
  int i;

  pid = fork();
  if (pid == -1) {
    perror("Fork failure");
    exit(EXIT_FAILURE);
  }
  else if (pid == 0) {
    printf("I'm the child %d, my parent is %d\n", getpid(), getppid());
  }
  else {
    printf("I'm the parent %d, my child is %d\n", getpid(), pid);
    wait(NULL);
  }
  exit(EXIT_SUCCESS);
}
