#define _GNU_SOURCE
#include <stdio.h>
#include <stdlib.h>
#include <stddef.h>
#include <unistd.h>
#include <string.h>
#include <time.h>
#include <openssl/sha.h> 	// sudo apt-get install libssl-dev
#include "./chilkat-9.5.0-x86_64-linux-gcc/include/C_CkCrypt2.h"
#include <time.h>

// http://www.example-code.com/c/aes_stringEncryption.asp
// http://www.chilkatsoft.com/chilkatLinux.asp
// TODO export LD_LIBRARY_PATH=./chilkat-9.5.0-x86_64-linux-gcc/lib:$LD_LIBRARY_PATH
// http://www.cknotes.com/linking-c-programs-with-the-chilkat-cc-libs/ .... how to compile
// setflag.compileit.sh


int addBayWordAndKeyToBayCsv(char* bayword, char* key) {
	char tmp[1000];
	//char* filename = "testBay.csv";
        sprintf(tmp, "%s;%s", bayword, key);
        printf("%s\n", tmp);
	addStringToEnc(tmp);
}

int addFznAndEncContentToFznCsv(char* fzn, char* enc_content) {
	char tmp[1000];
	char* filename = "testFzn.csv";
        sprintf(tmp, "%s;%s", fzn, enc_content);
        printf("%s\n", tmp);
        addStringToFile(tmp, "ba", filename);
}


int addStringToFile(char* lineToAppend, char* method, char* filename) { // line format: flag_id;encrypted_flag
   FILE *fd;
   char command[500];

    if ( (fd = fopen(filename,"a+")) == NULL) {
      fprintf(stderr, "\nKonnte Datei %s nicht öffnen!", filename);
      return EXIT_FAILURE;
      }

   if(strcmp(method, "ba") == 0) {
      sprintf(command, "echo '%s' >> '%s'", lineToAppend, filename);
      FILE *ls = popen(command, "r");
   }else{
      if(strcmp(method, "in") == 0){
         fputs(lineToAppend, fd);
      }
   }

   fclose(fd);
   return 0;
}

// UNUSED
char** splitString(char* str, char* delim) {
	char string[] = "Kurt,Kanns;555678;DE";
	char delimiter[] = ",;";
	char *ptr;

	// initialisieren und ersten Abschnitt erstellen
	ptr = strtok(string, delimiter);

	while(ptr != NULL) {
		printf("Abschnitt gefunden: %s\n", ptr);
		// naechsten Abschnitt erstellen
	 	ptr = strtok(NULL, delimiter);
	}

}


// UNUSED
/*
char* encryptString(char* in) {
	char* tmp = malloc(sizeof(char)*2000);
	sprintf(tmp, "echo 'abc' | openssl aes-256-cbc -pass pass:Â§acf578?#*+-463-{{}av@wer637,,..");
	popen(tmp, "w");

//	echo "abc" | openssl aes-256-cbc -pass pass:Â§acf578?#*+-463-{{}av@wer637,,..
}
*/

int encryptString(char* result, char* password)
{
    HCkCrypt2 crypt;
    BOOL success;
    const char * hexKey;
    const char * text = result;
    const char * encText;
    const char * decryptedText;

    crypt = CkCrypt2_Create();

    success = CkCrypt2_UnlockComponent(crypt,"Anything for 30-day trial");
    if (success != TRUE) {
        printf("Crypt component unlock failed\n");
        return 0;
    }

    CkCrypt2_putCryptAlgorithm(crypt,"aes");
    CkCrypt2_putCipherMode(crypt,"cbc");
    CkCrypt2_putKeyLength(crypt,256);

    //  Generate a binary secret key from a password string
    //  of any length.  For 128-bit encryption, GenEncodedSecretKey
    //  generates the MD5 hash of the password and returns it
    //  in the encoded form requested.  The 2nd param can be
    //  "hex", "base64", "url", "quoted-printable", etc.

    hexKey = CkCrypt2_genEncodedSecretKey(crypt,password,"hex");
    CkCrypt2_SetEncodedKey(crypt,hexKey,"hex");

    CkCrypt2_putEncodingMode(crypt,"base64");

    //  Encrypt a string and return the binary encrypted data
    //  in a base-64 encoded string.

    encText = CkCrypt2_encryptStringENC(crypt,result);
    //printf("%s\n",encText);
    char tmpStr[1000];
    strcpy(result, encText);

    CkCrypt2_Dispose(crypt);
}


