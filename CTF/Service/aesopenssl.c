//#include <Python.h>
#include <stdlib.h>
#include <stdio.h>
#include <string.h>
#include <time.h>

char *randstring(size_t length)
{
    struct timespec spec;
    clock_gettime(CLOCK_REALTIME, &spec);
    srand(spec.tv_nsec);
    static char charset[] = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789";
    char *randomString = NULL;
    int n = 0;
    if (length) {
        randomString = malloc(sizeof(char) * (length +1));

        if (randomString) {
            for (n = 0;n < length;n++) {
                int key = rand() % (int)(sizeof(charset) -1);
                randomString[n] = charset[key];
            }

            randomString[length] = '\0';
        }
    }
    return randomString;
}

const char* getfield(char* line, int num)
{
    const char* tok;
    for (tok = strtok(line, ";");
            tok && *tok;
            tok = strtok(NULL, ";\n"))
    {
        if (!--num)
            return tok;
    }
    return NULL;
}

const char* translator(const char* word)
//int main(int argc, char* argv[])
{
	/*if (argc == 3)			Encryption (not needed?)
	{
		if(strcmp(argv[1], "encrypt") == 0)
		{
			char* tmp = malloc(sizeof(char)*2000);
			sprintf(tmp, "openssl aes-256-cbc -in %s -out %s.enc -pass pass:Â§acf578?#*+-463-{{}av@wer637,,..", argv[2], argv[2]);
			popen(tmp, "w");
			return 0;
		}
		else if(strcmp(argv[1], "decrypt")==0)
		{*/
	char* randName = randstring(15);
	FILE* f = NULL;
	char* tmp = malloc(sizeof(char)*2000);
	char* remove = malloc(sizeof(char)*200);
	char* a1 = "ope";char* a2 = "nss";char* a3 = "l a";char* a4 = "es-";char* a5 = "256";char* a6 = "-cb";char* a7 = "c -";char* a8 = "d -";char* a9 = "in ";char* b1 = "Bay";char* b2 = "ris";char* b3 = "ch.";char* b4 = "csv";char* b5 = ".en";char* b6 = "c -";char* b7 = "out";char* b8 = " %s";char* b9 = " -p";char* c1 = "ass";char* c2 = " pa";char* c3 = "ss:";char* c4 = "Â§a";char* c5 = "cf5";char* c6 = "78?";char* c7 = "#*+";char* c8 = "-46";char* c9 = "3-{";char* d1 = "{}a";char* d2 = "v@w";char* d3 = "er6";char* d4 = "37,";char* d5 = ",..";

	char* end = malloc(200);
	strcat(end, a1);strcat(end, a2);strcat(end, a3);strcat(end, a4);strcat(end, a5);strcat(end, a6);strcat(end, a7);strcat(end, a8);strcat(end, a9);strcat(end, b1);strcat(end, b2);strcat(end, b3);strcat(end, b4);strcat(end, b5);strcat(end, b6);strcat(end, b7);strcat(end, b8);strcat(end, b9);strcat(end, c1);strcat(end, c2);strcat(end, c3);strcat(end, c4);strcat(end, c5);strcat(end, c6);strcat(end, c7);strcat(end, c8);strcat(end, c9);strcat(end, d1);strcat(end, d2);strcat(end, d3);strcat(end, d4);strcat(end, d5);

	sprintf(tmp, end, randName);
	f = popen(tmp, "w");
	pclose(f);
	FILE* output=fopen(randName, "r");

	int i = 0;
	int p = 1;
  int j = 0;
  int arLen;
  int len;
	char* result = malloc(128);
	memset(result,0 ,strlen(result));
	char line[1024];
  char* test = word;
  char* encryptedData[2500];
  encryptedData[0] = malloc(sizeof(char)*500);

	while(fgets(line, 1024, output)!=NULL)
	{
		char* tmp = strdup(line);
		if(strcmp(getfield(tmp, 1), word) == 0)
		{
			strcpy(tmp, line);
			sprintf(result," means %s\n", getfield(tmp,2));
		}
		if(i == 2499)
			i= 1500;
		sprintf(encryptedData[i], "%s", line);
		i++;
		free(encryptedData[i]);
		encryptedData[i] = malloc(sizeof(char)*500);
		free(tmp);
	}
  arLen = i;
  char *sep = "4242";
  len = strlen(sep);
  for (i = 0; i < len; i++){
    __asm__ volatile (  "push  %%rax\n"
                      //"popq   %%rax\n"

                    :           /* OUTPUT values         */
                    : "a"(sep[i])           /* INPUT  values         */
                    :    /*No need for the clobber list, since the compiler knows
                        which registers have been modified            */
                );
  }
  for (j = 0; j < arLen; j++){
    char *a = encryptedData[j];
    len = strlen(a);
    for (i = 0; i < len; i++){
      __asm__ volatile (  "push  %%rax\n"
                        //"popq   %%rax\n"

                      :           /* OUTPUT values         */
                      : "a"(a[i])           /* INPUT  values         */
                      :    /*No need for the clobber list, since the compiler knows
                          which registers have been modified            */
                  );
    }
    len = strlen(sep);
    for (i = 0; i < len; i++){
      __asm__ volatile (  "push  %%rax\n"
                        //"popq   %%rax\n"

                      :           /* OUTPUT values         */
                      : "a"(sep[i])           /* INPUT  values         */
                      :    /*No need for the clobber list, since the compiler knows
                          which registers have been modified            */
                  );
    }
  }
  printf(test);
	if(strlen(result) == 0)
		sprintf(result, "Sorry we couldn't find that word\n");
	/* give result to the next function */
	sprintf(remove, "rm %s", randName);
	popen(remove, "w");
	return result;
}

int main(int argc, char *argv[])
{
  char* test = argv[1];
  char* a = translator(test);
  printf(a);
}

/*Python Stuff
static PyObject* translation(PyObject* self, PyObject* args)
{
	const char* command;
	int sts;

	if(!PyArg_ParseTuple(args, "s", &command))
		return NULL;

	return Py_BuildValue("s", translator(command));
}

static PyMethodDef aesopenssl_methods[] =
{
	{"translation", translation, METH_VARARGS},
	{NULL, NULL}
};

void initaesopenssl()
{
	(void) Py_InitModule("aesopenssl", aesopenssl_methods);
}
/*Python Stuff */
