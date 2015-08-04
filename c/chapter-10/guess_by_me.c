#include <stdio.h>
#include <stdlib.h>
#include <time.h>
#include <ctype.h>

#define MAX_NUM 100

int generate_num(void);
int play_game(void);

int main(void)
{
  srand((unsigned) time (NULL));

  char option;
  int count;

  printf("Guess the secret number between 1 and %d.\n", MAX_NUM);

  for (;;) {
    printf("\nA new number has been chosen.\n");
    count = play_game();
    printf("You won in %d guesses!\n", count);
    printf("\nPlay again? (Y/N) ");
    option = getchar();
    getchar();
    if (tolower(option) != 'y') 
      break;
  }

  return 0;
}

int generate_num(void)
{
  int random_num;

  random_num = rand() % MAX_NUM + 1;
  return random_num;
}

int play_game(void)
{
  int num, guess, count = 1;

  num = generate_num();
  for (;;) {
    printf("Enter guess: ");
    scanf("%d", &guess);
    getchar();
    if (guess == num)
      break;
    else if (guess < num)
      printf("Too low; try again.\n");
    else
      printf("Too high; try again.\n");
    count++;
  }
  return count;
}
