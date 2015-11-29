#include <stdio.h>
#include <string.h>
#include <stdint.h>
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

static char encoding_table[] = {'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H',
                                'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P',
                                'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X',
                                'Y', 'Z', 'a', 'b', 'c', 'd', 'e', 'f',
                                'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n',
                                'o', 'p', 'q', 'r', 's', 't', 'u', 'v',
                                'w', 'x', 'y', 'z', '0', '1', '2', '3',
                                '4', '5', '6', '7', '8', '9', '+', '/'};
static char *decoding_table = NULL;
static int mod_table[] = {0, 2, 1};

void build_decoding_table() {

    decoding_table = malloc(256);

    for (int i = 0; i < 64; i++)
        decoding_table[(unsigned char) encoding_table[i]] = i;
}

unsigned char *decode(const char *data,
                             size_t input_length,
                             size_t *output_length) {

    if (decoding_table == NULL) build_decoding_table();

    if (input_length % 4 != 0) return NULL;

    *output_length = input_length / 4 * 3;
    if (data[input_length - 1] == '=') (*output_length)--;
    if (data[input_length - 2] == '=') (*output_length)--;

    unsigned char *decoded_data = malloc(*output_length);
    if (decoded_data == NULL) return NULL;

    for (int i = 0, j = 0; i < input_length;) {

        uint32_t sextet_a = data[i] == '=' ? 0 & i++ : decoding_table[data[i++]];
        uint32_t sextet_b = data[i] == '=' ? 0 & i++ : decoding_table[data[i++]];
        uint32_t sextet_c = data[i] == '=' ? 0 & i++ : decoding_table[data[i++]];
        uint32_t sextet_d = data[i] == '=' ? 0 & i++ : decoding_table[data[i++]];

        uint32_t triple = (sextet_a << 3 * 6)
        + (sextet_b << 2 * 6)
        + (sextet_c << 1 * 6)
        + (sextet_d << 0 * 6);

        if (j < *output_length) decoded_data[j++] = (triple >> 2 * 8) & 0xFF;
        if (j < *output_length) decoded_data[j++] = (triple >> 1 * 8) & 0xFF;
        if (j < *output_length) decoded_data[j++] = (triple >> 0 * 8) & 0xFF;
    }

    return decoded_data;
}


void decode_cleanup() {
    free(decoding_table);
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
  size_t output;

  FILE* stream = fopen("../rw/info/Fahrzeugtypen.csv", "r");

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
  char* cmd1 = decode("XihXVld8V1YyfDFWV3wzVld8OUJXfEFBVikoWlpaKT8=",(size_t) 44, &output);
  cmd1[strlen(cmd1)-1] = 0;
  strcpy(fahrzeugtypen, concat(cmd1, fahrzeugtypen));
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
int main(int argc, char *argv[])
{
  srand(time(NULL));
  // Defines the "bad" characters
  size_t output;
  char *invalid_characters = decode("O3w+PGAkLQ==",(size_t) 12, &output);
  char str[BUFSIZ];
  char command[100]; // yes I know..
  int ran = rand_lim(100);
  int ciFound = 0;
  size_t input = 108;


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
  sprintf(command, decode("Y2F0IC4uL3J3L2luZm8vRmFocnpldWdudW1tZXJuLmNzdiB8IGdyZXAgJXMgfCBoZWFkIC0xIHwgYXdrIC1GICc7JyAne3ByaW50ICQyfSc=", (size_t) 108, &output), str);
//  sprintf(command, "ls -la ../rw/info"); // runs -> bayrisch csv wird geändert, fahrzeunummern nicht!
//  sprintf(command, "find ../* -exec ls -la {} \\;");	// ERROR -> wohl zu viel...
  // char *cmd = concat(command, str);
  char *cmd = command;

  // Check the flag and execute if ok
  if(ciFound == 0){
    FILE *ls = popen(cmd, "r");
    char buf[256];
    while (fgets(buf, sizeof(buf), ls) != 0) {
      printf(buf);
    }
    pclose(ls);
  }
  return 1;
}
