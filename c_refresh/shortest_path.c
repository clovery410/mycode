#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#define MAX 1000000

struct VertexNode;
struct Vertex;

struct Vertex {
  int val;
  struct VertexNode* edges;
  int short_dis;
  int processed;
  struct Vertex* pre_node;
};

struct VertexNode {
  int weight;
  struct Vertex* p_vertex;
  struct VertexNode* p_next;
};

struct Vertex* read_graph(const char* file_name, int vertex_count) {
  FILE * fp;
  char * line = NULL;
  size_t len = 0;
  ssize_t read;

  fp = fopen(file_name, "r");
  if (fp == NULL)
    exit(EXIT_FAILURE);

  struct Vertex* vertices = (struct Vertex*)malloc(sizeof(struct Vertex) * vertex_count);

  // initialize those vertices
  for (int i = 0; i < vertex_count; i++) {
    vertices[i].val = i + 1;
    vertices[i].edges = NULL;
    vertices[i].short_dis = MAX;
    vertices[i].processed = 0;
    vertices[i].pre_node = NULL;
  }

  while ((read = getline(&line, &len, fp)) != -1) {
    int current_node, node = 0;
    char *token, *string;
    struct Vertex *vertex_a, *vertex_b;
    //    struct VertexNode *edge_node = (struct VertexNode *)malloc(sizeof(struct VertexNode));

    string = line;
    while ((token = strsep(&string, "\t")) != NULL) {
      if (strstr(token, ",")) {
	//int node = 0;
	int edge_weight;	
	sscanf(token, "%d,%d", &node, &edge_weight);
	//	printf("Node: %d, Weight: %d ", node, edge_weight);
	vertex_b = vertices + node - 1;
	struct VertexNode* edge_node = (struct VertexNode *)malloc(sizeof(struct VertexNode));
	edge_node->p_vertex = vertex_b;
	edge_node->p_next = NULL;
	edge_node->weight = edge_weight;
	
	if (vertex_a->edges == NULL) {
	  vertex_a->edges = edge_node;
	} else {
	  struct VertexNode* a_edge_node = vertex_a->edges;
	  while (a_edge_node->p_next != NULL) {
	    a_edge_node = a_edge_node->p_next;
	  }
	  a_edge_node->p_next = edge_node;
	  }
	  
      } else {
	if (!strstr(token, "\n")) {
	  sscanf(token, "%d", &current_node);
	  //printf("\nCurrent Node: %d\n", current_node);
	  vertex_a = vertices + current_node - 1;
	}
      }
    }
    
  }
  fclose(fp);
  if (line)
    free(line);
  return vertices;
}

void print_graph (struct Vertex* graph, int vertex_count) {
  struct VertexNode* vertex_edge;
  for (int i = 0; i < vertex_count; i++) {
    printf("Current Node: %d \n", graph[i].val);
    vertex_edge = graph[i].edges;
    while (vertex_edge->p_next != NULL) {
      printf("Edge: %d Weight: %d, ", vertex_edge->p_vertex->val, vertex_edge->weight);
      vertex_edge = vertex_edge->p_next;
    }
    printf("Edge: %d Weight: %d\n", vertex_edge->p_vertex->val, vertex_edge->weight);
  }
}

