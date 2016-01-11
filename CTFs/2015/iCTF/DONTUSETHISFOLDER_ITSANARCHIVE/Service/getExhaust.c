/* getline.c */
#define _GNU_SOURCE
#include <stdio.h>
#include <stdlib.h>
#include <stddef.h>
#include <unistd.h>
#include <string.h>
#include <time.h>

int main(void) {
   FILE *fd;
   
   char delimiter[] = ",";
   char *token;
   
   /* bitte die Datei und eventuell den Pfad anpassen */
   
   char *file = "gas.csv";
   int rand();
   int randomnumber;
   int nRet;
   int number;
   int i = 0;

 //  int test = 0;
   
   double CO2value = 0;   

   FILE *fd1;
   char *file1 = "gas.csv";
   int nRet1;
   size_t *t1 = malloc(0);   
   char **gptr1 = malloc(sizeof(char*));
   *gptr1 = NULL;

   int lineamount = 0;
   size_t *t = malloc(0);

   srand (time(NULL));
//   srand (number);

   char **gptr = malloc(sizeof(char*));
   *gptr = NULL;

   if ( (fd = fopen(file,"r")) == NULL) {
      fprintf(stderr, "\nKonnte Datei %s nicht öffnen!", file);
      return EXIT_FAILURE;
   }

   if ( (fd1 = fopen(file1,"r")) == NULL) {
      fprintf(stderr, "\nKonnte Datei %s nicht öffnen!", file1);
      return EXIT_FAILURE;
   }

   while( (nRet=getline(gptr, t, fd)) > 0){
	lineamount++;
	}
     
   do {
   randomnumber = rand() % (lineamount - 1) + 1;
   } while (randomnumber == 42 );

		
   do{ ( (nRet1=getline(gptr1, t1, fd1)) > 0);
        i++;
   }while(i != randomnumber );
	
//	printf("%s\n", *gptr1); 
	
   token = strtok(*gptr1, delimiter);
//	printf("%s\n",token);
   token = strtok(NULL, delimiter);
 	printf("%s\n", token);

   CO2value = atof ( token );   
//   printf("%.3f\n",CO2value);


return EXIT_SUCCESS;
}