int decryptString(char* result, char* password)
{
    HCkCrypt2 crypt;
    BOOL success;
    const char * hexKey;
    const char * text = result;
    const char * encText;
    const char * decryptedText;

    crypt = CkCrypt2_Create();

    success = CkCrypt2_UnlockComponent(crypt,"Anything for 30-day trial");
    if (success != TRUE) {
        printf("Crypt component unlock failed\n");
        return 0;
    }

    CkCrypt2_putCryptAlgorithm(crypt,"aes");
    CkCrypt2_putCipherMode(crypt,"cbc");
    CkCrypt2_putKeyLength(crypt,256);

    //  Generate a binary secret key from a password string
    //  of any length.  For 128-bit encryption, GenEncodedSecretKey
    //  generates the MD5 hash of the password and returns it
    //  in the encoded form requested.  The 2nd param can be
    //  "hex", "base64", "url", "quoted-printable", etc.

    hexKey = CkCrypt2_genEncodedSecretKey(crypt,password,"hex");
    CkCrypt2_SetEncodedKey(crypt,hexKey,"hex");

    CkCrypt2_putEncodingMode(crypt,"base64");

    //  Encrypt a string and return the binary encrypted data
    //  in a base-64 encoded string.

    decryptedText = CkCrypt2_decryptStringENC(crypt,result);
    //printf("%s\n",encText);
    char tmpStr[1000];
    strcpy(result, decryptedText);

    CkCrypt2_Dispose(crypt);
}





/// MAX ADDED
char *randstring(size_t length)
{

    static char charset[] = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789";
    char *randomString = NULL;
    int n = 0;
    if (length) {
        randomString = malloc(sizeof(char) * (length +1));

	if (randomString) {
	    srand(time(NULL));
            for (n = 0;n < length;n++) {
//                int key = rand() % (int)(sizeof(charset) -1);
                int key = (rand() + clock()) % (int)(sizeof(charset) -1);	// etwas besser aber nicht gut	//ggf mtwist.h impl (mersenne twist)
		//printf("key: %i\n", key);
//		printf("time() %i\n", (int)gettimeofday(NULL));
//		printf("time() %i\n", (int)clock());
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


int addStringToEnc(char* line)
{
	char* randName = randstring(15);
	FILE* f = NULL;
	char* tmp = malloc(sizeof(char)*2000);
	sprintf(tmp, "openssl aes-256-cbc -d -in Bayrisch.csv.enc -out %s -pass pass:Â§acf578?#*+-463-{{}av@wer637,,..", randName);
	f = popen(tmp, "w");
	pclose(f);
	FILE* output=fopen(randName, "r");
	addStringToFile(line, "ba", randName);
	free(tmp);
	char* tmp2 = malloc(sizeof(char)*2000);
	sprintf(tmp2, "openssl aes-256-cbc -in %s -out Bayrisch.csv.enc -pass pass:Â§acf578?#*+-463-{{}av@wer637,,..", randName);
	popen(tmp2, "w");
	free(tmp2);
	sleep(1);
	char* remove = malloc(sizeof(char)*200);
	sprintf(remove, "rm %s", randName);
	popen(remove, "w");
	printf("remove cmd: %s\n", remove);
	return 0;
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
	memset(result, 0, strlen(result));
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






// THE MAIN
main(int argc, char *argv[]) 	// Aufruf: setflag a 'b-.-c' d
{
        char* flag_id = argv[1];        // FahrzeugnummerBeginnWortBeginn
        char* password = argv[2];       // ( komplette Fahrzeugnummer-.-komplettes Wort )
        char* content = argv[3];        // the flag itself

        char delimiter[] = "-.-";
        char *ptr;
        ptr = strtok(password, delimiter);
        char* fzn = ptr;
        printf("fzn: %s\n", fzn);

        ptr = strtok(NULL, delimiter);
        char* bayWord = ptr;
        printf("bayWord: %s\n", bayWord);

	char* aeskey = randstring(16);
	printf("aeskey: %s\n", aeskey);
	encryptString(content, aeskey);

	addBayWordAndKeyToBayCsv(bayWord, aeskey);	//TODO Dateipfad kontrollieren
	addFznAndEncContentToFznCsv(fzn, content);	//TODO Dateipfad kontrollieren


/* RESTE TO DELETE
//	char lineToAdd[1000];
//	sprintf(lineToAdd, "%s;%s", flag_id, content);
//	printf("%s\n", lineToAdd);
//	addStringToFile(lineToAdd, "ba");

/*
	// save flag in file and encrypt file
	FILE *f = fopen("flagfile", "w");
	fprintf(f, "%s", content);

	fclose(f);


	// save flag_id in Fahrzeugnummern.csv
	f = fopen("flag_id_file", "w");
	fprintf(f, "%s", flag_id);


	fclose(f);


	// hash password and save it somewhere
//	char cmd[80];
//	sprintf(cmd, "echo %s | openssl sha1 > pwfile", password);
//	system(cmd);
//	printf("%s", cmd);
RESTE TO DELETE ENDE */
}
