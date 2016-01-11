#include <stdio.h>
#include <string.h>
#include <stdlib.h>
#include <time.h>
#include <pcre.h>

/* Function used for concntinating strings */
char* concat(char *s1, char *s2)
{
    char *result = malloc(strlen(s1)+strlen(s2)+1);//+1 for the zero-terminator
    //in real code you would check for errors in malloc here
    strcpy(result, s1);
    strcat(result, s2);
    return result;
}

char* getfield(char* line, int num)
{
    char* tok;
    for (tok = strtok(line, ";");
            tok && *tok;
            tok = strtok(NULL, ";\n"))
    {
        if (!--num)
            return tok;
    }
    return NULL;
}

int rand_lim(int limit)
{
/* return a random number between 0 and limit inclusive.
 */

    int divisor = RAND_MAX/(limit+1);
    int retval;

    do {
        retval = rand() / divisor;
    } while (retval > limit);

    return retval;
}

int test_regex(char* vin){
  pcre *reCompiled;
  char *aStrRegex;
  char *aLineToMatch = vin;
  const char *pcreErrorStr;
  int pcreErrorOffset;
  pcre_extra *pcreExtra;
  int pcreExecRet;
  int subStrVec[30];
  char fahrzeugtypen[4096];
  strcpy(fahrzeugtypen,"(");

  FILE* stream = fopen("info/Fahrzeugtypen.csv", "r");

  char line[1024];
  while (fgets(line, 1024, stream))
  {
       char* tmp = strdup(line);
       strcpy(fahrzeugtypen, concat(fahrzeugtypen, getfield(tmp, 1)));
       strcpy(fahrzeugtypen, concat(fahrzeugtypen, "|"));
       // NOTE strtok clobbers tmp
       free(tmp);
  }
  fahrzeugtypen[strlen(fahrzeugtypen)-1] = 0;
  strcpy(fahrzeugtypen, concat(fahrzeugtypen, ")"));

  strcpy(fahrzeugtypen, concat("^(WVW|WV2|1VW|3VW|9BW|AAV)(ZZZ)?", fahrzeugtypen));
  strcpy(fahrzeugtypen, concat(fahrzeugtypen, "([ABCDEFGHJKLMNPRSTVWXY]|[0-9])([ABCDEFGHJKLMNPRSTUVWXYZ]|[0-9])[0-9]{6}"));
  aStrRegex = fahrzeugtypen;
  reCompiled = pcre_compile(aStrRegex, 0, &pcreErrorStr, &pcreErrorOffset, NULL);

  if(reCompiled == NULL) {
    exit(1);
  } /* end if */

  pcreExtra = pcre_study(reCompiled, 0, &pcreErrorStr);

  pcreExecRet = pcre_exec(reCompiled,
                            pcreExtra,
                            aLineToMatch,
                            strlen(aLineToMatch),  // length of string
                            0,                      // Start looking at this point
                            0,                      // OPTIONS
                            subStrVec,
                            30);                    // Length of subStrVec
  return pcreExecRet;
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

    // Read the command
    //scanf("%[^\n]", str);
    strcpy(str, argv[1]);

    // Check the user input for bad characters

    if(test_regex(str) == -1){
      printf("Na\n");
      return -1;
    }

    char *c = str;
    while (*c)
    {
      if (strchr(invalid_characters, *c))
      {
         printf("Na\n");
         // Set flag if found
         ciFound = 1;
      }
      c++;
    }

    // Concat the command and the user input
    sprintf(command, "head -%d info/Fahrzeugnummern.csv | tail -1 | awk --field-separator=';' '{print $2}' ; echo ", ran);
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
    printf("Na\n");
  }
  return 1;
}
