#include <stdio.h>
#include <string.h>
#include <stdlib.h>

main(int argc, char *argv[])
{

  char test[1024];
  char test2[1024];
  strcpy(test,argv[1]);
  strcpy(test2,argv[2]);
  printf(test);
}
