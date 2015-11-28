#define _GNU_SOURCE
#include <stdio.h>
#include <stdlib.h>
#include <stddef.h>
#include <unistd.h>
#include <string.h>
#include <time.h>
#include <time.h>
#include <gcrypt.h>

// sudo apt-get install libgcrypt20-dev
// setflag.compileit.sh


int addBayWordAndKeyToBayCsv(char* bayword, char* key) {
	char tmp[1000];
	//char* filename = "testBay.csv";
  			sprintf(tmp, "%s;%s\n", bayword, key);
        printf("%s\n", tmp);
	addStringToEnc(tmp);
}

int addFznAndEncContentToFznCsv(char* fzn, char* enc_content) {
	char tmp[1000];
	char* filename = "../rw/info/Fahrzeugnummern.csv";
        sprintf(tmp, "%s;%s\n", fzn, enc_content);
        printf("%s\n", tmp);
        addStringToFile(tmp, "in", filename);
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
                int key = (rand()) % (int)(sizeof(charset) -1);
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
	addStringToFile(line, "in", randName);
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
{
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
    #define GCRY_CIPHER GCRY_CIPHER_AES128   // Pick the cipher here
    int gcry_mode = GCRY_CIPHER_MODE_CBC;
    char* iniVector = "a test ini value";

    gcry_error_t     gcryError;
    gcry_cipher_hd_t gcryCipherHd;
    size_t           index;

    size_t keyLength = gcry_cipher_get_algo_keylen(GCRY_CIPHER);
    size_t blkLength = gcry_cipher_get_algo_blklen(GCRY_CIPHER);
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
}

void addPad(char* in) {
    int pad = 15 - (strlen(in) % 16);
    //printf("adding %i chars\n", pad);
    char tmp[1024];
    if (pad > 0)
    {
        int cnt;
        for (cnt = 0; cnt < pad; cnt++)
        {
            sprintf(tmp, "%s=", in);
            strcpy(in, tmp);
        }
    }
}

void remPad(char* in) {
    char tmp[1024];
    while (in[strlen(in)-1] == '=') {
        //printf("found =\n");
        in[strlen(in)-1] = '\0';
    }
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
    size_t txtLength = strlen(encBuffer); // string plus termination
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
    strcpy(encBuffer, outBuffer);
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
    char* hex = malloc(sizeof(char)*4096);
    char c[2];
    for (index = 0; index<strlen(in); index++) {
          sprintf(c, "%02X", (unsigned char)in[index]);
          hex[2*index] = c[0];
          hex[2*index+1] = c[1];
    }
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
    return ascii;
}


// THE MAIN
char* main(int argc, char *argv[])
// param options:
// decrypt some aes encrypted string:			enc_string key
// set a new flag d with id=a and token='b-.-c':	a 'b-.-c' d
// add a new fzn with value:				fzn value
{
	if (strcmp(argv[1], "-h") == 0) {	// decryption not really needed but management want me to leave it...
		char* encrypted_flag = argv[2];
		char* aes_key = argv[3];
		char* ascii_flag = hexToString(encrypted_flag);
		decryptString2(ascii_flag, aes_key);
		remPad(ascii_flag);
		printf("%s", ascii_flag);
		return ascii_flag;	// is decryped
	}
	else if (argc == 4) {	// for managers only!!11
	int done = 0;
	int tries = 0;
	while (done == 0) {		// some weird workaround...
		tries++;

		char* flag_id = argv[1];        // FahrzeugnummerBeginnWortBeginn
	        char* password = argv[2];       // ( komplette Fahrzeugnummer-.-komplettes Wort )
        	char* content_arg = argv[3];        // the flag itself
		char content[4096];
		strcpy(content, content_arg);
		printf("content1: %s\n", content);

        	char delimiter[] = "-.-";
	        char *ptr;
	        ptr = strtok(password, delimiter);
	        char* fzn = ptr;
	        printf("fzn: %s\n", fzn);

        	ptr = strtok(NULL, delimiter);
	        char* bayWord = ptr;
	        printf("bayWord: %s\n", bayWord);

		char* aeskey = randstring(16);
		printf("aeskey: ||%s||\n", aeskey);
		addPad(content);
		printf("content2: ||%s||\n", content);
		encryptString2(content, aeskey);
		printf("content3: ||%s||\n", content);
		if (strlen(content) < 32) {
			printf("strlen %i\n", (int)(strlen(content)));
			int rofl = 0;
			printf("As s: ||");
			for (rofl = 0; rofl < 32; rofl++)
			{
				printf("%c", content[rofl]);
			}
			printf("||\nAs x02: ||");
			for (rofl = 0; rofl < 32; rofl = rofl+2) {
				printf("%02X", content[rofl]);
			}
			printf("||\n");
		}
		printAsHex(content);
		char* hex_content = stringToHex(content);
		printf("content4: ||%s||\n", hex_content);
		printf("Alles: ||%s|| ; ||%s|| ; ||%s|| ; ||%s||\n", bayWord, aeskey, fzn, hex_content);

	if ((( strlen(hex_content) > 0 && strlen(content) > 0 && (strlen(hex_content) % 16) == 0 && (strlen(content) % 16) == 0) ) || tries > 2 ) {
		done = 1;
		addBayWordAndKeyToBayCsv(bayWord, aeskey);
		addFznAndEncContentToFznCsv(fzn, hex_content);
	}
//		char tmpstr[8096];
//		sprintf(tmpstr, "echo 'tries: %i || done: %i || strlen content: (%i) || hex_content: %s (%i) || content_arg: %s (%i) || ' >> setflaglog.log", tries, done, (int)(strlen(content)), hex_content, (int)(strlen(hex_content)), content_arg, (int)(strlen(content_arg)));
//		popen(tmpstr, "r");

	}
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
}
