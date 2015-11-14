#include <Python.h>
#include <stdlib.h>
#include <stdio.h>
#include <string.h>


char *randstring(size_t length) 
{

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
	sprintf(tmp, "openssl aes-256-cbc -d -in Bayrisch.csv.enc -out %s -pass pass:Â§acf578?#*+-463-{{}av@wer637,,..", randName);
	f = popen(tmp, "w");
	pclose(f);
	FILE* output=fopen(randName, "r");
	char* encryptedData[1500];
	int i = 0;
	int p = 1;
	char* result = malloc(128);
	memset(result,0 ,strlen(result));
	encryptedData[0] = malloc(sizeof(char)*500);
	char line[1024];
	while(fgets(line, 1024, output)!=NULL)
	{
		char* tmp = strdup(line);
		if(strcmp(getfield(tmp, 1), word) == 0)
		{
			strcpy(tmp, line);
			sprintf(result,"The word %s means %s\n", word, getfield(tmp,2));
		}
		sprintf(encryptedData[i], "%s", line); 
		i++;
		encryptedData[i] = malloc(sizeof(char)*500);
		free(tmp);
	}
	if(strlen(result) == 0)
		sprintf(result, "Sorry we couldn't find that word\n");
	/* give result to the next function */
	sprintf(remove, "rm %s", randName);
	popen(remove, "w");
	return result;
}


/*Python Stuff */
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

