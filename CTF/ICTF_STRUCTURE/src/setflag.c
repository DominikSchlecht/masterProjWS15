#define _GNU_SOURCE
#include <stdio.h>
#include <stdlib.h>
#include <stddef.h>
#include <unistd.h>
#include <string.h>
#include <time.h>
#include <time.h>
#include <gcrypt.h>

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
	char* filename = "../rw/info/Fahrzeugnummern.csv";
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



/// MAX ADDED
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
//                int key = rand() % (int)(sizeof(charset) -1);
                int key = (rand()) % (int)(sizeof(charset) -1);	// etwas besser aber nicht gut	//ggf mtwist.h impl (mersenne twist)
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
	sprintf(tmp, "openssl aes-256-cbc -d -in ../rw/info/Bayrisch.csv.enc -out %s -pass pass:Â§acf578?#*+-463-{{}av@wer637,,..", randName);
	f = popen(tmp, "w");
	pclose(f);
	FILE* output=fopen(randName, "r");
	addStringToFile(line, "ba", randName);
	free(tmp);
	char* tmp2 = malloc(sizeof(char)*2000);
	sprintf(tmp2, "openssl aes-256-cbc -in %s -out ../rw/info/Bayrisch.csv.enc -pass pass:Â§acf578?#*+-463-{{}av@wer637,,..", randName);
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
	sprintf(tmp, "openssl aes-256-cbc -d -in ../rw/info/Bayrisch.csv.enc -out %s -pass pass:Â§acf578?#*+-463-{{}av@wer637,,..", randName);
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


int encryptString2(char* txtBuffer, char* aesSymKey)
{
    //printf("encrypting...: %s\n", txtBuffer);
    #define GCRY_CIPHER GCRY_CIPHER_AES128   // Pick the cipher here
    int gcry_mode = GCRY_CIPHER_MODE_CBC;
    char* iniVector = "a test ini value";

    gcry_error_t     gcryError;
    gcry_cipher_hd_t gcryCipherHd;
    size_t           index;

    size_t keyLength = gcry_cipher_get_algo_keylen(GCRY_CIPHER);
    size_t blkLength = gcry_cipher_get_algo_blklen(GCRY_CIPHER);
    //char * txtBuffer = "123456789 abcdefghijklmnopqrstuvwzyz ABCDEFGHIJKLMNOPQRSTUVWZYZ";
    size_t txtLength = strlen(txtBuffer)+1; // string plus termination
    char * encBuffer = malloc(txtLength);
    char * outBuffer = malloc(txtLength);
    //char * aesSymKey = "one test AES key"; // 16 bytes

    gcryError = gcry_cipher_open(
        &gcryCipherHd, // gcry_cipher_hd_t *
        GCRY_CIPHER,   // int
        gcry_mode,     // int
        0);            // unsigned int
    if (gcryError)
    {
        printf("gcry_cipher_open failed:  %s/%s\n",
               gcry_strsource(gcryError),
               gcry_strerror(gcryError));
        return;
    }

    gcryError = gcry_cipher_setkey(gcryCipherHd, aesSymKey, keyLength);
    if (gcryError)
    {
        printf("gcry_cipher_setkey failed:  %s/%s\n",
               gcry_strsource(gcryError),
               gcry_strerror(gcryError));
        return;
    }

    gcryError = gcry_cipher_setiv(gcryCipherHd, iniVector, blkLength);
    if (gcryError)
    {
        printf("gcry_cipher_setiv failed:  %s/%s\n",
               gcry_strsource(gcryError),
               gcry_strerror(gcryError));
        return;
    }

    gcryError = gcry_cipher_encrypt(
        gcryCipherHd, // gcry_cipher_hd_t
        encBuffer,    // void *
        txtLength,    // size_t
        txtBuffer,    // const void *
        txtLength);   // size_t
    if (gcryError)
    {
        printf("gcry_cipher_encrypt failed:  %s/%s\n",
               gcry_strsource(gcryError),
               gcry_strerror(gcryError));
        return;
    }
    //printf("just encrypted: %s\n", encBuffer);

    strcpy(txtBuffer, encBuffer);
    //txtBuffer[strlen(txtBuffer)] = '\0';
}

void addPad(char* in) {
    //printf("beginnnnnnnnnnn\n");
    int pad = 15 - (strlen(in) % 16);
    //printf("adding %i chars\n", pad);
    char tmp[1024];
    if (pad > 0)
    {
        int cnt;
        for (cnt = 0; cnt < pad; cnt++)
        {
            sprintf(tmp, "%s=", in);
            //printf("new value: %s\n", tmp);
            strcpy(in, tmp);
            //printf("new value: %s with strlen %i\n", in, (int)strlen(in));
        }
    }
    //printf("inp2: %s\n", in);
    //printf("ennnnnnnnd\n");
}

void remPad(char* in) {
    //printf("beginnnnnnnnnnn\n");
    char tmp[1024];
    while (in[strlen(in)-1] == '=') {
        //printf("found =\n");
				//printf("strlen: %i\n", (int)strlen(in));
        in[strlen(in)-1] = '\0';
        //printf("%s\n", in);
    }
    //printf("inp2: %s\n", in);
    //printf("ennnnnnnnd\n");
}

