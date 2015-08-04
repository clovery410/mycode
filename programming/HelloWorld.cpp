#include <iostream>

using namespace std;

void merge_sort(int a[], int len)
{
  if (len <= 1) return;
  int mid = len / 2;
  merge_sort(a, mid);
  merge_sort(a + mid, len - mid);

  int* tmp = new int[len];
  int i1 = 0, i2 = mid, i = 0;
  while (i1 < mid && i2 < len)
    {
      if (a[i1] < a[i2])
	tmp[i++] = a[i1++];
      else
	tmp[i++] = a[i2++];
    }
  while (i1 < mid)
    tmp[i++] = a[i1++];
  while (i2 < len)
    tmp[i++] = a[i2++];

  for (int i = 0; i < len; ++i)
    a[i] = tmp[i];
}  

int main()
{
  int arr[] = {1,9,8,4,1,0,1,8};
  int len = 8;
  merge_sort(arr, len);
  for (int i = 0; i < len; ++i)
    cout << arr[i] << ' ';
  cout << endl;
  return 0;
}
