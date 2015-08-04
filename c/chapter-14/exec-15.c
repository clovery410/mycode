#include <stdio.h>

#define ENGLISH
#define FRENCH
#define SPANISH

int main(void)
{
#undef ENGLISH
#undef FRENCH
#if defined(ENGLISH)
  printf("Insert Disk 1\n");
#elif defined(FRENCH)
  printf("Inserez Le Disque 1\n");
#elif defined(SPANISH)
  printf("Inserte El Disco 1\n");
#endif
}
