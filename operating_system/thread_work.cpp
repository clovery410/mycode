#include <pthread.h>
#include <stdio.h>
#include <stdlib.h>
#include <sys/types.h>
#include <cctype>
#include <iostream>
#include <map>
#include <string>

using namespace std;

#define NUMBER_OF_THREAD 10
struct _split{
  char *word;
  int start;
  int end;
  map<string, int> *result;
};

void *count_word_frequency (void *_data){
  struct _split *data = (struct _split *)_data;
  bool is_space = false;
  int word_start = 0;
  map<string, int> *word_freq = new map<string, int>();
  int i, size;
  char* text = data->word + data->start;
  size = data->end - data->start;

  for (i = 0; i <= size; ++i){
    if (i == size || isspace(text[i])){
	if (!is_space){
	  string one_word(text + word_start, i - word_start);
	  ++(*word_freq)[one_word];
	}
	is_space = true;
    } 
    else {
      if (is_space) {
	word_start = i;
      }
      is_space = false;
    }
  }
  data->result = word_freq;

  pthread_exit(NULL);
}

int main(int argc, char *argv[]){
  pthread_t threads[NUMBER_OF_THREAD];
  int status, i;
  FILE *fp;
  char ch;
  char *source = NULL;
  long buff_size;

  fp = fopen("test.txt", "r");
  if (fp != NULL) {
    if (fseek(fp, 0, SEEK_END) == 0) {
      buff_size = ftell(fp);
      if (buff_size == -1)
	perror("Empty file");
      
      source = (char *)malloc(sizeof(char) * (buff_size + 1));
      
      if (fseek(fp, 0, SEEK_SET) != 0)
	perror("Return to file head failure");

      size_t f_len = fread(source, sizeof(char), buff_size, fp);

      if (f_len == 0)
	perror("Read from memory failure");
      else
	source[f_len] = '\0';
    }
  }
  fclose(fp);

  int start, end;
  start = 0;
  struct _split *word_splits[NUMBER_OF_THREAD];
  for (i = 0; i < NUMBER_OF_THREAD; i++){
    struct _split *word_split = (struct _split *)malloc(sizeof(struct _split));
    word_splits[i] = word_split;

    end = buff_size / NUMBER_OF_THREAD * (i + 1);
    while ((ch = source[end]) != ' ' && ch != '\0'){
      end ++;
    }

    word_split->word = source;
    word_split->start = start;
    word_split->end = end;

    status = pthread_create(&threads[i], NULL, count_word_frequency, word_split);
    if (status != 0){
      printf("pthread_create returned error code %d\n", status);
      exit(EXIT_FAILURE);
    }
    
    start = end + 1;
  }
  for (i = 0; i < NUMBER_OF_THREAD; i++) {
    pthread_join(threads[i], NULL);
  }

  map<string, int> all_results;
  for (int i = 0; i < NUMBER_OF_THREAD; ++i) {
    map<string, int> *pResult = word_splits[i]->result;
    for (auto elem : *pResult) {
      all_results[elem.first] += elem.second;
    }
  }


  for (auto elem : all_results) {
    cout << elem.first << " " << elem.second << endl;
  }

  free(source);
  exit(EXIT_SUCCESS);
}
