#include <stdio.h>

int evaluate_position(char board[8][8]);

int main(void)
{
  int result;
  char board[8][8] = {{'r', 'n', 'b', 'q', 'k', 'b', 'n', 'r'}, 
		      {'p', 'p', 'p', 'p', 'p', 'p', 'p', 'p'}, 
		      {0},
		      {0}, 
		      {0}, 
		      {0}, 
		      {'P', 'P', 'P', 'P', 'P', 'P', 'P', 'P'},
		      {'R', 'N', 'B', 'Q', 'K', 'B', 'N', 'R'}};

  result = evaluate_position(board);
  if (result > 0)
    printf("White has advantage\n");
  else if (result < 0)
    printf("Black has advantage\n");
  else
    printf("It's draw till now\n");

  return 0;
}

int evaluate_position(char board[8][8])
{
  int i, j, white = 0, black = 0;
  
  for (i = 0; i < 8; i++)
    for (j = 0; j < 8; j++) {
      switch (board[i][j]) {
      case 'Q': white += 9; break;
      case 'R': white += 5; break;
      case 'B': case 'N': white += 3; break;
      case 'P': white += 1; break;
      case 'q': black += 9; break;
      case 'r': black += 5; break;
      case 'b': case 'n': black += 3; break;
      case 'p': black += 1; break;
      default: break;
      }
    }
  return white - black;
}
     
