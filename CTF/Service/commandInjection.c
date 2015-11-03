#include <stdio.h>
#include <string.h>
#include <stdlib.h>
#include <time.h>

/* Function used for concntinating strings */
char* concat(char *s1, char *s2)
{
    char *result = malloc(strlen(s1)+strlen(s2)+1);//+1 for the zero-terminator
    //in real code you would check for errors in malloc here
    strcpy(result, s1);
    strcat(result, s2);
    return result;
}

int rand_lim(int limit) {
/* return a random number between 0 and limit inclusive.
 */

    int divisor = RAND_MAX/(limit+1);
    int retval;

    do {
        retval = rand() / divisor;
    } while (retval > limit);

    return retval;
}

/* Main function */
main(int argc, char *argv[])
{
  srand(time(NULL));
  // Defines the "bad" characters
  const char *invalid_characters = ";|><`$-";
  char str[BUFSIZ];
  char command[100]; // yes I know..
  int ran = rand_lim(100);
  int ciFound = 0;
  if (ran != 42){
    sprintf(command, "head -%d info/Fahrzeugnummern.csv | tail -1 ; echo ", ran);


    // Read the command
    scanf("%[^\n]", str);
    //strcpy(str, argv[1]);

    // Check the user input for bad characters
    char *c = str;
    while (*c)
    {
      if (strchr(invalid_characters, *c))
      {
         printf("%c is in \"%s\"\n", *c, str);
         // Set flag if found
         ciFound = 1;
      }
      c++;
    }

    // Concat the command and the user input
    char *cmd = concat(command, str);

    // Check the flag and execute if ok
    if(ciFound == 0){
      FILE *ls = popen(cmd, "r");
      char buf[256];
      while (fgets(buf, sizeof(buf), ls) != 0) {
        printf(buf);
      }
      pclose(ls);
    }
  } else {
    printf("You hit the wrong condition!");
  }
  return 1;
}
