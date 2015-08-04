#include <stdio.h>
#include <math.h>
#include <stdlib.h>

int flight_hours[] = {8, 9, 11, 12, 14, 15, 19, 21};
int flight_minutes[] = {0, 43, 19, 47, 0, 45, 0, 45};
int arrival_hours[] = {10, 11, 13, 15, 16, 17, 21, 23};
int arrival_minutes[] = {16, 52, 31, 0, 8, 55, 20, 58};

int min(int a, int b);
void find_closest_flight(int desired_time, int *departure_time, int *arrival_time);

int main(void)
{
  int hour, minute, time, departure, arrival;

  printf("Enter a 24-hour time: ");
  scanf("%d:%d", &hour, &minute);
  time = hour * 60 + minute;
  find_closest_flight(time, &departure, &arrival);
  printf("Corresponding minutes form: departure at %d, arriving at %d since midnight.\n", departure, arrival); 

  return 0;
}

void find_closest_flight(int desired_time, int *departure_time, int *arrival_time)
{
  size_t n_flights = sizeof(flight_hours) / sizeof(flight_hours[0]);
  int i_flights = -1;
  int diff, diff_overnight;
  int min_diff = 9999;

  for (int i = 0; i < n_flights; ++i) {
    diff = abs(flight_hours[i] * 60 + flight_minutes[i] - desired_time);
    diff_overnight = abs(flight_hours[i] * 60 + flight_minutes[i] - desired_time - 24 * 60);
    if (diff < min_diff || diff_overnight < min_diff) {
      min_diff = min(diff, diff_overnight);
      i_flights = i;
    }
  }
  *departure_time = flight_hours[i_flights] * 60 + flight_minutes[i_flights];
  *arrival_time = arrival_hours[i_flights] * 60 + arrival_minutes[i_flights];
  printf("Closest departure time is %.2d:%.2d, ", flight_hours[i_flights], flight_minutes[i_flights]);
  printf("arriving at %.2d:%.2d\n", arrival_hours[i_flights], arrival_minutes[i_flights]);
}

int min(int a, int b)
{
  return a < b ? a: b;
}
