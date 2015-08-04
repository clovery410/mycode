#include <stdio.h>
#include <time.h>
#include <stdlib.h>
#include <stdbool.h>
#include <ctype.h>

int roll_dice(void);
bool play_game(void);

int main(void) 
{
  srand((unsigned) time (NULL));

  int win = 0, lose = 0;
  char option;

  for (;;) {
    if (play_game()) {
      printf("You win!\n");
      win++;
    }
    else {
      printf("You lose!\n");
      lose++;
    }
    printf("Play again? ");
    option = getchar();
    getchar();
    //printf("User input: %c\n", toupper(option));
    if (toupper(option) != 'Y') {
      break;
    }
  }
  
  printf("Wins: %d Losses: %d\n", win, lose);
  return 0;
}

int roll_dice(void)
{
  int dice1, dice2;
  
  dice1 = rand() % 6 + 1;
  dice2 = rand() % 6 + 1;

  return dice1 + dice2;
}

bool play_game(void)
{
  int first_try, later_try;

  first_try = roll_dice();
  printf("You rolled: %d\n", first_try);
  if (first_try == 7 || first_try == 11)
    return true;

  else if (first_try == 2 || first_try == 3 || first_try == 12)
    return false;

  else {
    printf("Your point is %d\n", first_try);
    while ((later_try = roll_dice()) != 7) {
      printf("You rolled: %d\n", later_try);
      if (later_try == first_try)
	return true;
    }
    printf("You rolled: %d\n", later_try);
    return false;
  }
}

