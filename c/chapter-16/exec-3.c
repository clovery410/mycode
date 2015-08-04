struct complex {
  double real, imaginary;
};

struct complex c1, c2, c3;

struct complex make_complex(double n1, double n2)
{
  struct complex s;
  s.real = n1;
  s.imaginary = n2;
  return s;
}

struct complex add_complex(struct complex s1, struct complex s2)
{
  struct complex s_sum;
  s_sum.real = s1.real + s2.real;
  s_sum.imaginary = s1.imaginary + s2.imaginary;
  return s_sum;
}