int decryptString2(char* encBuffer, char* aesSymKey)
{
    //printf("decrypting...: %s\n", encBuffer);
    #define GCRY_CIPHER GCRY_CIPHER_AES128   // Pick the cipher here
    int gcry_mode = GCRY_CIPHER_MODE_CBC;
    char* iniVector = "a test ini value";

    gcry_error_t     gcryError;
    gcry_cipher_hd_t gcryCipherHd;
    size_t           index;

    size_t keyLength = gcry_cipher_get_algo_keylen(GCRY_CIPHER);
    size_t blkLength = gcry_cipher_get_algo_blklen(GCRY_CIPHER);
    //char * txtBuffer = "123456789 abcdefghijklmnopqrstuvwzyz ABCDEFGHIJKLMNOPQRSTUVWZYZ";
    size_t txtLength = strlen(encBuffer); // string plus termination
    //char * encBuffer = malloc(txtLength);
    char * outBuffer = malloc(txtLength);
    //char * aesSymKey = "one test AES key"; // 16 bytes

    gcryError = gcry_cipher_open(
        &gcryCipherHd, // gcry_cipher_hd_t *
        GCRY_CIPHER,   // int
        gcry_mode,     // int
        0);            // unsigned int
    if (gcryError)
    {
        printf("gcry_cipher_open failed:  %s/%s\n",
               gcry_strsource(gcryError),
               gcry_strerror(gcryError));
        return;
    }

    gcryError = gcry_cipher_setkey(gcryCipherHd, aesSymKey, keyLength);
    if (gcryError)
    {
        printf("gcry_cipher_setkey failed:  %s/%s\n",
               gcry_strsource(gcryError),
               gcry_strerror(gcryError));
        return;
    }
    gcryError = gcry_cipher_setiv(gcryCipherHd, iniVector, blkLength);
    if (gcryError)
    {
        printf("gcry_cipher_setiv failed:  %s/%s\n",
               gcry_strsource(gcryError),
               gcry_strerror(gcryError));
        return;
    }

    gcryError = gcry_cipher_decrypt(
        gcryCipherHd, // gcry_cipher_hd_t
        outBuffer,    // void *
        txtLength,    // size_t
        encBuffer,    // const void *
        txtLength);   // size_t
    if (gcryError)
    {
        printf("gcry_cipher_decrypt failed:  %s/%s\n",
               gcry_strsource(gcryError),
               gcry_strerror(gcryError));
        return;
    }
    //printf("just decrypted: %s\n", outBuffer);
    //printf("%s\n", outBuffer);
    //printf("%s\n", encBuffer);
    strcpy(encBuffer, outBuffer);
    //encBuffer[strlen(encBuffer)-1] = '\0';
}

void printAsHex(char* string)
{
    printf("As String: %s\n", string);
    int index = 0;
    printf("As Hexxxx: ");
    for (index = 0; index<strlen(string); index++) {
        printf("%02X", (unsigned char)string[index]);
    }
    printf("\n");
}

char* stringToHex(char* in)
{
    int index;
    //printf("hex1: ");
    //char hex[4096];
    char* hex = malloc(sizeof(char)*4096);
    char c[2];
    for (index = 0; index<strlen(in); index++) {
          //printf("%02X", (unsigned char)in[index]);
          sprintf(c, "%02X", (unsigned char)in[index]);
          //printf("\nc is: %s\n", c);
          hex[2*index] = c[0];
          hex[2*index+1] = c[1];
    }
    //printf("\n");
    hex[2*index] = '\0';
    return hex;
}

int hex_to_int(char c){
        int first = c / 16 - 3;
        int second = c % 16;
        int result = first*10 + second;
        if(result > 9) result--;
        return result;
}

char* hexToString(char* in)
{
    int index;
    //printf("asci: ");
    //char ascii[4096];
    char* ascii = malloc(sizeof(char)*4096);
    int high;
    int low;
    int c;
    for (index = 0; index<strlen(in); index = index+2) {
        high = hex_to_int(in[index]) * 16;
        low = hex_to_int(in[index+1]);
        c = (high+low);
      //  printf("%c", c);
        if (index == 0)
          ascii[0] = c;
        else
          ascii[index/2] = c;
    }
    ascii[(index+1)/2] = '\0';
    //printf("\n");
    //printf("asci: %s\n", ascii);
    return ascii;
}


// THE MAIN
char* main(int argc, char *argv[]) 	// Aufruf: setflag a 'b-.-c' d		 oder: setflag fzn value
{
		if (strcmp(argv[1], "-h") == 0) {
			char* encrypted_flag = argv[2];
			char* aes_key = argv[3];
			char* ascii_flag = hexToString(encrypted_flag);
			decryptString2(ascii_flag, aes_key);
			remPad(ascii_flag);
			printf("%s", ascii_flag);
			return ascii_flag;	// is decryped
		}
		else if (argc == 4) {	// for managers only!!11
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
				addPad(content);
				encryptString2(content, aeskey);
				char* hex_content = stringToHex(content);

				addBayWordAndKeyToBayCsv(bayWord, aeskey);	//TODO Dateipfad kontrollieren
				addFznAndEncContentToFznCsv(fzn, hex_content);	//TODO Dateipfad kontrollieren
		} else {	// official functionality
			char* fzn = argv[1];
			char* value = argv[2];
			if (fzn != NULL && value != NULL) {
					addFznAndEncContentToFznCsv(fzn, value);
					printf("FZN ADDED\n");
			} else {
					printf("you have to provide fzn and value\n");
			}
		}

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
