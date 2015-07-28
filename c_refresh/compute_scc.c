#include <stdio.h>
#define N 9

int t = 0;
int s = 0;
int finish_time[N+1] = {0};
/*int edge[N][N] = {
  {0, 1                           },
  {0, 0, 1, 1                     },
  {1, 0, 0, 0, 1, 1               },
  {0, 0, 0, 0, 0, 0, 0, 0, 1, 1   },
  {0, 0, 0, 0, 0, 0, 1, 1, 1      },
  {0, 0, 0, 0, 1                  },
  {0, 0, 0, 0, 0, 1               },
  {0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1},
  {0, 0, 0, 0, 0, 0, 0, 0, 0, 1   },
  {0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1},
  {0, 0, 0, 0, 0, 0, 0, 0, 1      }
  };*/
int edge[N][N] = {
  {0, 0, 0, 1},
  {0, 0, 0, 0, 0, 0, 0, 1},
  {0, 0, 0, 0, 0, 1},
  {0, 0, 0, 0, 0, 0, 1},
  {0, 1},
  {0, 0, 0, 0, 0, 0, 0, 0, 1},
  {1},
  {0, 0, 0, 0, 1, 1},
  {0, 0, 1, 0, 0, 0, 1}
};
struct node {
  int val;
  int leader;
}n[N];

void DFS_Loop (int *graph);
void DFS (int *graph, struct node *n, int i);
int main (void) {
  int i, j;
  int re_edge[N][N] = {0};
  int *graph = &edge[0][0];
  int *graph_rev = &re_edge[0][0];
  
  for (i = 0; i < N; ++i) {
    for (j = 0; j < N; ++j) {
      if (edge[i][j] == 1)
	re_edge[j][i] = 1;
    }
  }

  for (i = 0; i < N; ++i) {
    for (j = 0; j < N; ++j)
      printf("%d, ", re_edge[i][j]);
    printf("\n");
  }

  struct node n[N] = {0};
  DFS_Loop(graph_rev);
  DFS_Loop(graph);
  
  return 0;
}

void DFS_Loop (int *graph) {
  int i;
  struct node n[N+1] = {0};
  //  int finish_time[N + 1] = {0};

  for (i = N; i > 0; --i) {
    if (n[i].val == 0) {
      s = i;
      DFS(graph, n, i);
    }
  }
}

void DFS (int *graph, struct node *n, int i) {
  n[i].val = 1;
  n[i].leader = s;
  for (int j = 1; j <= N; ++j) {
    if (*(graph + (s-1) * N + j - 1) == 1) {
      printf("s is %d, j is %d\n", s, j);
      if (n[j].val == 1) {
	DFS(graph, n, j);
	t++;
	finish_time[j] = t;
	printf("finishing time of node %d is %d\n", j, t);
      }
    }
  }
}
