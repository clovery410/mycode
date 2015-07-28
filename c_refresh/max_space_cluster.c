#include <stdio.h>
#include <stdlib.h>

struct VertexNode;
struct Vertex;

struct Vertex {
  int val;
  struct VertexNode *edges;
  int processed;
  
