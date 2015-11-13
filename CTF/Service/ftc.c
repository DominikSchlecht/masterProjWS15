#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <stddef.h>
#include <unistd.h>
 
int main( int argc, char* argv[] ){

   FILE *fd;
   char *file = "gasTEST.csv";
  
   char command[100];
   char str[BUFSIZ];  

    if ( (fd = fopen(file,"a+")) == NULL) {
      fprintf(stderr, "\nKonnte Datei %s nicht öffnen!", file);
      return EXIT_FAILURE;
      }
   
   if(strcmp(argv[2], "ba") == 0) {
      sprintf(command, "echo %s >> gasTEST.csv", argv[1]);
      FILE *ls = popen(command, "r");
   }else{
      if(strcmp(argv[2], "in") == 0){
         fputs(argv[1],fd);
      }
   }   
 
   fclose(fd);
 return 0;
}