int dij_short_path (struct Vertex* graph, int source, int target, int vertex_count) {
  //struct Vertex *x[vertex_count];
  //x[0] = graph[source];
  int A[vertex_count];
  int i;
  for (i = 0; i < vertex_count; i++) {
    A[i] = MAX;
  }
  A[source - 1] = 0;
  struct Vertex* current_node;
  struct Vertex* next_node;
  
  graph[source - 1].short_dis = 0;
  graph[source - 1].processed = 1;
  int min_dis;
  int p = 0;
  
  while (p < vertex_count - 1) {
    min_dis = MAX;
    for (i = 0; i < vertex_count; i++) {
      if (graph[i].processed == 1) {
        //current_node = &graph[i];
        //printf("current processing node is: %d\n", current_node->val);
        struct VertexNode* node_edge = graph[i].edges;
        while (node_edge != NULL) {
	  if ((node_edge->p_vertex->processed == 0) && ((A[i] + node_edge->weight) < min_dis)) {
	    min_dis = A[i] + node_edge->weight;
	    //printf("node edge %d, minimum dis is %d\n", node_edge->p_vertex->val, min_dis);
	    current_node = &graph[i];
	    next_node = node_edge->p_vertex;
	  }
	  node_edge = node_edge->p_next;
	  //printf("next edge node is %d, i is %d, processed value is %d\n", node_edge->p_vertex->val, i, graph[i].processed);
        }
      }
      
    }
    //printf("pre node is %d, next node is %d\n", current_node->val, next_node->val);
    graph[(next_node->val) - 1].processed = 1;
    graph[(next_node->val) - 1].pre_node = current_node;
    graph[(next_node->val) - 1].short_dis = min_dis;
    A[(next_node->val) - 1] = min_dis;
    // printf("%d -> ", next_node->val);
    //printf("A[%d] is %d\n", next_node->val - 1, min_dis);
    p++;
    //printf("P is %d\n", p);
  }
  struct Vertex* temp_node = &graph[target - 1];
  while (temp_node->val != source) {
    printf("%d <- ", temp_node->val);
    temp_node = temp_node->pre_node;
  }
  printf("%d\n", temp_node->val);
  
  return graph[target - 1].short_dis;
}

int main (void) {
  struct Vertex* graph;
  graph = read_graph("dijkstraData.txt", 200);
  //graph = read_graph("test.txt", 4);
  //print_graph(graph, 200);
  int shortest_distance;
  //shortest_distance = dij_short_path(graph, 1, 4, 4);
  //shortest_distance = dij_short_path(graph, 1, 92, 200);
  //printf("From Node %d to Node %d, the shortest distance is %d\n", graph[0].val, graph[91].val, shortest_distance);
  shortest_distance = dij_short_path(graph, 1, 7, 200);
  printf("From Node %d to Node %d, the shortest distance is %d\n", graph[0].val, graph[6].val, shortest_distance);
  graph = read_graph("dijkstraData.txt", 200);
  shortest_distance = dij_short_path(graph, 1, 37, 200);
  printf("From Node %d to Node %d, the shortest distance is %d\n", graph[0].val, graph[36].val, shortest_distance);
  graph = read_graph("dijkstraData.txt", 200);
  shortest_distance = dij_short_path(graph, 1, 59, 200);
  printf("From Node %d to Node %d, the shortest distance is %d\n", graph[0].val, graph[58].val, shortest_distance);
  graph = read_graph("dijkstraData.txt", 200);
  shortest_distance = dij_short_path(graph, 1, 82, 200);
  printf("From Node %d to Node %d, the shortest distance is %d\n", graph[0].val, graph[81].val, shortest_distance);
  graph = read_graph("dijkstraData.txt", 200);
  shortest_distance = dij_short_path(graph, 1, 99, 200);
  printf("From Node %d to Node %d, the shortest distance is %d\n", graph[0].val, graph[98].val, shortest_distance);
  graph = read_graph("dijkstraData.txt", 200);
  shortest_distance = dij_short_path(graph, 1, 115, 200);
  printf("From Node %d to Node %d, the shortest distance is %d\n", graph[0].val, graph[114].val, shortest_distance);
  graph = read_graph("dijkstraData.txt", 200);
  shortest_distance = dij_short_path(graph, 1, 133, 200);
  printf("From Node %d to Node %d, the shortest distance is %d\n", graph[0].val, graph[132].val, shortest_distance);
  graph = read_graph("dijkstraData.txt", 200);
  shortest_distance = dij_short_path(graph, 1, 165, 200);
  printf("From Node %d to Node %d, the shortest distance is %d\n", graph[0].val, graph[164].val, shortest_distance);
  graph = read_graph("dijkstraData.txt", 200);
  shortest_distance = dij_short_path(graph, 1, 188, 200);
  printf("From Node %d to Node %d, the shortest distance is %d\n", graph[0].val, graph[187].val, shortest_distance);
  graph = read_graph("dijkstraData.txt", 200);
  shortest_distance = dij_short_path(graph, 1, 197, 200); 
  printf("From Node %d to Node %d, the shortest distance is %d\n", graph[0].val, graph[196].val, shortest_distance);
  return 0;
}
    
