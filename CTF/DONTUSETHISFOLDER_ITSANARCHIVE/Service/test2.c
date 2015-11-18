#include <stdio.h>
#include <string.h>
#include <pcre.h>

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

char* concat(char *s1, char *s2)
{
    char *result = malloc(strlen(s1)+strlen(s2)+1);//+1 for the zero-terminator
    //in real code you would check for errors in malloc here
    strcpy(result, s1);
    strcat(result, s2);
    return result;
}

main()
{
  pcre *reCompiled;
  char *aStrRegex;
  char *aLineToMatch;
  aLineToMatch = "1VWZZZ6N398795955";
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
  strcpy(fahrzeugtypen, concat(fahrzeugtypen, "([ABCDEFGHJKLMNPRSTVWXY]|[0-9])([ABCDEFGHJKLMNPRSTUVWXYZ]|[0-9])[0-9]{6}$"));
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
  printf("%d", pcreExecRet);
}
