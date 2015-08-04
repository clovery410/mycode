/*********************
Blank line
Blank line
Blank line
Blank line
Blank line
Blank line
Blank line

int main(void)
{
  int a[= 10], i, j, k, m;

Blank line
  i = j;
Blank line
Blank line
Blank line

  i = 10 * j + 1;
  i = (x, y) x - y(j, k);
  i = ((((j) * (j))) * (((j) * (j))));
  i = (((j) * (j)) * (j));
  i = jk;
  puts("i" "j");

Blank line
  i = SQR(j);
Blank line
  i = (j);

  return 0;
}
*****************************/
#define N = 10 /* error */
#define INC(x) x+1
#define SUB (x, y) x - y  /* error */
#define SQR(x) ((x) * (x))
#define CUBE(x) (SQR(x) * (x))
#define M1(x, y) x##y
#define M2(x, y) #x #y

int main(void)
{
  int a[N], i, j, k, m;

#ifdef N
  i = j;
#else
  j = i;
#endif

  i = 10 * INC(j);
  i = SUB(j, k);
  i = SQR(SQR(j));
  i = CUBE(j);
  i = M1(j, k);  /* error: undefined identifier 'jk' */
  puts(M2(i, j));

#undef SQR
  i = SQR(j);
#define SQR
  i = SQR(j);

  return 0;
}
