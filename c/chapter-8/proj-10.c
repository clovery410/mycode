#include <stdio.h>
#include <stdlib.h>

#define NUM 8

int main(void)
{
  int i, hour, minute, time, closest, depart_time, arrive_time;
  const int depart[NUM] = {480, 583, 679, 767, 840, 945, 1140, 1305};
  const int arrive[NUM] = {616, 712, 811, 900, 968, 1075, 1280, 1438};

  printf("Enter a 24-hour time: ");
  scanf("%d:%d", &hour, &minute);

  time = hour * 60 + minute;
  closest = 1440;

  for (i = 0; i < NUM; i++) {
    if (abs(time - depart[i]) < closest) {
      closest = abs(time - depart[i]);
      depart_time = depart[i];
      arrive_time = arrive[i];
    }
    else if ((1440 - depart[i] + time) < closest) {
      closest = 1440 - depart[i] + time;
      depart_time = depart[i];
      arrive_time = arrive[i];
    }
  }

  printf("Closest departure time is %d:%.2d, arriving at %d:%.2d\n", depart_time / 60, depart_time % 60, arrive_time / 60, arrive_time % 60);

  return 0;
}
